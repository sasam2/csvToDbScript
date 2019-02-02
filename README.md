#csvToDB

Application to read cvs file to DB table.

- DB (sqlite3) file is csvdata.db 
- csv file is provided as argument (commas within double quotes not admissible)
- Table is (deleted and) recreated each call, according to csv table header

#Usage

./run.sh <testfile>

Ex.: ./run.sh ./test/TechCrunchcontinentalUSA.csv

Or
python csvtodb.py <testfile>

Ex.: python csvtodb.py ./test/TechCrunchcontinentalUSA.csv


#Prerequisites
python 3.7

