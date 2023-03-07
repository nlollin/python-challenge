import os
import csv
import statistics

file = os.path.join("Resources","budget_data.csv")


with open(file,'r') as textio:
    csvreader = csv.reader(textio,delimiter=',')
    csv_header = next(csvreader)

    #count the total number of months
    months_total = len(list(csvreader))

    #return to the top of the file
    textio.seek(0)
    csvreader = csv.reader(textio,delimiter=',')
    csv_header = next(csvreader)
    #start net total at 0
    net_total = 0
    
    #create list to store the profit/losses from month to month 
    #create list to store the dates on record
    profit_loss = []
    dates = []

    #loop through each row
    #sum the profits/losses each month to calculate the net total
    #record the profit/losses & the dates in their own separate lists
    for row in csvreader:
        net_total += int(row[1])
        profit_loss.append(int(row[1]))
        dates.append(row[0])

    #create a list to store the differences in profits/losses from month to month   
    i = 0 
    differences = []

    #loop through every row with the exception of the last row
    while i < 85:
        #calculate the difference between the profits/losses in the current row & the following row
        #add that value to the differences list
        difference = (profit_loss[i + 1])-(profit_loss[i])
        i = i + 1
        differences.append(int(difference))

    #calculate the average difference using the imported statistics module
    #round to the appropriate number of decimal places    
    avg_change = statistics.mean(differences)
    rounded_avg_change = round(avg_change, 2)

    #calculate the greatest increase and decrease
    greatest_increase = max(differences)
    greatest_decrease = min(differences)

    #Find the location of the greatest increase & decrease in the list
    index_increase = differences.index(greatest_increase)
    index_decrease = differences.index(greatest_decrease)

    #Find the month associated with the greatest increase & decrease
    great_month = dates[index_increase+1]
    worst_month = dates[index_decrease+1]

    #print results
    print("Financial Analysis")
    print("------------------------------------")
    print("Total Months: " + str(months_total))
    print("Total: $" + str(net_total))
    print("Average Change: $" +str(rounded_avg_change))
    print("Greatest Increase in Profits: " +great_month+ " $" +str(greatest_increase))
    print("Greatest Decrease in Profits: " +worst_month+ " $" +str(greatest_decrease))
    
    #print results again in a text file
    with open("output.txt", "w") as results:
        results.write("Financial Analysis\n")
        results.write("------------------------------------\n")
        results.write("Total Months: " + str(months_total) +"\n")
        results.write("Total: $" + str(net_total) +"\n")
        results.write("Average Change: $" +str(rounded_avg_change) +"\n")
        results.write("Greatest Increase in Profits: " +great_month+ " $" +str(greatest_increase)+"\n")
        results.write("Greatest Decrease in Profits: " +worst_month+ " $" +str(greatest_decrease)+"\n")