import os
import csv
import statistics

file = os.path.join("Resources","budget_data.csv")


with open(file,'r') as textio:
    csvreader = csv.reader(textio,delimiter=',')
    csv_header = next(csvreader)

    months_total = len(list(csvreader))
    textio.seek(0)
    csvreader = csv.reader(textio,delimiter=',')
    csv_header = next(csvreader)
    net_total = 0
    
    changes = []
    dates = []
    for row in csvreader:
        net_total += int(row[1])
        changes.append(int(row[1]))
        dates.append(row[0])

       
    i = 0 
    differences = []
    while i < 85:
        difference = (changes[i + 1])-(changes[i])
        i = i + 1
        differences.append(int(difference))
        
    avg_change = statistics.mean(differences)
    rounded_avg_change = round(avg_change, 2)

    greatest_increase = max(differences)
    greatest_decrease = min(differences)
    index_increase = differences.index(greatest_increase)
    index_decrease = differences.index(greatest_decrease)
    great_month = dates[index_increase+1]
    worst_month = dates[index_decrease+1]

    print("Financial Analysis")
    print("------------------------------------")
    print("Total Months: " + str(months_total))
    print("Total: $" + str(net_total))
    print("Average Change: $" +str(rounded_avg_change))
    print("Greatest Increase in Profits: " +great_month+ " $" +str(greatest_increase))
    print("Greatest Decrease in Profits: " +worst_month+ " $" +str(greatest_decrease))
    
    with open("output.txt", "w") as results:
        results.write("Financial Analysis\n")
        results.write("------------------------------------\n")
        results.write("Total Months: " + str(months_total) +"\n")
        results.write("Total: $" + str(net_total) +"\n")
        results.write("Average Change: $" +str(rounded_avg_change) +"\n")
        results.write("Greatest Increase in Profits: " +great_month+ " $" +str(greatest_increase)+"\n")
        results.write("Greatest Decrease in Profits: " +worst_month+ " $" +str(greatest_decrease)+"\n")