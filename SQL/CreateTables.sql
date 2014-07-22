#SQL Create Tables
Drop Table Administrator, Course, Grad, Professor, Rates, Recommends, Student, Tutor, Tutors, TutorTimeSlots, Undergrad, User, Summary;
CREATE TABLE User (
	Gtid INTEGER(9) PRIMARY KEY,
	Password VARCHAR(30) NOT NULL
);

CREATE TABLE Administrator (
	AdminID INTEGER(9) PRIMARY KEY,
	FOREIGN KEY (AdminID) REFERENCES User(Gtid)
);

CREATE TABLE Student (
	StudentID INTEGER(9) PRIMARY KEY,
	Email VARCHAR(30) NOT NULL,
	Name VARCHAR(30) NOT NULL,
	FOREIGN KEY (StudentID) REFERENCES User(Gtid)
);

CREATE TABLE Professor (
	ProfessorID Integer(9) PRIMARY KEY,
	FOREIGN KEY (ProfessorID) REFERENCES User(Gtid)
);

CREATE TABLE Grad (
	GradID Integer(9) NOT NULL,
	Email VARCHAR(30) PRIMARY KEY,
	FOREIGN KEY (GradID) REFERENCES User(Gtid),
	FOREIGN KEY (Email) REFERENCES Student(Email)
);

CREATE TABLE Undergrad (
	UndergradID Integer(9) NOT NULL PRIMARY KEY,
	FOREIGN KEY (UndergradID) REFERENCES Student(StudentID)
);

CREATE TABLE Tutor (
	TutorID Integer(9) NOT NULL PRIMARY KEY,
	Phone VARCHAR(15),
	GPA double,
	FOREIGN KEY (TutorID) REFERENCES Student(StudentID)
);

CREATE TABLE Course (
	School VARCHAR(30) NOT NULL,
	Number Integer(4) NOT NULL,
	PRIMARY KEY (School, Number)
);

CREATE TABLE TutorTimeSlots (
	TutorID Integer(9) NOT NULL,
	Time TIME NOT NULL,
	Semester VARCHAR(30) NOT NULL,
	Weekday VARCHAR(30) NOT NULL,
	TuteeID INTEGER(9),
	School VARCHAR(30),
	Number Integer(4),
	FOREIGN KEY(School, Number) REFERENCES Tutors(School, Number),
	FOREIGN KEY (TuteeID) REFERENCES User(Gtid),
	FOREIGN KEY (TutorID) REFERENCES Tutor(TutorID),
	PRIMARY KEY (TutorID, Time, Semester, Weekday)
);

CREATE TABLE Rates (
	StudentID Integer(9) NOT NULL,
	TutorID  Integer(9),
	School VARCHAR(30) NOT NULL,
	Number Integer(4) NOT NULL,
	NumEvaluation Integer(2),
	DescEvaluation VarChar(200),
	Semester VarChar(30),
	Primary Key(StudentID, School, Number),
	Foreign Key(TutorID) REFERENCES Tutor(TutorID),
	Foreign Key(StudentID) REFERENCES User(Gtid)	
);


CREATE TABLE Tutors (
	TutorID Integer(9) NOT NULL,
	School VARCHAR(30) NOT NULL,
	Number Integer(4) NOT NULL,
	GTA BOOLEAN NOT NULL,
    Foreign Key(TutorID) REFERENCES Tutor(TutorID),
    Foreign Key(School, Number) REFERENCES Course(School, Number),
	Primary Key(TutorID, School, Number)
);

CREATE TABLE Recommends (
	TutorID Integer(9) NOT NULL,
	ProfessorID Integer(9) NOT NULL,
	NumEvaluation Integer(2),
	DescEvaluation VarChar(200),
	Primary Key(TutorID, ProfessorID),
	Foreign Key (ProfessorID) REFERENCES Professor(ProfessorID)
);

