-- Active: 1663667278013@@127.0.0.1@3306@scholar

create table
    scholar(
        roll int(5),
        address varchar(50),
        name VARCHAR(50),
        city varchar(20),
        class int(2),
        phone int(10),
        age int(2),
        regfee int(10)
    );

delete from scholar where roll=5;

select * from scholar where roll =5;

select * from scholar;