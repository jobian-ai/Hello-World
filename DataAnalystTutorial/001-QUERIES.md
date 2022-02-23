# SQL Queries for this Project

[Video Tutorial](https://youtu.be/qfyynHBFOsM)

[Dataset from Here](https://ourworldindata.org/covid-deaths)

## These are SQL queries from the first video

Some of them do not give accurate results but the syntax, I wanted to save.
There is problems with the dataset I down loaded.  For example, CHINA has 14 BILLION people, not 1.4b.

I did this project with SQLITE not MSSQLServer.  Hence, the code if different than the tutorial.  The injest to SQLITE is shown in the accompanying Python Juniper Notebooks.

## Chance of dying from COVID by country

```SQL
SELECT LOCATION,
       DATE,
       TOTAL_CASES,
       TOTAL_DEATHS,
       ROUND((total_deaths / total_cases) * 100,2) as DEATH_PERCENT
  FROM deaths 
 ORDER BY 1,
          2 DESC;
```

## Country's with Highest Infection compared to Population

```SQL
SELECT LOCATION,
       Population,
       MAX(total_cases) AS Highest_Infection_count,
       MAX(ROUND( (total_cases / population) * 100, 2) ) AS PercentPopulationInfected
  FROM deaths
 GROUP BY Location,
          Population
 ORDER BY 4 DESC;
 ```

## Percent of US population

 ```SQL
 SELECT LOCATION,
       DATE,
       TOTAL_CASES,
       Population,
       ROUND( (total_deaths / population) * 100, 2) AS Percent_Population
  FROM deaths
 WHERE LOCATION LIKE "United States"
 ORDER BY 1,
          2 DESC
```

## Highest Death Count per Population
<!-- note the "continent" part -->
```SQL
SELECT Location, MAX(Total_deaths) as TotalDeathCount
FROM deaths
WHERE continent is NOT NULL 
Group by Location
ORDER by TotalDeathCount desc;
```

## Break down by continent

```SQL
SELECT continent, MAX(Total_deaths) as TotalDeathCount
FROM deaths
WHERE continent is not NULL 
Group by continent
ORDER by TotalDeathCount desc;
```

## Global Death Percentage

```SQL
SELECT SUM(new_cases) as total_cases, 
SUM(new_deaths) as total_deaths, 
SUM(new_deaths)/SUM(New_Cases)*100 as DeathPercentage
FROM deaths
WHERE continent is not null
ORDER BY 1,2;
```

## Population vs Vaccinations

```SQL
SELECT d.continent, d.location, d.date,
d.population, v.new_vaccinations
FROM deaths d
JOIN vacs v
ON d.location = v.location
AND d.date = v.date
WHERE d.continent is not null
ORDER by 2,3;
```

## Table Join & Partitioning w/running total Vaccinations

```SQL
SELECT d.continent, d.location, d.date,
d.population, v.new_vaccinations, SUM(v.new_vaccinations)
OVER (PARTITION by d.location ORDER by d.location,d.date) as RollingSumofVaccinated
FROM deaths d
JOIN vacs v
ON d.location = v.location
AND d.date = v.date
WHERE d.continent is not null
ORDER by 2,3;
```

## Showing Rounded Percentages of Vaccinated (doesn't calculate right, but the code is interesting)

```SQL
WITH PopvsVac (
    continent,
    location,
    date,
    population,
    new_vaccinations,
    RollingSumofVaccinated
)
AS (
    SELECT d.continent,
           d.location,
           d.date,
           d.population,
           v.new_vaccinations,
           SUM(v.new_vaccinations) OVER (PARTITION BY d.location ORDER BY d.location,
           d.date) AS RollingSumofVaccinated
      FROM deaths d
           JOIN
           vacs v ON d.location = v.location AND 
                     d.date = v.date
     WHERE d.continent IS NOT NULL
     --ORDER BY 2,
              --3
)
SELECT *, ROUND((RollingSumofVaccinated/population)*100,2) as PercentVaxxed
  FROM PopvsVac;
  ```

## Temp Table Example

```SQL
DROP TABLE PercentPopulationVaccinated;

CREATE TEMP TABLE [temp].PercentPopulationVaccinated (
    continent,
    location,
    date,
    population,
    new_vaccinations,
    RollingSumofVaccinated
);

INSERT INTO [temp].PercentPopulationVaccinated SELECT d.continent,
                                                      d.location,
                                                      d.date,
                                                      d.population,
                                                      v.new_vaccinations,
                                                      SUM(v.new_vaccinations) OVER (PARTITION BY d.location ORDER BY d.location,
                                                      d.date) AS RollingSumofVaccinated
                                                 FROM deaths d
                                                      JOIN
                                                      vacs v ON d.location = v.location AND 
                                                                d.date = v.date
                                                WHERE d.continent IS NOT NULL AND 
                                                      d.location LIKE "UNITED STATES";
-- ORDER BY 2,3
SELECT *,
       ROUND( (RollingSumofVaccinated / population) * 100, 2) AS PercentVaxxed
  FROM [temp].PercentPopulationVaccinated;
  ```
