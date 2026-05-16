from src.utils.query_loader import QueryLoader
from db.database import DBManagement
from src.utils.logger import logger
from config import QUERIES_PATH
import pandas as pd

class DataAnalisys:

    def __init__(self, db: DBManagement):

        self.db = db
    
    def _run_report(self, filename:str, dict_args:dict=None) -> pd.DataFrame:
        try:
            query_path = QUERIES_PATH/filename
            query = QueryLoader.load(path=query_path)
            if dict_args:
                query = query.format(**dict_args)

            return self.db.fetch_df(query=query)
        
        except Exception:
            logger.exception(f"Failed executing report query: {filename}")
    
    def get_top_products(self):

        top_products_data = {
            "top_products_by_profit": self._run_report(filename="top_products.sql", 
                                                       dict_args={"field_order":"gross_profit"}),
            "top_products_by_margin": self._run_report(filename="top_products.sql", 
                                                       dict_args={"field_order":"gross_margin_pct"})
        }
        return top_products_data 
    
    def get_top_brands(self):

        top_brands_data = {
            "top_brands_by_profit": self._run_report("top_brands.sql", dict_args={"field_order":"total_gross_profit"}),
            "top_brands_by_margin": self._run_report("top_brands.sql", dict_args={"field_order":"brand_margin_pct"})
        }
        return top_brands_data
    
    def get_unprofit(self):

        return self._run_report("unprofitable.sql")
    
    def get_summary_metrics(self):

        summary_metrics = self._run_report("summary_metrics.sql")
        summary= {
            "total_profit": f"{summary_metrics.iloc[0]['total_profit']:,.2f}",
            "total_units_sold": f"{summary_metrics.iloc[0]['total_units_sold']:,.0f}",
            "avg_margin_pct": f"{summary_metrics.iloc[0]['avg_margin_pct']:.2f}"
            }
        
        return summary
    
    