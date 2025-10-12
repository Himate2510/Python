create table if not exists product (
pro_id int Primary Key,
pro_name text,
quantity int,
price int);
insert into product(pro_id, pro_name, quantity, price) VALUES
(1, 'Laptop', 50, 800),
(2, 'Smartphone', 200, 600),
(3, 'Tablet', 150, 300),
(4, 'Monitor', 80, 150),
(5, 'Keyboard', 300, 50);
select pro_name, price from product where price = (select min(price) from product);
select pro_name, price from product where price = (select max(price) from product);
