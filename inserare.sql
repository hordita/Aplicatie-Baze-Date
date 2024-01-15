--CLIENTI
INSERT INTO clienti VALUES (NULL, 'Ion Popescu', 'Str. 1 Decembrie','popescu@email.com', '0712345678');
INSERT INTO clienti VALUES (NULL, 'Maria Petrescu', 'Str. Libertatii','maria@email.com', '0723456789');
INSERT INTO clienti VALUES (NULL, 'Andrei Popescu', 'Str. Stefan cel mare','andrei@email.com', '0723456123');
INSERT INTO clienti VALUES (NULL, 'Bogdan Ionescu', 'Str. 1 Mai','bogdan@email.com', '0723456234');
INSERT INTO clienti VALUES (NULL, 'Cristi Pop', 'Str. Victoriei','cristi@email.com', '0723456745');	

for rec in 10000 to 20000
loop
INSERT INTO clienti VALUES (NULL, 'Cristi Pop', 'Str. Victoriei',null, '07123'||to_char(i));

end loop,

--tabela produse
INSERT INTO produse VALUES (NULL, 'Laptop', 'Laptop gaming Asus ROG', 2500, 5);
INSERT INTO produse VALUES (NULL, 'Telefon', 'iPhone 13 Pro Max', 5000, 3);
INSERT INTO produse VALUES (NULL, 'Monitor', 'Monitor 27 inch LG', 1000, 10);
INSERT INTO produse VALUES (NULL, 'Tastatura', 'Tastatura mecanica Logitech', 200, 20);
INSERT INTO produse VALUES (NULL, 'Casti', 'Casti gaming Razer', 300, 15);

--recenzii
INSERT INTO recenzii VALUES (NULL, 'Laptopul este foarte performant', 1, 1);
INSERT INTO recenzii VALUES (NULL, 'Telefonul are o camera excelenta', 2, 2);
INSERT INTO recenzii VALUES (NULL, 'Monitorul are o calitate excelenta', 3, 3);
INSERT INTO recenzii VALUES (NULL, 'Tastatura este foarte confortabila', 4, 4);
INSERT INTO recenzii VALUES (NULL, 'Castile au un sunet bun', 5, 5);

--Inserare date in tabela comenzi
INSERT INTO comenzi VALUES (NULL, TO_DATE('01-01-2023', 'DD-MM-YYYY'), 5000, 1);
INSERT INTO comenzi VALUES (NULL, TO_DATE('15-02-2023', 'DD-MM-YYYY'), 7500, 2);
INSERT INTO comenzi VALUES (NULL, TO_DATE('15-03-2023', 'DD-MM-YYYY'), 3000, 3);
INSERT INTO comenzi VALUES (NULL, TO_DATE('01-04-2023', 'DD-MM-YYYY'), 1500, 4);
INSERT INTO comenzi VALUES (NULL, TO_DATE('15-04-2023', 'DD-MM-YYYY'), 2500, 5);

--istoric pret
INSERT INTO istoric_pret VALUES (NULL, 1000, 1500, TO_DATE('01-01-2023', 'DD-MM-YYYY'), 1);
INSERT INTO istoric_pret VALUES (NULL, 1200, 1300, TO_DATE('15-02-2023', 'DD-MM-YYYY'), 2);
INSERT INTO istoric_pret VALUES (NULL, 800, 1000, TO_DATE('01-03-2023', 'DD-MM-YYYY'), 3);
INSERT INTO istoric_pret VALUES (NULL, 900, 1100, TO_DATE('15-04-2023', 'DD-MM-YYYY'), 4);
INSERT INTO istoric_pret VALUES (NULL, 700, 900, TO_DATE('01-05-2023', 'DD-MM-YYYY'), 5);

--detalii comanda
INSERT INTO detalii_comanda VALUES ((select id_produs from produse where nume_produs = 'Laptop'), 1, 1);
INSERT INTO detalii_comanda VALUES ((select id_produs from produse where nume_produs = 'Telefon'), 1, 2);
INSERT INTO detalii_comanda VALUES ((select id_produs from produse where nume_produs = 'Laptop'), 2, 1);
INSERT INTO detalii_comanda VALUES ((select id_produs from produse where nume_produs = 'Casti'), 3, 4);
INSERT INTO detalii_comanda VALUES ((select id_produs from produse where nume_produs = 'Laptop'), 3, 4);