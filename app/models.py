from app import db

class Vue_bieres(db.Model):
    id_biere = db.Column(db.Integer, primary_key=True)
    nom_biere = db.Column(db.String(255), nullable=False, unique=True)
    volume = db.Column(db.Integer, nullable=False)
    taux_alcool = db.Column(db.Numeric(3,1), nullable=False)
    couleur = db.Column(db.String(50), nullable=False)
    prix = db.Column(db.Numeric(10,2), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(255), nullable=True)
    id_brasserie = db.Column(db.Integer)
    nom_brasserie = db.Column(db.String(255), nullable=False)
    ville_brasserie = db.Column(db.String(255), nullable=False)
    pays_brasserie = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return (f'{self.id_biere} : {self.nom} : {self.volume}ml : '
                f'{self.taux_alcool}% : {self.couleur} : {self.prix}€ : '
                f'stock {self.stock} : {self.nom_brasserie} '
                f'({self.ville_brasserie}, {self.pays_brasserie})')