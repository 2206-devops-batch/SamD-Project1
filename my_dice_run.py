#created by Sam Dare 
#runs the dice statistics using my_dice_ver_5 as the backbone

import argparse
import my_dice_ver_5

def main():
        # Parse command line
        parser = argparse.ArgumentParser()
        parser.add_argument(dest="argument1", type=int, nargs="?", help="enter the result of a dice roll to see what numbers come up the most")

        args = parser.parse_args()
        if args.argument1:     #if there is an argument set
            polyhedral_count = args.argument1
        else:
            polyhedral_count = 6   #default if not
        
        filename="DiceDATA.csv"
        #get the file as a multidimensional list
        data_row = my_dice_ver_5.get_file_array(filename, polyhedral_count)
        #if top row is equal to current poly load the data
        if data_row[0][1] == str(polyhedral_count):
            print(f"loaded:  {data_row[0]}")
            working_data_row=list(map(int, data_row[0][2:])) #[2:]strip the datime and poly and int it 
        else:     #if it doesnt match
            print("test22")
            working_data_row = list()
            for i in range(polyhedral_count):   #make new data
                working_data_row.append(0)
            print(f"profile: {working_data_row}")

        #build the row to be written to the file
        result_list=my_dice_ver_5.get_set(polyhedral_count)

        file_data_row = list()    #a new list that will write to the csv file
        file_data_row.extend(my_dice_ver_5.sort_set(polyhedral_count, result_list, working_data_row))
        #if the current row poly count is equal
        if data_row[0][1] == str(polyhedral_count):
            lema=str(data_row[0][1])   #take the existing date
            delta=str(data_row[0][0])  #and poly count
            file_data_row.insert(0, lema)
            file_data_row.insert(0, delta)
            data_row[0] = file_data_row   #and set the first row with the new data 

        else:      #if its new data
            file_data_row.insert(0, str(polyhedral_count))
            file_data_row.insert(0, str(my_dice_ver_5.datetime.datetime.now())) #add a time stamp

            data_row.insert(0, file_data_row)    #and add a new line on top so it is current

        my_dice_ver_5.display_data(polyhedral_count, file_data_row)

        my_dice_ver_5.write_to_file(filename, data_row) #changed from data_row
main()