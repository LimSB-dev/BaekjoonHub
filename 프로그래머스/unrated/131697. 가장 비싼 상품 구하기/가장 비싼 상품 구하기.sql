-- 코드를 입력하세요
SELECT PRICE AS MAX_PRICE FROM PRODUCT
WHERE PRICE IN (SELECT MAX(PRICE) FROM PRODUCT);
