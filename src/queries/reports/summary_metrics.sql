SELECT
    ROUND(SUM(gross_profit), 2) AS total_profit,
    ROUND(SUM(cogs), 2) AS total_cogs,
    SUM(total_units_sold) AS total_units_sold,
    ROUND(
        (SUM(gross_profit) / NULLIF(SUM(total_revenue), 0)) * 100, 2
    ) AS avg_margin_pct
FROM mart_profits