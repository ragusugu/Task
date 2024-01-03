import csv
import json

csv_file_path = r'C:\Users\HI\Documents\git\sample\Task\pyspark\ds_salaries.csv'
json_file_path = r'C:\Users\HI\Documents\git\sample\Task\pyspark\salary.json'

# Read CSV file and convert to JSON
data = []
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append(row)

# Write JSON data to a file
with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file, indent=2)

print(f'Conversion completed. JSON data written to {json_file_path}')
