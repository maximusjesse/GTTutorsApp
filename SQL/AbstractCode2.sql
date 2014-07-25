SQL ABSTRACT CODE
*Get all $variables from application/UI

/*Login*/
SELECT Gtid, Password
FROM User
WHERE Gtid=$Gtid
AND Password=$Password
//If this returns a row, then Successful Login
//Else, check Username and Password
	SELECT Gtid, Password
	FROM User
	WHERE Gtid=$Gtid
	AND Password=$Password
$Weekday=M

/*Search Tutor*/
Select Name, Email, ProfAvgRating, ProfNumRatings, StuAvgRating, StuNumRatings
	FROM (
	SELECT *
	FROM Figure3
	WHERE @School=Figure3.School
	AND @Number=Figure3.Number
	AND @Weekday=Figure3.Weekday
	AND @Time=Figure3.Time
) A
#Figure4 Select Tutor
Select Name, Email, Weekday, Time
	FROM (
	SELECT *
	FROM Figure3
	WHERE 'CS'=Figure3.School
	AND 4400=Figure3.Number
	AND 'W'=Figure3.Weekday
	AND '14:00:00'=Figure3.Time
) A

/*Schedule Tutor*/
Insert into Hires
Values(@TuteeID,@School,@Number,@TutorID,@Time,@Semester,@Weekday)

/*Tutor Evaluation By Student*/
INSERT INTO Rates
VALUES ($StudentUserID, $SelectedTutorID, $School, $Number, $NumEvaluation, $DescEvaluation, $Semester)

/*Tutor Application*/
INSERT INTO Student
Values ($ID, $Email, $Name)

INSERT INTO Tutor
Values($ID, $Phone, $GPA)
//If Undergraduate
INSERT INTO Undergrad
Values ($ID)
//Else (Grad)
INSERT INTO Grad
Values ($ID)
//Selecting Courses
INSERT INTO Tutors
Values ($ID, $School, $Number)
//Choosing Times
INSERT INTO Hires
Values ($TuteeID, $Time, $Semester, $Weekday, $TutorID, $School, $Number)

/*Find Tutor Schedule*/
SELECT Day, Time, Name, Email, Course
FROM TutorSchedule
WHERE StudentID=$TutorID

/*Prof Recommends Tutor*/
INSERT INTO Recommends
Value ($TutorID, $ProfessorID, $NumEvaluation, $DescEvaluation)

/*Summary Report 1*/
#Creates a temporary view based on the semesters selected
SET @IncludeFall='Fall',@IncludeSpring='Spring',@IncludeSummer='Summer'
DROP VIEW IF EXISTS Summary1;
CREATE VIEW Summary1 AS
	SELECT CONCAT(TRIM(h.school), TRIM(CAST(h.Number AS CHAR))) as 'Course', h.Semester, Count(Distinct h.TuteeID) as 'NumStudents', COUNT(DISTINCT h.TutorID) as 'NumTutors'
	FROM Hires h
	WHERE Semester=@IncludeFall
	OR Semester=@IncludeSpring
	OR Semester=@IncludeSummer
	GROUP BY Course, Semester

/*Summary 2 Report*/
//Similar to Summary 1, Uses Summary2 view
Select *
From Summar2
Where Semester=@IncludeSpring
OR Semester=@IncludeFall
OR Semester=@IncludeSummer
OR Semester IS NULL

#Returns the boolean where Gtid exists
SELECT EXISTS( SELECT * FROM Administrator WHERE AdminID=%s)
SELECT EXISTS( SELECT * FROM Student WHERE StudentID=%s)
SELECT EXISTS( SELECT * FROM Professor WHERE ProfessorID=%s)
SELECT EXISTS( SELECT * FROM Tutor WHERE TutorID=%s)