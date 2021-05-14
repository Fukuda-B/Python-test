'''
    Syoboi B

    SyoboiB.tvList_update()
    -> リストの取得、self.allに入れておく。
    
    SyoboiB.tvList_get()
    -> リストの取得。

    SyoboiB.tvList_search(year)
    -> self.allから、yearのリスト取得。
'''

import json
import requests

class SyoboiB:

    def __init__(self):
        self.url = "https://cal.syoboi.jp/json.php?Req=TitleLarge"
        self.all = SyoboiB.tvList_get(self)
    
    def tvList_update(self):
        ''' update all list '''
        self.all = SyoboiB.tvList_get(self.url)

    def tvList_get(self):
        ''' get all list '''
        session = requests.Session()
        data = session.get(self.url)
        json_data = json.loads(data.text)

        map_dict = {}

        for i in range(1, len(json_data['Titles'])):
            year = str(json_data['Titles'][str(i)]['FirstYear'])
            tit = json_data['Titles'][str(i)]['Title']

            if year in map_dict:
                map_arr = list(map_dict[year])
            else:
                map_arr = []

            map_arr.append(tit)
            map_dict[year] = map_arr
        return map_dict

    def tvList_search(self, year):
        ''' search the list in year '''
        if str(year) in self.all: return self.all[str(year)]
        return []

# ----- 

    def search_title(year, AnimeTitleList):
        ''' update AnimeTItleList '''
        session = requests.Session()
        data = session.get(url)
        json_data = json.loads(data.text)

        for i in range(1, len(json_data['Titles'])):
            try:
                if (json_data['Titles'][str(i)]['FirstYear'] == str(year)):
                    AnimeTitleList.append(json_data['Titles'][str(i)]['Title'])
            except KeyError:
                pass
        return AnimeTitleList

 # -----
 
if __name__ == '__main__':
    syobo = SyoboiB()
    res = syobo.tvList_search('2021')
    print(res)
