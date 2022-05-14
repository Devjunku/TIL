-- SELECT CASE WHEN GROUPING(job) THEN "합계"
--        THEN job
--        END AS JOB,
--        CASE WHEN GROUPING(deptno) THEN "소계"
--        THEN DENSE
--        END AS deptno,
--        SUM(sal) AS TOTAL_SAL
-- FROM EMP
-- WHERE JON in ("MANAGER", "CLECK", "SALESMAN")
-- GROUP BY ROLLUP(JOB, DEPTNO)

SELECT c.user_id, c.name, CC.spent
FROM (select c.user_id as , c.name as name, sum(cp.price) as spent, RANK() over(order by sum(cp.price)) as sdas
       from carts c LEFT JOIN carts_product cp on c.id = cp.carts_id
       GROUP BY c.user_id, cp.name) CC
GROUP BY c.user_id
WHERE CC.sdas = 1
ORDER BY CC.user_id, CC.name
