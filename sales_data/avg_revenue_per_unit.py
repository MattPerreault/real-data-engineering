import csv
import glob
from collections import defaultdict

totals = defaultdict(lambda: {"total_revenue": 0.0, "total_units_sold": 0})
all_rev_per_unit_day = []
for file in glob.glob("./daily_sales/*.csv"):
    with open(file, "r") as daily_sales:
        csv_reader = csv.DictReader(
            daily_sales,
            fieldnames=["product_id", "region", "units_sold", "revenue", "date"],
        )
        next(csv_reader)

        for row in csv_reader:
            product_id = row["product_id"]
            revenue = float(row["revenue"])
            units_sold = float(row["units_sold"])

            totals[product_id]["total_revenue"] += revenue
            totals[product_id]["total_units_sold"] += units_sold


avg_rev_per_unit = []
for product, totals in totals.items():
    if totals["total_units_sold"] > 0:
        avg_revenue = totals["total_revenue"] / totals["total_units_sold"]
        avg_rev_per_unit.append({"product_id": product, "avg": avg_revenue})

for avg in avg_rev_per_unit:
    print(
        f"Product {avg['product_id']}, average revenue per unit sold: {round(avg['avg'], 2)}"
    )
