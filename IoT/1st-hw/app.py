from flask import Flask, render_template
import pandas as pd

df = pd.read_csv("marks.csv")
print(df)

#average for each test and order them from greater to smaller -> /tests
averTests = pd.DataFrame(df[["Test1", "Test2", "Test3", "Test4"]].mean())
df2 = averTests.rename(columns={0:'Average'})
averTestsSorted=df2.sort_values(by='Average', ascending=False)
print(averTestsSorted)

#average for each students grades, return students with less than 50 -> /failed
averStudents = pd.DataFrame(df.mean(axis=1, numeric_only=True))
averStudents = averStudents.rename(columns={0:'Average'})
namesColumn=df['Name']
averStudents.insert(0, "Name", namesColumn)
print(averStudents)
failedStudents = averStudents.loc[averStudents['Average'] < 50]
print(failedStudents)


app = Flask(__name__)

@app.route('/', methods = ("POST", "GET"))
def home():
    return render_template('home.html', tables=[df.to_html()], titles='')

@app.route('/tests', methods = ("POST", "GET"))
def tests():
    return render_template('tests.html', tables=[averTestsSorted.to_html()], titles='')


@app.route('/failed', methods=("POST", "GET"))
def failed():
    return render_template('failed.html', tables=[failedStudents.to_html()], titles='')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000)
