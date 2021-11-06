-- Base customers

select *
from customers

-- atividade 1
select
	contact_name
	,	city
	,	country
from
	customers
order by 1

-- atividade 2
select
	contact_name
	,	city
	,	country
from
	customers
where
	country in ('Germany', 'France', 'Spain')
	and city not in ('Berlin', 'Paris', 'Madrid')
order by 1


-- Base products

-- atividade 1

SELECT * FROM products

SELECT * FROM products WHERE category_id = 2;

SELECT COUNT (*) FROM products WHERE category_id = 2; -- 12


-- atividade 2

SELECT COUNT (*) FROM products WHERE category_id = supplier_id; -- 5

SELECT product_name, category_id, supplier_id FROM products WHERE category_id = supplier_id;

SELECT COUNT (*) FROM products WHERE unit_price > 10; -- 63

SELECT product_name, unit_price FROM products WHERE unit_price > 10;

-- atividade 3

SELECT product_name, category_id, unit_price, units_in_stock, units_on_order FROM products WHERE category_id IN (1, 2, 7); 

-- atividade 4

SELECT product_name FROM products WHERE product_name LIKE 'A%' OR product_name LIKE '%h%' LIMIT 5;

SELECT product_name AS "Nome do Produto" FROM products WHERE product_name LIKE 'A%' OR product_name LIKE '%h%' LIMIT 5;

-- atividade 5

SELECT category_id, ROUND(AVG(unit_price)::NUMERIC, 1) FROM products WHERE category_id <= 5
GROUP BY category_id;

-- atividade 6

SELECT * FROM products

SELECT supplier_id, COUNT(product_id), ROUND(AVG(unit_price)::NUMERIC, 1) FROM products
GROUP BY supplier_id
ORDER BY 3 DESC
LIMIT 5;


-- Base Orders

-- atividade 1

SELECT * FROM orders ORDER BY order_date;
SELECT employee_id, COUNT(order_id) FROM orders WHERE order_date >= '1996-07-01' AND order_date <= '1996-09-30'
GROUP BY employee_id
ORDER BY 2 DESC
LIMIT 3;

-- Plus

SELECT employee_id, extract(MONTH FROM order_date)::integer, COUNT(order_id) FROM orders WHERE order_date >= '1996-07-01' AND order_date <= '1996-09-30'
GROUP BY employee_id, extract(MONTH FROM order_date)::integer
ORDER BY 2 DESC
LIMIT 3;

SELECT employee_id, extract(MONTH FROM order_date)::integer, extract(YEAR FROM order_date)::integer, COUNT(order_id) FROM orders WHERE order_date >= '1996-07-01' AND order_date <= '1996-09-30'
GROUP BY employee_id, extract(MONTH FROM order_date)::integer, extract(YEAR FROM order_date)::integer
ORDER BY 2 DESC;


-- atividade 2

SELECT * FROM orders;
SELECT customer_id, COUNT(order_id) AS CNT FROM orders WHERE employee_id IS NOT NULL
GROUP BY customer_id
-- HAVING = Coluna 2 maior que 2 nesse caso
HAVING COUNT(order_id) >= 2
ORDER BY 2 DESC;

-- Base suppliers

-- atividade 1

SELECT * FROM suppliers

SELECT * FROM suppliers WHERE country = 'USA'

SELECT country, CASE WHEN country IN ('USA', 'Brazil', 'Canada') THEN 'Americas' ELSE 'Outros' END AS "Continent",  COUNT(company_name) FROM suppliers
WHERE phone NOT LIKE '(1%'
GROUP BY country;

-- atividade 2
/*2) Existe algum código de área de telefone que pertence a mais de uma cidade?*/

-- VERSÃO GAMESHARK
-- CRIANDO UMA TABELA AUXILIAR, sendo GROUP BY s a tabela auxiliar
SELECT city FROM (
SELECT COUNT(city) AS CNT, (SUBSTRING(phone, '\(([0-9]+)\)')) AS DDD FROM suppliers
GROUP BY (SUBSTRING(phone, '\(([0-9]+)\)')))s
LEFT JOIN suppliers ss ON (SUBSTRING(ss.phone, '\(([0-9]+)\)')) = s.DDD AND CNT > 1 
WHERE ss.city IS NOT NULL;

-- OUTRA VERSÃO
SELECT COUNT(city) as contador_cidades, SPLIT_PART(phone, ' ', 1) as codigo_telefone
FROM suppliers
WHERE SPLIT_PART(phone, ' ', 1) LIKE '(%'
GROUP BY SPLIT_PART(phone, ' ', 1)

-- atividade 3

SELECT CIDADE, CNT, city, RANK() OVER(PARTITION BY city ORDER BY city)
FROM (
SELECT LEFT(city,1) AS CIDADE, COUNT(city) AS CNT FROM suppliers
GROUP BY LEFT(city,1)
ORDER BY 2 DESC
LIMIT 5)s
LEFT JOIN suppliers ss ON s.CIDADE = LEFT(city, 1)
ORDER BY 2 DESC;


-- outra versão
SELECT SUBSTR(city, 1, 1), COUNT(city) FROM suppliers
GROUP BY SUBSTR(city, 1, 1);


SELECT LEFT(city,1) AS CIDADE, COUNT(city) AS CNT FROM suppliers
GROUP BY LEFT(city,1)
ORDER BY 2 DESC

SELECT city, cnt, index FROM suppliers 
INNER JOIN (
SELECT  LEFT(city,1) as ci, COUNT(LEFT(city,1))as cnt, ROW_NUMBER() OVER ( ORDER BY COUNT(LEFT(city,1)) DESC)  as index FROM suppliers
GROUP BY LEFT(city,1)
ORDER BY 2 DESC
LIMIT 5) s
ON s.ci = LEFT(suppliers.city,1) 
ORDER BY s.cnt DESC