from urllib2 import urlopen
from json import load

#sf open data source: film location in sf
apiUrl = "http://www.yerkee.com/api/fortune/wisdom"

#open the apiUrl and assign data to variable
response = urlopen(apiUrl)

json_obj = load(response)

print json_obj["fortune"]

# print json_obj