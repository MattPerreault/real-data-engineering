import glob
import csv
from collections import defaultdict


rev_by_product = defaultdict(lambda: defaultdict(float))

# Loop over every file and sum up the revenue grouped by product and region


def get_revenue_by_product_region() -> dict[dict]:
    for file in glob.glob("./daily_sales/*.csv"):
        with open(file, "r") as daily_file:
            csv_reader = csv.DictReader(
                daily_file,
                fieldnames=["product_id", "region", "units_sold", "revenue", "date"],
            )
            next(csv_reader)
            for row in csv_reader:
                # Super sexy use of nested default dicts for grouping by more than one dimension.
                rev_by_product[row["product_id"]][row["region"]] += float(
                    row["revenue"]
                )  # total revenue by product and region.
    return rev_by_product


def get_top_three_regions_by_product(
    rev_by_product: dict[dict[str:float]],
) -> dict[str : list[dict[str:float]]]:
    # the outer dict groups by product id
    # the inner dict gets the revenue per region
    top_regions_by_product = {}
    for product_id, regions in rev_by_product.items():
        # A list sorted by revenue descending
        # items returns a list of tuples like ('north', 1234.56)
        sorted_regions = sorted(regions.items(), key=lambda x: x[1], reverse=True)
        # take the top three from the sorted list per product_id
        top_regions_by_product[product_id] = sorted_regions[:3]
    return top_regions_by_product


def pretty_print(top_regions_sorted: dict[str:list]):
    for product_id, top_regions in top_regions_sorted.items():
        print(f"Product ID: {product_id}")
        for region, revenue in top_regions:
            print(f"Region: {region}. Revenue: {revenue}")
        print("\n")


revenue_by_product_region = get_revenue_by_product_region()
top_three_regions_by_product_sorted = get_top_three_regions_by_product(
    rev_by_product=revenue_by_product_region
)
pretty_print(top_three_regions_by_product_sorted)
