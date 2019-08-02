import os
import codecs

#Sena wrote this code with Zeynep

## Read_Card

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

## Write_Card

#ask user number between 0 and 9999
hex_num =""
number = input ("Enter number")
while number<0 or number>9999:
    number=input("Please enter the number again")
#convert input to hex
hex_num=hex(number).lstrip('0x').rstrip('L')

#add 0 to complete 2 bytes
while (len(hex_num))!=4:
    hex_num+="0"

hex_num+=" "

#read file
f=open("mycardUltra.hex","r")
first=f.readline()
second=f.readline()
third=f.readline()
fourth=f.readline()
#substring the second line, change id number
id_num_hex=second[9:14]
new_id_num_hex =second.replace(id_num_hex,hex_num,1) #fix this
print(new_id_num_hex)

n=open("NewMycardUltra.hex","w")
newfirst=n.writeline(first)
newsecond=n.writeline(new_id_num_hex)
newthird=n.writeline(third)
newfourth=n.writeline(fourth)


#convert hex file to mfd
id_num_hex_to_card = 'xxd -r mycardUltra.hex mycardUltra.mfd'
os.system(id_num_hex_to_card)

#run command to write into the card
write_to_card = 'yes N | nfc-mfultralight w mycardUltra.mfd'
os.system(run_to_card )
