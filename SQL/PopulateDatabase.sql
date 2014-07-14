Populate Database

INSERT INTO User
VALUES(333333333, 'tutor1')
VALUES(222222222, 'stud1')
Values(111111111, 'tutor')
Values(888888888, 'undergrad')
Values(987654321, 'grad')
Values(902803967, 'junior17')
Values(000000000, 'admin')
Values(123456789, 'prof')
Values(902928313, 'pink')
Values(902000000, 'hey')
Values(903000000, 'ok')
Values(100000000, 'a')
Values(200000000, 'b')
Values(300000000, 'c')
Values(400000000, 'd')
Values(500000000, 'e')
Values(600000000, 'f')
Values(700000000, 'g')
Values(800000000, 'h')
Values(900000000, 'i')
Values(101000000, 'j')

INSERT INTO Grad
Values(987654321, 'grad@gatech.edu')

INSERT INTO Undergrad
Values(888888888)

INSERT INTO Tutor
VALUES(333333333,333333333,4.0)
Values(111111111,111111111,4.0)

INSERT INTO Course
Values('MATH', 4305)
Values('CS', 4400)

INSERT INTO TutorTimeSlots
Values(333333333, '09', 'Fall 2014', 'Thursday')
Values(111111111, '10', 'Fall 2014', 'Wednesday')
Values(333333333, '11', 'Spring 2014', 'Tuesday')
Values(111111111,'12:00:00','Summer 2014', 'Monday')

INSERT INTO Rates
Values(902803967, 111111111, 'CS', 4400, 4, 'SO GOOD', 'Summer 2014')

INSERT INTO Tutors
Values(111111111, 'Math', 4305, 902803967)
VALUES(111111111, 'Math', 4305, 888888888)
Values(333333333, 'Math', 4305, 222222222)
Values(111111111, 'CS', 4400, 902803967)

INSERT INTO Recommends
Values(111111111, 123456789, 4, 'VERY GOOD')

INSERT INTO Administrator
Values(000000000)

INSERT INTO Student
Values(222222222, 'stud1@gatech.edu', 'Student 1')
VALUES(333333333, 'tutor1@gatech.edu', 'Tutor 1')
Values(111111111, 'tutor@gatech.edu', 'Tutor Tutorson')
Values(888888888, 'undergrad@gatech.edu', 'Undergrad Mcgrad')
VALUES(987654321, 'grad@gatech.edu', 'Grad McGrad')
VALUES(902803967, 'jzhao@gatech.edu', 'Jesse Zhao')

INSERT INTO Professor
VALUES(123456789)

INSERT INTO TutorTimeSlots
VALUES('12:00:00', 'Fall', 'Wednesday')

INSERT INTO Tutor
VALUES(902803967, 'JZHAO@GATECH.EDU', 'Password', 'Jesse', 'Zhao', '6787431685', '3.5')

SELECT * FROM Tutor

INSERT INTO Course
VALUES('CS', 4400)

SHOW KEYS FROM Course WHERE Key_name = 'PRIMARY'

INSERT INTO student
VALUES(902803967, 'JZHAO@GATECH.EDU', 'Password', 'Jesse', 'Zhao')

Select * from User

drop table tutor
select * from Student

