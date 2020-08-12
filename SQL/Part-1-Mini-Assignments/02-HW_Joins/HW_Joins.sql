/* Query to Create Table players in the NBA_DB Database */
CREATE TABLE players (
  id INT,
  player VARCHAR,
  height INT,
  weight INT,
  college VARCHAR,
  born INT,
  birth_city VARCHAR,
  birth_state VARCHAR
);

/* Query to Create Table seasons_stat in the NBA_DB Database */

CREATE TABLE seasons_stats (
  player_id INT,
  year DEC,
  position VARCHAR,
  age DEC,
  Tm VARCHAR,
  G VARCHAR,
  TS_Percentage DEC,
  FTr DEC,
  OWS DEC,
  DWS DEC,
  WS DEC,
  FG DEC,
  FGA DEC,
  FG_Percentage DEC,
  Two_Points DEC,
  Two_PA DEC,
  Two_Point_Percentage DEC,
  eFG_Percentage DEC,
  FT DEC,
  FTA DEC,
  FT_Percentage DEC,
  AST DEC,
  PF DEC,
  PTS DEC
);

/* Data imported into players TABLE and seasons_stats TABLE using the import/Export Tool in 
pgAdmin */

/*Query in line 46 used to verify data was loaded correctly into the players TABLE in NBA_DB Database*/
SELECT * FROM public.players

/*Query in line 46 used to verify data was loaded correctly into the seasons_stats TABLE in NBA_DB Database*/
SELECT * FROM public.seasons_stats

/* join to Query for ![Basic Info](Images/basic_info.png) */

SELECT p.id, p.player, p.height, p.weight, p.college, p.born, s.position, s.tm 
FROM public.players AS p
INNER JOIN public.seasons_stats AS s 
ON p.id = s.player_id
Where id in (0,1,2)
LIMIT 6;


/* join to Query ![Percent Stats](Images/percent_stats.png) */

SELECT s.player_id, p.college, s.year, s.position, s.two_point_percentage, s.fg_percentage, s.ft_percentage, s.ts_percentage
FROM public.seasons_stats AS s
INNER JOIN public.players AS p  
ON s.player_id = p.id
Where id in (0,1,2)
LIMIT 6;







