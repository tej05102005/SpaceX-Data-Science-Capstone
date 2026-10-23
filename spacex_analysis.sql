-- Adapt table and column names to the actual cleaned course dataset.
-- These queries assume a table named spacex_launches.

-- 1. Launch count by site
SELECT launch_site, COUNT(*) AS launch_count
FROM spacex_launches
GROUP BY launch_site
ORDER BY launch_count DESC;

-- 2. Landing outcomes by site
SELECT launch_site, landing_success, COUNT(*) AS record_count
FROM spacex_launches
GROUP BY launch_site, landing_success
ORDER BY launch_site, landing_success;

-- 3. Payload summary by landing outcome
SELECT landing_success,
       COUNT(*) AS n,
       AVG(payload_mass_kg) AS avg_payload_kg,
       MIN(payload_mass_kg) AS min_payload_kg,
       MAX(payload_mass_kg) AS max_payload_kg
FROM spacex_launches
WHERE payload_mass_kg IS NOT NULL
GROUP BY landing_success;

-- 4. Yearly launch activity
SELECT launch_year, COUNT(*) AS launch_count
FROM spacex_launches
WHERE launch_year IS NOT NULL
GROUP BY launch_year
ORDER BY launch_year;
