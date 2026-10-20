
SELECT state, ptr_primary
FROM education_ptr
WHERE ptr_primary IS NOT NULL
ORDER BY ptr_primary DESC
LIMIT 20;
