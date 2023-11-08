import DandelionSpread as ds
import Environment as e
import Utility as u
import math

envs = e.get_environment()
selected_location = 'FL'

##########################################################################
# sensitivity analysis
##########################################################################
def sa(variable, param_min, param_max, param_gap):
    numbers = []
    distances = []
    params = [param_min + i * param_gap for i in range(int((param_max - param_min) / param_gap) + 1)]
    for param in params:
        env = envs[selected_location]
        env[variable] = param
        data = ds.solve_dandelion_spread(10, env, 360)
        numbers.append(ds.get_mean_number_all(data))
        distances.append(ds.get_mean_dist_all(data))

    rows = [['id', variable, 'number', 'number_value', 'mean_distance', 'distance_value']]
    first = True
    pre_number = -1
    pre_distance = -1
    index = -1
    for param in params:
        index += 1
        if not first:
            number_value = (numbers[index] - pre_number)/numbers[index]
            distance_value = (distances[index] - pre_distance)/distances[index]
            rows.append([len(rows) + 1, param, numbers[index], number_value, distances[index], distance_value])

        pre_number = numbers[index]
        pre_distance = distances[index]
        first = False

    u.output_csv('output\\' + variable + '_sa.csv', rows)

##########################################################################
# output sensitivity analysis result
##########################################################################
sa('MuT', 0, 30, 1)
sa('StdT', 0, 10, 0.5)
sa('MuW', 0, 15, 0.5)
sa('StdW', 0, 10, 0.5)
sa('Hum', 0, 1, 0.05)

