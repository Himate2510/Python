CREATE TABLE students(
Rno int PRIMARTY KEY,
Name text,
city text,
subject text);
insert into students (Rno, Name, city, subject) values
(1, 'Alice', 'New York', 'Math'),
(2, 'Bob', 'Los Angeles', 'Science'),
(3, 'Charlie', 'Chicago', 'History'),
(4, 'David', 'Houston', 'Math'),
(5, 'Eve', 'Phoenix', 'Science');

Select * From students;
Select * from students where name = "David" and subject = "Math";
Select * from students where name = "Eve" Or name= "Charlie";
