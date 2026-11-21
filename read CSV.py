import csv

# Read an existing CSV file
with open("data.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        string_list = [str(value) for value in row]
        print(string_list)
