import requests
from bs4 import BeautifulSoup

from getProblem import get_problem

def get_contest(url, problems_=[]):    
    # 输出比赛网址
    print(url)
    
    # 获得比赛名称与题目数量
    homepage = requests.get(url)
    soup_homepage = BeautifulSoup(homepage.content, "html.parser")
    contest = soup_homepage.find(class_="left").text
    num = len(soup_homepage.findAll(class_="id"))

    # 选择有效的比赛列表
    problems = []
    if problems_:
        # 如果传入的题目在实际比赛题目范围内，则添加
        for problem in problems_:
            if ord('A') <= ord(problem) and ord(problem) < ord('A') + num:
                problems.append(problem)
    else:
        # 如果未选择problems或者传入空列表，则默认选择所有的题目
        for problem in range(ord('A'), ord('A') + num):
            problems.append(chr(problem))
    
    # 输出题目列表
    print(f"problems: {problems}")
    print('')
    
    # 创建md文件
    filename = '../file/' + contest.replace(' ', '_') + '.md'  
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# [{contest}]({url})\n")

    with open(filename, "a", encoding="utf-8") as f:
        # 获取对应的题目信息 
        for problem in problems:
            # 获取题目的url与html
            nurl = url + "/problem/" + problem 
            print(nurl)

            # 获取题目结果
            res = get_problem(nurl, False)
            
            # 写入文件
            f.write(res)
            
def main():
    get_contest("https://codeforces.com/contest/1554", ['A', 'B', 'C', 'D', 'E', 'F'])
    
if __name__ == '__main__':
    main()