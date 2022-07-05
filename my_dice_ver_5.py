#rev5

import datetime
import csv

    
#generic function for loop
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

def get_file_array(filename, polyhedral_count):
    file_aaray=list()
    try:
        with open(filename, mode ='r', newline='') as csvfile:   
            sumreader = csv.reader(csvfile, delimiter=",")   #, quotechar="|"
            for x in sumreader:
                file_aaray.append(x)
        print(f"loaded file...")
        return file_aaray

    except FileNotFoundError:     #if no file create a multidimensional list
        print("no file loaded...")
        empty_string2 = list()
        empty_string2.append(str(datetime.datetime.now()))
        empty_string2.append(str(polyhedral_count))
        for i in my_range(1, polyhedral_count, 1):
            empty_string2.append('0')

        empty_string_set = list()
        empty_string_set.insert(0, empty_string2)

        with open(filename, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(empty_string_set)
        return empty_string_set

# writing to csv file
def write_to_file(filename, data_row_in):

    with open(filename, 'w', newline='') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # writing the data rows 
        csvwriter.writerows(data_row_in)

def get_set(polyhedral_count):
    my_list=list()
    while True:
        value = input("Enter a number: ")
        #end on done
        #add options to remove last input
        if value == "done" :
            break
        if value == "r" or value == "re" or value == "remove":
            my_list = my_list[:-1]     #slice item -1 off the end
            continue
        try:
            value = int(value)
            if value > polyhedral_count:
                print(f"{value} is greater than {polyhedral_count}")
                continue
            elif value <= 0:
                print("cannot be less than one")
            else:
                my_list.append(value)
        except:
            print("Invalid input:")
            continue
    return my_list

def sort_set(polyhedral_count, my_sort_list, file_row):
    result_list = []
    for i in my_range(1, polyhedral_count, 1): 
        x = 3 #my_sort_list.count(i)
        y = 2 #file_row[i - 1]
        result_of_adding_new_count_with_old_count = x + y
        result_list.append(str(result_of_adding_new_count_with_old_count))
    return result_list

def display_data(cnt, dta):
    new_dta = dta[2:]   #strp date and poly count off
    for n in my_range(1, cnt, 1):
        print(f"{n}: {new_dta[n-1]}") 

