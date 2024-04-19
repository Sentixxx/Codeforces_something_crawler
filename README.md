# README
## prepare
```
pip install -r requirements.txt
```
## how to use
example:
```
python src/main.py -u https://codeforces.com/contest/1956 -p a,b,c,d
```
- `-u, --url`
- `-p, --problems`
## setting
if you want, you can add environment variables with such format:
```
CF_USERNAME = 'your_username'
CF_PASSWORD = 'your_password'
```
to auto fetch your latest accepted code for each problem above.