CREATE DATABASE EcommerceDB;
GO

USE EcommerceDB;
GO

-- 1. Top 10 sản phẩm bán chạy nhất (theo số lượng)
SELECT TOP 10 
    StockCode,
    Description,
    SUM(quantity) AS total_sold
FROM cleaned_data
GROUP BY StockCode, Description
ORDER BY total_sold DESC;

-- 2. Top 10 sản phẩm theo doanh thu
SELECT TOP 10 
    StockCode,
    Description,
    SUM(linerevenue) AS revenue
FROM cleaned_data
GROUP BY StockCode, Description
ORDER BY revenue DESC;

-- 3. Doanh thu theo tháng
SELECT 
    Year, 
    Month, 
    SUM(total_revenue) AS revenue
FROM cleaned_data
GROUP BY Year, Month
ORDER BY Year, Month;

-- 4. Top 10 khách hàng
SELECT TOP 10 
    customer_id, 
    SUM(total_revenue) AS revenue
FROM cleaned_data
GROUP BY customer_id
ORDER BY revenue DESC;

-- 5. Doanh thu theo quốc gia
SELECT 
    Country, 
    SUM(total_revenue) AS revenue
FROM cleaned_data
GROUP BY Country
ORDER BY revenue DESC;
--AOV
SELECT 
    AVG(order_value) AS AOV
FROM (
    SELECT order_id, SUM(linerevenue) AS order_value
    FROM cleaned_data
    GROUP BY order_id
) t;
--Doanh thu theo năm
SELECT 
    Year,
    SUM(total_revenue) AS revenue
FROM cleaned_data
GROUP BY Year
ORDER BY Year;