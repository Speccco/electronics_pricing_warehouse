{{ config(materialized='table') }}

WITH distinct_dates AS (
    SELECT DISTINCT
        captured_at::DATE AS date
    FROM {{ ref('int_product_enrichment') }}
)

SELECT
    date,
    EXTRACT(YEAR FROM date) AS year,
    EXTRACT(MONTH FROM date) AS month,
    EXTRACT(DAY FROM date) AS day,
    EXTRACT(QUARTER FROM date) AS quarter,
    (EXTRACT(YEAR FROM date) || '-Q' || EXTRACT(QUARTER FROM date))::VARCHAR AS year_quarter,
    CASE
        WHEN EXTRACT(DAYOFWEEK FROM date) IN (0, 6) THEN TRUE
        ELSE FALSE
    END AS is_weekend
FROM distinct_dates