-- 코드를 입력하세요
WITH U AS (
    SELECT FLAVOR, TOTAL_ORDER
    FROM FIRST_HALF

    UNION

    SELECT FLAVOR, TOTAL_ORDER
    FROM JULY
)
SELECT FLAVOR
FROM U
GROUP BY FLAVOR
ORDER BY SUM(TOTAL_ORDER) DESC
LIMIT 3