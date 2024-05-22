import csv

# Read data from the first CSV file
csv_file1 =
data1 = []
with open(csv_file1, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        data1.append(row)

# Read data from the second CSV file
csv_file2 = 
data2 = []
with open(csv_file2, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        data2.append(row)

# Combine data from both files horizontally
combined_data = []
for row1, row2 in zip(data1, data2):
    combined_data.append(row1 + row2)

# Write combined data to a new CSV file
combined_csv_file = 'combined_file_horizontal.csv'
with open(combined_csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(combined_data)

print("Combined CSV file in horizontal way has been created:", combined_csv_file)
