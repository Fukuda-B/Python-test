# -*- coding: utf-8 -*-
# しょぼいカレンダーのjsonよりアニメタイトルを取得する。
import json
import requests

url = "https://cal.syoboi.jp/json.php?Req=TitleMedium"
session = requests.Session()
data = session.get(url)
json_data = json.loads(data.text.encode("utf8"))

# list型ver


def search_title(year, AnimeTitleList):
    '''しょぼいカレンダーのjsonから指定された放送開始年のタイトルを取得してリストに代入する'''
    for i in range(1, len(json_data['Titles'])):
        try:
            if (json_data['Titles'][str(i)]['FirstYear'] == str(year)):
                # print(json_data['Titles'][str(i)]['Title'])  # debag
                AnimeTitleList.append(json_data['Titles'][str(i)]['Title'])
        except KeyError:
            pass
    return AnimeTitleList

# 辞書型ver


def search_title_dic(year:str, AnimeTitleDict):
    '''しょぼいカレンダーのjsonから指定された放送開始年のタイトルを取得してTIDとタイトル名を辞書型に代入する'''
    for i in range(1, len(json_data['Titles'])):
        try:
            if (json_data['Titles'][str(i)]['FirstYear'] == str(year)):
                # print(json_data['Titles'][str(i)]['Title'])  # debag
                AnimeTitleDict[json_data['Titles']
                               [str(i)]['TID']] = json_data['Titles'][str(i)]['Title']
            
        except KeyError:
            pass
    return AnimeTitleDict


def search_subTitle(source, SearchName):
    '''辞書型に入っているタイトル名を検索タイトル名(部分一致)で探し見つかったらTIDを返す
    TIDからサブタイトルを取得しサブタイトルリストを返す'''
    subTitle = []
    # print(source)
    title: str
    for k, v in source.items():
        # print(v)
        # print(SearchName)
        # print(v.find(SearchName))
        if v.find(SearchName) == 0:
            # print(v)
            TID = k

    subTitle = get_subTitle(TID)

    return subTitle, TID


def get_subTitle(TID: str):
    '''TIDからサブタイトルを取得しリスト型で返す'''
    urlSub = "https://cal.syoboi.jp/json.php?Req=SubTitles&TID=" + TID
    # print(urlSub)
    session = requests.Session()
    data = session.get(urlSub)
    json_data1 = json.loads(data.text)

    return json_data1


if __name__ == "__main__":
    anime = []  # listの初期化
    Dic = {}  # 辞書型の初期化
    SearchName = input('検索したいタイトル文字列を入力してください : ')
    try:
        year = input('そのタイトルは何年に放送されましたか？　例) 2021 : ')
    except ValueError:
        print('半角数字で入力してください')

    print(SearchName+'で一致するタイトルを検索し、一致する場合はサブタイトルを表示します')
    # anime = search_title(2021, anime)
    # print(anime)

    search_title_dic(year, Dic)
    # print(animeDic)

    subtitle, TID = search_subTitle(Dic, SearchName)
    # print(subtitle)
    for i in range(1, len(subtitle['SubTitles'][str(TID)])+1):
        print('第'+"{:2d}".format(i)+'話 : '+subtitle['SubTitles'][str(TID)][str(i)])
