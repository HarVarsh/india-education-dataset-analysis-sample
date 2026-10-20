
SELECT
    ROUND(AVG(ptr_primary), 2) AS primary_mean,
    ROUND(AVG(ptr_upper_secondary), 2) AS upper_secondary_mean,
    ROUND(AVG(ptr_secondary), 2) AS secondary_mean
FROM education_ptr;
