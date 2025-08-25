--Câu 1: Lấy tất cả nhân viên có lương > 1000
SELECT * FROM employees 
WHERE salary > 1000;

--Câu 2: Tính lương trung bình mỗi phòng ban

SELECT department, AVG(salary) as luong_tb 
FROM employees 
GROUP BY department;

--Câu 3: Lấy nhân viên có lương cao nhất trong mỗi phòng ban

SELECT department, MAX(salary) as luong_cao_nhat
FROM employees 
GROUP BY department;