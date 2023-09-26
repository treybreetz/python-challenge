#create variables
TotalMonths = 0
NetTotal = 0 
PreviousProfitLoss = 0 
TotalChange = 0 
GreatestIncreaseAmount = float()
GreatestIncreaseMonth = ""
GreatestDecreaseAmount = float()
GreatestDecreaseMonth = ""

#define output file location and filename
OutputFile = "C:/Users/baseb/OneDrive/Desktop/Data Analytics Course/Module 3/python-challenge/PyBank/analysis/analysis.txt"

#read CSV file
with open('C:/Users/baseb/OneDrive/Desktop/Data Analytics Course/Module 3/python-challenge/PyBank/Resources/budget_data.csv', 'r') as csvfile:
    header = next(csvfile) # Skips header row
    for line in csvfile :
        #split column into two columns
        date, ProfitLoss = line.strip().split(',')

        #changepProfit or loss to an integer
        ProfitLoss = int(ProfitLoss)

        #find total months
        TotalMonths += 1

        #find net profit/loss
        NetTotal += ProfitLoss

        #find change in profit/loss. need if for first row. no change in first row. 
        if TotalMonths > 1: 
            change = (ProfitLoss) - (PreviousProfitLoss)
        else :
            change = 0 
        
        #add up total change
        TotalChange += change

        #update biggest increases and decreases
        if change > GreatestIncreaseAmount: 
            GreatestIncreaseAmount = change
            GreatestIncreaseMonth = date
        if change < GreatestDecreaseAmount:
            GreatestDecreaseAmount = change
            GreatestDecreaseMonth = date
            
        #update Profit/Loss value
        PreviousProfitLoss = ProfitLoss

#find Average Change
AverageChange = TotalChange / (TotalMonths - 1)

#print results
print("Financial Analysis")
print("----------------------------")    
print(f"Total Months: {TotalMonths}")
print(f"Total: ${NetTotal}")
print(f"Average Change: ${AverageChange : .2f}")
print(f"Greatest Increase in Profits: {GreatestIncreaseMonth} (${GreatestIncreaseAmount})")
print(f"Greatest Decrease in Profits: {GreatestDecreaseMonth} (${GreatestDecreaseAmount})")

#prints results to txt file and terminal
with open(OutputFile, "w") as OutputFile:
    OutputFile.write("Financial Analysis\n")
    OutputFile.write("----------------------------\n")
    OutputFile.write(f"Total Months: {TotalMonths}\n")
    OutputFile.write(f"Total: ${NetTotal}\n")
    OutputFile.write(f"Average Change: ${AverageChange:.2f}\n")
    OutputFile.write(f"Greatest Increase in Profits: {GreatestIncreaseMonth} (${GreatestIncreaseAmount})\n")
    OutputFile.write(f"Greatest Decrease in Profits: {GreatestDecreaseMonth} (${GreatestDecreaseAmount})\n")

# lets us know results were printed in txt file.
print(f"The financial analysis results have been exported to {OutputFile}")
