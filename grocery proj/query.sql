-- Active: 1662631171343@@127.0.0.1@3306@grocery

create table
    item_list (
        sno int(5) AUTO_INCREMENT PRIMARY KEY,
        name varchar(60),
        price DECIMAL(7, 2)
    );

show tables;

select * from item_list;

drop table item_list;

insert into
    item_list(name, price)
values ('Chips', 10.00), ('Eggs', 12.00);

create table
    history(
        name VARCHAR(100),
        phone_no int(10),
        date date DEFAULT(curdate()),
        items varchar(10000),
        total decimal(8, 2)
    );

select * from history;