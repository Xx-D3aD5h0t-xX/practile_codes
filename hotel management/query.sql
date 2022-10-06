-- Active: 1664989589964@@127.0.0.1@3306@hotel_management

show tables;

drop table c_details;

drop table booking_record;

create table
    c_details(
        c_id char(5) primary key,
        c_name varchar(30),
        c_phno varchar(10),
        c_address VARCHAR(50),
        c_email varchar(40),
        room int DEFAULT(0),
        pool int DEFAULT(0),
        restaurant int DEFAULT(0),
        total int
    );

create table
    booking_record(
        c_id char(5),
        restaurant int,
        total int,
        pool int,
        room int,
        FOREIGN key(c_id) REFERENCES c_details(c_id) on update CASCADE on delete cascade
    );

desc c_details;