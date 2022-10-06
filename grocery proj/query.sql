-- Active: 1664971720388@@127.0.0.1@3306@grocery

create table
    item_list (
        sno int(5) AUTO_INCREMENT PRIMARY KEY,
        name varchar(60),
        quan int,
        price DECIMAL(7, 2)
    );

show tables;

select * from item_list;

drop table item_list;

insert into
    item_list(name, quan, price)
values ('Chips', 100, 10.00), ('Eggs', 200, 12.00), ("Chocolate", 250, 10.00), ("Bread", 50, 45.00), ("Milk", 70, 17.50), ("Cold Drinks", 50, '40.00');

insert into
    history(name, phone_no, items, total)
values (
        'man',
        7636576365,
        '["doesnt matter"]',
        133
    );

create table
    history(
        name VARCHAR(100),
        phone_no bigint,
        date date DEFAULT(curdate()),
        items varchar(10000),
        total decimal(8, 2)
    );

select * from history;

drop table history;

desc item_list;

desc history;