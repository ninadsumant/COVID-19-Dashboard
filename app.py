from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/blood')
def blood():
    return render_template('bloodDonation.html')

@app.route('/donate')
def donate():
    return render_template('donate.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/precautions')
def precautions():
    return render_template('precautions.html')

@app.route('/country', methods=["GET","POST"])
def country(): 
    try:
            country = request.form['country']
            ctry = country.capitalize()
            r = requests.get('https://covid19.mathdro.id/api/countries/%s' % country)
            resp1=json.loads(r.text)
            w = requests.get('https://covid19.mathdro.id/api')
            resp=json.loads(w.text)
            return render_template('main.html', confirmed=resp['confirmed']['value'],deaths=resp['deaths']['value'],recovered=resp['recovered']['value'],
                                    conf=resp1['confirmed']['value'],deat=resp1['deaths']['value'],reco=resp1['recovered']['value'],country=ctry
                                )
    except:
        return render_template('error.html')

@app.route('/')    
def index():
    try:
        country = 'india'
        ctry = country.capitalize()
        r = requests.get('https://covid19.mathdro.id/api/countries/%s' % country)
        resp1=json.loads(r.text)
        w = requests.get('https://covid19.mathdro.id/api')
        resp=json.loads(w.text)
        return render_template('main.html', confirmed=resp['confirmed']['value'],deaths=resp['deaths']['value'],recovered=resp['recovered']['value'],
                                conf=resp1['confirmed']['value'],deat=resp1['deaths']['value'],reco=resp1['recovered']['value'],country=ctry
                            )
    except:
        return render_template('error.html')



if __name__ == '__main__':
  app.run(debug=True)
 