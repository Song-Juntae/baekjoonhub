-- 코드를 작성해주세요
WITH T AS (
    SELECT T1.ITEM_ID
    FROM ITEM_TREE AS T1
    LEFT JOIN ITEM_TREE AS T2
    ON T1.ITEM_ID = T2.PARENT_ITEM_ID
    WHERE T2.PARENT_ITEM_ID IS NULL
)
SELECT I.ITEM_ID, ITEM_NAME, RARITY
FROM ITEM_INFO AS I
INNER JOIN T
ON I.ITEM_ID = T.ITEM_ID
ORDER BY I.ITEM_ID DESC