-- Active: 1659458632197@@127.0.0.1@3306@library

show tables;

desc lib_table;

select * from lib_table;

/ / Book_No,
Book_Title,
Author,
Stu_name,
Class,
Roll_No,
fine,
lentdate(curdate),
duedate
create table
    daanseva(
        Book_No int(6),
        Stu_name varchar(30),
        Class int(2),
        Roll_No int(2),
        date DATE DEFAULT(curdate())
    );

create table
    lib_table(
        Book_No int(6) PRIMARY KEY,
        Book_Title VARCHAR(80),
        Author VARCHAR(60),
        Publisher VARCHAR(60),
        year VARCHAR(4),
        Type VARCHAR(40),
        Price DECIMAL(6, 2)
    );

desc brail;

desc daanseva;

insert into brail
VALUES (
        123,
        'Catcher In The Rye',
        'Moby Dick',
        'Light Novel',
        '6.99'
    );

insert into
    daanseva(
        Book_No,
        Stu_name,
        Class,
        Roll_No
    )
VALUES (
        123,
        'jai singh kharbandha',
        '12',
        '69'
    );

select * from daanseva;

SELECT * from brail;

alter table daanseva
add
    FOREIGN key(Book_No) REFERENCES lib_table(Book_No) on update CASCADE on delete cascade;

delete from brail where Book_No = 135 ;

drop table lib_table;

insert into lib_table
values (
        2,
        "work",
        "thara baap",
        "bhaiation",
        "2022",
        "Friction",
        "69.00"
    );

delete from lib_table where Book_No = 32069 ;

select * from lib_table where Book_No = 32069;

# LIB SQL UPDTE (ADDING CABINET COLUMN);

alter table lib_table add shelf VARCHAR(10) DEFAULT(NULL);

alter table lib_table drop COLUMN shelf;

drop table lending_table;

create table
    lending_table(
        Book_No int(6),
        Stu_name VARCHAR(40),
        Roll int(3),
        Class VARCHAR(7),
        Islost varchar(3) DEFAULT('no'),
        Date DATE DEFAULT(curdate()),
        Days_left int(100) DEFAULT(0),
        Fee DECIMAL(7, 2) DEFAULT(0),
        FOREIGN KEY (Book_No) REFERENCES lib_table(Book_No)
    );

desc lending_table;

insert into
    lending_table(Book_No, Stu_name, Roll, Class)
VALUES (415, 'Mama', 26, '9C');

select a.*, b.Book_Title
from
    lending_table a,
    lib_table b
where a.Book_No = b.Book_No;