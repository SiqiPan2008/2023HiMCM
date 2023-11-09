import DandelionSpread as ds
import Environment as e
import Utility as u

##########################################################################
# sensitivity analysis
##########################################################################
def sa(variable, param_min, param_max, param_gap):
    envs = e.get_environment()
    selected_location = 'FL'
    numbers = []
    distances = []
    params = [param_min + i * param_gap for i in range(int((param_max - param_min) / param_gap) + 1)]
    for param in params:
        env = envs[selected_location]
        env[variable] = param
        data = ds.solve_dandelion_spread(1000, env, env['StartMonth'])
        numbers.append(ds.get_mean_number_all(data))
        distances.append(ds.get_mean_dist_all(data))

    rows = [['id', variable, 'number', 'mean_distance']]
    for param in params:
        index = len(rows) - 1
        rows.append([index + 1, param, numbers[index], distances[index]])

    u.output_csv('output\\' + variable + '_sa.csv', rows)

##########################################################################
# output sensitivity analysis result
##########################################################################
sa('MuT', 0, 30, 1)
sa('StdT', 0, 10, 0.5)
sa('MuW', 0, 15, 0.5)
sa('StdW', 0, 10, 0.5)
sa('Hum', 0, 1, 0.05)

