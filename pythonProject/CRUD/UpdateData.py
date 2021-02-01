#  author: Olanrewaju Alawode

import FormattedData
import os.path

if not os.path.isfile("test_file.csv"):  # specify path to file
    print("run correct file please")
    quit()

new_data = FormattedData.read_data("test_file.csv")  # reads data into memory
FormattedData.for_loop(new_data)

print("\r\n adding a new record")  # writes/adds to read data
new_record = "'glory', 24, False"
new_data.append(new_record)
FormattedData.for_loop(new_data)

print("\r\n removing record")  # removes a record from read data
index = new_data.index("'louis', 27, False")
record = new_data[index]
new_data.remove(record)
FormattedData.for_loop(new_data)

print("\r\n modifying record")  # modifying record from read data
index = new_data.index("'glory', 24, False")
record = new_data[index]
split_record = record.split(",")
mod_record = FormattedData.FormatData(split_record[0].replace("glory", "ajishebiyawo"), int(split_record[1]))
mod_record.married = True
new_data.remove(record)
new_data.append(mod_record)
FormattedData.for_loop(new_data)

FormattedData.save_data("updated_test_file.csv", new_data)
