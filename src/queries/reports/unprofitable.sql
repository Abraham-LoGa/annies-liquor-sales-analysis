WITH thresholds AS (
    SELECT 
        PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY gross_profit) AS loss_threshold
    FROM mart_profits 
    WHERE gross_profit < 0
)


SELECT
    mp.brand_id,
    mp.product_description,
    mp.size,
    mp.total_units_sold,
    mp.total_revenue AS revenue,
    mp.gross_profit,
    mp.gross_margin_pct AS margin_profits,
    ROUND(mp.avg_unit_cost, 2) AS avg_unit_cost,
    ROUND(mp.avg_sales_price, 2) AS avg_sales_price,
    ROUND(mp.avg_unit_cost - mp.avg_sales_price, 2) AS loss_per_unit,

    CASE 
        WHEN mp.gross_profit <= t.loss_threshold
        THEN 'Drop this product'
        WHEN mp.gross_profit < 0 THEN 'Review Pricing'
        ELSE 'Keep'
    END AS recommendation
FROM mart_profits mp
CROSS JOIN thresholds t
WHERE mp.gross_profit <= t.loss_threshold AND mp.gross_profit < 0
ORDER BY mp.gross_profit ASC