import csv
import datetime
import glob

from collections import defaultdict


# Get last 30 days worth of files
# Iterate through each file
# keep a running total of revenue and units sold per product id


def get_files_in_date_range(pattern: str, start: str, end: str) -> list[str]:
    files = []

    for file_path in glob.glob(pattern):
        file_date_str = file_path.split("_")[2][:-4]
        file_date = datetime.datetime.strptime(file_date_str, "%m%d%Y").date()

        if file_date <= start and file_date >= end:
            files.append(file_path)
    return files


pattern = "./daily_sales/*.csv"
start = datetime.datetime.strptime("11202024", "%m%d%Y").date()
end = datetime.datetime.strptime("10212024", "%m%d%Y").date()
fields = ["product_id", "region", "units_sold", "revenue", "date"]

totals = defaultdict(lambda: {"revenue": 0.0, "units_sold": 0})

files = get_files_in_date_range(pattern, start, end)
for file in files:
    with open(file, "r") as daily_sale_file:
        csv_reader = csv.DictReader(daily_sale_file, fieldnames=fields)
        next(csv_reader)  # This skips the header row
        for row in csv_reader:
            product_id = row["product_id"]

            totals[product_id]["revenue"] += float(row["revenue"])
            totals[product_id]["units_sold"] += int(row["units_sold"])

results = [{"product_id": k, **v} for k, v in totals.items()]

for row in results:
    print(row)
