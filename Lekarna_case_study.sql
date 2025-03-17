SELECT * FROM dim_lekarna
SELECT * FROM dim_vedouci
SELECT * FROM dim_zbozi
SELECT * FROM fact_prodej

SELECT * FROM fact_prodej_1_25


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
FROM fact_prodej_2_25

SELECT *
FROM fact_prodej
WHERE 
    YEAR(datum) = 2024 AND
    MONTH(datum) = 11

DELETE FROM fact_prodej
WHERE  
	MONTH(datum) = 2 AND
	YEAR(datum) = 2025

DELETE FROM fact_prodej
WHERE  
	MONTH(CAST(datum AS DATE)) = 12 AND
	YEAR(CAST(datum) AS DATE)) = 2024

DROP TABLE fact_prodej_2_25