{{ config(materialized = 'view') }}

SELECT
    product_id::VARCHAR AS product_id,
    title::VARCHAR AS title,
    product_link::VARCHAR AS product_link,
    source::VARCHAR AS source,
    captured_at::DATE AS captured_at,
    price::DOUBLE AS price,
    full_price::DOUBLE AS original_price,
    REPLACE(tag, ' OFF', '') AS tag,
    second_hand_condition IS NOT NULL AS second_hand_condition,
    rating::DOUBLE AS rating,
    reviews::INTEGER AS reviews,
    delivery::VARCHAR AS delivery
FROM {{ source('raw', 'shopping_results') }}