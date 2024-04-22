from getopt import getopt
import sys
from getContest import get_contest
from getProblem import get_problem

print('main')

# 获取参数
opts, args = getopt(
    sys.argv[1:],
    "u:p:i:o:",
    ["url=", "problems=","id=", "only="]
)

# 获取比赛网址
url = ''
problems = []
for opt, arg in opts:
    print(opt, arg)
    
    if opt in ('-u', '--url'):
        url = arg
    if opt in ('-p', '--problems'):
        problems = arg.split(',')
        print(problems)
    if opt in ('-i', '--id'):
        url = f'https://codeforces.com/contest/{arg}'
    if opt in ('-o', '--only'):
        url = arg
        get_problem(url=url)
        sys.exit()


print(url)
print(problems)

# 获取比赛题目
get_contest(url, problems)
