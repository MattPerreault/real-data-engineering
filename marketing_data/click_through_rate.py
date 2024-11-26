import glob
import json
from collections import defaultdict


def get_ads_by_type() -> dict[str:float]:
    ads_by_type = defaultdict(lambda: {"clicks": 0.0, "impressions": 0.0})
    for file in glob.glob("./marketing_campaign_daily_data/*.json"):
        with open(file, "r") as campaign_file:
            row = campaign_file.readline()
            json_row = json.loads(row)
            ad_type = json_row["ad_type"]
            clicks = json_row["clicks"]
            impressions = json_row["impressions"]

            ads_by_type[ad_type]["clicks"] += clicks
            ads_by_type[ad_type]["impressions"] += impressions
    return ads_by_type


def calculate_ctr_per_ad_type(ads_by_type: dict) -> list[dict[str:float]]:
    return [
        {"ad_type": ad_type, "CTR": data["clicks"] / data["impressions"]}
        for ad_type, data in ads_by_type.items()
        if data["impressions"] > 0  # prevent divide by 0 error.
    ]


ads_by_type = get_ads_by_type()
ctr_per_type = calculate_ctr_per_ad_type(ads_by_type=ads_by_type)


for ctr in ctr_per_type:
    print(f"Ad-Type: {ctr['ad_type']}, CTR: {round(ctr['CTR'], 4)}")
