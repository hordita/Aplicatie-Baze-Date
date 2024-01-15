
-- Afisare date
SELECT * FROM clienti;
SELECT * FROM produse;
SELECT * FROM comenzi ORDER BY id_comanda ASC;
SELECT * FROM detalii_comanda ORDER BY produse_id_produs, comenzi_id_comanda ASC;
SELECT * FROM istoric_pret ORDER BY id_pret ASC;
SELECT * FROM recenzii ORDER BY id_recenzie ASC;


-- Inserare date valide
INSERT INTO clienti (id_client, nume_client, adresa, email, telefon) VALUES (clienti_id_client_seq.nextval, 'Nume', 'Adresa', NULL, '0762345678');
INSERT INTO produse (id_produs, nume_produs, pret,stoc_disponibil) VALUES (produse_id_produs_seq.nextval, 'Produs', 100,8);
INSERT INTO comenzi (id_comanda, data_comanda, total_plata, id_client) VALUES (comenzi_id_comanda_seq.nextval, SYSDATE, 1000, 1);
INSERT INTO recenzii (id_recenzie, comentariu, id_client, id_produs) VALUES (recenzii_id_recenzie_seq.nextval, 'Recenzie 1', 1, 1);
INSERT INTO istoric_pret (id_pret, data_schimbare,pret_vechi, pret_nou, id_produs) VALUES (istoric_pret_id_pret_seq.nextval, TO_DATE('29-10-2023','DD-MM-YYYY'),200,100, 1);


-- Inserare date nevalide
INSERT INTO clienti VALUES (null, 'a', 'b','ajskssjk' ,'0712000000'); -- email invalid
INSERT INTO produse VALUES (null, 'P', -50); -- pret negativ


-- Modificare date
UPDATE clienti SET nume_client='Nume Modificat' WHERE id_client=1;
UPDATE produse SET pret=150 WHERE id_produs=2;


-- Stergere date
DELETE FROM istoric_pret WHERE id_pret=2;
DELETE FROM recenzii WHERE id_recenzie=1;


-- Verificare constrangeri
INSERT INTO detalii_comanda VALUES (8,2,6); -- cheie straina invalida


-- Afisare detalii comenzi cu produse
SELECT c.id_comanda, c.data_comanda, d.produse_id_produs, d.cantitate
FROM comenzi c, detalii_comanda d
WHERE c.id_comanda = d.comenzi_id_comanda;


-- Afisare detalii clienti cu comenzi
SELECT c.id_client, c.nume_client, c.adresa, cc.data_comanda, cc.total_plata
FROM clienti c, comenzi cc
WHERE c.id_client = cc.id_client;


-- Afisare detalii produse cu recenzii
SELECT p.id_produs, p.nume_produs, p.pret, r.comentariu
FROM produse p, recenzii r
WHERE p.id_produs = r.id_produs;


-- Calculul valorii medii a totalului comenzilor
SELECT AVG(total_plata) "Comanda medie"
FROM comenzi;


-- Afisare detalii produse cu recenzii si istoric preturi
SELECT p.id_produs, p.nume_produs, p.pret, r.comentariu, i.pret_nou
FROM produse p, recenzii r, istoric_pret i
WHERE p.id_produs = r.id_produs AND p.id_produs = i.id_produs AND p.pret > i.pret_nou;


-- Afisare detalii utilizator
SELECT c.id_client, c.nume_client, c.adresa, c.email, c.telefon
FROM clienti c;


-- Afisare numar comenzi ale fiecarui client
SELECT c.nume_client, COUNT(o.id_comanda) AS "Numar comenzi"
FROM clienti c, comenzi o
WHERE c.id_client = o.id_client(+)
GROUP BY c.nume_client;


-- Afisare istoric preturi cu detalii produse 
SELECT i.id_pret, i.pret_vechi, i.pret_nou, i.data_schimbare, p.nume_produs
FROM istoric_pret i, produse p
WHERE i.id_produs = p.id_produs(+);


-- Inserare in tabelul clienti
INSERT INTO clienti VALUES (null, 'Client Test', 'Adresa Test', 'test@email.com', '0123456789');


-- Afisare informatii clienti dupa inserare
SELECT * FROM clienti ORDER BY id_client ASC;


-- Actualizare in tabelul comenzi
UPDATE comenzi SET total_plata = 150 WHERE id_comanda = 1;


-- Afisare informatii comenzi dupa actualizare
SELECT * FROM comenzi ORDER BY id_comanda ASC;


-- Stergere din tabelul recenzii
DELETE FROM recenzii WHERE id_recenzie = 1;


-- Afisare informatii recenzii dupa stergere
SELECT * FROM recenzii ORDER BY id_recenzie ASC;


-- Verificare constrangere email unic in tabela clienti
UPDATE clienti SET email = 'test@email.com' WHERE id_client = 2;


-- Verificare constrangere telefon unic in tabela clienti
UPDATE clienti SET telefon = '0123456789' WHERE id_client = 2;


-- Verificare constrangere data_schimbare in tabela istoric_pret
INSERT INTO istoric_pret VALUES (null, 20, 25, TO_DATE('01-01-2024', 'DD-MM-YYYY'), 1);


-- Afisare informatii istoric_pret dupa inserare
SELECT * FROM istoric_pret ORDER BY id_pret ASC;


-- Afisare informatii recenzii dupa stergere 
SELECT r.id_recenzie, r.comentariu, c.nume_client, p.nume_produs
FROM recenzii r, clienti c, produse p
WHERE r.id_client = c.id_client AND r.id_produs = p.id_produs;


-- Afisare informatii comenzi cu detalii produse 
SELECT c.id_comanda, c.data_comanda, c.total_plata, d.produse_id_produs, d.cantitate
FROM comenzi c, detalii_comanda d
WHERE c.id_comanda = d.comenzi_id_comanda;







