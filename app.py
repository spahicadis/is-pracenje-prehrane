from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from pony.orm import Database, PrimaryKey, Required, db_session, select
import os
from datetime import datetime

app = Flask(__name__)

db = Database()
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)

class Obrok(db.Entity):
    id = PrimaryKey(int, auto=True)
    datum = Required(str)
    naziv_obroka = Required(str)
    hrana = Required(str)
    kalorije = Required(float)
    proteini = Required(float)
    ugljikohidrati = Required(float)
    masti = Required(float)
    created_at = Required(datetime, default=datetime.now)
    updated_at = Required(datetime, default=datetime.now)

   
    def set_created_at(self):
        self.created_at = datetime.now()

    
    def set_updated_at(self):
        self.updated_at = datetime.now()

db.generate_mapping(create_tables=True)


@app.route('/')
def index():
    return render_template('index.html')  


@app.route('/dodaj_obrok', methods=['GET', 'POST'])
@db_session
def dodaj_obrok():
    if request.method == 'POST':
        datum = request.form['datum']
        naziv_obroka = request.form['naziv_obroka']
        hrana = request.form['hrana']
        kalorije = float(request.form['kalorije'])
        proteini = float(request.form['proteini'])
        ugljikohidrati = float(request.form['ugljikohidrati'])
        masti = float(request.form['masti'])
        Obrok(datum=datum, naziv_obroka=naziv_obroka, hrana=hrana, kalorije=kalorije, proteini=proteini, ugljikohidrati=ugljikohidrati, masti=masti)
        return redirect(url_for('index'))
    return render_template('dodaj_obrok.html')  


@app.route('/prikazi_sve_obroke')
@db_session
def prikazi_sve_obroke():
    obroci = Obrok.select()
    return render_template('prikazi_sve_obroke.html', obroci=obroci)  


@app.route('/uredi_obrok/<int:obrok_id>', methods=['GET', 'POST'])
@db_session
def uredi_obrok(obrok_id):
    obrok = Obrok[obrok_id]
    if request.method == 'POST':
        obrok.datum = request.form['datum']
        obrok.naziv_obroka = request.form['naziv_obroka']
        obrok.hrana = request.form['hrana']
        obrok.kalorije = float(request.form['kalorije'])
        obrok.proteini = float(request.form['proteini'])
        obrok.ugljikohidrati = float(request.form['ugljikohidrati'])
        obrok.masti = float(request.form['masti'])
        obrok.updated_at = datetime.now()
        return redirect(url_for('prikazi_sve_obroke'))
    return render_template('uredi_obrok.html', obrok=obrok)  


@app.route('/obrisi_obrok/<int:obrok_id>', methods=['POST'])
@db_session
def obrisi_obrok(obrok_id):
    obrok = Obrok[obrok_id]
    obrok.delete()
    return redirect(url_for('prikazi_sve_obroke'))


@app.route('/vizualizacija')
@db_session
def vizualizacija():
    obroci = select(o for o in Obrok)
    ukupno_kalorije = sum(o.kalorije for o in obroci)
    ukupno_proteini = sum(o.proteini for o in obroci)
    ukupno_ugljikohidrati = sum(o.ugljikohidrati for o in obroci)
    ukupno_masti = sum(o.masti for o in obroci)
    podaci = {
        'kalorije': ukupno_kalorije,
        'proteini': ukupno_proteini,
        'ugljikohidrati': ukupno_ugljikohidrati,
        'masti': ukupno_masti
    }
    return render_template('vizualizacija.html', podaci=podaci) 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

