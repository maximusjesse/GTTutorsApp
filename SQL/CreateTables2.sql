#SQL Create Tables
Drop Table IF EXISTS Administrator, Course, Grad, Professor, Rates, Recommends, Student, Tutor, Tutors, TutorTimeSlots, Undergrad, User, Summary, Hires;
CREATE TABLE User (
	Gtid VARCHAR(9) PRIMARY KEY,
	Password VARCHAR(30) NOT NULL
);

CREATE TABLE Administrator (
	AdminID VARCHAR(9) PRIMARY KEY,
	FOREIGN KEY (AdminID) REFERENCES User(Gtid)
);

CREATE TABLE Student (
	StudentID VARCHAR(9) PRIMARY KEY,
	Email VARCHAR(30) NOT NULL,
	Name VARCHAR(30) NOT NULL,
	FOREIGN KEY (StudentID) REFERENCES User(Gtid)
);

CREATE TABLE Professor (
	ProfessorID VARCHAR(9) PRIMARY KEY,
	FOREIGN KEY (ProfessorID) REFERENCES User(Gtid)
);

CREATE TABLE Grad (
	GradID VARCHAR(9) NOT NULL,
	PRIMARY KEY (GradID),
	FOREIGN KEY (GradID) REFERENCES User(Gtid)
);

CREATE TABLE Undergrad (
	UndergradID VARCHAR(9) NOT NULL PRIMARY KEY,
	FOREIGN KEY (UndergradID) REFERENCES Student(StudentID)
);

CREATE TABLE Tutor (
	TutorID VARCHAR(9) NOT NULL PRIMARY KEY,
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
	TutorID VARCHAR(9) NOT NULL,
	Time TIME NOT NULL,
	Semester VARCHAR(30) NOT NULL,
	Weekday VARCHAR(30) NOT NULL,
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
	Semester VarChar(30) NOT NULL,
	Primary Key(StudentID, School, Number),
	Foreign Key(TutorID) REFERENCES Tutor(TutorID),
	Foreign Key(StudentID) REFERENCES User(Gtid),
	Foreign Key(Semester) REFERENCES TutorTimeSlots(Semester)
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

CREATE TABLE Hires (
	TuteeID VARCHAR(9) NOT NULL,
	School VARCHAR(30) NOT NULL,
	Number Integer(4) NOT NULL,
	TutorID VARCHAR(9) NOT NULL,
	Time TIME NOT NULL,
	Semester VARCHAR(30) NOT NULL,
	Weekday VARCHAR(30) NOT NULL,
	PRIMARY KEY(TutorID, Time, Semester, Weekday),
	Foreign key (TuteeID) REFERENCES Student(Gtid),
	Foreign key(School, Number) REFERENCES Course(School, Number),
	Foreign key(TutorID, Time, Semester, Weekday) REFERENCES TutorTimeSlots(TutorID, Time, Semester, Weekday)
);

/*CREATED VIEWS*/
Drop View IF EXISTS Summary1, Summary2, TutorInfo, TutorSchedule, ProfessorRecs, StudentRecs, CombinedRecExtra, RecsTTS, Figure3, TTS, TTS2;

CREATE VIEW TTS as
	SELECT *
	FROM TutorTimeSlots tts
	Natural Join Tutors;

CREATE VIEW TTS2 as
	SELECT *
	FROM TTS
	NATURAL JOIN Hires;

CREATE VIEW TutorInfo AS
	SELECT s.Name, s.Email, Avg(r.NumEvaluation) as 'AvgProfRating', Count(distinct r.ProfessorID) as 'NumProfessors', Avg(ra.NumEvaluation) as 'AvgStudentRating', Count(distinct ra.StudentID) as 'NumStudents', s.StudentID as 'TutorID'
	FROM Student s, Recommends r, Rates ra
	Where s.StudentID=r.TutorID
	AND s.StudentID=ra.TutorID;

CREATE VIEW TutorSchedule AS
	SELECT h.Weekday as 'Day', h.Time as 'Time', h.TuteeID as 'Name', s.Email as 'Email', Concat(h.School,CAST(h.Number as char)) as 'Course', h.TutorID as 'StudentID'
	FROM Hires h, Student s;

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
	INNER JOIN TTS on cre.ProfTutorID=TTS.TutorID;

#Figure 3 table
CREATE VIEW Figure3 AS
	SELECT s.Name, s.Email, r.profTutorID, r.ProfNumRatings, r.ProfAvgRating, r.StuTutorID, r.StuNumRatings, r.StuAvgRating, r.School, r.Number, r.TutorID, r.Time, r.Semester, r.Weekday
	From Student s, RecsTTS r
	Where s.StudentID=r.TutorID;

CREATE VIEW Summary2 AS
	SELECT CONCAT(r.School, CAST(r.Number as char)) as 'Course', r.Semester, Count(CASE WHEN t.GTA=True AND r.TutorID=t.TutorID THEN r.TutorID END) as 'TA', AVG(CASE WHEN t.GTA=TRUE AND t.TutorID=r.TutorID THEN r.NumEvaluation END) as 'AvgRatingTA', Count(CASE WHEN t.GTA=FALSE AND r.TutorID=t.TutorID THEN t.TutorID END) as 'nonTA', AVG(Case WHEN r.TutorID=t.TutorID and t.GTA=FALSE THEN r.NumEvaluation END) as 'AvgRatingNTA'
	From Rates r, Tutors t
	WHERE r.TutorID=t.TutorID
	Group by Course, Semester;
#Averages Line+Selection clause based on user inputs of semesters
/*SELECT Course, '~Avg', '', Avg(AvgRatingTA), '', Avg(AvgRatingNTA) FROM Summary2 Group by Course;*/
/*SELECT * FROM Summary2 WHERE Semester='Spring' OR Semester='Summer' OR Semester=NULL */

/*Summary Report 1*/
#Creates a temporary view based on the semesters selected.  Commentted out because View is dynamic based on user inputs
/*DROP VIEW IF EXISTS Summary1;
CREATE VIEW Summary1 AS
	SELECT CONCAT(h.school, CAST(h.Number AS CHAR)) as 'Course', h.Semester, CountIDISTINCT h.TuteeID) as 'NumStudents', COUNT(DISTINCT h.TutorID) as 'NumTutorrs'
	FROM Hires
	WHERE Semester=@IncludeFall
	OR Semester=@IncludeSpring
	OR Semester=@IncludeSummer
	GROUP BY Course, Semester;
#SELECT Course, 'Total', Sum(NumStudents), Sum(NumTutors) FROM Summary1 Group by Course;
#SELECT '~Total for all courses', '', Sum(NumStudents), Sum(NumTutors) FROM Summary1;
*/