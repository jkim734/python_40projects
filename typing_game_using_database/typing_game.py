import random
import time
import winsound
import sqlite3
import datetime

conn = sqlite3.connect('C:/python_basic/resource/records.db', isolation_level= None)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS records( id INTEGER PRIMARY KEY AUTOINCREMENT, cor_cnt INTEGER, record text, regdate text)")

words = [] #영어 단어 리스트 로드
n = 1 #게임 시도 횟수
cor_cnt = 0 #정답 개수

with open('./typing_game_using_database/resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())

a = input("Ready? Press Enter Key!") #Enter game start!
start = time.time()

while n <= 5:
    random.shuffle(words)
    q = random.choice(words)

    print()

    print("*Question # {}".format(n))
    print(q) #문제 출력
    x = input() #타이핑 입력

    print()

    if str(q).strip() == str(x).strip():
        print("Pass!")
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
        cor_cnt += 1

    else:
        winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
        print("Wrong!")

    n += 1

end = time.time()
et = end - start
et = format(et, ".3f")

if cor_cnt >= 3:
    print("합격")
else:
    print('불합격')

cursor.execute("INSERT INTO records('cor_cnt', 'record', 'regdate') VALUES (?, ?, ?)",
(cor_cnt, et, datetime.datetime.now().strftime('%Y - %m - %d %H:%M:%S')))

print("게임시간: ", et, '초', '정답 개수 : {}'.format(cor_cnt))
if __name__ == "__main__":
    pass