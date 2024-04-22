import requests
from bs4 import BeautifulSoup
import os

from getProblem import get_problem
from getHead import get_head
from login import login

CF_USERNAME = 'CF_USERNAME'
CF_PASSWORD = 'CF_PASSWORD'

def get_contest(url, problems_=[], head=True):    
    username = os.environ.get(CF_USERNAME)
    password = os.environ.get(CF_PASSWORD)

    login(username, password)    
    
    # 输出比赛网址
    print(url)
    
    # 获得比赛名称与题目数量
    homepage = requests.get(url)
    soup_homepage = BeautifulSoup(homepage.content, "html.parser")
    contest = soup_homepage.find(class_="left").text
    num = len(soup_homepage.findAll(class_="id"))

    problems = problems_
    for i in range(len(problems)):
        problems[i] = problems[i].upper()    
    
    # 输出题目列表
    print(f"problems: {problems}")
    print('')
    
    # 创建md文件
    filename = 'file/' + contest.replace(' ', '_') + '.md'
    res = get_head(contest)
    # with open(filename, "w", encoding="utf-8") as f:
    #     f.write(f"# [{contest}]({url})\n")
    res += f'# [{contest}]({url})\n'

#     with open(filename, "a", encoding="utf-8") as f:
        # 获取对应的题目信息 
    for problem in problems:
        # 获取题目的url与html
        nurl = url + "/problem/" + problem 
        print(nurl)

        # 获取题目结果
        res += get_problem(nurl, write_down_file=False, head=False)
        
        # 写入文件
        # f.write(res)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(res)
        
def main():
    get_contest("https://codeforces.com/contest/1554", ['A', 'B', 'C', 'D', 'E', 'F'])
    
if __name__ == '__main__':
    main()