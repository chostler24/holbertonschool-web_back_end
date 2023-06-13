-- SQL script ranks country origin of bands, ordered by number
-- of non-unique fans
SELECT origin, COUNT(*) AS nb_fans
FROM bands
GROUP BY origin
ORDER BY nb_fans DESC;
