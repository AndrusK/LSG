import random
import string
import requests
import json
import sys


#print(len(sys.argv))
if len(sys.argv) < 3:
    amount = 0
    print("Usage: serials.py <output file> <serials to generate>")
    sys.exit()
else:
    file = sys.argv[1]
    amount = int(sys.argv[2])


serials = []
working_serials = []
prefix = ["PF","MP", "R9", "MJ"]
infix = ["0","1"]
upper_alphabet = string.ascii_uppercase
postfix = ["0","1","2","3","4","5","6","7","8","9"]

def makeSerial():
    return random.choice(prefix) + random.choice(infix) + random.choice(upper_alphabet) + random.choice(upper_alphabet) + random.choice(upper_alphabet) + random.choice(upper_alphabet) + random.choice(postfix)


for i in range(1,amount):
    serials.append(makeSerial())

for serial in serials:
    r = requests.get("https://pcsupport.lenovo.com/us/en/api/v4/mse/getproducts?productId="+ serial)
    if "id" in r.text:
        x = json.loads(r.text)
        print(x[0]["Serial"] + " : " + x[0]["Id"])
        working_serials.append(x[0]["Serial"] + " : " + x[0]["Id"])
        
with open(file, 'w') as file_handler:
    for item in working_serials:
        file_handler.write("{}\n".format(item))
