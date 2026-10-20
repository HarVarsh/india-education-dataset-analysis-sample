
SELECT
    COUNT(ptr_primary) AS states_with_data,
    ROUND(AVG(ptr_primary), 2) AS average_ptr,
    ROUND(MIN(ptr_primary), 2) AS minimum_ptr,
    ROUND(MAX(ptr_primary), 2) AS maximum_ptr
FROM education_ptr;
