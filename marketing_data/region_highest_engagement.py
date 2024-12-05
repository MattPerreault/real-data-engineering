import glob
import json
from collections import defaultdict

# Get all data for the last quarter. i.e. last 3 months. We only have 60 days worth so we will do the last 2 months
# Calculate the CTR per region. Sort by CTR DESC

click_impressions_by_region = defaultdict(lambda: {"clicks": 0.0, "impressions": 0.0})

for file in glob.glob("./marketing_campaign_daily_data/*.json"):
    with open(file, "r") as daily_campaign:
        for row_str in daily_campaign:
            row_json = json.loads(row_str)

            region = row_json["region"]
            clicks = row_json["clicks"]
            impressions = row_json["impressions"]

            click_impressions_by_region[region]["clicks"] += clicks
            click_impressions_by_region[region]["impressions"] += impressions


ctr_per_region = []
for region, data in click_impressions_by_region.items():
    ctr = data["clicks"] / data["impressions"] if data["impressions"] > 0 else 0.0

    ctr_per_region.append({"region": region, "ctr": ctr})


ctr_per_region.sort(key=lambda x: x["ctr"], reverse=True)
for region in ctr_per_region:
    print(region)
