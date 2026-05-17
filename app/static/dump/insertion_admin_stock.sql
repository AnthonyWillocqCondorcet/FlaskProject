-- Ajout d'un utilisateur administrateur
INSERT INTO Utilisateur (nom, prenom, email, mot_de_passe, date_inscription, type_utilisateur)
VALUES ('DUPLUMIER', 'Joséphine', 'jduplumier@bdvm.com', 'gestion', CURRENT_DATE, 'administrateur');

-- Ajout dans la table Administrateur
INSERT INTO Administrateur (id_utilisateur, niveau_acces)
VALUES (currval('utilisateur_id_utilisateur_seq'), 'gestion_stock');