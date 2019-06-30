import csv

py_poll = r"C:\Users\sobai\Zewari_DataBootcamp_HW\Homework 3\PyPoll\election_data.csv"

with open(py_poll, newline="") as electiondata:
    reader = csv.reader(electiondata, delimiter=",")
    
#Total votes cast
    w_header=len(reader["Candidate"])
    total_votes=(w_header-1)
    print(total_votes)


    