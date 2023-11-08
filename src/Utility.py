import csv

def output_csv(file_name, rows):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow(row)
