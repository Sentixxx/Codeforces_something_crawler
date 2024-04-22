import requests
from bs4 import BeautifulSoup
import json
import getopt
import sys

from login import load_session

def get_index(url):
    session = load_session('KuriyamaMashiro')
    print('request...')
    souce = session.get(url)
    print('parse...')
    soup = BeautifulSoup(souce.content, "html.parser")
    select = soup.find('select', {'name': 'submittedProblemIndex'})
    
    print('get options...')
    options = select.find_all('option')
    options = [(option.get('value'), option.text) for option in options if option.get('value') != '']
    print(options)

    print('write down json...')
    file_path_json = 'file/options.json'
    with open(file_path_json, 'w', encoding='utf-8') as f:
        json.dump(options, f)
    
def main():
    opts, args = getopt.getopt(
        sys.argv[1:],
        'u:',
        'url='
    )
    url = 'none'
    
    print(f'opts: {opts}')
    print(f'args: {args}')
    
    for opt, arg in opts:
        if opt in ('-u', '--url'):
            url = arg
    
    print(f'url: {url}')
    get_index(url)
    
    
if __name__ == '__main__':
    main()
    
    # url = 'https://codeforces.com/contest/1955'
    # get_index(url=url)