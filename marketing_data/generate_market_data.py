from collections import defaultdict
import datetime

import json
import random
import string


class Campaign(defaultdict):
    campaign_id: str
    region: str
    ad_type: str
    clicks: int
    impressions: int
    budget_spent: float


regions = ["North America", "Europe", "Asia", "South America", "Africa"]

ad_types = ["Search", "Display", "Video", "Social"]


campaign_day = datetime.datetime.now()

for i in range(0, 60):
    campaign_day_str = datetime.datetime.strftime(campaign_day, "%Y-%m-%d")
    daily_file = f"./marketing_campaign_daily_data/campaign-{campaign_day_str}.json"

    with open(daily_file, "w") as file:
        for j in range(0, random.randint(1, 12)):
            clicks = random.randint(100, 10000)
            impressions = random.randint(clicks * 100, clicks * 1_000)
            budget_spent = round(clicks * random.uniform(0.5, 5.0), 2)

            campaign = Campaign(
                campaign_id=random.randint(1, 5),
                region=random.choice(regions),
                ad_type=random.choice(ad_types),
                clicks=clicks,
                impressions=impressions,
                budget_spent=budget_spent,
            )

            json.dump(campaign, file)
            file.write("\n")

    campaign_day -= datetime.timedelta(days=1)
