import requests
from bs4 import BeautifulSoup
import pickle

session = requests.Session()  # 使用会话来保持cookie

def save_html(html, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
        
def save_session(session, username):
    filename = '../user/' + username + '.pkl'
    with open(filename, 'wb') as f:
        pickle.dump(session, f)
        
def load_session(username):
    filename = '../user/' + username + '.pkl'
    with open(filename, 'rb') as f:
        return pickle.load(f)

def login(username, password):
    global session
    
    login_url = 'https://codeforces.com/enter?back=%2F'
    
    print('get login page...')
    page_login = session.get(login_url)
    soup = BeautifulSoup(page_login.content, "html.parser")
    # save_html(soup.prettify(), 'login.html')
    print('done')
        
    # 从HTML中提取CSRF令牌
    csrf_token = soup.find('input', {'name': 'csrf_token'}).get('value')
    
    print(f"crypto token: {csrf_token}")
    
    data = {
        "handleOrEmail": username, 
        "password": password,
        "csrf_token": csrf_token,  # 添加CSRF令牌
        "query": "",
        "action": "enter",
        "ftaa": "",
        "bfaa": "",
        "remember": "off",
        "submit": "Login"
    }

    print('login ...')    
    response = session.post(login_url, data=data)
    print(response.status_code)
    # save_html(response.text, 'login_response.html')
    save_session(session, username)
    print('done')
    
    return session
    
def main():
    login('KuriyamaMashiro', '')

if __name__ == '__main__':
    main()