import pymysql
conn = pymysql.connect(db='testapp', user='root', passwd='helloworld', host='localhost',port=3308)
cur = conn.cursor()
cur.execute("select * from testapp.Teams")
allTeams=cur.fetchall()[0][0]
print(allTeams)
