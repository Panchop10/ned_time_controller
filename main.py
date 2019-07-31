import os
import codecs

read_card = 'nfc-mfultralight r mycardUltra.mfd'
os.system(read_card)

card_to_hex = 'xxd mycardUltra.mfd > mycardUltra.hex'
os.system(card_to_hex)



id_num_hex=card_to_hex[:19]
print(id_num_hex)
# id_num_hex1=id_num_hex.replace(' ', '').rstrip('0')
#
# if (len(id_num_hex1))%2 == 1:
#     id_num=id_num_hex1 + "0"
# os.system(id_num)
#
#
#
# id_num = codecs.decode(id_num, 'hex').decode('ascii')
#
# if text_hex== "":
#     print("is empty")
# os.system(id_num)
#
#
# write_card = 'yes N | nfc-mfultralight w mycardUltra.mfd'
# os.system(write_card)
