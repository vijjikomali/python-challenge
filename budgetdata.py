import csv
import os
os.chdir('C:/Users/Vijayalaskmi/Desktop/ROOT FOLDER/PREWORK-VJK/MODULE3/homework')

file_to_load = os.path.join("Resources","budget_data.csv")
file_to_output = os.path.join("Output", "budget.txt")

# we have to initialize some variables so that we can run the loop when we create!
# read csv file and convert into dictioneries of list

with open(file_to_load) as financial_data:
    
    reader = csv.reader(financial_data)
    
    # to count the columns we have to skip the header
    header = next(reader)
    Months=[]
    total_months = []
    net_profit = []
    mon_avg_change  = []
    rev_change_list = []
    highest_profit = 0
    lowest_profit = 0
    monthly_change=[]
   # print(header)

    # adding total months by counting row
    for row in reader:
        total_months.append(row[0])
        # adding total profit using append adding each row
        net_profit.append(row[1])
        Months.append(row[0])
#   print(net_profit[85])

    # Calculating average change / needs to find the difference between
    # each row and adding them
    for i in range(len(net_profit)-1):
        mon_avg_change.append(int(net_profit[i+1])- int(net_profit[i]))
        monthly_change.append(Months[i])
       
#    print(sum(mon_avg_change)/len(mon_avg_change))

   # finding the greatest increase of the profit and 
   # finding greatest decrease of loss 
    highest_profit = max(mon_avg_change)
    lowest_profit = min(mon_avg_change)

   # print(highest_profit)
    #print(lowest_profit)

    # # using the monthly index locating hightest and lowest profit per mon
    highest_profit_mon = monthly_change[(mon_avg_change.index(highest_profit))+1]
    lowest_profit_mon = monthly_change[(mon_avg_change.index(lowest_profit))+1]

    # print(highest_profit_mon)
    # print(lowest_profit_mon)
   
    # # statemt Financials output result
    # print("Financial  analysis")
    # print("--------------------------------")
    # #Q1 printing the total months
    # print("Total Number of Months - ",total_months)
    # #Q2 - Net Profit / Loss
    # print("Net Profit/Loss - $", net_profit)
    # #Q3 - average change in months
    # print(f"Average Change: {round(sum(monthly_avg_change/len(monthly_avg_change),2)}")
    # # Q4 - printing Greatest Increase of profits
    # print(f"Greatest Increase in Profits: {total_months[highest_profit]} (${(str(highest_profit))})")
    # #Q5 - printing Greatest Decrease of profits
    # print(f"Greatest Decrease in Profits: {total_months[lowest_profit]} (${(str(lowest_profit))})")

output=(
f"\n Financial Analysis \n"
f"---------------------------- \n"  
f" Total Months: {len(total_months)} \n"
f" Total: $ {sum([int(x) for x in net_profit])} \n"
f" Average  Change: $ {sum(mon_avg_change)/len(mon_avg_change)}\n"  
f" Greatest Increase in Profits: {str(highest_profit_mon)} {str(highest_profit)} \n"
f" Greatest Decrease in Profits:{str(lowest_profit_mon)}{(str(lowest_profit))}\n"
)


with open(file_to_output,"w+") as text_file:
    text_file.write(output)