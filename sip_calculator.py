from flask import Flask
from flask import Flask,render_template,request,Response
import pandas as pd


app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def login():
    new_row = pd.DataFrame(columns=['Year', 'Invested_Value','Value'])

    if request.method == 'POST':
        Amount = int(request.form['Amount'])
        Duration  = int(request.form['Durations'])
        Returns  = int(request.form['Returns'])
        roi = (Returns)/120
        fund_value = 0
        
        for i in range(1,Duration+1):
            months= i*12
            row = []
            row.append(i)
            invested_value = Amount*12*i
            row.append(invested_value)
            #new_value= round(Amount*(1+(roi/12))**(12*i))
            new_value = round(Amount * ((((1 + roi)**12) - 1) / roi) * (1 + roi))
            fund_value += new_value
            row.append(fund_value)
            new_row.loc[len(new_row)] = row
        html_table = new_row.to_html(index=False, classes="table table-striped")    
        return html_table
                       
    return render_template('form.html')

if __name__ == '__main__':


    app.debug = True
    app.run(host='0.0.0.0', port=5000)

