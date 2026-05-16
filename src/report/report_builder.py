from jinja2 import Environment, FileSystemLoader
from src.utils.logger import logger
from pathlib import Path
from config import TEMPLATES
#from weasyprint import HTML

TEMPLATE_DIR = TEMPLATES
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

def build_report(
    top_products, 
    top_brands,
    unprofit,
    summary_metrics
):
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template("report.html")
    html_content = template.render(
        summary_data = summary_metrics,
        top_products_by_profit = top_products.get("top_products_by_profit").to_dict(orient="records"),
        top_products_by_margin = top_products.get("top_products_by_margin").to_dict(orient="records"),
        top_brands_by_profit = top_brands.get("top_brands_by_profit").to_dict(orient="records"),
        top_brands_by_margin = top_brands.get("top_brands_by_margin").to_dict(orient="records"),
        unprofitable=unprofit.to_dict(orient="records")
    )
    html_file = OUTPUT_DIR / "report.html"
    pdf_file = OUTPUT_DIR / "report.pdf"

    #html_file.write_text(html_content, encoding="utf-8")
    #HTML(string=html_content, base_url=str(OUTPUT_DIR)).write_pdf(pdf_file)

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    logger.info(f"Report generated: {html_file}")
