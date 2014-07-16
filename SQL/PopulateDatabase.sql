Populate Database

INSERT INTO User
VALUES(000000000,'admin'),
(000000001,'undergrad1'),
(000000002,'undergrad2'),
(000000003,'undergrad3'),
(000000004,'undergrad4'),
(000000005,'undergrad5'),
(000000006,'undergrad6'),
(000000007,'undergrad7'),
(000000008,'undergrad8'),
(000000009,'undergrad9'),
(000000010,'undergrad10'),
(000000011,'undergrad11'),
(000000012,'undergrad12'),
(000000013,'undergrad13'),
(000000014,'undergrad14'),
(000000015,'undergrad15'),
(000000110,'grad1'),
(000000120,'grad2'),
(000000130,'grad3'),
(000000140,'grad4'),
(000000150,'grad5'),
(000001100,'prof1'),
(000001200,'prof2'),
(000001300,'prof3'),
(000001400,'prof4')

INSERT INTO Grad
Values(987654321, 'grad@gatech.edu')

INSERT INTO Undergrad
Values(888888888)

INSERT INTO Tutor
VALUES(333333333,333333333,4.0)
Values(111111111,111111111,4.0)

INSERT INTO Course
Values('MATH', 4305)
('CS', 4400),
('CS', 2316),
('Math', 1000),
('MATH', 2000),
('Bio', 4313),
('CS', 1301),
('ME', 2110),
('ME', 3000),
('ISYE', 2027),
('ISYE', 2028),
('ISYE', 3232)
('ISYE', 3133),
('ISYE', 3039),
('ISYE', 4316),
('Chem', 1310),
('Chem', 1211),
('Chem', 1212),
('Psyc', 1101),
('COE', 2110),
('BIO', 4000)

INSERT INTO TutorTimeSlots
Values(333333333, '09', 'Fall 2014', 'Thursday'),
(111111111, '10', 'Fall 2014', 'Wednesday'),
(333333333, '11', 'Spring 2014', 'Tuesday'),
(111111111,'12:00:00','Summer 2014', 'Monday')

INSERT INTO Rates
Values(902803967, 111111111, 'CS', 4400, 4, 'SO GOOD', 'Summer 2014')

INSERT INTO Tutors
Values(111111111, 'Math', 4305, 902803967),
(111111111, 'Math', 4305, 888888888),
(333333333, 'Math', 4305, 222222222),
(111111111, 'CS', 4400, 902803967)

INSERT INTO Recommends
Values(111111111, 123456789, 4, 'VERY GOOD')

INSERT INTO Administrator
Values(000000000)

INSERT INTO Student
Values(222222222, 'stud1@gatech.edu', 'Student 1'),
(333333333, 'tutor1@gatech.edu', 'Tutor 1'),
(111111111, 'tutor@gatech.edu', 'Tutor Tutorson'),
(888888888, 'undergrad@gatech.edu', 'Undergrad Mcgrad'),
(987654321, 'grad@gatech.edu', 'Grad McGrad')

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

