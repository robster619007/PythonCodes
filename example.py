import json
from json import *
import re
from urllib.request import urlopen 

with urlopen("http://www.macs.hw.ac.uk/~hwloidl/Courses/F21SC/issuu_sample.json") as response:
    src = response.read()

doc = json.load(src)
print(doc)
print(type(doc))