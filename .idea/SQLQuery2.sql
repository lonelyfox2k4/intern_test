-- 1. Lấy tất cả sản phẩm có giá > 100
SELECT * FROM products 
WHERE price > 100;

-- 2. Lấy ra tên và giá của các sản phẩm thuộc danh mục 'Điện tử', sắp xếp theo giá giảm dần
SELECT name, price 
FROM products 
WHERE category = 'Điện tử' 
ORDER BY price DESC;

-- 3. Đếm số sản phẩm trong mỗi danh mục ('category')
SELECT category, COUNT(*) as so_luong_san_pham
FROM products 
GROUP BY category;
