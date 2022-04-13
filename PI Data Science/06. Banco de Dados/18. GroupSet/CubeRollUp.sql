DROP TABLE IF EXISTS #inventory;
CREATE TABLE #inventory (
    warehouse VARCHAR(255),
    product VARCHAR(255) NOT NULL,
    model VARCHAR(50) NOT NULL,
    quantity INT,
    PRIMARY KEY (warehouse,product,model)
);

INSERT INTO #inventory(warehouse, product, model, quantity)
VALUES('San Jose', 'iPhone','6s',100);
INSERT INTO #inventory(warehouse, product, model, quantity)
VALUES('San Fransisco', 'iPhone','6s',50);
INSERT INTO #inventory(warehouse, product, model, quantity)
VALUES('San Jose','iPhone','7',50);
INSERT INTO #inventory(warehouse, product, model, quantity)
VALUES('San Fransisco', 'iPhone','7',10);
INSERT INTO #inventory(warehouse, product, model, quantity)
VALUES('San Jose','iPhone','X',150);
INSERT INTO #inventory(warehouse, product, model, quantity)
VALUES('San Fransisco', 'iPhone','X',200);
INSERT INTO #inventory(warehouse, product, model, quantity)
VALUES('San Jose','Samsung','Galaxy S',200);
INSERT INTO #inventory(warehouse, product, model, quantity)
VALUES('San Fransisco','Samsung','Galaxy S',200);
INSERT INTO #inventory(warehouse, product, model, quantity)
VALUES('San Fransisco','Samsung','Note 8',100);
INSERT INTO #inventory(warehouse, product, model, quantity)
VALUES('San Jose','Samsung','Note 8',150);


SELECT
    warehouse,
    product, 
    SUM (quantity) qty
FROM
    #inventory
GROUP BY
    GROUPING SETS(
        (warehouse,product),
        (warehouse),
        (product),
        ()
    );



SELECT
   COALESCE(warehouse, '...All Warehouses') warehouse,
  COALESCE(product, '...All Products') product,
   SUM(quantity) 
FROM
   #inventory
GROUP BY
   CUBE(warehouse,product)
ORDER BY
   warehouse,
   product; 

SELECT 
    warehouse, product, SUM(quantity)
FROM
    #inventory
GROUP BY ROLLUP (warehouse , product);

-- soma parcial
SELECT 
    warehouse, product, SUM(quantity)
FROM
    #inventory
GROUP BY warehouse, ROLLUP (product);