from enum import Enum
import random
import time
import math

####################################################################
# helper functions
####################################################################
def get_guass_data(min_limit, max_limit, ratio):
    span = max_limit - min_limit
    sdv = span / 12.
    act_min = min_limit + sdv * 3
    mu = span * 0.5 * ratio + act_min
    data = random.gauss(mu, sdv)
    if data < min_limit:
        data = min_limit
    if data > max_limit:
        data = max_limit
    return data

def get_adaption_ratio(humidity, temperatuer):
    h_level = 3
    if humidity >= 0.8 or humidity <= 0.4:
        h_level = 1
    elif humidity >= 0.7 or humidity <= 0.5:
        h_level = 2
    t_level = 3
    if temperatuer >= 30 or temperatuer <= 6:
        t_level = 1
    elif temperatuer >= 24 or temperatuer <= 12:
        t_level = 2
    level = 0.5 * h_level + 0.5 * t_level
    return (level - 1) / 2

####################################################################
# data define
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
# solve dandelion spread
####################################################################
def solve_dandelion_spread(run_times, env, days):
    ####################################################################
    # input data
    ####################################################################
    T_mean = env['MuT']
    T_sd = env['StdT']
    W_mean = env['MuW']
    W_sd = env['StdW']
    humidity = env['Hum']
    run_time = run_times

    T_not_dis = 24
    p_dis = 0.125
    
    start_day = 120

    stalk_h_min = 0.12
    stalk_h_max = 0.40

    days_seed_dev = 3
    days_dev_dis_min = 69
    days_dev_dis_max = 107
    days_dis_interdis = 10
    days_interdis_dis = 180

    num_flower = 5
    num_seed_per_flower_min = 150
    num_seed_per_flower_max = 200

    prop_seed_survival = 0.02

    v_v = 0.4

    max_num_in_block = 45

    gap_limit = 0.15

    ####################################################################
    # data proceed
    ####################################################################
    p_seed_dev = 1.0 / days_seed_dev
    days_dis_per_flower = days_dis_interdis / num_flower

    ####################################################################
    # begin simulating
    ####################################################################
    start_time = time.time()

    id = 1
    rows = []

    for iRun in range(run_time):
        dandelions = []
        dandelions.append(Dandelion(Status.Unknown, 120))
        number_map = {}
        for iDay in range(days):
            cur_day = start_day + iDay
            act_day = cur_day % 360
            cur_Temp = - 1.41421 * T_sd * math.cos(act_day*math.pi/180) + T_mean
            cur_dandelion_count = len(dandelions)
            adaption_ratio = get_adaption_ratio(humidity, cur_Temp)

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
                        limit_days = get_guass_data(days_dev_dis_min, days_dev_dis_max, adaption_ratio) 
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
                        left_seed = get_guass_data(num_seed_per_flower_min, num_seed_per_flower_max, adaption_ratio)
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
                        distance = wind * get_guass_data(stalk_h_min, stalk_h_max, adaption_ratio) / v_v
                        #try long-distance dispersal
                        r = random.uniform(0, 1)
                        ldd = -1.316 * math.log(r)
                        if ldd > distance:
                            distance = ldd
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

        for iDandelion in range(len(dandelions)):
            dandelion = dandelions[iDandelion]
            row = [id, iDandelion+1, iRun+1, str(dandelion.status), dandelion.x, dandelion.y]
            rows.append(row)
            id = id + 1

    print('total time = ' + str(time.time() - start_time))
    return rows

####################################################################
# get mean distance from rows
####################################################################
def get_mean_dist(rows):
    total_distance = 0
    for row in rows:
        total_distance = total_distance + math.sqrt(row[4]*row[4] + row[5]*row[5])
    return total_distance / len(rows)
