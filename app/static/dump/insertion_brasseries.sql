-- Insertion des adresses (données fictives)
INSERT INTO Adresse (rue, numero, code_postal, ville, pays) VALUES
('Rue de la Brasserie', '1', '1000', 'Bruxelles', 'Belgique'),     -- id 1
('Chaussée de Haecht', '12', '1030', 'Schaerbeek', 'Belgique'),    -- id 2
('Place de l''Abbaye', '8', '6464', 'Chimay', 'Belgique');          -- id 3

-- Insertion des brasseries
INSERT INTO Brasserie (nom, id_adresse) VALUES
('Hoegaarden', 1),
('Van Honsebrouck', 2),
('Scourmont', 3);