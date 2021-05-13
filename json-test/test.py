import json
import requests

url = "http://cal.syoboi.jp/json.php"
session = requests.Session()
data = session.get(url)
json_data = json.loads(data.text)
print(json_data['Titles']['1'])
