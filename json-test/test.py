# しょぼいカレンダーのjsonよりアニメタイトルを取得する。

import json
import requests

url = "https://cal.syoboi.jp/json.php?Req=TitleLarge"
session = requests.Session()
data = session.get(url)
json_data = json.loads(data.text)


def search_title(year, AnimeTitleList):
    for i in range(1, 100000):
        try:
            if (json_data['Titles'][str(i)]['FirstYear'] == str(year)):
                #print(json_data['Titles'][str(i)]['Title'])       #debag
                AnimeTitleList.append(json_data['Titles'][str(i)]['Title'])
        except KeyError:
            pass
    return AnimeTitleList
