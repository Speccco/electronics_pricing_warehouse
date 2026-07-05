{{ config(materialized='table') }}

SELECT
    product_id,
    title,
    product_link,
    source,
    captured_at,
    price,
    original_price,
    tag,
    second_hand_condition,
    rating,
    reviews,
    delivery,
    popularity_score,
    free_delivery,
    price_tier,
    AVG(price) OVER(
        partition by price_tier
    ) AS avg_price_per_tier
FROM {{ ref('int_product_enrichment') }}