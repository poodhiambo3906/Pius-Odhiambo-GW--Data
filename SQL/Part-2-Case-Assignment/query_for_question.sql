-- 1. List the following details of each employee: employee number, last name, first name, sex, and salary.*/

SELECT e.emp_no AS "Employee Number", last_name, first_name, sex, s.salary 
FROM tbl_employee e
JOIN tbl_salary s
ON e.emp_no = s.emp_no;

-- 2. List first name, last name, and hire date for employees who were hired in 1986.

SELECT first_name, last_name, hire_date
FROM tbl_employee
WHERE date_part('year',hire_date) = '1986';

-- 3. List the manager of each department with the following information: 
--department number, department name, the manager's employee number, last name, first name.

SELECT ma.dept_no AS "department number", dp.dept_name AS "department name",  ma.emp_no "Manager employee number", last_name, first_name 
FROM tbl_employee AS e
JOIN tbl_dept_manager AS ma
ON e.emp_no = ma.emp_no 
JOIN tbl_department AS dp
ON ma.dept_no = dp.dept_no;

--4. List the department of each employee with the following information: 
--employee number, last name, first name, and department name.

SELECT e.emp_no "employee number", last_name, first_name,  dp.dept_name AS "department name" 
FROM tbl_employee AS e
JOIN tbl_dept_emp AS de
ON e.emp_no = de.emp_no
JOIN tbl_department AS dp
ON de.dept_no = dp.dept_no;

--5. List first name, last name, and sex for employees 
--whose first name is "Hercules" and last names begin with "B."

SELECT first_name, last_name, sex
FROM tbl_employee
WHERE first_name = 'Hercules' AND last_name LIKE 'B%';


--6. List all employees in the Sales department, 
--including their employee number, last name, first name, and department name.

SELECT e.emp_no "employee number", last_name, first_name,  dp.dept_name AS "department name" 
FROM tbl_employee AS e
JOIN tbl_dept_emp AS de
ON e.emp_no = de.emp_no
JOIN tbl_department AS dp
ON de.dept_no = dp.dept_no
WHERE dp.dept_name = 'Sales';

--7. List all employees in the Sales and Development departments, 
--including their employee number, last name, first name, and department name.

SELECT e.emp_no "employee number", last_name, first_name,  dp.dept_name AS "department name" 
FROM tbl_employee AS e
JOIN tbl_dept_emp AS de
ON e.emp_no = de.emp_no
JOIN tbl_department AS dp
ON de.dept_no = dp.dept_no
WHERE dp.dept_name IN ('Sales', 'Development');

--8. In descending order, list the frequency count of employee last names, i.e., 
-- how many employees share each last name.

SELECT last_name, COUNT(last_name) FROM tbl_employee
GROUP BY last_name
ORDER BY COUNT(last_name) DESC;





