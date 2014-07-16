SQL Create Tables

CREATE TABLE User (
	Gtid INTEGER(9) PRIMARY KEY,
	Password VARCHAR(30) NOT NULL
)

CREATE TABLE Administrator (
	AdminID INTEGER(9) PRIMARY KEY,
	FOREIGN KEY (AdminID) REFERENCES User(Gtid)
)

CREATE TABLE Student (
	StudentID INTEGER(9) NOT NULL,
	Email VARCHAR(30) PRIMARY KEY,
	Name VARCHAR(30) NOT NULL,
	FOREIGN KEY (StudentID) REFERENCES User(Gtid)
)

CREATE TABLE Professor (
	ProfessorID Integer(9) PRIMARY KEY,
	FOREIGN KEY (ProfessorID) REFERENCES User(Gtid)
)

CREATE TABLE Grad (
	GradID Integer(9) NOT NULL,
	Email VARCHAR(30) PRIMARY KEY,
	FOREIGN KEY (GradID) REFERENCES User(Gtid),
	FOREIGN KEY (Email) REFERENCES Student(Email)
)

CREATE TABLE Undergrad (
	UndergradID Integer(9) NOT NULL PRIMARY KEY,
	FOREIGN KEY (UndergradID) REFERENCES Student(StudentID)
)

CREATE TABLE Tutor (
	TutorID Integer(9) NOT NULL PRIMARY KEY,
	Phone Integer(10),
	GPA double,
	FOREIGN KEY (TutorID) REFERENCES Student(StudentID)
)

CREATE TABLE Course (
	School VARCHAR(30) NOT NULL,
	Number Integer(4) NOT NULL,
	PRIMARY KEY (School, Number)
)

CREATE TABLE TutorTimeSlots (
	TutorID Integer(9) NOT NULL,
	Time TIME NOT NULL,
	Semester VARCHAR(30) NOT NULL,
	Weekday VARCHAR(30) NOT NULL,
	FOREIGN KEY (TutorID) REFERENCES User(Gtid),
	PRIMARY KEY (TutorID, Time, Semester, Weekday)
)

CREATE TABLE Rates (
	StudentID Integer(9) NOT NULL,
	TutorID  Integer(9),
	School VARCHAR(30) NOT NULL,
	Number Integer(4) NOT NULL,
	NumEvaluation Integer(2),
	DescEvaluation VarChar(200),
	Semester VarChar(30),
	Primary Key(StudentID, School, Number),
    Foreign Key(TutorID) REFERENCES TutorTimeSlots(TutorID),
    Foreign Key(Semester) REFERENCES TutorTimeSlots(Semester),
	Foreign Key (StudentID) REFERENCES User(Gtid)
)

CREATE TABLE Tutors (
	TutorID Integer(9) NOT NULL,
	School VarChar(30) NOT NULL,
	Number Integer(4) NOT NULL,
	StudentID Integer(9),
    Foreign Key(TutorID) REFERENCES Student(StudentID),
    Foreign Key(School) REFERENCES Course(School),
    Foreign Key(Number) REFERENCES Course(Number),
	Primary Key(TutorID, School, Number)
)

CREATE TABLE Recommends (
	TutorID Integer(9) NOT NULL,
	ProfessorID Integer(9) NOT NULL,
	NumEvaluation Integer(2),
	DescEvaluation VarChar(200),
	Primary Key(TutorID, ProfessorID),
	Foreign Key (ProfessorID) REFERENCES Professor(ProfessorID)
)

/*CREATED VIEWS*/

CREATE VIEW Summary1 AS
	SELECT CONCAT(t.School, t.Number) as 'Course', tts.Semester, Count(t.StudentID) as 'NumStudents', Count(t.TutorID) as 'NumTutors'
	FROM tutors t, tutortimeslots tts
	WHERE t.TutorID=tts.TutorID
	Group by Course, Semester WITH ROLLUP

CREATE VIEW Summary2 AS
	SELECT CONCAT(t.School, t.Number) as 'Course', tts.Semester, Count(g.GradID) as 'TA', AVG(r.numEvaluation) as 'AvgRating', Count(u.undergradID) as 'nonTA', AVG(r2.numEvaluation) as 'AvgRating'
	FROM tutors t, tutortimeslots tts, grad g, rates r, undergrad u, rates r2
	WHERE t.TutorID=tts.TutorID
	AND g.GradID=r.TutorID
	AND u.undergradID=r2.TutorID
	Group by Course, Semester WITH ROLLUP

CREATE VIEW TutorInfo AS
	SELECT s.Name, s.Email, Avg(r.NumEvaluation) as 'AvgProfRating', Count(r.ProfessorID) as 'NumProfessors', Avg(ra.NumEvaluation) as 'AvgStudentRating', Count(ra.StudentID) as 'NumStudents', s.StudentID as 'TutorID'
	FROM Student s, Recommends r, Rates ra
	Where s.StudentID=r.TutorID
	AND s.StudentID=ra.TutorID

CREATE VIEW TutorSchedule AS
	SELECT tts.Weekday as 'Day', tts.Time, ti.Name, ti.Email, CONCAT(c.School, c.Number) as 'Course', ti.TutorID
	From tutortimeslots tts, TutorInfo ti, course c, tutors t
	Where tts.TutorID=ti.TutorID
	AND t.school=c.school
	AND t.number=c.number
