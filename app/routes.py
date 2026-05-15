from flask import render_template, url_for
from app import app

@app.route('/')
@app.route("/accueil")
def accueil():
    return render_template('accueil.html', title='Bienvenue dans notre boutique')

@app.route('/tous_produits')
def tous_produits():
    return render_template('tous_produits.html', title='Nos produits')