import os
import codecs

#read card and save file in mdf
read_card = 'nfc-mfultralight r mycardUltra.mfd'
os.system(read_card)

#convert mdf file to hex
card_to_hex = 'xxd mycardUltra.mfd > mycardUltra.hex'
os.system(card_to_hex)

#read file
f=open("mycardUltra.hex","r")
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

print(id_num)

# if text_hex== "":
#     print("is empty")
# os.system(id_num)


# write_card = 'yes N | nfc-mfultralight w mycardUltra.mfd'
# os.system(write_card)
