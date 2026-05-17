from flask import render_template, request
from app import app, models, db

@app.route('/')
@app.route("/accueil")
def accueil():
    # Récupérer les couleurs distinctes avec une bière exemple chacune
    couleurs = db.session.query(models.Vue_bieres.couleur).distinct().filter(
        models.Vue_bieres.couleur.isnot(None)).all()
    couleurs_liste = []

    for (couleur,) in couleurs:
        # Récupère la première bière de cette couleur
        biere_exemple = models.Vue_bieres.query.filter_by(couleur=couleur).first()
        if biere_exemple:
            couleurs_liste.append({
                'nom': couleur,
                'biere_exemple': biere_exemple,
                'nb': models.Vue_bieres.query.filter_by(couleur=couleur).count()
            })

    # Pour les bières sans alcool
    biere_sans_alcool_exemple = models.Vue_bieres.query.filter(models.Vue_bieres.taux_alcool == 0).first()
    nb_sans_alcool = models.Vue_bieres.query.filter(models.Vue_bieres.taux_alcool == 0).count()

    return render_template('accueil.html',
                           title='Bienvenue chez Beer&Co',
                           couleurs=couleurs_liste,
                           biere_sans_alcool_exemple=biere_sans_alcool_exemple,
                           nb_sans_alcool=nb_sans_alcool)

@app.route('/bieres_couleur')
def bieres_couleur():
    couleur = request.args.get('couleur')
    bieres = models.Vue_bieres.query.filter_by(couleur=couleur).all()
    titre = f"Bières {couleur}"
    return render_template('bieres_liste.html', bieres=bieres, title=titre)

@app.route('/bieres_sans_alcool')
def bieres_sans_alcool():
    bieres = models.Vue_bieres.query.filter(models.Vue_bieres.taux_alcool == 0).all()
    return render_template('bieres_liste.html', bieres=bieres, title='Bières sans alcool')
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
