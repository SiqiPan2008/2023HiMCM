import DandelionSpread as ds
import Environment as e
import Utility as u
import math

envs = e.get_environment()
data_best = {}
spread_result_best = {}
spread_result_location = {}
month_data_best = {}

##########################################################################
# output number and distance per day
##########################################################################
for location, paras in envs.items():
    env = envs[location]
    day_data = []
    all_data = ds.solve_dandelion_spread(1, env, env['StartMonth'], day_data, False)[0]
    while math.fabs(len(all_data) - env['Number']) / env['Number'] > 0.01:
        day_data = []
        all_data = ds.solve_dandelion_spread(1, env, env['StartMonth'], day_data, False)[0]

    row_time_course = [['day', 'number', 'mean_distance']]
    for iday in range(len(day_data)):
        data = day_data[iday]
        distance = ds.get_mean_dist(data)
        row_time_course.append([iday + 1, len(data), distance])
    u.output_csv('output\spread_day_result_' + location + '.csv', row_time_course)