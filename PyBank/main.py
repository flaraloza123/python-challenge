# import modules needed to analyze csv files
import csv
import os

#Set path to csv file to be analyzed
csvdata=os.path.join("Resources","budget_data.csv")

#Set path for output txt file
output_txt= os.path.join("analysis","BudgetAnalysis.txt")


#create variables needed for analysis
total_months = 0
total_revenue = 0
profit_loss = []
average_change = []
pl_change = []
date = []
#open csv file
with open(csvdata) as csvfile:

    csvread=csv.reader(csvfile, delimiter=",")

    #skip the header row
    header= next(csvread)
    
    #create for loop to read rows after header row
    for row in csvread:
      # calculate Total of Months
      total_months = total_months + 1
      # calculate the total
      total_revenue = total_revenue + int(row[1])
      
      #change value of profit_loss
      profit_loss.append(row[1])
      #change value of date
      date.append(row[0])

    # create for loop to find average change of profit/losses column
    for x in range(1,len(profit_loss)):
        #gather all entries in profit/losses column
        pl_change.append(int(profit_loss[x])-int(profit_loss[x-1]))
    
    # formula to find average change
    average_change = sum(pl_change) / len(pl_change)

    #find greatest increase
    greatest_increase = max(pl_change)
    
    #find greatest decrease
    greatest_decrease = min(pl_change)
    
    #find greatest decrease date
    gd_date = date[pl_change.index(greatest_decrease)+1]

    #find greatest increase date
    gi_date = date[pl_change.index(greatest_increase)+1]

#create layout for print ouput to terminal
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {str(total_months)}\n"
    f"Total: ${str(total_revenue)}\n"
    f"Average Change: ${str(round(average_change,2))}\n"
    f"Greatest Increase in Profits: {gi_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {gd_date} (${greatest_decrease})"
)
#print output to terminal
print(output)

# ouput analysis results to txt file
with open(output_txt,"w") as txtfile:
    txtfile.write(output)


      
      



