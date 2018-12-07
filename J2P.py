import json
from json import *
import re
from urllib.request import urlopen 

#with urlopen("http://www.macs.hw.ac.uk/~hwloidl/Courses/F21SC/issuu_sample.json") as response:
    #src = response.read().decode("utf-8")

with urlopen("http://www.macs.hw.ac.uk/~hwloidl/Courses/F21SC/issuu_cw2.json") as response:
    src = response.read().decode()

NOT_WHITESPACE = re.compile(r'[^\s]')

def decode_stacked(document, pos=0, decoder=JSONDecoder()):
    while True:
        match = NOT_WHITESPACE.search(document, pos)
        if not match:
            return
        pos = match.start()

        try:
            obj, pos = decoder.raw_decode(document, pos)
        except JSONDecodeError:
            # do something sensible if there's some error
            raise
        yield obj
   

x = []
for obj in decode_stacked(src):
    x.append(obj)
print("\n\t\t------------JSON Format After Dumps-----------------------------------\n")



D = {'Visitor' : x }
with open("visitor.json","w") as outfile:
    D = json.dumps(D, indent = 2)
    json.dump(D, outfile)
print(D)

#Load_D = json.loads(D)
print("\n\t\t------------JSON Format after Loads-----------------------------------\n")
with open('visitor.json','r') as infile:
    data = json.load(infile)
    print("Data\n" + data)

Data = json.loads(data)
Vid = []
Vbrowser = []
Vcountry = []

for i in Data['Visitor']:
    Vid.append(i['visitor_uuid'])
    Vbrowser.append(i['visitor_useragent'])
    Vcountry.append(i['visitor_country'])   
    
print("Visitor ids:")
print(Vid)
print("\nVisitor Browser:")
print(Vbrowser)
print("\nVisitor Country:")
print(Vcountry)