import os
import codecs

read_card = 'nfc-mfultralight r mycardUltra.mfd'
os.system(read_card)

card_to_hex = 'xxd mycardUltra.mfd > mycardUltra.hex'
os.system(card_to_hex)

f=open("mycardUltra.hex","r")
first=f.readline()
second=f.readline()

id_num_hex=second[9:18]
id_num_hex1=id_num_hex.replace(' ', '').rstrip('0')
print(id_num_hex1)



#if (len(id_num_hex1))%2 == 1:
#   id_num=id_num_hex1 + "0"
#os.system(id_num)

#id_num = codecs.decode(id_num, 'hex').decode('ascii')

#print(id_num)

# if text_hex== "":
#     print("is empty")
# os.system(id_num)


# write_card = 'yes N | nfc-mfultralight w mycardUltra.mfd'
# os.system(write_card)

