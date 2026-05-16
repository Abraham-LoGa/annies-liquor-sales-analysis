SELECT 
    brand_id, 
    product_description,
    size,
    total_units_sold,
    total_revenue AS revenue,
    gross_profit,
    gross_margin_pct AS margin_pct,
    avg_unit_cost,
    avg_sales_price
FROM mart_profits
WHERE gross_profit IS NOT NULL
ORDER BY {field_order} DESC
LIMIT 10