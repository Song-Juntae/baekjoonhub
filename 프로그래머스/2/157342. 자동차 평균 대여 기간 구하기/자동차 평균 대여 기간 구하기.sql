-- 코드를 입력하세요
WITH DD AS (
    SELECT CAR_ID, DATEDIFF(END_DATE, START_DATE) + 1 AS D
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
)
SELECT CAR_ID, ROUND(AVG(D), 1) AS AVERAGE_DURATION
FROM DD
GROUP BY CAR_ID
HAVING AVERAGE_DURATION >= 7
ORDER BY AVERAGE_DURATION DESC, CAR_ID DESC