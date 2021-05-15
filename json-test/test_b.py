'''
    年ごとに保存するびぃ
'''

import os
import json
import requests

url = "http://cal.syoboi.jp/json.php?Req=TitleLarge"
save_dir = "/dataset/"


def tvList_get(url):
    ''' Get tv program list '''
    session = requests.Session()
    data = session.get(url)
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

def tvList_save(tv_l):
    ''' Save tv program list '''
    print(os.getcwd())
    os.chdir(os.getcwd()+save_dir)
    for i in tv_l.keys():
        fp = open(i+'.txt', 'w', encoding='UTF-8')
        fp.write('\n'.join(tv_l[i]))
        fp.close


if __name__ == '__main__':
    tv_l = tvList_get(url)
    tvList_save(tv_l)
