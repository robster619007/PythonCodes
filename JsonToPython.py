import json
from json import *
import re
from urllib.request import urlopen 

with urlopen("http://www.macs.hw.ac.uk/~hwloidl/Courses/F21SC/issuu_sample.json") as response:
    src = response.read().decode("utf-8")

#with urlopen("http://www.macs.hw.ac.uk/~hwloidl/Courses/F21SC/issuu_cw2.json") as response:
    #src = response.read().decode()

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
D = json.dumps(D, indent = 2)
print(D)
Load_D = json.loads(D)
print("\n\t\t------------JSON Format after Loads-----------------------------------\n")
print(Load_D)
print("\n\t\t------------------------------------------After for-----------------------------------\n")
vList = []
for item in Load_D['Visitor']:
    Visitor_ID = item['visitor_uuid']
    vList.append(Visitor_ID)
    print(Visitor_ID)
print("\n\t\t------------------------------------------out of for-----------------------------------\n")

print(vList)
