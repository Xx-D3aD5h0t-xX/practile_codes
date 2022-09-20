-- Active: 1663667278013@@127.0.0.1@3306@paris

select * from items;

desc items;

create table
    student(
        Admno int(4),
        Roll int(3),
        Name VARCHAR(40),
        Class int(2)
    );

drop table student;

desc student;

insert into student VALUES(3021, 1, 'Aarin', 12);

insert into student VALUES(3302, 6, 'Bhavika', 12);

insert into student VALUES(3214, 9, 'Joe', 12);

insert into student VALUES(3619, 21, 'Sahil', 12);

insert into student VALUES(3451, 30, 'Andrew', 12);

insert into student(marks) ;

Alter table student add Marks VARCHAR(100);

Alter table student modify Marks int(100);

alter table student drop Class;

UPDATE student set admno = 3021 where Roll = 1;

DELETE from student where Roll = 21;

select * from student GROUP BY(marks);