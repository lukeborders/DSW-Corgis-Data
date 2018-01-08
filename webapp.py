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
   
def get_numberz(name):   
    with open('health.json') as health_data:
        data = json.load(health_data)
    fact = 0
    for n in data:
        if name == n["disease"]:
            fact += n["number"]
    return fact
            
@app.route("/")
def render_main():
    return render_template('index.html')

@app.route("/statistics")
def render_stats():
    return render_template('statistics.html', years = get_options())
    
@app.route("/selection", methods = ['GET','POST'])
def render_chart():
    year = request.args['years']
    return render_template('statistics.html', years = get_options(), measles = get_numberz("MEASLES"), polio = get_numberz("POLIO"), smallpox = get_numberz("SMALLPOX"), pertussis = get_numberz("PERTUSSIS"), hepatitusa = get_numberz("HEPATITUS A"), rubella = get_numberz("RUBELLA"), mumps = get_numberz("MUMPS"))   
 
if __name__ =="__main__":
    app.run(debug=True, port=5000)
