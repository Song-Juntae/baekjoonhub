-- 코드를 작성해주세요
WITH ROOT AS (
    SELECT PARENT_ID
    FROM ECOLI_DATA
)
SELECT E.ID, COUNT(R.PARENT_ID) AS CHILD_COUNT
FROM ECOLI_DATA AS E
LEFT OUTER JOIN ROOT AS R
ON E.ID = R.PARENT_ID
GROUP BY ID
ORDER BY ID ASC