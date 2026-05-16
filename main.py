from src.report.report_builder import build_report
from src.report.analisys import DataAnalisys
from db.database import DBManagement
from src.utils.logger import logger

def main():
    logger.info("Starting reporting pipeline ....")

    db = DBManagement()
    analyzer = DataAnalisys(db=db)

    top_products = analyzer.get_top_products()
    top_brands = analyzer.get_top_brands()
    unprofit = analyzer.get_unprofit()
    summary_metrics = analyzer.get_summary_metrics()

    build_report(
        top_products=top_products,
        top_brands=top_brands,
        unprofit=unprofit,
        summary_metrics=summary_metrics
    )

    logger.info("Report generated successfully.")



if __name__ == "__main__":
    main()