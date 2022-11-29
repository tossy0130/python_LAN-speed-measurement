import subprocess
from unittest import result
import sys
import os
import datetime
import time
import re


hosts = ["192.168.254.204"]

result_arr = []
res_str = ""
for host in hosts:
    res = subprocess.run(
        ["ping", host, "-n", "10", "-l", "60000"], stdout=subprocess.PIPE)

    print(res.stdout.decode("cp932"))

    if res.returncode == 0:
        print("成功\n")
        print(res.stdout.decode("cp932"))

        result_arr = res.stdout
        res_str = res.stdout.decode("cp932")

    else:
        print("失敗\n\n")


print("========= テスト出力 =========" + "\n\n" + res_str)


def speed_calculation(res_str):

    ttt = re.search(r'(?<=最大 = ).*?(?=ms、平均)', res_str)

    print('=== 取得 ===' + ttt.group())

    t_tmp = int(ttt.group()) / 1000

    k = (60000 * 2) / t_tmp
    result_num = k / 1048576

    return '{:.1f}'.format(result_num)


result = speed_calculation(res_str)
print("出力：：：" + result)
