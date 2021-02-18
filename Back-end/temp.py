import csv
with open('user-transaction.csv','a',newline='') as f:
    thewriter = csv.writer(f)
    temp = ['ID','TOTAL']
    thewriter.writerow(temp)
    for i in range(1,101):
        temp = [i,0]
        thewriter.writerow(temp)
