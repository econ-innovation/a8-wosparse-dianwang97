import csv
file_path = 'qje2014_2023.txt'

with open(file_path, 'r', encoding='utf-8', newline='') as file:
    reader = csv.DictReader(file, delimiter='\t')

    table1_columns = ['ut', 'PY', 'SO', 'SN', 'DI', 'IS', 'VL']
    table1_data = {col: [] for col in table1_columns}

    table2_columns = ['ut', 'AB']
    table2_data = {col: [] for col in table2_columns}

    table3_columns = ['ut', 'TI']
    table3_data = {col: [] for col in table3_columns}
    table4_columns = ['ut', 'AF']
    table4_data = {col: [] for col in table4_columns}

    table5_columns = ['ut', 'AF', 'C1',]
    table5_data = {col: [] for col in table5_columns}

    table6_columns = ['ut', 'CR']
    table6_data = {col: [] for col in table6_columns}

    for row in reader:
        for col in table1_columns:
            table1_data[col].append(row[col])

        for col in table2_columns:
            table2_data[col].append(row[col])

        for col in table3_columns:
            table3_data[col].append(row[col])

        for col in table4_columns:
            table4_data[col].append(row[col])

        for col in table5_columns:
            table5_data[col].append(row[col])

        for col in table6_columns:
            table6_data[col].append(row[col])

def write_csv(file_name, columns, data):
    with open(file_name, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        for i in range(len(data[columns[0]])):
            row_data = {col: data[col][i] for col in columns}
            writer.writerow(row_data)

write_csv('table1.csv', table1_columns, table1_data)
write_csv('table2.csv', table2_columns, table2_data)
write_csv('table3.csv', table3_columns, table3_data)
write_csv('table4.csv', table4_columns, table4_data)
write_csv('table5.csv', table5_columns, table5_data)
write_csv('table6.csv', table6_columns, table6_data)
