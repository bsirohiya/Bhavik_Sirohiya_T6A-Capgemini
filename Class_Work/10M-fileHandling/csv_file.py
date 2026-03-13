import csv
from datetime import date

file = open("csv_file.csv", "a+")

w = csv.writer(file)
w.writerow(['DATE', 'CATEGORY', 'AMOUNT']) # For column names
w.writerows([ 
    [date.today(), "Travel", 200],
    [date.today(), "Food", 100],
    [date.today(), "Timepass", 50]
])

file.close()