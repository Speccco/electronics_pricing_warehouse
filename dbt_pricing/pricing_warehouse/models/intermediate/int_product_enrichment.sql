{{ config(materialized = 'view') }}

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
    ROUND(rating * LN(reviews + 1), 2)::NUMERIC AS popularity_score,
    CASE
        WHEN delivery ILIKE '%Free%' THEN TRUE
        ELSE FALSE
    END::BOOLEAN AS free_delivery,
    CASE
        WHEN price <= 100 THEN 'cheap'
        WHEN price <= 250 THEN 'medium'
        ELSE 'expensive'
    END AS price_tier
FROM {{ ref('stg_shopping_results') }}

-- fct for marts and flat table