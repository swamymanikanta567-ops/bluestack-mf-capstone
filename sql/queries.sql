SELECT COUNT(*) FROM fund_master;

SELECT COUNT(*) FROM nav_history;

SELECT AVG(nav) FROM nav_history;

SELECT MAX(nav) FROM nav_history;

SELECT MIN(nav) FROM nav_history;

SELECT fund_house, COUNT(*)
FROM fund_master
GROUP BY fund_house;

SELECT category, COUNT(*)
FROM fund_master
GROUP BY category;

SELECT * FROM fund_master
LIMIT 10;

SELECT * FROM nav_history
LIMIT 10;

SELECT COUNT(DISTINCT fund_house)
FROM fund_master;