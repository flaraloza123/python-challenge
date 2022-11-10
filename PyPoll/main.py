#import necessary modules to complete analysis
import os
import csv

# set path to csv file that needs to be analyzed
csvdata=os.path.join("Resources","election_data.csv")

# set path for analysis output
output_txt= os.path.join("analysis","BudgetAnalysis.txt")

#create varibles needed for this analysis
total_votes = 0
canidate = []
canidate_votes = {}
canidate_average = {}
win_count = 0
winner = ""


#open csv file
with open(csvdata) as csvfile:

    csvread=csv.reader(csvfile, delimiter=",")

    #skip the header row
    header= next(csvread)
    #create for loop to read rows after header row
    for row in csvread:
      # calculate Total of votes
      total_votes = total_votes + 1

      #create if statement to find canidates and count votes
      if row[2] not in canidate:
        canidate.append(row[2])
        canidate_votes[row[2]] = 1
      else:
        canidate_votes[row[2]] += 1

#create variable for v_output
v_output = ""
   
#create for loop inside of canidate_votes
for canidate in canidate_votes:
    ind_votes = canidate_votes.get(canidate)
    prcnt_votes = (ind_votes / total_votes) * 100
    v_output += f"{canidate}: {prcnt_votes:.3f}% ({ind_votes:,})\n"


    #create if statement to find winning canidate
    if ind_votes > win_count:
        win_count = ind_votes
        winner = canidate

# create output for terminal to output
output = (
    f"Election Results\n"
    f"----------------------------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"----------------------------------------------\n"
    f"{v_output}\n"
    f"----------------------------------------------\n"
    f"Winner: {winner}\n"
    f"----------------------------------------------\n"
    )

#print output to terminal
print(output)

# ouput analysis results to txt file
with open(output_txt,"w") as txtfile:
    txtfile.write(output)



   


      
