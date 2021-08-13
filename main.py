#!/usr/bin/env python3
# xmlファイルから、csvファイルに変換するモジュール

import xml.etree.ElementTree as ET
import csv
import pandas as pd
import datetime

# 時間の取得
dt_now = datetime.datetime.now()
# 衝突を防ぐために1分後に実行する
dt_int = int(dt_now.strftime('%Y%m%d%H%M')) - 1


# ファイルの保存先
path_w = f'/home/vagrant/workspace/itunes-ranking/itunes-ranking-{dt_int}.csv' 

# 読み込むファイル(xml形式)
xml_read = f"/home/vagrant/workspace/itunes-topsong-rss/hourly-ranking-{dt_int}.xml"
xmlns = "{http://www.w3.org/2005/Atom}"

# 変換を行う関数
def convert():
  titles = []
  tree = ET.parse(xml_read)
  root = tree.getroot() # 最上位の要素を取り出す(feedタグ)

  # entryより下の階層を取り出す(title)
  for entry in root.findall(f'{xmlns}entry'):
    title = entry.find(f'{xmlns}title').text
    titles.append(title)

  for i in range(0,100):
    print(f"{i + 1}位：{titles[i]}")

  # データフレームに変換して、csvファイルに書き込む
  titles_df = pd.DataFrame({'ranking':titles})
  titles_df.to_csv(path_w, header=False, index=False)

convert()