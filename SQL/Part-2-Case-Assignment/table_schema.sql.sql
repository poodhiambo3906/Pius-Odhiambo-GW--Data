-- table schema query

CREATE TABLE tbl_title (
	title_id 	VARCHAR 	PRIMARY KEY NOT NULL,
	title 		VARCHAR
);


CREATE TABLE tbl_employee (
	emp_no 			int 	PRIMARY KEY NOT NULL,
	emp_title_id 	VARCHAR references tbl_title(title_id),
	birth_date 		Date,
	first_name 		VARCHAR,
	last_name 		VARCHAR,
	sex       		VARCHAR,
	hire_date 		Date
);

CREATE TABLE tbl_department(
	dept_no 	VARCHAR PRIMARY KEY NOT NULL,
	dept_name 	VARCHAR
);



CREATE TABLE tbl_dept_emp(
	emp_no 		int 		references tbl_employee(emp_no),
	dept_no 	VARCHAR 	references tbl_department(dept_no)
);



CREATE TABLE tbl_dept_manager(
	emp_no 		int 		references tbl_employee(emp_no),
	dept_no 	VARCHAR 	references tbl_department(dept_no)
);


CREATE TABLE tbl_salary ( 
	emp_no 	int references tbl_employee(emp_no),
	salary 	REAL
);



