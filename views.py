from flask import Flask,render_template,url_for,request
from prettytable import PrettyTable
import base64
app = Flask(__name__)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')




@app.route('/titanic')
def titanic():
    graph = request.args.get('graph')
    if graph == "1":
        return render_template('titanic.html')
    elif graph == "0":
        to_html_converter('/titanic')
        return render_template('table.html')
    else:
        return render_template('home.html')
        






def to_html_converter(path):
    path = 'data/{}.csv'.format(path)
    csv_file = open(path,'r')
    csv_file = csv_file.readlines()

    #creates a list of 6 first items of csv_file
    line = [] 
    for i in range(6):
        line.append(csv_file[i])
    #splits items at ','
    for i in range(len(line)):
        line[i] = line[i].split(',')
    
    x = PrettyTable()
    column_names = []
    for i in range(len(line[0])):
        column_names.append(line[0][i])
    # column_names = [line[0][0],line[0][1],line[0][2],line[0][3]]
    for i in range(len(column_names)):
        x.add_column(column_names[i],[line[1][i],line[2][i],line[3][i],line[4][i],line[5][i]])
    html_code = x.get_html_string()
    html_file = open('templates/table.html','w')
    html_file = html_file.write(html_code)
    




titan = pd.read_csv('data/titanic.csv')
data = titan['Age'].fillna(method='ffill')

bins = np.arange(0,100,5)
plt.xlim([min(data)-5,max(data)+5])
plt.hist(data,bins=bins,alpha = 0.5)
plt.xlabel('Age')
plt.ylabel('count')
plt.savefig('./static/fig_1.png')



import seaborn as sns
import matplotlib.pyplot as plt 
data = sns.load_dataset("data/titanic")
plt.figure(figsize=(8,8))
ax = sns.violinplot(x='age',y='sex',data = data)
plt.savefig('./static/fig_2.png')


if __name__=='__main__':
    app.run(debug=True)