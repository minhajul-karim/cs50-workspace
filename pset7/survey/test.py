import csv

fname = "Minhajul"
lname = "Karim"

with open('survey.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    #writer.writeheader()
    writer.writerow({'first_name': fname, 'last_name': lname})
