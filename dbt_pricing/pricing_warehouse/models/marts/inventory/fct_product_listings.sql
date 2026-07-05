{{ config(
    materialized='incremental',
    unique_key='product_id'
    ) }}

SELECT
    p.product_id,
    s.source_key,
    p.captured_at,
    p.price,
    p.original_price,
    p.rating,
    p.reviews,
    p.popularity_score
FROM 
    {{ ref('int_product_enrichment') }} p
LEFT JOIN {{ ref('dim_source') }} s
ON p.source = s.source

{% if is_incremental() %}
WHERE p.product_id NOT IN (
    SELECT p.product_id
    FROM {{ this }}
)
{% endif %}