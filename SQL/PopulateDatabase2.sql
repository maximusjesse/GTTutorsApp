#Populate Database
DELETE FROM Administrator;
DELETE FROM Course;
DELETE FROM Grad; 
DELETE FROM Professor; 
DELETE FROM Rates; 
DELETE FROM Recommends; 
DELETE FROM Student; 
DELETE FROM Tutor; 
DELETE FROM Tutors; 
DELETE FROM TutorTimeSlots; 
DELETE FROM Undergrad;
DELETE FROM User;
DELETE FROM Hires;

INSERT INTO Administrator
VALUES(000000000);

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
(000000013,'undergrad13t'),
(000000014,'undergrad14t'),
(000000015,'undergrad15t'),
(000000110,'grad1t'),
(000000120,'grad2t'),
(000000130,'grad3t'),
(000000140,'grad4'),
(000000150,'grad5'),
(000001100,'prof1'),
(000001200,'prof2'),
(000001300,'prof3'),
(000001400,'prof4'),
(100000000,'password'),
(200000000,'password'),
(300000000,'password');

INSERT INTO Student
VALUES
(000000001, NULL, NULL),
(000000002, 'undergrad2@gatech.edu', 'Undergrad 2'),
(000000003, 'undergrad3@gatech.edu', 'Undergrad 3'),
(000000004, 'undergrad4@gatech.edu', 'Undergrad 4'),
(000000005, 'undergrad5@gatech.edu', 'Undergrad 5'),
(000000006, 'undergrad6@gatech.edu', 'Undergrad 6'),
(000000007, 'undergrad7@gatech.edu', 'Undergrad 7'),
(000000008, 'undergrad8@gatech.edu', 'Undergrad 8'),
(000000009, 'undergrad9@gatech.edu', 'Undergrad 9'),
(000000010, 'undergrad10@gatech.edu', 'Undergrad 10'),
(000000011, 'undergrad11@gatech.edu', 'Undergrad 11'),
(000000012, 'undergrad12@gatech.edu', 'Undergrad 12'),
(000000013, 'undergrad13t@gatech.edu', 'Undergrad 13t'),
(000000014, 'undergrad14t@gatech.edu', 'Undergrad 14t'),
(000000015, 'undergrad15t@gatech.edu', 'Undergrad 15t'),
(000000110, 'grad1t@gatech.edu', 'Grad 1t'),
(000000120, 'grad2t@gatech.edu', 'Grad 2t'),
(000000130, 'grad3t@gatech.edu', 'Grad 3t'),
(000000140, 'grad4@gatech.edu', 'Grad 4'),
(000000150, 'grad5@gatech.edu', 'Grad 5'),
(100000000, null, null),
(200000000, null, null),
(300000000, null, null);

INSERT INTO Grad
Values(000000110),
(000000120),
(000000130),
(000000140),
(000000150);

INSERT INTO Undergrad
VALUES
(000000002),
(000000003),
(000000004),
(000000005),
(000000006),
(000000007),
(000000008),
(000000009),
(000000010),
(000000011),
(000000012),
(000000013),
(000000014),
(000000015);

INSERT INTO Professor
VALUES(000001100),
(000001200),
(000001300),
(000001400);

INSERT INTO Tutor
VALUES(000000013, 6780000013, 4.0),
(000000014,6780000014,3.5),
(000000015,6780000015,3.8),
(000000110,6780000110,3.7),
(000000120,6780000120,4.0),
(000000130,6780000130,3.5);

INSERT INTO Course
Values('MATH', 4305),
('CS', 4400),
('CS', 2316),
('MATH', 1000),
('MATH', 2000),
('Bio', 4313),
('CS', 1301),
('ME', 2110),
('ME', 3000),
('ISYE', 2027),
('ISYE', 2028),
('ISYE', 3232);
-- ('ISYE', 3133),
-- ('ISYE', 3039),
-- ('ISYE', 4316),
-- ('Chem', 1310),
-- ('Chem', 1211),
-- ('Chem', 1212),
-- ('Psyc', 1101),
-- ('COE', 2110),
-- ('BIO', 4000)

