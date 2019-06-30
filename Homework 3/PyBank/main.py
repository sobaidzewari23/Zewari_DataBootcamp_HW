import os
import csv

py_bank = r"C:\Users\sobai\Zewari_DataBootcamp_HW\Homework 3\PyBank\budget_data.csv"

with open(py_bank, newline="") as budgetdata:

    reader = csv.reader(budgetdata, delimiter=",")
    #print(reader)  
    next(reader)
    
    months = []
    values = []
    totals = []
    
    for row in reader:
        month = row[0]
        value = int(row[1])
        months.append(month)
        values.append(value)
        
    total_months = len(months)
    print(total_months)
    
    total_profit = sum(values)
    print(total_profit)
    
    
    avg_chg = total_profit/total_months
    print(avg_chg)
    
    diffs = []
    counter = 0
    for value in values:
        if counter == 0:
            pass
        else:
            diff = value - values[counter - 1]
            diffs.append(diff)
        counter += 1
        
        print(min(diffs))
        print(max(diffs))
         
        
        greatest_increase = ["", 0]
        greatest_decrease = ["", 9999999999999999999999]
    
        if (avg_chg > greatest_increase[1]):
            greatest_increase[0] = avg_chg
            greatest_increase[1] = row["Date"]

        if (avg_chg < greatest_decrease[1]):
            greatest_decrease[0] = avg_chg
            greatest_decrease[1] = row["Date"]
 
            avg_chg.append(int(row["Profit/Losses"]))               
                

    

pybank_analysis = r"C:\Users\sobai\Zewari_DataBootcamp_HW\Homework 3\PyBank\Analysis.txt"

with open(pybank_analysis, "w") as txt_file:
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total Profit: " + "$" + str(total_profit))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(sum(avg_chg) / len(avg_chg),2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")

#
#
