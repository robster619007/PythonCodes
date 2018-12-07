import urllib, json


url = "http://www.macs.hw.ac.uk/~hwloidl/Courses/F21SC/issuu_sample.json"

response = urllib.request.urlopen(url)

data = json.loads(response.read())

print("data")

