import pandas as pd
import numpy as np
import AHP as ahp
import Utility as u

globalW = np.array(ahp.GetGlolbaW());

data = pd.read_csv('input\\plant.csv')

num = 0
values = np.empty(14, dtype=float)
output_row = [['Impact factor']]
for index, row in data.iterrows():

    num += 1

    pho = 100
    if row['degreeOfEstablishment']=='invasive (category D2)':
        pho = 90

    index = 0
    if row['Duration'] == 'Annual':
        values[index] = 0.5
    elif row['Duration'] == 'Biennial':
        values[index] = 0.75
    elif row['Duration'] == 'Perennial':
        values[index] = 1

    index += 1
    if row['Growing Habbit'] == 'Tree':
        values[index] = 0
    elif row['Growing Habbit'] == 'Shrub':
        values[index] = 0.25
    elif row['Growing Habbit'] == 'Vine':
        values[index] = 0.5
    elif row['Growing Habbit'] == 'Graminoid':
        values[index] = 0.75
    elif row['Growing Habbit'] == 'Forb/herb':
        values[index] = 1
    
    index += 1
    if row['Growth Rate'] == 'Slow':
        values[index] = 0.5
    elif row['Growth Rate'] == 'Moderate':
        values[index] = 0.75
    elif row['Growth Rate'] == 'Rapid':
        values[index] = 1

    index += 1
    if row['Duration'] == 'Annual':
        values[index] = 0.25
    elif row['Lifespan'] == 'Short':
        values[index] = 0.5
    elif row['Lifespan'] == 'Moderate':
        values[index] = 0.75
    elif row['Lifespan'] == 'Long':
        values[index] = 1

    index += 1
    if row['Fertility Requirement'] == 'Low':
        values[index] = 0.5
    elif row['Fertility Requirement'] == 'Medium':
        values[index] = 0.75
    elif row['Fertility Requirement'] == 'High':
        values[index] = 1

    index += 1
    if row['Fruit/Seed Abundance'] == 'Low':
        values[index] = 0.5
    elif row['Fruit/Seed Abundance'] == 'Medium':
        values[index] = 0.75
    elif row['Fruit/Seed Abundance'] == 'High':
        values[index] = 1
    else:
        values[index] = 0.25

    index += 1
    if row['Propagated Methods'] == 1:
        values[index] = 0.25
    elif row['Propagated Methods'] == 2:
        values[index] = 0.5
    elif row['Propagated Methods'] == 3:
        values[index] = 0.75
    elif row['Propagated Methods'] >= 4:
        values[index] = 1

    index += 1
    if row['Seed Spread Rate'] == 'Slow':
        values[index] = 0.5
    elif row['Seed Spread Rate'] == 'Moderate':
        values[index] = 0.75
    elif row['Seed Spread Rate'] == 'Rapid':
        values[index] = 1
    else:
        values[index] = 0.25

    index += 1
    if row['Seedling Vigor'] == 'Low':
        values[index] = 0.5
    elif row['Seedling Vigor'] == 'Medium':
        values[index] = 0.75
    elif row['Seedling Vigor'] == 'High':
        values[index] = 1

    index += 1
    if row['Toxicity'] == 'Slight':
        values[index] = 0.5
    elif row['Toxicity'] == 'Moderate':
        values[index] = 0.75
    elif row['Toxicity'] == 'Severe':
        values[index] = 1
    else:
        values[index] = 0

    index += 1
    if row['productable'] == 0:
        values[index] = 1
    elif row['productable'] == 1:
        values[index] = 0.75
    elif row['productable'] == 2:
        values[index] = 0.5
    elif row['productable'] == 3:
        values[index] = 0.25
    elif row['productable'] == 4:
        values[index] = 0

    index += 1
    if row['Palatable Animal'] == 'High':
        values[index] = 0
    elif row['Palatable Animal'] == 'Moderate':
        values[index] = 0.5
    elif row['Palatable Animal'] == 'Low':
        values[index] = 0.75
    else:
        values[index] = 1

    index += 1
    if row['Palatable Human'] == 'Yes':
        values[index] = 0.5
    elif row['Palatable Human'] == 'No':
        values[index] = 1

    index += 1
    if row['Commercial Availability'] == 1:
        values[index] = 0.5
    elif row['Commercial Availability'] == 0:
        values[index] = 1

    result = np.dot(values, globalW) * pho
    output_row.append([result])

u.output_csv('output\Impact_factor_global.csv', output_row)