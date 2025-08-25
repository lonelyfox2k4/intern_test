

CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    price FLOAT,
    category VARCHAR(50)
);

-- Thêm dữ liệu mẫu
INSERT INTO products VALUES 
(1, 'Laptop Dell', 150.5, 'Điện tử'),
(2, 'iPhone 15', 200.0, 'Điện tử'),
(3, 'Áo thun', 50.0, 'Thời trang'),
(4, 'Máy tính bảng', 120.0, 'Điện tử'),
(5, 'Giày sneaker', 80.0, 'Thời trang'),
(6, 'Tai nghe', 30.0, 'Điện tử');