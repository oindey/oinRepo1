import csv

def read_csv_file(file_path):
    data = []
    try:
        with open(file_path, 'r', newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                data.append(row)
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

print(read_csv_file(r"C:\Users\oindey\Desktop\Ansible\dataDump\samplecsv.csv"))

