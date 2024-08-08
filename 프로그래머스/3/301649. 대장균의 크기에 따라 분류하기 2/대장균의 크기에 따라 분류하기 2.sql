-- 코드를 작성해주세요
WITH N AS (
    SELECT NTILE(4) OVER(ORDER BY SIZE_OF_COLONY DESC) Q, ID
    FROM ECOLI_DATA
)
SELECT E.ID,
CASE WHEN Q = 1 THEN 'CRITICAL'
    WHEN Q = 2 THEN 'HIGH'
    WHEN Q = 3 THEN 'MEDIUM'
    WHEN Q = 4 THEN 'LOW'
END AS COLONY_NAME
FROM ECOLI_DATA AS E
LEFT OUTER JOIN N
ON E.ID = N.ID
ORDER BY E.ID