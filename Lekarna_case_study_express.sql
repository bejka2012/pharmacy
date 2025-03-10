SELECT * FROM dim_lekarna
SELECT * FROM dim_vedouci
SELECT * FROM dim_zbozi
SELECT * FROM fact_prodej
SELECT * FROM fact_prodej_12_24




SELECT *
FROM fact_prodej
JOIN dim_lekarna ON fact_prodej.ID_lekarna = dim_lekarna.ID_lekarna


SELECT *
FROM fact_prodej p
JOIN dim_lekarna l ON p.ID_lekarna = l.ID_lekarna
JOIN dim_vedouci v ON v.ID_vedouci = p.ID_vedouci
JOIN dim_zbozi z ON z.ID_zbozi = p.ID_zbozi



INSERT INTO 
    fact_prodej (
        ID_zbozi, 
        ID_lekarna, 
        ID_vedouci, 
        datum, 
        pocet_prodanych_ks, 
        nakupni_cena_CZK, 
        prodejni_cena_CZK,
        marze_CZK,
        trzba_CZK)
SELECT 
        ID_zbozi, 
        ID_lekarna, 
        ID_vedouci, 
        datum, 
        pocet_prodanych_ks, 
        nakupni_cena_CZK, 
        prodejni_cena_CZK,
        marze_CZK,
        trzba_CZK
FROM fact_prodej_



DROP TABLE fact_prodej_1_25

SELECT *
FROM fact_prodej
WHERE 
    YEAR(datum) = 2024 AND
    MONTH(datum) = 11

DELETE FROM fact_prodej
WHERE  
	MONTH(datum) = 12 AND
	YEAR(datum) = 2024

DELETE FROM fact_prodej
WHERE  
	MONTH(CAST(datum AS DATE)) = 12 AND
	YEAR(CAST(datum) AS DATE)) = 2024

SELECT COLUMN_NAME, DATA_TYPE 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_NAME = 'fact_prodej' AND COLUMN_NAME = 'datum';
		
