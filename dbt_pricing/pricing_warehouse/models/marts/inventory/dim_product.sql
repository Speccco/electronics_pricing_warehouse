{{ config(
    materialized='incremental',
    unique_key='product_id'
) }}

SELECT DISTINCT
    product_id,
    title,
    tag,
    product_link,
    second_hand_condition,
    price_tier
FROM {{ ref('int_product_enrichment') }}

{% if is_incremental() %}
WHERE product_id NOT IN (
    SELECT product_id
    FROM {{ this }}
)
{% endif %}