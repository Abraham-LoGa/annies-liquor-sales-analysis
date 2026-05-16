CREATE OR REPLACE TABLE mart_profits AS
WITH sales_agg AS (
    SELECT
        brand_id,
        product_description,
        size,
        SUM(sales_quantity)  AS total_units_sold,
        SUM(sales_dollars)   AS total_revenue,
        AVG(sales_price)     AS avg_sales_price
    FROM clean_sales
    GROUP BY brand_id, product_description, size
),
purchase_costs AS (
    SELECT
        brand_id,
        product_description,
        size,
        SUM(dollars)    AS total_cost_paid,
        SUM(quantity)   AS total_units_purchased,
        SUM(dollars) / NULLIF(SUM(quantity), 0) AS avg_unit_cost
    FROM clean_purchases
    GROUP BY brand_id, product_description, size
)
SELECT
    s.brand_id,
    s.product_description,
    s.size,
    s.total_units_sold,
    s.total_revenue,

    
    ROUND(p.avg_unit_cost * s.total_units_sold, 2)  AS cogs,

   
    ROUND(s.total_revenue - (p.avg_unit_cost * s.total_units_sold), 2) AS gross_profit,

    
    ROUND(
        (s.total_revenue - (p.avg_unit_cost * s.total_units_sold))
        / NULLIF(s.total_revenue, 0) * 100,
        2
    ) AS gross_margin_pct,

    p.avg_unit_cost,
    s.avg_sales_price

FROM sales_agg s
LEFT JOIN purchase_costs p
    ON  s.brand_id            = p.brand_id
    AND s.product_description = p.product_description
    AND s.size                = p.size
WHERE p.avg_unit_cost IS NOT NULL