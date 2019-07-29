import os

read_card = 'nfc-mfultralight r mycardUltra.mfd'
os.system(read_card)

card_to_hex = 'xxd mycardUltra.mfd > mycardUltra.hex' 
os.system(card_to_hex)


