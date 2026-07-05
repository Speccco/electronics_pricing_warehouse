{% snapshot fct_product_listings_snapshot %}
{{
    config(
        target_schema='snapshots',
        unique_key='product_id',
        strategy='timestamp',
        updated_at='captured_at'
    )
}}

SELECT
    p.product_id,
    s.source_key, 
    p.captured_at::TIMESTAMP AS captured_at, 
    p.price, 
    p.original_price, 
    p.rating, 
    p.reviews, 
    p.popularity_score 
FROM {{ ref('int_product_enrichment') }} p
LEFT JOIN {{ ref('dim_source') }} s ON p.source = s.source
{% endsnapshot %}