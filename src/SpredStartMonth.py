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
# output number and distance start from different month
##########################################################################
for location, paras in envs.items():
    for begin_month in range(12):
        all_data = ds.solve_dandelion_spread(1000, envs[location], begin_month + 1)
        number = ds.get_mean_number_all(all_data)

        month_data = []
        all_data = ds.solve_dandelion_spread(1, envs[location], begin_month + 1, month_data)[0]
        while math.fabs(len(all_data) - number) > 10:
            month_data = []
            all_data = ds.solve_dandelion_spread(1, envs[location], begin_month + 1, month_data)[0]

        row_time_course = [['month', 'number', 'mean_distance']]
        for imonth in range(len(month_data)):
            data = month_data[imonth]
            distance = ds.get_mean_dist(data)
            row_time_course.append([imonth + 1, len(data), distance])
        u.output_csv('output\spread_begin_' + str(begin_month + 1) + '_' + location + '.csv', row_time_course)