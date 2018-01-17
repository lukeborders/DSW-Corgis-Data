from flask import Flask, url_for, render_template, request, Markup
import json
import os

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

def get_options():
    with open('health.json') as health_data:
        data = json.load(health_data)
    options=""
    year = 1927
    for t in data:
        #dank if statement
        if t["year"] != year:
            options += Markup("<option value=" + '"' +str(t["year"]) + '"'+">" + str(t["year"]) + "</option>")
        year = t["year"]
    return options 
    #logang 
   
def get_numberz(name,year):   
    with open('health.json') as health_data:
        data = json.load(health_data)
    diseaseDict = {}
    fact = 0
    for n in data:
        if name == n["disease"] and str(n["year"]) == year:
            fact += n["number"]
    print(year)
    print(name)
    print(fact)
    return fact
 
def get_options2():
    with open('health.json') as health_data:
        data = json.load(health_data)
    options=""
    dis = []
    for t in data:
        if t["disease"] not in dis:
            dis.append(t["disease"])
    print(dis)
    for c in range(0,len(dis)-1):
        options += Markup("<option value=\"" + dis[c] + "\">" + dis[c] + "</option>")
    return options

def get_fact(disease , year):
    with open('health.json') as health_data:
        data = json.load(health_data)
    fact = 0
    numcount = 0
    for c in data:
        if disease == c["disease"] and year == c["year"]
            fact += c["increase"]
            numcount += 1
    fact = round(fact/numCount,2)
    funfact = Markup("<p>" + "Percent Increase of " + disease + " in the year " + year + "is " + str(fact) + " %" + "</p>")

@app.route("/funfact", methods=['GET', 'POST'])
def render_funfact():
    year = request.args['year']
    disease = request.args['disease']
    return render_template('U.html', fact = get_fact(disease, year))

@app.route("/")
def render_main():
    return render_template('index.html')

@app.route("/U")
def render_U():
    return render_template('U.html',yearOpt = get_options(), diseaseOpt = get_options2())

@app.route("/statistics")
def render_stats():
    return render_template('statistics.html', years = get_options())
    
@app.route("/selection", methods = ['GET','POST'])
def render_chart():
    year = request.args['years']
    return render_template('statistics.html', years = get_options(), measles = get_numberz("MEASLES",year), polio = get_numberz("POLIO",year), smallpox = get_numberz("SMALLPOX",year), pertussis = get_numberz("PERTUSSIS",year), hepatitusa = get_numberz("HEPATITUS A",year), rubella = get_numberz("RUBELLA",year), mumps = get_numberz("MUMPS",year))   
 
@app.route("/yes", methods = ['GET','POST'])
def render_jfact():
    year = request.args['year']
    return render_template("U.html",yearOpt = get_options(), diseaseOpt = get_options2())
 
if __name__ =="__main__":
    app.run(debug=True, port=5000)
