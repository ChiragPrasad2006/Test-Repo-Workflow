import csv
import json
import os

folder = os.path.dirname(__file__)

def my_logger(func):
    def wrapper(*args, **kwargs):
        f = open(os.path.join(folder, "log.txt"), "a")
        f.write("Starting function: " + func.__name__ + "\n")
        f.close()
        output = func(*args, **kwargs)
        f = open(os.path.join(folder, "log.txt"), "a")
        f.write("Done with function: " + func.__name__ + "\n")
        f.close()
        return output
    return wrapper

@my_logger
def get_data():
    file = open(os.path.join(folder, "employees.csv"), "r")
    reader = csv.reader(file)
    data = []
    next(reader)
    for row in reader:
        data.append(row)
    file.close()
    return data

@my_logger
def convert_and_save(csv_data):
    json_list = []

    for item in csv_data:
        person = {
            "employee_id": int(item[0]),
            "name": item[1],
            "salary": float(item[2]),
        }
        json_list.append(person)
    out_file = open(os.path.join(folder, "employees.json"), "w")
    json.dump(json_list, out_file, indent=4)
    out_file.close()
    print("Finished saving json!")

raw_data = get_data()
convert_and_save(raw_data)