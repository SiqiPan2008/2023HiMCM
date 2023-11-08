import DandelionSpread as ds
import Environment as e
import Utility as u
import math

envs = e.get_environment()
data_best = {}
spread_result_best = {}
spread_result_location = {}
month_data_best = {}
selected_location = 'FL'

##########################################################################
# pick best result for every location
##########################################################################
for location, paras in envs.items():
    spread_results = []
    all_data = ds.solve_dandelion_spread(1000, paras)
    for data in all_data:
        distance = ds.get_mean_dist(data)
        spread_results.append(ds.Spread_Result(len(data), distance))
  
    number_sum = 0
    distance_sum = 0
  
    for ispread_result in range(len(spread_results)):
        spread_result = spread_results[ispread_result]
        number_sum += spread_result.number
        distance_sum += spread_result.distance
    number_mean = number_sum / len(spread_results)
    distance_mean = distance_sum / len(spread_results)

    # look for best data set
    ibest = -1
    min_number_diff = 10000
    for ispread_result in range(len(spread_results)):
        spread_result = spread_results[ispread_result]
        number_diff = math.fabs(spread_result.number - number_mean)
        if number_diff < min_number_diff:
            ibest = ispread_result
            min_number_diff = number_diff
    data_best[location] = all_data[ibest]
    spread_result_best[location] = spread_results[ibest]
    spread_result_location[location] = spread_results

##########################################################################
# output (number, distance) for selected_location
##########################################################################
output_results = [['run_times', 'number', 'distance']]
spread_results = spread_result_location[selected_location]
for ispread_result in range(len(spread_results)):
    spread_result = spread_results[ispread_result]
    output_results.append([ispread_result + 1, spread_result.number, spread_result.distance])
u.output_csv('output\spread_result_' + selected_location + '.csv', output_results)

##########################################################################
# output spread course for selected_location
##########################################################################
row_time_course = [['month', 'number', 'mean_distance']]
month_data = []
all_data = ds.solve_dandelion_spread(1, envs[selected_location], month_data)[0]
while math.fabs(len(all_data) - spread_result_best[selected_location].number) > 10:
    month_data = []
    all_data = ds.solve_dandelion_spread(1, envs[selected_location], month_data)[0]

for imonth in range(len(month_data)):
    data = month_data[imonth]
    distance = ds.get_mean_dist(data)
    row_time_course.append([imonth + 1, len(data), distance])

    rows = [['id', 'status', 'x', 'y']]
    for idandelion in range(len(data)):
        dandelion = data[idandelion]
        rows.append([idandelion+1, dandelion[3], dandelion[4], dandelion[5]])
    u.output_csv('output\spread_course_' + str(imonth + 1) + '_' + selected_location + '.csv', rows)

u.output_csv('output\spread_result_time_' + selected_location + '.csv', row_time_course)

##########################################################################
# output spread coordinate for all locations
##########################################################################
for location, data in data_best.items():
    rows = [['id', 'status', 'x', 'y']]
    for idandelion in range(len(data)):
        dandelion = data[idandelion]
        rows.append([idandelion+1, dandelion[3], dandelion[4], dandelion[5]])
    u.output_csv('output\spread_coordinate_' + location + '.csv', rows)
