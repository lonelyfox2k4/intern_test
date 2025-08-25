--Câu 1: Lấy tất cả sách xuất bản từ năm 2020 trở đi

SELECT * FROM books 
WHERE year >= 2020;

-- Câu 2: Đếm số sách mỗi tác giả

SELECT author, COUNT(*) as so_sach 
FROM books 
GROUP BY author;

--Câu 3: Lấy sách mới nhất của mỗi tác giả

SELECT author, MAX(year) as nam_moi_nhat
FROM books 
GROUP BY author;