INSERT INTO TutorTimeSlots
Values(000000013, '09:00:00', 'Fall', 'Tr'),
(000000013, '10:00:00', 'Fall', 'Tr'),
(000000013, '11:00:00', 'Fall', 'Tr'),
(000000014, '13:00:00', 'Fall', 'W'),
(000000014, '14:00:00', 'Fall', 'W'),
(000000014, '15:00:00', 'Fall', 'W'),
(000000014, '10:00:00', 'Spring', 'W'),
(000000014, '11:00:00', 'Spring', 'W'),
(000000014, '12:00:00', 'Spring', 'W'),
(000000015, '11:00:00', 'Spring', 'T'),
(000000015, '12:00:00', 'Spring', 'T'),
(000000015, '13:00:00', 'Spring', 'T'),
(000000110,'08:00:00','Spring', 'M'),
(000000110,'09:00:00','Spring', 'M'),
(000000110,'10:00:00','Spring', 'M'),
(000000110,'10:00:00','Summer', 'Tr'),
(000000120,'12:00:00','Summer', 'M'),
(000000120,'13:00:00','Summer', 'Tr'),
(000000120,'14:00:00','Summer', 'M'),
(000000120,'14:00:00','Summer', 'W'),
(000000130,'15:00:00','Summer', 'M'),
(000000130,'16:00:00','Summer', 'F'),
(000000130,'17:00:00','Summer', 'M'),
(000000120, '11:00:00', 'Spring', 'T'),
(000000120, '09:00:00', 'Fall', 'F');

INSERT INTO Hires
Values
(000000005, 'CS', 4400, 000000014, '14:00:00', 'Fall', 'W'),
(000000004, 'CS', 4400, 000000014, '12:00:00', 'Spring', 'W'),
(000000002, 'MATH', 2000, 000000120,'13:00:00','Summer', 'Tr'),
(000000003, 'CS', 4400, 000000120,'14:00:00','Summer', 'W'),
(000000001, 'ISYE', 3232, 000000120, '11:00:00', 'Spring', 'T');

INSERT INTO Rates
Values(000000001, 000000013, 'MATH', 4305, 4, 'I only did this to get extra credit', 'FALL'),
(000000002, 000000014, 'CS', 4400, 1, 'PLEASE WASH YOUR HAIR', 'Summer'),
(000000003, 000000110, 'Math', 1000, 4, 'I LOVE YOU', 'SPRING'),
(000000004, 000000015, 'ISYE', 2028, 3, 'YOU ARE ONE STEP ABOVE MEDIOCRITY', 'Spring');

INSERT INTO Tutors
Values(000000013, 'MATH', 4305, FALSE),
(000000014, 'CS', 4400, FALSE),
(000000014, 'ME', 2110, FALSE),
(000000014, 'ISYE', 2027, FALSE),
(000000015, 'CS', 2316, FALSE),
(000000015, 'CS', 4400, FALSE),
(000000015, 'ISYE', 2028, FALSE),
(000000110, 'MATH', 1000, TRUE),
(000000120, 'MATH', 2000, FALSE),
(000000120, 'CS', 4400, TRUE),
(000000130, 'BIO', 4313, FALSE),
(000000130, 'CS', 4400, TRUE),
(000000120, 'ISYE', 3232, FALSE),
(000000120, 'BIO', 4313, TRUE);

INSERT INTO Recommends
Values(000000110, 000001100, 4, 'VERY GOOD'),
(000000110, 000001200, 3, 'MOSTLY GOOD'),
(000000110, 000001300, 4, 'I WISH I WERE YOU'),
(000000013, 000001100, 2, 'VERY GOOD'),
(000000014, 000001400, 4, 'NOT BAD'),
(000000014, 000001200, 4, 'TEACH MY KIDS'),
(000000015, 000001100, 1, 'I LEARNED MORE WATCHING BILL NYE'),
(000000120, 000001400, 4, 'FINE, YOU SHOW SUPERB UNDERSTANDING OF THE MATERIAL, BUT MORE IMPORTANTLY, YOU INSPIRE CHILDREN.'),
(000000130, 000001100, 1, 'GET OUTTA HERE'),
(000000140, 000001100, 3, 'OK');