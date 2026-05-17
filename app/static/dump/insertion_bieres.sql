INSERT INTO Biere (nom, volume, taux_alcool, couleur, prix, stock, image, id_brasserie, id_administrateur)
VALUES
-- Hoegaarden
('Hoegaarden Rosée', 25, 3.0, 'Ambre', 2.00, 100, 'hoegaarden-rosee.jpg',
 (SELECT id_brasserie FROM Brasserie WHERE nom = 'Hoegaarden'), 1),

('Hoegaarden Rosée 0,0%', 25, 0.0, 'Rose fruitée', 1.90, 100, 'hoegaarden-rosee-00.png',
 (SELECT id_brasserie FROM Brasserie WHERE nom = 'Hoegaarden'), 1),

('Hoegaarden Blanche', 25, 4.9, 'Blonde', 1.70, 100, 'hoegaarden-25cl.webp',
 (SELECT id_brasserie FROM Brasserie WHERE nom = 'Hoegaarden'), 1),

-- Van Honsebrouck
('Kasteelbier Rouge', 33, 8.0, 'Ambre', 2.97, 100, 'kasteelbier-rouge.webp',
 (SELECT id_brasserie FROM Brasserie WHERE nom = 'Van Honsebrouck'), 1),

('Kasteelbier Rouge 0,0%', 33, 0.0, 'Ambre', 3.04, 100, 'kasteelbier-rouge-00-33cl.png',
 (SELECT id_brasserie FROM Brasserie WHERE nom = 'Van Honsebrouck'), 1),

('Kasteelbier Brune', 33, 11.0, 'Brune', 3.07, 100, 'kasteelbier-brune.png',
 (SELECT id_brasserie FROM Brasserie WHERE nom = 'Van Honsebrouck'), 1),

('St Louis Premium Pêche', 25, 2.6, 'Blonde', 2.30, 100, 'st-louis-premium-peche.jpg',
 (SELECT id_brasserie FROM Brasserie WHERE nom = 'Van Honsebrouck'), 1),

('St Louis Kriek', 25, 4.0, 'Rouge', 1.67, 100, 'st-louis-kriek-25cl.webp',
 (SELECT id_brasserie FROM Brasserie WHERE nom = 'Van Honsebrouck'), 1),

-- Scourmont
('Chimay Blanche (Triple- Cinq Cents)', 33, 8.0, 'Blonde', 2.93, 100, 'chimay-blanche-triple-cinq-cents.webp',
 (SELECT id_brasserie FROM Brasserie WHERE nom = 'Scourmont'), 1),

('Chimay Rouge', 33, 7.0, 'Brune', 2.51, 100, 'chimay-rouge-premiere.png',
 (SELECT id_brasserie FROM Brasserie WHERE nom = 'Scourmont'), 1),

('Chimay Doree', 33, 4.8, 'Blonde', 2.46, 100, 'chimay-doree.webp',
 (SELECT id_brasserie FROM Brasserie WHERE nom = 'Scourmont'), 1);