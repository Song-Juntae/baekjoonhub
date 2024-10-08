-- 코드를 작성해주세요
WITH T1 AS (
    SELECT
        FISH_TYPE,
        CASE
            WHEN LENGTH <= 10 THEN 10
            WHEN LENGTH IS NULL THEN 10
        ELSE LENGTH
        END AS LENGTH
    FROM FISH_INFO
)
SELECT 
    COUNT(*) AS FISH_COUNT,
    MAX(LENGTH) AS MAX_LENGTH,
    FISH_TYPE
FROM T1
GROUP BY FISH_TYPE
HAVING AVG(LENGTH) >= 33
ORDER BY FISH_TYPE ASC