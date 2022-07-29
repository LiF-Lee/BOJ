import re
str = re.sub('[^0-9|^)][+-/*]|\(\)', 'ROCK', f" {input()}")

if 'ROCK' in str:
    print('ROCK')
    quit()
    
try:
    print(eval(str.replace('/', '//')))
except:
    print('ROCK')