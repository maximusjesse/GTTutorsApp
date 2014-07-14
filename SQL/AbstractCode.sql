Login 	4
Search Tutor 	6
Schedule Tutor 	4
Tutor Evaluation By Student 	5
Tutor Application 	10
Tutor Schedule 	6
Prof Recommends Tutor 	5
Summary Report 1 	10
Summary Report 2 	10

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

/*Search Tutor*/
Select TutorID
From TutorTimeSlots
Where $Weekday=TutorTimeSlots.Weekday
And $Time=TutorTimeSlots.Time
//With the TutorID, we can generate a tuple from view TutorInfo
Select Name, Email, AvgProfRating, NumProfessors, AvgStudentRating, NumStudents
From TutorInfo
Where $ID=TutorInfo.TutorID

/*Schedule Tutor*/
UPDATE Tutors
SET StudentId=$StudentUserID
WHERE TutorID=$SelectedTutorID

/*Tutor Evaluation By Student*/
INSERT INTO Ratesrates
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
INSERT INTO TutorTimeSlots
Values ($ID, $Time, $Semester, $Weekday)

/*Find Tutor Schedule*/
SELECT Day, Time, Name, Email, Course
FROM TutorSchedule
WHERE 111111111=TutorSchedule.TutorID

/*Prof Recommends Tutor*/
INSERT INTO Recommends
Value ($TutorID, $ProfessorID, $NumEvaluation, $DescEvaluation)

/*Summary Report 1*/
//Application will return either String for semester, or an incorrect string if unchecked
//Use Summary1 View, which has null values for Semester where totals are present
Select *
From Summary1
Where Semester=$Spring
OR Semester=$Summer
OR Semester=$Fall
OR Semester IS NULL

/*Summary 2 Report*/
//Similar to Summary 1, Uses Summary2 view, which null values in Semester for totals
Select *
From Summar2
Where Semester=$Spring
OR Semester=$Summer
OR Semester=$Fall
OR Semester IS NULL