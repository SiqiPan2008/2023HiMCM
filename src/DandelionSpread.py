from enum import Enum
import random
import time
import math
import csv

####################################################################
#data define
####################################################################
class Status(Enum):
    Unknown = 0
    Seed = 1
    Dev = 2
    Dis = 3
    InterDis = 4
    Dormancy = 5
    Hold = 6

class Dandelion:
    def __init__(self, status, day):
        self.status = status
        self.pre_status = Status.Unknown
        self.day = day
        self.x = 0
        self.y = 0

####################################################################
#input data
####################################################################
T_mean = 22.10648148
T_sd = 4.76404288
W_mean = 6.5
W_sd = 1.71
humidity = 0.87

#wind updraft

T_not_dis = 24
p_dis = 0.125

run_time = 1
start_day = 120

# vary
stalk_h = 0.4

days_seed_dev = 3
# vary
days_dev_dis = 70
days_dis_interdis = 10
days_interdis_dis = 180

num_flower = 5
# vary
num_seed_per_flower = 200

prop_seed_survival = 0.02

v_v = 0.4

max_num_in_block = 45

gap_limit = 0.15

####################################################################
#data proceed
####################################################################
p_seed_dev = 1.0 / days_seed_dev
days_dis_per_flower = days_dis_interdis / num_flower

####################################################################
#begin simulating
####################################################################
start_time = time.time()

file = open('output\dandelion.csv', 'w', newline='')
writer = csv.writer(file)
writer.writerow(['id', 'index', 'run', 'status', 'x', 'y']);

id = 1
for iRun in range(run_time):
    dandelions = []
    dandelions.append(Dandelion(Status.Unknown, 120))
    number_map = {}
    for iDay in range(360):
        cur_day = start_day + iDay
        act_day = cur_day % 360
        cur_Temp = - 1.41421 * T_sd * math.cos(act_day*math.pi/180) + T_mean
        cur_dandelion_count = len(dandelions)

        for iDandelion in range(cur_dandelion_count):
            dandelion = dandelions[iDandelion]
            cur_status = dandelion.status
            day_in_status = cur_day - dandelion.day

            if cur_Temp <= 0 and cur_status != Status.Dormancy:
                dandelion.pre_status = dandelion.status
                dandelion.status = Status.Dormancy
                continue
            elif cur_Temp <= 0 and cur_status == Status.Dormancy:
                continue
            elif cur_Temp > 0 and cur_status == Status.Dormancy:
                dandelion.status = dandelion.pre_status
                dandelion.pre_status = Status.Unknown
                dandelion.day = cur_day
                continue

            if dandelion.status == Status.Unknown:
                dandelion.day = cur_day
                dandelion.status = Status.Dis

            elif dandelion.status == Status.Hold:
                if cur_Temp <  T_not_dis:
                    dandelion.status = dandelion.pre_status

            elif dandelion.status == Status.Seed:
                r_seed_dev = random.uniform(0, 1)
                if r_seed_dev < p_seed_dev * day_in_status:
                    dandelion.day = cur_day
                    dandelion.status = Status.Dev
            
            elif dandelion.status == Status.Dev or dandelion.status == Status.InterDis:
                if dandelion.status == Status.Dev:
                    limit_days = days_dev_dis
                else:
                    limit_days = days_interdis_dis
                if day_in_status >= limit_days:
                    enable_dis = True
                    if cur_Temp >= T_not_dis:
                        r_dis = random.uniform(0, 1)
                        if r_dis >= p_dis:
                            enable_dis = False

                    if enable_dis:
                        dandelion.day = cur_day
                        dandelion.status = Status.Dis
                    else:
                        dandelion.pre_status = cur_status
                        dandelion.status = Status.Hold

            elif dandelion.status == Status.Dis:
                r_dis = random.uniform(0, 1)
                dis_seed = 0
                if day_in_status % days_dis_per_flower == 1:
                    left_seed = num_seed_per_flower
                if day_in_status % days_dis_per_flower == 0:
                    dis_seed = left_seed
                else:
                    dis_seed = left_seed * r_dis
                    left_seed = left_seed - dis_seed

                dis_seed = int(dis_seed * prop_seed_survival)
                for iSeed in range(dis_seed):
                    angle = random.uniform(0, math.pi/2)
                    wind = -1
                    while wind < 0:
                        wind = random.gauss(W_mean, W_sd)
                    distance = wind * stalk_h / v_v
                    newDandelion = Dandelion(Status.Seed, cur_day)
                    newDandelion.x = distance * math.cos(angle)
                    newDandelion.y = distance * math.sin(angle)
                    if newDandelion.x < 0:
                        newDandelion.x = 0
                    if newDandelion.y < 0:
                        newDandelion.y = 0
                    block_x = int(newDandelion.x)
                    block_y = int(newDandelion.y)
                    item_in_block = number_map.get((block_x, block_y))
                    if item_in_block is None:
                        item_in_block = 0
                    if item_in_block < max_num_in_block:
                        found = False
                        for dandelionTemp in dandelions:
                            if math.fabs(dandelionTemp.x - newDandelion.x) < gap_limit \
                                and math.fabs(dandelionTemp.y - newDandelion.y) < gap_limit:
                                found = True
                                break
                        if not found:
                            number_map[((block_x, block_y))] = (item_in_block + 1)
                            dandelions.append(newDandelion)

                if day_in_status >= days_dis_interdis:
                    dandelion.day = cur_day
                    dandelion.status = Status.InterDis

    print(str(len(dandelions)))
    for iDandelion in range(cur_dandelion_count):
        dandelion = dandelions[iDandelion]
        row = [id, iDandelion+1, iRun+1, str(dandelion.status), dandelion.x, dandelion.y]
        writer.writerow(row)
        id = id + 1

print('total time = ' + str(time.time() - start_time))
