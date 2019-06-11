
%defaultDatasource jdbc:h2:mem:db

DROP TABLE IF EXISTS Alzheimer;
CREATE TABLE Alzheimer (
  NACCID VARCHAR(10),
  NACCBRAA SMALLINT,
  PRIMARY KEY(NACCID)
) AS SELECT
  NACCID, NACCBRAA
FROM CSVREAD('../data/RedestoAlzheimer.csv');

SELECT *
FROM Alzheimer
LIMIT 20;

SELECT a1.NACCID as t1, a2.NACCID as t2
FROM Alzheimer a1 inner join Alzheimer a2
WHERE a1.NACCBRAA=a2.NACCBRAA 
LIMIT 20;
