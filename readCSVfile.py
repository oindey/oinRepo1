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

# Example usage:
file_path = 'path/to/your/csvfile.csv'
csv_data = read_csv_file(file_path)
if csv_data:
    for row in csv_data:
        print(row)
This Python code defines a function read_csv_file that takes the file path as input and returns a list of lists containing the data from the CSV file. Each row in the CSV file is represented as a list, and the entire data is stored in the data list. If the file is not found or any error occurs during the reading process, appropriate messages will be displayed, and the function will return None.

To use this code, replace 'path/to/your/csvfile.csv' with the actual path to your CSV file and run the Python script. It will read the CSV file and print its contents row by row.

Remember to make sure that the CSV file is in the correct format, with rows separated by newlines and columns separated by commas (or any other specified delimiter).





