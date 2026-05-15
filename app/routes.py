from flask import render_template, url_for, request
from app import app, models

@app.route('/')
@app.route("/accueil")
def accueil():
    return render_template('accueil.html', title='Bienvenue dans notre boutique')

@app.route('/tous_bieres')
def tous_bieres():
    bieres = models.Vue_bieres.query.all()
    return render_template('bieres_liste.html', bieres=bieres, title='Toutes nos bières')

@app.route('/bieres_brasserie')
def bieres_brasserie():
    id_brasserie = request.args.get('id_brasserie', type=int)
    bieres = models.Vue_bieres.query.filter_by(id_brasserie=id_brasserie).all()
    return render_template('bieres_liste.html', bieres=bieres, title='Bières par brasserie')


@app.route('/brasseries')
def brasseries():
    brasseries = models.Vue_bieres.query.with_entities(
        models.Vue_bieres.id_brasserie,
        models.Vue_bieres.nom_brasserie,
        models.Vue_bieres.ville_brasserie
    ).distinct().all()
    return render_template('brasseries.html',
                           title='Nos brasseries',
                           brasseries=brasseries)
