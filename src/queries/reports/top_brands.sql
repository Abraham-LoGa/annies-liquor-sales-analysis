SELECT
    brand_id,
    STRING_AGG(DISTINCT product_description, ', ') AS product_descriptions,
    SUM(total_units_sold) AS total_units_sold,
    ROUND(SUM(total_revenue), 2) AS total_revenue,
    ROUND(SUM(gross_profit), 2) AS total_gross_profit,
    ROUND(
        SUM(gross_profit) / NULLIF(SUM(total_revenue), 0) * 100,
        2
    ) AS brand_margin_pct
FROM mart_profits
WHERE gross_profit IS NOT NULL
GROUP BY brand_id
ORDER BY {field_order} DESC
LIMIT 10