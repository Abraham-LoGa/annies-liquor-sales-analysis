CREATE OR REPLACE TABLE clean_sales AS
WITH deduplicated AS (
    SELECT DISTINCT
        *
    FROM stg_sales
    WHERE Brand IS NOT NULL 
        AND SalesQuantity > 0
        AND SalesDollars > 0
)

SELECT
    TRIM(InventoryId) as inventory_id,
    Store AS store_id,
    Brand AS brand_id,

    TRIM(Description) AS product_description,
    TRIM(Size) AS Size,
    VendorNo AS vendor_no,
    TRIM(VendorName) AS vendor_name,

    CAST(SalesQuantity AS INTEGER) AS sales_quantity,
    CAST(SalesDollars AS DOUBLE) AS sales_dollars,
    CAST(SalesPrice AS DOUBLE) AS sales_price,
    CAST(ExciseTax AS DOUBLE) AS excise_tax,
    
FROM deduplicated