# しょぼいカレンダーのjsonよりアニメタイトルを取得する。

import json
import requests

url = "https://cal.syoboi.jp/json.php?Req=TitleMedium"
session = requests.Session()
data = session.get(url)
json_data = json.loads(data.text)

# list型ver
def search_title(year, AnimeTitleList):
    for i in range(1, len(json_data['Titles'])):
        try:
            if (json_data['Titles'][str(i)]['FirstYear'] == str(year)):
                print(json_data['Titles'][str(i)]['Title'])  # debag
                AnimeTitleList.append(json_data['Titles'][str(i)]['Title'])
        except KeyError:
            pass
    return AnimeTitleList

# 辞書型ver
def search_title_dic(year, AnimeTitleDict):
    for i in range(1, len(json_data['Titles'])):
        try:
            if (json_data['Titles'][str(i)]['FirstYear'] == str(year)):
                #print(json_data['Titles'][str(i)]['Title'])  # debag
                AnimeTitleDict[json_data['Titles']
                               [str(i)]['TID']] = json_data['Titles'][str(i)]['Title']
        except KeyError:
            pass
    return AnimeTitleDict

def search_subTitle(source, SearchName):
    subTitle=[]
    try:
        if SearchName in source.values():
            print('True')
            TID = source.get('TID')
            subTitle = get_subTitle(TID)
                
    except:
        pass

    return subTitle

def get_subTitle(TID):
    urlSub = "https://cal.syoboi.jp/json.php?Req=SubTitles&TID=" + TID
    session = requests.Session()
    data = session.get(urlSub)
    json_data1 = json.loads(data.text)

    return json_data1
    

if __name__ == "__main__":
    anime = []
    Dic = {}
    SearchName="イジらないで"
    anime = search_title(2021, anime)
    # print(anime)

    animeDic = search_title_dic(2021, Dic)
    #print(animeDic)

    subtitle=search_subTitle(animeDic,SearchName)
    print(subtitle)
