DROP TABLE students;

CREATE TABLE students(
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    student_first_name VARCHAR(255) NOT NULL,
    student_last_name VARCHAR(255) NOT NULL,
    campus_id INT,
    FOREIGN KEY (campus_id) REFERENCES campuses(campus_id),
);

INSERT INTO students(student_first_name, student_last_name, campus_id) 
VALUES
    ("Amal", "Chamlee", 1),
    ("Clair", "Hansel", 1),
    ("David", "Byer", 2),
    ("Drew", "Kenyon", 3),
    ("John", "Snow", 3)
)