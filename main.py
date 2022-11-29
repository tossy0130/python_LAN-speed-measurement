import subprocess
from unittest import result
import sys
import os
import datetime
import time
import re

import schedule
from time import sleep

# 01

# === 日付け取得


def get_timestamp():
    date = datetime.datetime.now()
    timestamp = str(date.strftime('%Y-%m-%d %H:%M:%S'))
    return timestamp


def Make_dir(path_w):

    try:
        if(os.path.isdir(path_w)):
            pass
        else:
            os.makedirs(path_w)
    except FileExistsError:
        print('関数名:Check_Dir ::: ディレクトリ作成エラー')

# === 速度計算　関数


def speed_calculation(res_str):

    ttt = re.search(r'(?<=最大 = ).*?(?=ms、平均)', res_str)

    print('=== 取得 ===' + ttt.group())

    t_tmp = int(ttt.group()) / 1000

    k = (60000 * 2) / t_tmp
    result_num = k / 1048576

    return '{:.1f}'.format(result_num)


def Ping():
    hosts = ["192.168.254.204"]

    result_arr = []
    for host in hosts:
        res = subprocess.run(
            ["ping", host, "-n", "10", "-l", "60000"], stdout=subprocess.PIPE)

        print(res.stdout.decode("cp932"))

        if res.returncode == 0:
            print("成功\n")
            print(res.stdout.decode("cp932"))
            result_arr = res.stdout.decode("cp932")

            return res.stdout

        else:
            print("失敗\n\n")


def Go_Speed_Search():

    # デスクトップのパス　取得
    desktop_dir = os.path.expanduser(r'~/Desktop\\server_speed_search\\')
    Make_dir(desktop_dir)
    path_w = r'~/Desktop\\server_speed\\encoding.txt'
    if not os.path.isfile(desktop_dir + "encoding.txt"):
        with open(desktop_dir + "encoding.txt", "w") as f:
            timestamp = get_timestamp()
            f.write(" --------" + timestamp + "--------" + '\r\n')
            f.write("sys.stdout.encoding = " + sys.stdout.encoding + "\r\n")
            f.write("sys.getdefaultencoding() = " +
                    sys.getdefaultencoding() + "\r\n")
            ping_str = Ping()
            f.write(ping_str.decode('cp932').strip() + "\r\n")
            result_speed = speed_calculation(ping_str.decode('cp932') + "\r\n")
            f.write("回線速度：" + result_speed + 'Mbytes/s' + "\r\n")
            f.write("================================================" + "\r\n")
    else:
        with open(desktop_dir + "encoding.txt", "a") as f:
            timestamp = get_timestamp()
            f.write(" --------" + timestamp + "--------" + '\r\n')
            f.write("sys.stdout.encoding = " + sys.stdout.encoding + "\r\n")
            f.write("sys.getdefaultencoding() = " +
                    sys.getdefaultencoding() + "\r\n")
            ping_str = Ping()
            f.write(ping_str.decode('cp932').strip() + "\r\n")
            result_speed = speed_calculation(ping_str.decode('cp932'))
            f.write("回線速度：" + result_speed + 'Mbytes/s' + "\r\n")
            f.write("================================================" + "\r\n")

 # 02 スケジュール登録
schedule.every(30).seconds.do(Go_Speed_Search)

# 03 イベント実行
while True:
    schedule.run_pending()
    sleep(1)
