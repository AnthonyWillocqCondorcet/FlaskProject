CREATE OR REPLACE VIEW vue_bieres AS
SELECT 
    b.id_biere,
    b.nom AS nom_biere,
    b.volume,
    b.taux_alcool,
    b.couleur,
    b.prix,
    b.stock,
    b.image,
    br.id_brasserie,
    br.nom AS nom_brasserie,
    a.ville AS ville_brasserie,
    a.pays AS pays_brasserie,
    a.code_postal AS cp_brasserie
FROM Biere b
JOIN Brasserie br ON b.id_brasserie = br.id_brasserie
JOIN Adresse a ON br.id_adresse = a.id_adresse;