#標準ライブラリにあるcsvモジュールをインポート
import csv

#コンテキストマネージャを利用して、csvファイルを読み出しモードで開く
with open('kadai.csv','r') as input_csv:
    #ファイルから読み出したデータを変数inputに格納する
    input = csv.reader(input_csv)
    #inputは読み出したデータの各行が要素になったリストになっているので
    #まず各行を取り出すループとその行の各要素を取り出すループの2つを回す
    for content in input:
        for i in content:
            #個々の要素は半角スペースで区切りたいので後ろに半角スペースをつける
            #また、元のデータの各行の要素は同じ行で出力したいので改行はしない
            print(i+' ',end='')
        #１行文出力したら最後に改行する
        print()
