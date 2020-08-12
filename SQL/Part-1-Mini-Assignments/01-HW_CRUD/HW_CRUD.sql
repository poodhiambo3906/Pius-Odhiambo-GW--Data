/*The below line of codes [Line 2 - 16 ] was used to create 
  Table firepower in the GlobalFirePower  */
  
CREATE TABLE firepower (
	country VARCHAR,
	ISO3 VARCHAR,
	Rank INT,
	TotalPopulation INT,
	ManpowerAvailable INT,
	TotalMilitaryPersonnel INT,
	ActivePersonnel INT,
	ReservePersonnel INT,
	TotalAircraftStrength INT,
	FighterAircraft INT,
	AttackAircraft INT,
	TotalHelicopterStrength INT,
	AttackHelicopters INT
);

/*The below line of codes [Line 21 ] was used to Delete from the 
  Table firepower in the GlobalFirePower where the record has ReservePersonnel equal to 0 */
  
DELETE FROM public.firepower WHERE ReservePersonnel = 0;


/* Query to Update Records with 0 FighterAircraft */
  
UPDATE public.firepower
SET FighterAircraft = 1
WHERE FighterAircraft = 0;

/* Query to get the Average TotalMilitaryPersonnel and Rename the returned column with
Average TotalMilitaryPersonnel*/

SELECT AVG(totalmilitarypersonnel) "Average TotalMilitaryPersonnel"
FROM public.firepower

/* Query to get the Average TotalAircraftStrength and Rename the returned column with
Average TotalAircraftStrength*/

SELECT AVG(totalaircraftstrength) "Average TotalAircraftStrength"
FROM public.firepower

/* Query to get the Average TotalHelicopterStrength and Rename the returned column with
Average TotalHelicopterStrength*/
SELECT AVG(totalhelicopterstrength) "Average TotalHelicopterStrength"
FROM public.firepower


/* Query to get the Average TotalPopulation and Rename the returned column with
Average TotalPopulation*/
SELECT AVG(totalpopulation) "Average TotalPopulation"
FROM public.firepower

