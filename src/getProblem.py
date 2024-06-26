import requests
from bs4 import BeautifulSoup
import os
from login import load_session
from getHead import get_head

CF_USERNAME = 'CF_USERNAME'
CF_PASSWORD = 'CF_PASSWORD'

def get_problem(url, write_down_file=True, head=True):
    username = os.environ.get(CF_USERNAME)
    
    session = load_session(username)
    
    print('request...')
    x = session.get(url)
    print('done\n')
    
    print('parse...')
    soup = BeautifulSoup(x.content, "html.parser")
    print('done\n')
   
    # 写入题目的描述 
    statement = soup.find(class_="problem-statement")
    
    # 题目的标题 
    header = statement.find(class_="header")
    title = header.find(class_="title").text
    print(title)
   
    if head:
        res = get_head(title)
    else:
        res = ''
   
    filename = 'file/' + title.replace('.', '_') + '.md'
    res += (f"## [{title}]({url})\n")
   
    res += '### 题目:\n'
    
    # 时间限制
    res += ("#### Limit: \n")
    time_limit = header.find(class_="time-limit")
    time_limit_text = []
    for p in time_limit:
        time_limit_text.append(p.text)
    res += (f"{time_limit_text[0]}: {time_limit_text[1]}\n")
    
    # 空间限制
    memory_limit = header.find(class_="memory-limit")
    memory_limit_text = []
    for p in memory_limit:
        memory_limit_text.append(p.text)
    
    res += (f"{memory_limit_text[0]}: {memory_limit_text[1]}\n")
    
    # 题目陈述
    res += ("#### Describe: \n")
    describe = header.next_sibling
    for p in describe:
        str = p.text
        str = str.replace("$$$", "$")
        res += (f"{str} \n")

    # 输入描述 
    res += ("#### Input: \n")
    input = describe.next_sibling
    first = True
    for p in input:
        str = p.text
        str = str.replace("$$$", "$")
        if first:
            first = False
            continue
        else:
            res += (f"{str} \n")

    # 输出描述 
    res += ("#### output: \n")
    output = describe.next_sibling
    first = True
    for p in output:
        str = p.text
        str = str.replace("$$$", "$")
        if first:
            first = False
            continue
        else:
            res += (f"{str} \n")

    # 输入说明
    res += ("#### Input-describe: \n")
    describe = describe.next_sibling
    first = True
    for p in describe:
        str = p.text
        str = str.replace("$$$", "$")
        if first:
            first = False
            continue
        else:
            res += (f"{str} \n")

    # 输出说明
    res += ("#### Output-describe: \n")
    describe = describe.next_sibling
    first = True
    for p in describe:
        str = p.text
        str = str.replace("$$$", "$")
        if first:
            first = False
            continue
        else:
            res += (f"{str} \n")

    # 样例
    example = soup.find(class_="sample-tests")
    if example:
        res += ("#### Example: \n")
        
        soup_input = example.find('pre')
        
        print(f'input:\n {soup_input.prettify()}')
        with open('file/soup_input.html', 'w') as f:
            f.write(soup_input.prettify())
        
        res += ("##### Input: \n")
        first = True
        
        cnt = 0
        for p in soup_input:
            cnt += 1
            str = p.text
            str = str.replace("$$$", "$")
            res += (f"{str} \n")
        print(f'cnt: {cnt}')
        
        output = example.find(class_="output")
        res += ("##### Output: \n")
        first = True
        for p in output:
            if first:
                first = False
                continue
            str = p.text
            str = str.replace("$$$", "$")
            res += (f"{str} \n")
        
    res += ("### 思路\n\n")

    res += ("### 代码\n\n")
    code, lang = getCode(url)
    print(f'code: {code}, lang: {lang}')
    if lang != '':
        print(lang)
        if lang[:3] == 'C++':
            lang = 'cpp'
        elif lang[:2] == 'Py':
            lang = 'python'
        res += (f"```{lang}\n")
        res += code
        res += ("\n```\n")


    # 查看结果
    # print(res)
    
    # 如果选择写入文件，则写入
    if write_down_file:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(res)
    
    # 返回结果
    return res    

def getCode(url):
    username = os.environ.get(CF_USERNAME)
    
    session = load_session(username)
    
    print('request...')
    response = session.get(url)
    print('done\n')
    
    print('parse...')
    soup_problem = BeautifulSoup(response.content, "html.parser")
    print('done\n')
    
#     with open('page_problem.html', 'w', encoding='utf-8') as f:
#         f.write(soup_problem.prettify())    

    # 提取代码地址
    address = soup_problem.find('span', {'class': 'verdict-accepted'})
    if not address:
        return '', ''
    
    address = address.parent.find_previous_sibling().find_previous_sibling().find('a').get('href')
    address = 'codeforces.com' + address
    print(address)
    
    print('request...')
    response = session.get('https://' + address)
    print('done\n')
    print('parse...')
    soup_code = BeautifulSoup(response.content, "html.parser")
    print('done\n')
    
   #  with open('page_code.html', 'w', encoding='utf-8') as f:
        # f.write(soup_code.prettify())

    code = soup_code.find('pre', {'id': 'program-source-text'}).text

    lang = soup_code.find('span', {'class': 'verdict-accepted'}).parent.find_previous_sibling().text.strip()
    
    return code, lang


def main():
    url = 'https://codeforces.com/contest/1554/problem/B'
    get_problem(url)

if __name__ == '__main__':
    main()