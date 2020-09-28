WITH RECURSIVE
consec_day_count (UserName, UserDate, CONSEC) AS
(
    SELECT
        curr.UserName,
        curr.UserDate,
        1 AS CONSEC
    FROM UserTable curr
    WHERE NOT EXISTS (
        SELECT 1
        FROM UserTable prev
        WHERE DATE(curr.UserDate, '-1 day') = prev.UserDate
        AND curr.UserName = prev.UserName
    )
    UNION ALL
    SELECT
        curr.UserName,
        DATE(curr.UserDate, '+1 day') AS UserDate,
        curr.CONSEC + 1
    FROM consec_day_count curr
    WHERE EXISTS (
        SELECT 1
        FROM UserTable u
        WHERE DATE(curr.UserDate, '+1 day') = u.UserDate
        AND curr.UserName = u.UserName
    )
)
SELECT
    UserName, MAX(CONSEC) AS CONSEC
FROM consec_day_count
GROUP BY UserName
;
