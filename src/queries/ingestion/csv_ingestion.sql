CREATE OR REPLACE TABLE {table_name} AS

SELECT * FROM read_csv_auto(
    '{file_path}',
    HEADER=TRUE
)