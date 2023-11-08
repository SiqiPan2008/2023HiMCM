import DandelionSpread as ds
import Environment as e
import Utility as u

envs = e.get_environment()
for location, paras in envs.items():
    numbers = []
    distances = []

    data.append(['id', 'index', 'run', 'status', 'x', 'y'])
    data = ds.solve_dandelion_spread(1, paras, 360)

        
    u.output_csv('output\dandelion_' + location + '.csv', data)







