from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/update_bills", methods=["POST"])
def update_bills():
    bills = request.form.get("bills")
    #amount = request.form.get("amount")
    
    # Write the updated bill information to the appropriate CSV file
    filename = ""
    rows = []
    if bills == "mariam_bills":
        filename = "mariam_bills.csv"
        rows = [["Rent", "£1200"], ...]
    elif bills == "tosin_bills":
        filename = "tosin_bills.csv"
        rows = [["Studio", "£60✅"], ...]
    elif bills == "income":
        filename = "income.csv"
        rows = [["Salary", "Total left"], ...]
    
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([bills.upper()])
        writer.writerow(["Bills"])
        writer.writerows(rows)
    
    return "Bills updated successfully!"

if __name__ == "__main__":
    app.run()
