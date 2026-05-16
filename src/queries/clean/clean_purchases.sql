CREATE OR REPLACE TABLE clean_purchases AS
WITH deduplicated AS (
    SELECT DISTINCT
    *
    FROM stg_purchases
    WHERE Brand IS NOT NULL
        AND Quantity > 0
        AND Dollars > 0
        AND PurchasePrice > 0
)

SELECT
    TRIM(InventoryId) AS inventory_id,
    Store AS store_id,
    Brand AS brand_id,
    TRIM(Description) AS product_description,
    TRIM(Size) AS size,
    VendorName AS vendor_name,
    CAST(PurchasePrice AS DOUBLE) AS purchase_price,
    CAST(Quantity AS INTEGER) AS quantity,
    CAST(Dollars AS DOUBLE) AS dollars,
    CAST(PODate AS DATE) AS po_date,
    CAST(ReceivingDate AS DATE) AS receiving_date,
    CAST(InvoiceDate AS DATE) AS invoice_date,
    CAST(PayDate AS DATE) AS pay_date,

FROM deduplicated