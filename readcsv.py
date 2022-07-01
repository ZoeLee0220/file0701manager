import pandas
import sqlite3
dt='2022-06-23'
a=pandas.read_csv('./$RJ31Z2V.csv',encoding='gbk')
# a.to_sql()
print(a)
conn=sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

for index, row in a.iterrows():
    # print(index,row['作者'])
	cursor.execute(f"insert into papers_papers values({index+1}, '{row['题目']}', '{row['所属板块']}', '{row['所属板块']}', '空', '空', '空', '{dt}', 1, '空')")
Tables=cursor.fetchall()
print(Tables)
conn.commit()
cursor.close()
conn.close()