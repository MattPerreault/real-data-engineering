import os
import datetime
import csv
import random

# Write 60 days worth of sales data to ./daily_sales
# Each csv file will contain date, product_id, region, units_sold, revenue

regions = ["west", "east", "midwest", "south"]


start_date = datetime.datetime.now()
for i in range(1, 60):
    formatted_date = start_date.strftime("%m%d%Y")
    file_path = os.path.join("./daily_sales", f"sales_{formatted_date}.csv")

    with open(file_path, "w") as daily_sales:
        fields = ["product_id", "region", "units_sold", "revenue", "date"]
        csv_writer = csv.DictWriter(daily_sales, fieldnames=fields)
        csv_writer.writeheader()

        num_sales = random.randint(1, 50)
        for j in range(0, num_sales):
            product_id = random.randint(1, 10)
            units = random.randint(1, 1000)
            random_float = random.uniform(1000, 100000)
            rev = round(random_float, 2)

            csv_writer.writerow(
                {
                    "product_id": product_id,
                    "region": regions[random.randint(0, 3)],
                    "units_sold": units,
                    "revenue": rev,
                    "date": formatted_date,
                }
            )
    start_date -= datetime.timedelta(days=1)
