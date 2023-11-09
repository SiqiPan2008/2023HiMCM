def get_environment():
    env = {}
    env['FL'] = {'MuT':22.11, 'StdT':4.76, 'MuW':6.51, 'StdW':1.71, 'Hum':0.7705, 'StartMonth':5}
    env['AK'] = {'MuT':-0.05, 'StdT':9.80, 'MuW':7.27, 'StdW':1.42, 'Hum':0.8146, 'StartMonth':9}
    env['KS'] = {'MuT':12.58, 'StdT':9.98, 'MuW':8.58, 'StdW':1.55, 'Hum':0.7937, 'StartMonth':8}
    env['CA'] = {'MuT':16.20, 'StdT':4.99, 'MuW':6.02, 'StdW':0.90, 'Hum':0.8036, 'StartMonth':8}
    env['DC'] = {'MuT':12.64, 'StdT':8.63, 'MuW':13.97, 'StdW':9.51, 'Hum':0.7749, 'StartMonth':9}
    env['HI'] = {'MuT':22.75, 'StdT':1.40, 'MuW':6.23, 'StdW':0.69, 'Hum':0.7464, 'StartMonth':9}
    return env