/*CREATED VIEWS*/
Drop View Summary1, Summary2, TutorInfo, TutorSchedule, ProfessorRecs, StudentRecs, CombinedRecExtra, RecsTTS, Figure3;
CREATE VIEW Summary1 AS
	SELECT CONCAT(tts.School, CAST(tts.Number as char)) as 'Course', tts.Semester, Count(tts.TuteeID) as 'NumStudents', Count(t.TutorID) as 'NumTutors'
	FROM Tutors t, TutorTimeSlots tts
	WHERE t.TutorID=tts.TutorID
	Group by Course, Semester WITH ROLLUP;

CREATE TABLE Summary 
	As (
	SELECT CONCAT(tts.School, CAST(tts.Number as char)) as 'Course', tts.Semester, Count(tts.TuteeID) as 'NumStudents', Count(t.TutorID) as 'NumTutors'
	FROM Tutors t, TutorTimeSlots tts
	WHERE t.TutorID=tts.TutorID
	Group by Course, Semester WITH ROLLUP);
Update Summary Set Semester="Total" Where LENGTH(Semester)<1;
Update Summary s Set Course="GRAND" Where Course IS NULL;

CREATE VIEW Summary2 AS
	SELECT CONCAT(tts.School, CAST(tts.Number as char)) as 'Course', tts.Semester, Count(g.GradID) as 'TA', AVG(r.numEvaluation) as 'AvgRating', Count(u.undergradID) as 'nonTA', AVG(r2.numEvaluation) as 'AvgRating2'
	FROM Tutors t, TutorTimeSlots tts, Grad g, Rates r, Undergrad u, Rates r2
	WHERE t.TutorID=tts.TutorID
	AND g.GradID=r.TutorID
	AND u.UndergradID=r2.TutorID
	Group by Course, Semester
	Order by Course;

CREATE VIEW TutorInfo AS
	SELECT s.Name, s.Email, Avg(r.NumEvaluation) as 'AvgProfRating', Count(distinct r.ProfessorID) as 'NumProfessors', Avg(ra.NumEvaluation) as 'AvgStudentRating', Count(distinct ra.StudentID) as 'NumStudents', s.StudentID as 'TutorID'
	FROM Student s, Recommends r, Rates ra
	Where s.StudentID=r.TutorID
	AND s.StudentID=ra.TutorID;

CREATE VIEW TutorSchedule AS
	SELECT tts.Weekday as 'Day', tts.Time, s.Name, s.Email, CONCAT(tts.School, CAST(tts.Number as char)) as 'Course', s.StudentID
	From TutorTimeSlots tts, Student s
	Where tts.TutorID=s.StudentID;

CREATE VIEW ProfessorRecs AS 
	SELECT TutorID as ProfTutorID, Count(*) as ProfNumRatings, Avg(NumEvaluation) as ProfAvgRating
	From Recommends 
	Group by TutorID;

CREATE VIEW StudentRecs AS
	SELECT TutorID as StuTutorID, Count(*) as StuNumRatings, Avg(NumEvaluation) as StuAvgRating
	From Rates 
	Group by TutorID;

CREATE VIEW CombinedRecExtra AS
	SELECT *
	FROM ProfessorRecs PR
	LEFT JOIN StudentRecs SR
	ON PR.ProfTutorID=SR.StuTutorID
	UNION
	SELECT *
	FROM ProfessorRecs PR
	RIGHT JOIN StudentRecs SR
	ON PR.ProfTutorID=SR.StuTutorID;

CREATE VIEW RecsTTS as
	SELECT * 
	FROM CombinedRecExtra cre 
	INNER JOIN TutorTimeSlots A on cre.ProfTutorID=A.TutorID;

#Figure 3 table
CREATE VIEW Figure3 AS
	SELECT s.Name, s.Email, r.profTutorID, r.ProfNumRatings, r.ProfAvgRating, r.StuTutorID, r.StuNumRatings, r.StuAvgRating, r.School, r.Number, r.TutorID, r.Time, r.Semester, r.Weekday, r.TuteeID
	From Student s, RecsTTS r
	Where s.StudentID=r.TutorID;