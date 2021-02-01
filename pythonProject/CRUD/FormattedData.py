#  author: Olanrewaju Alawode

import csv


def save_data(file_name=" ", data_list=None):
    if data_list is None:
        data_list = []

    with open(file_name, "w", newline='\n') as csv_file:
        data_writer = csv.writer(csv_file, delimiter='\n', quotechar=" ", quoting=csv.QUOTE_NONNUMERIC)
        data_writer.writerow(data_list)
        csv_file.close()
        print("data saved!")


def read_data(file_name=" "):
    with open(file_name, "r", newline='\n') as csv_file:
        data_reader = csv.reader(csv_file, delimiter="\n", quotechar=" ", quoting=csv.QUOTE_NONNUMERIC)

        output = []
        for item in data_reader:
            output.append(item[0])

        csv_file.close()
        print("data read!")
        return output


def for_loop(new_data):
    for count, entry in enumerate(new_data):
        print(f"{count}. {entry}")


class FormatData:

    def __init__(self, name="", age=0, married=False):
        self.name = name
        self.age = age
        self.married = married

    def __str__(self):
        output_string = "{0}, {1}, {2}".format(self.name, self.age, self.married)
        return output_string
