#連番ファイル名に変更する
import os
import glob
import sys

argsys = sys.argv
argc = len(argsys)

#コマンドライン引数が入力されていないまたは2つ以上の場合はエラーを出して終了する
if (argc != 3):
    print (r"フォルダが指定されていません")
    quit()

#連番変更したいファイルが存在するフォルダを指定する　
#コマンドライン引数を格納するリストからパスを取り出す
#[0]はこのプログラムファイルなので[1]でパスを取り出す
path  = argsys[1]
ext  = argsys[2]
#指定フォルダにあるファイル一覧を取得する
files = glob.glob(path + r"/*" + ext)
if (len(files)==0):
    print(r"指定したフォルダが見つからないかファイルがありません")

#enumerateはインデックス番号付き(かつ開始番号指定)で一覧を返す
for i,f in enumerate(files, 1):
    #ファイル名を【接頭部("img_") + 5桁連番 + 拡張子 】で変更する
    os.rename(f, os.path.join(path, "img_" + '{0:05d}'.format(i) + ext))
    print(f)
