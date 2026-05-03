from app import app
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/accueil')
def accueil():  # put application's code here
    return "Page d'accueil!"

@app.route('/produits')
def tous_les_produits():  # put application's code here
    return "Page des produits"