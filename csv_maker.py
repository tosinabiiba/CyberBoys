import csv

fields = ['Bills', 'Amount']

# Mariam's bills
rows_mariam = [
    ['Rent', '£1200'],
    ['Nova Nursery', '£504'],
    ['Food', '£140(£70 per week) in monzo (£72.30) ✅'],
    ['Adobe', '£16.24'],
    ['Swimming', '£32.50'],
    ['Disney', '£7.99'],
    ['Bus for work', '£24'],
    ['Phone storage', '£4.98'],
    ['Watch', '£15.82 (my half)'],
    ['Gym', '£25'],
    ['Total', '£1,970.43']
]

# Tosin's bills
rows_tosin = [
    ['Studio', '£60✅'],
    ['Vanquis', '£45.78(paid £145)✅'],
    ['BT', '£30'],
    ['EE', '£213.24'],
    ['Thames water', '£61'],
    ['Council tax', '£130'],
    ['British Gas', '£55/move to 80(not yet)'],
    ['Car insurance', '£155.43'],
    ['Cleaner', '£100 (in monzo)✅'],
    ['Benson beds', '£43.19'],
    ['Nova essentials', '£60 (sent to monzo)✅'],
    ['Food', '£140 (70pounds a week) In monzo ✅'],
    ['Total', '£1093.64']
]

# Income
rows_income = [
    ['Salary', 'Total left'],
    ['Tosin (1850)', '£858.87'],
    ['Mariam (2,459.59)', '£919.59'],
    ['Universal credit', '£1,270.21']
]

# Write Mariam's bills to CSV
filename = "mariam_bills.csv"
with open(filename, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Mariam BILLs'])
    writer.writerow(fields)
    writer.writerows(rows_mariam)

# Write Tosin's bills to CSV
filename = "tosin_bills.csv"
with open(filename, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['TOSIN BILLs'])
    writer.writerow(fields)
    writer.writerows(rows_tosin)

# Write Income to CSV
filename = "income.csv"
with open(filename, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['INCOME'])
    writer.writerow(fields)
    writer.writerows(rows_income)
