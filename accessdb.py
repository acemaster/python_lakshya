import MySQLdb
from cardselect import *
import sys

connection=MySQLdb.connect(host="localhost",user="root",passwd="********",db="wsdc_students")
cursor=connection.cursor()
ufid=cardselect.card.uid;
rollno=input("Enter the rollno: ");
cursor.execute("SELECT * FROM student_data WHERE roll_number="+str(rollno))
row=cursor.fetchone()
print "User ",row[0]," : ",row[1]
cursor.close()
connection.close()
sys.exit
