from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/country', methods=["GET","POST"])
def country(): 
    try:
            country = request.form['country']
            ctry = country.capitalize()
            r = requests.get('https://covid19.mathdro.id/api/countries/%s/recovered' % country)
            resp1=json.loads(r.text)
            w = requests.get('https://covid19.mathdro.id/api')
            resp=json.loads(w.text)
            return render_template('main.html', confirmed=resp['confirmed']['value'],deaths=resp['deaths']['value'],recovered=resp['recovered']['value'],
                                    conf=resp1[0]['confirmed'],deat=resp1[0]['deaths'],reco=resp1[0]['recovered'],country=ctry
                                )
    except:
        return render_template('error.html')

@app.route('/')    
def index():
    try:
        country = 'india'
        ctry = country.capitalize()
        r = requests.get('https://covid19.mathdro.id/api/countries/%s/recovered' % country)
        resp1=json.loads(r.text)
        w = requests.get('https://covid19.mathdro.id/api')
        resp=json.loads(w.text)
        return render_template('main.html', confirmed=resp['confirmed']['value'],deaths=resp['deaths']['value'],recovered=resp['recovered']['value'],
                                conf=resp1[0]['confirmed'],deat=resp1[0]['deaths'],reco=resp1[0]['recovered'],country=ctry
                            )
    except:
        return render_template('error.html')



if __name__ == '__main__':
  app.run(debug=False)
 