CREATE OR REPLACE TABLE clean_purchases_prices AS 

WITH deduplicated AS (
    SELECT DISTINCT *
    FROM stg_purchase_prices
    WHERE Brand IS NOT NULL
        AND PurchasePrice > 0
)

SELECT
    
    Brand AS brand_id,
    TRIM(Description) AS product_description,
    TRIM(Size) AS size,
    CAST(Price AS DOUBLE) AS retail_price,
    CAST(PurchasePrice AS DOUBLE) AS purchase_price,
    TRIM(VendorName) AS vendor_name,
    VendorNumber AS vendor_no,

FROM deduplicated
