#First we will import os module that will allow us to create file path
import os
import csv

py_bank = r"C:\Users\sobai\GWARL201906DATA1\02-Homework\03-Python\Instructions\PyBank\Resources\budget_data.csv"


with open(py_bank) as budgetdata:

    reader = csv.reader(budgetdata, delimiter=',')
    
    print(reader)
    
    #for row in reader:
        
        #print(row) 
     
    total_months = list(reader)
    row_count = len(total_months)
    print(row_count)
    
    profit = row_count['Profit/Losses'].sum()
    print(row_count)
    
    
    
    







total_months = range(0,1)
    print(total_months)
    
          

    
total_months = len(py_bank)
    print(total_months)
        
month_total= list(reader)
total_months = len(month_total)
print(month_total)

       
  
total_months = sum(0 for row in total_months)     
    print(total_months)



Total_Months=len(reader[0])
    print("Total number of months is" + Total_Months)

profit_losses=sum(row[1])
   print("Net Profit/Losses are" + profit_losses)
    
ave_profloss= (profit_losses/months_total)
   print ("The average profit/losses is =" + ave_profloss)
    
   list_ofPL=[]
    for x in csvreader:
        list_ofPL.append(row[1])
        difference_PL = np.diff(list_ofPL)
    
        increases = difference_PL[difference_PL > 0]
        print(increases)
        print(increases.mean())
    
        print(increases.max())
        print(increases.min())


Total_Months = Data[0]
count(0)
print(Total_Months)

   
   
           
           
    
        
    



