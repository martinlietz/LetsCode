-- 1. Obtenha uma tabela que contenha o id do pedido e o valor total do mesmo

SELECT order_details.order_id, 
SUM((order_details.quantity * order_details.discount)) + AVG(orders.freight) AS valor_total
FROM order_details 
INNER JOIN orders ON orders.order_id = order_details.order_id
GROUP BY order_details.order_id
LIMIT 1

-- 2. Obtenha uma lista dos 10 clientes que realizaram o maior número de pedidos, bem como o número de pedidos de cada, ordenados em ordem decrescente de nº de pedidos.
SELECT customers.customer_id, customers.company_name
,COUNT(orders.order_id) AS num_pedidos
FROM orders 
INNER JOIN customers ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_id
ORDER BY 3 DESC
LIMIT 10

--3. Obtenha uma tabela que contenha o id e o valor total do pedido e o nome do cliente que o realizou.

SELECT order_details.order_id, 
SUM((products.unit_price * order_details.quantity * (1 - order_details.discount))) + AVG(orders.freight) as total_order_price
, customers.company_name
, customers.contact_name
FROM order_details 
INNER JOIN products ON order_details.product_id = products.product_id
INNER JOIN orders ON orders.order_id = order_details.order_id
INNER JOIN customers ON customers.customer_id = orders.customer_id
GROUP BY order_details.order_id, customers.company_name, customers.contact_name
LIMIT 1


--4. Obtenha uma tabela que contenha o país do cliente e o valor da compra que ele realizou.

SELECT order_details.order_id, 
ROUND(
      SUM((products.unit_price * order_details.quantity * (1 - order_details.discount))) + AVG(orders.freight)
  ) as total_order_price
, customers.company_name
, customers.country
FROM order_details 
INNER JOIN products ON order_details.product_id = products.product_id
INNER JOIN orders ON orders.order_id = order_details.order_id
INNER JOIN customers ON customers.customer_id = orders.customer_id
GROUP BY order_details.order_id, customers.company_name, customers.country
LIMIT 4


-- 5. Obtenha uma tabela que contenha uma lista dos países dos clientes e o valor total de compras realizadas em cada um dos países. 
      -- Ordene a tabela, na order descrescente, considerando o valor total de compras realizadas por país.
      
SELECT  customers.country
,SUM((order_details.quantity * order_details.discount)) + AVG(orders.freight) AS valor_total
FROM customers 
INNER JOIN orders ON customers.customer_id = orders.customer_id
INNER JOIN order_details ON order_details.order_id = orders.order_id
GROUP BY customers.country
ORDER BY customers.country DESC
LIMIT 5


--6. Obtenha uma tabela com o valor médio das vendas em cada mês (ordenados do mês com mais vendas para o mês com menos vendas).
WITH base as (
SELECT  extract(MONTH FROM orders.order_date)::INTEGER AS "Mes"
,extract(YEAR FROM orders.order_date)::INTEGER AS "Ano"
,order_details.order_id
,(
      SUM((products.unit_price * order_details.quantity * (1 - order_details.discount))) + AVG(orders.freight)
  ) / COUNT(orders.order_id) as mean_order_price
FROM orders 
INNER JOIN order_details ON order_details.order_id = orders.order_id
INNER JOIN products ON order_details.product_id = products.product_id

GROUP BY order_details.order_id,
extract(MONTH FROM orders.order_date)::INTEGER 
,extract(YEAR FROM orders.order_date)::INTEGER )

SELECT "Mes","Ano", AVG(mean_order_price) AS "ValorMedia" FROM base
GROUP BY "Ano", "Mes"
ORDER BY 3 DESC
--LIMIT 5