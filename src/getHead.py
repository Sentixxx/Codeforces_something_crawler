from datetime import datetime

def get_head(title, asfile=False):
    res = "---\n"
    res += f'title: {title}\n'
    res += f'date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n'
    res += 'categories: \n'
    res += '    - 算法\n'
    res += 'tags:\n'
    res += '\n'
    res += 'cover: \n'
    res += '    /img/cover.jpg\n'
    res += 'top_img: \n'
    res += '    /img/top_img.jpg\n'
    res += '---\n\n'    
    print(res)
    if asfile:
        with open(f'file/{title}.md', 'w') as f:
            f.write(res)
    return res
    
def main():
    print('title: ')
    title = input()
    get_head(title=title, asfile=True)

if __name__ == '__main__':
    main()
    