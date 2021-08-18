import re


def regex_extract(filename): #本研究は、Xを構築する
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            res = re.findall('本研究は、(.*)を構築する', line)
            if len(res) > 0:
                print(res)

def regex_extract(filename): #本研究では、YのためのXを開発する
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            res = re.findall('本研究では、(.*)のための(.*)を構築する', line)
            if len(res) > 0:
                print(res)

regex_extract('kaken_line.txt')