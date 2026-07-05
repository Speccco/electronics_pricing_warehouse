{{ config(materialized='table') }}

SELECT
    ROW_NUMBER() OVER (ORDER BY source) AS source_key,
    source,
    free_delivery
FROM
    {{ ref('int_product_enrichment') }}