
DROP TABLE IF EXISTS utilisateurs;

-- commandes de destruction des tables
CREATE TABLE utilisateurs (username text not null, 
                        pass text not null,  
                        spublickey text not null, 
                        sprivatekey text not null,
                        epublickey text not null,
                        eprivatekey text not null);