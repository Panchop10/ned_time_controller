"""Class card with read and write methods"""

import os
import codecs

class Card:
        def __init__(self):
            self.id = self.get_id_number()

        def read_card_into_file(self, name):
            print('read card into file')
            #read card and save file in mdf
            file_mdf = 'nfc-mfultralight r {}.mfd'.format(name)
            os.system(file_mdf)

            #convert mdf file to hex
            card_to_hex = 'xxd {}.mfd > {}.hex'.format(name, name)
            os.system(card_to_hex)

            #return the name of the file in hex format
            return '{}.hex'.format(name)

        def get_id_number(self):
            print('get id number')
            #read the card and get the file name
            file = self.read_card_into_file('myCardUltra')

            #read file
            f=open(file,"r")
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
            return id_num

        def save_id_number(self, id_number):
            """Save id number in card, if there is any error it returns 0
            otherwise returns 1"""
            print('save id number')
            #check id_number is between 0 and 9999
            if(id_number<0 or id_number>9999):
                return 0

            #read the card and get the file name
            file = self.read_card_into_file('myCardUltra')

            #convert input to hex
            hex_num=hex(id_number).lstrip('0x').rstrip('L')

            #add 0 to complete 2 bytes
            while (len(hex_num))!=4:
                hex_num+="0"

            hex_num+=" "

            #create new hex file
            n=open("NewMycardUltra.hex","w")

            #counter for old hex file
            counter = 0

            with open(file, "r") as f:
                for line in f:
                    #add 1 to counter to know which line of the file is the pointer
                    counter += 1

                    #change the id_number when we are in second line
                    if(counter == 2):
                        line = line[9:14].replace(id_num_hex,hex_num,1)

                    #write the line into the new file
                    n.writeline(line)

                    if 'str' in line:
                        break

            #close new hex file
            n.close()

            self.write_card("NewMycardUltra")

            return 1

        def write_card(self, file_name):
            print('write card')
            #convert hex file to mfd
            hex_to_card = 'xxd -r {}.hex {}.mfd'.format(file_name, file_name)
            os.system(id_num_hex_to_card)

            #run command to write into the card
            #write_to_card = 'yes N | nfc-mfultralight w {}.mfd'.format(file_name)
            #os.system(run_to_card)
