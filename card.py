"""Class card with read and write methods"""

import os
import codecs
import uuid

class Card:
        def __init__(self):
            self.id = self.get_id_number()

        def read_card_into_file(self):
            """Save file.mfd with card information"""

            #Create a unique file name
            name = str(uuid.uuid4())

            #read card and save file in mdf
            file_mdf = 'nfc-mfultralight r .temp/{}.mfd'.format(name)
            os.system(file_mdf)

            #convert mdf file to hex
            card_to_hex = 'xxd .temp/{}.mfd > .temp/{}.hex'.format(name, name)
            os.system(card_to_hex)

            #return the name of the file in hex format
            return '{}.hex'.format(name)

        def get_id_number(self):
            """Getting id number in the first 4 bytes of the card"""

            #read the card and get the file name
            file = self.read_card_into_file()

            #read file
            f=open(".temp/{}".format(file),"r")
            first=f.readline()
            second=f.readline()

            #substring the second line, strip 0 and spaces
            id_num_hex=second[9:18]
            id_num_hex1=id_num_hex.replace(' ', '').rstrip('0')

            #add 0 if lenght of the hex is odd
            if (len(id_num_hex1))%2 == 1:
                id_num_hex1=id_num_hex1 + "0"

            #decode hex into ascii
            id_num = codecs.decode(id_num_hex1, 'hex').decode('ascii')

            #return id of the card
            return id_num

        def save_id_number(self, id_number):
            """Save id number in card, if there is any error it returns 0
            otherwise returns 1"""

            #check id_number is between 0 and 9999
            if(id_number<0 or id_number>9999):
                return 0

            #read the card and get the file name
            file = self.read_card_into_file()

            #convert input to hex
            hex_num=hex(id_number).lstrip('0x').rstrip('L')

            #add 0 to complete 2 bytes
            while (len(hex_num))!=4:
                hex_num+="0"

            hex_num+=" "


            #Create a unique file name for new file
            name_new_file = str(uuid.uuid4())

            #create new hex file
            new_file=open(".temp/{}.hex".format(name_new_file) ,"w")

            #counter for old hex file
            counter = 0

            with open(".temp/{}".format(file), "r") as f:
                for line in f:
                    #add 1 to counter to know which line of the file is the pointer
                    counter += 1

                    #change the id_number when we are in second line
                    if(counter == 2):
                        line = line[9:14].replace(id_num_hex,hex_num,1)

                    #write the line into the new file
                    new_file.writeline(line)

                    if 'str' in line:
                        break

            #close new hex file
            new_file.close()

            #write the new file into the card
            self.write_card(name_new_file)

            return 1

        def write_card(self, file_name):
            #convert hex file to mfd
            hex_to_card = 'xxd -r .temp/{}.hex .temp/{}.mfd'.format(file_name, file_name)
            os.system(id_num_hex_to_card)

            #run command to write into the card
            #write_to_card = 'yes N | nfc-mfultralight w {}.mfd'.format(file_name)
            #os.system(run_to_card)
