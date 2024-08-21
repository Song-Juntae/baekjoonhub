-- 코드를 입력하세요
SELECT ANIMAL_TYPE, COUNT(*) AS `count`
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
HAVING ANIMAL_TYPE = 'Cat' OR ANIMAL_TYPE = 'Dog'
ORDER BY FIELD(ANIMAL_TYPE, 'Cat', 'Dog')