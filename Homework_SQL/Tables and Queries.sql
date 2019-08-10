--create departments table
DROP TABLE IF EXISTS departments;
Create Table departments(
	dept_no VARCHAR (4) PRIMARY KEY NOT NULL,
	dept_name VARCHAR(30) NOT NULL
);
SELECT * FROM departments

--create dept_emp table
DROP TABLE IF EXISTS dept_emp;
Create Table dept_emp(
	emp_no INTEGER NOT NULL,
	FOREGIN KEY (emp_no) REFERENCES employees(emp_no),
	dept_no VARCHAR (4) NOT NULL,
	FOREGIN KEY (dept_no) REFERENCES departments(dept_no),
	from_date DATE NOT NULL,
	to_date DATE NOT NULL
);
SELECT * FROM dept_emp

--create dept_manager
DROP TABLE IF EXISTS dept_manager;
Create Table dept_manager(
	dept_no VARCHAR(4) NOT NULL,
	FOREGIN KEY (dept_no) REFERENCES departments(dept_no),
	emp_no INTEGER NOT NULL,
	FOREGIN KEY (emp_no) REFERENCES employees(emp_no),
	from_date DATE NOT NULL,
	to_date DATE NOT NULL
);
SELECT * FROM dept_manager

--create employees table
DROP TABLE IF EXISTS employees;
Create Table employees(
	emp_no INT PRIMARY KEY NOT NULL,
	birth_date VARCHAR(30) NOT NULL,
	first_name VARCHAR(30) NOT NULL,
	last_name VARCHAR(30) NOT NULL,
	gender VARCHAR(1) NOT NULL,
	hire_date VARCHAR(30) NOT NULL
);
SELECT * FROM employees

--create salaries table
DROP TABLE IF EXISTS salaries;
Create Table salaries(
	emp_no INT NOT NULL,
	FOREIGN KEY (emp_no) REFERENCES employees(emp_no),
	salary INT NOT NULL,
	from_date VARCHAR(30) NOT NULL,
	to_date VARCHAR(30) NOT NULL
);
SELECT * FROM salaries

--create titles table
DROP TABLE IF EXISTS titles;
Create Table titles(
	emp_no INT NOT NULL,
	FOREIGN KEY (emp_no) REFERENCES employees(emp_no),
	title VARCHAR(30) NOT NULL,
	from_date VARCHAR(30) NOT NULL,
	to_date VARCHAR(30) NOT NULL	
);
SELECT * FROM titles	
	
-- Question 1 - List the following details of each employee: employee number, last name, first name, gender, and salary.	
-- Perform an INNER JOIN on the two tables
SELECT e.first_name, e.last_name, e.emp_no, e.gender, s.salary
FROM employees AS e
LEFT JOIN salaries AS s
ON e.emp_no=s.emp_no;	

--Question 2 - List employees who were hired in 1986
SELECT first_name, last_name, hire_date FROM employees
    WHERE hire_date >= '1986-01-01'
    AND hire_date <= '1986-12-31'
    ORDER BY hire_date
	
--Question 3 - Select the Manager of each department with the following information: department number, department name, the manager's employee number, last name, first name, and start and end employment dates
SELECT e.first_name,e.last_name, e.emp_no, d.from_date, d.to_date, d.dept_no, s.dept_name
    FROM dept_manager AS d
    LEFT JOIN employees AS e
    ON e.emp_no=d.emp_no
    LEFT JOIN departments AS s
    ON d.dept_no=s.dept_no
	
--Question 4 - List the department of each employee with the following information: employee number, last name, first name, and department name.

SELECT e.first_name,e.last_name, e.emp_no, s.dept_name
    FROM employees AS e
    INNER JOIN dept_emp AS d
    ON e.emp_no=d.emp_no
    INNER JOIN departments AS s
    ON d.dept_no=s.dept_no


--Question 5 - List all employees whose first name is "Hercules" and last names begin with "B."

SELECT first_name, last_name FROM employees
    WHERE first_name = 'Hercules'
    AND last_name LIKE 'B%'

--Question 6 - List all employees in the Sales department, including their employee number, last name, first name, and department name.
SELECT e.last_name, e.first_name,d.emp_no, x.dept_name
	from employees AS e
	Left Join dept_emp AS d
	ON e.emp_no=d.emp_no
	Left Join departments AS x
	ON d.dept_no=x.dept_no
	where d.dept_no = 'd007'
	
--Question 7 - List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
	
SELECT e.first_name,e.last_name, e.emp_no, s.dept_name
    FROM employees AS e
    INNER JOIN dept_emp AS d
    ON e.emp_no=d.emp_no
    INNER JOIN departments AS s
    ON d.dept_no=s.dept_no
    WHERE dept_name = 'Development' OR dept_name = 'Sales'
	
--Question 8 - In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.

SELECT last_name, COUNT(*)
    FROM employees
    GROUP BY last_name
    ORDER BY count DESC