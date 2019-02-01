import sqlite3
import sys

if len(sys.argv)==1:
    print('No input file provided.')
    exit(1)

filename = sys.argv[1]
file = open(filename, "r")

header = file.readline()
conn = sqlite3.connect('csvdata.db')
c = conn.cursor()

column_names = header.split(',')

strg=''
for col in column_names:
    strg=strg+','+col+' text'
strg=strg[1::]

c.execute('DROP TABLE IF EXISTS csvdata')
c.execute('CREATE TABLE csvdata('+strg+')')
conn.commit()

lnCnt=0
for line in file:
    vals = line.split(',')
    lineVals = ''
    for v in vals:
        lineVals = lineVals + ', \''+v.replace('\'', '\'\'')+'\'' #csv with commas within quotes not supported
    lineVals=lineVals[1::]
    c.execute('INSERT INTO csvdata VALUES ('+lineVals+')')
    lnCnt=lnCnt+1

conn.commit()

rwCnt=c.execute('SELECT COUNT(*) FROM csvdata').fetchone()[0]

conn.close()

print(str(lnCnt)+' records inserted. Total table records are '+str(rwCnt)+'.')
