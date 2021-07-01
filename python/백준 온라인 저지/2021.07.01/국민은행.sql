SELECT u.USER_ID, COUNT(*), SUM(t.MONEY)
FROM USERS u, TRANSACTIONS t
where u.USER_ID = t.USER_ID and (DATE(t.DATE_TIME) >= 2020-09-01 or DATE(t.DATE_TIME) <= 2020-09-07)
GROUP BY u.USER_ID
ORDER BY u.USER_ID


SELECT u.USER_ID as "회원 아이디(USER_ID)", COUNT(*) as "총 저축 횟수", SUM(t.MONEY) as "총 저축 금액 합계"
FROM USERS u
LEFT OUTER JOIN TRANSACTIONS t ON u.USER_ID = t.USER_ID
WHERE (date_format(t.DATE_TIME, "20%y-%m-%d") >= "2020-09-01" and date_format(t.DATE_TIME, "20%y-%m-%d") <= "2020-09-07") 
GROUP BY u.USER_ID
ORDER BY u.USER_ID


SELECT u.USER_ID as "회원 아이디(USER_ID)", COUNT(*) as "총 저축 횟수", SUM(t.MONEY) as "총 저축 금액 합계"
FROM USERS u
LEFT OUTER JOIN TRANSACTIONS t ON u.USER_ID = t.USER_ID
WHERE (date_format(t.DATE_TIME, "20%y-%m-%d") >= "2020-09-01" and date_format(t.DATE_TIME, "20%y-%m-%d") <= "2020-09-07") 
GROUP BY u.USER_ID
ORDER BY u.USER_ID