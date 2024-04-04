# codeforces_contest_information_crawler

## 描述

给定比赛，爬取每个题目的信息，以markdown形式保存

## 使用

进入FILES文件夹

### 使用url指定比赛

- python main.py -u \<url>

- python main.py --url=\<url>

例如：

python main.py -u https://codeforces.com/contest/1945

python main.py --url=https://codeforces.com/contest/1945

### 使用索引指定比赛

- python main.py -i \<index>
- python main.py --index=\<index>

例如：

python main.py -i 1945

python main.py --index=1945

### 指定题目列表

#### 范围指定

- python main.py -p \<start>-\<end>
- python main.py --problem=\<start>-\<end>

例如：

python main.py -p A-D

python main.py --problem=A-D

#### 逐个指定

- python main.py -p \<problem1>,\<problem2>,...
- python main.py --problem==\<problem1>,\<problem2>,...

例如：

python main.py -p A,C,F

python main.py --problem=A,C,F

### 获取帮助

[**项目文档**](https://github.com/KuriSh32/codeforces_contest_information_crawler)

- python main.py -h

- python main.py --help

## 库依赖

- requests
- BeautifulSoup4