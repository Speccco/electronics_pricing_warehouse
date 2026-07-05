{% snapshot dim_product_snapshot %}

{{
  config(
    target_schema='snapshots',
    unique_key='product_id',
    strategy='check',
    check_cols=['title', 'product_link', 'tag', 'second_hand_condition']
  )
}}

select
    product_id,
    title,
    product_link,
    tag,
    second_hand_condition
from {{ ref('dim_product') }}

{% endsnapshot %}