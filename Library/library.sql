show tables;

desc lib_table;

select * from lib_table;

create table daanseva(
    Book_No int(6),
    Stu_name varchar(30),
    Class int(2),
    Roll_No int(2),
    date DATE DEFAULT(curdate())
);

drop TABLE lib_table;

create table lib_table(
    Book_No int(6) PRIMARY KEY,
    Book_Title VARCHAR(50),
    Author VARCHAR(30),
    Publisher VARCHAR(30),
    year VARCHAR(4),
    Type VARCHAR(15),
    Price DECIMAL(6, 2)
);

desc brail;

desc daanseva;

insert into
    brail
VALUES(
        123,
        'Catcher In The Rye',
        'Moby Dick',
        'Light Novel',
        '6.99'
    );

insert into
    daanseva(Book_No, Stu_name, Class, Roll_No)
VALUES(123, 'jai singh kharbandha', '12', '69');

select * from daanseva;

SELECT * from brail;

alter table
    daanseva
add
    FOREIGN key(Book_No) REFERENCES lib_table(Book_No) on update CASCADE on delete cascade;

delete from brail where Book_No = 135 ;

drop table lib_table;

insert into
    lib_table
values
    (
        2,
        "work",
        "thara baap",
        "bhaiation",
        "2022",
        "Friction",
        "69.00"
    );