import glob
import json
from collections import defaultdict

# Get sum of clicks and sum of budget for each campaign. cost-per-click budget/click

campaign_click_budget = defaultdict(lambda: {"clicks": 0.0, "budget": 0.0})

for file in glob.glob("./marketing_campaign_daily_data/*.json"):
    with open(file, "r") as daily_file:
        row = daily_file.readline()
        json_row = json.loads(row)

        campaign_id = json_row["campaign_id"]
        campaign_clicks = json_row["clicks"]
        campaign_budget = json_row["budget_spent"]

        campaign_click_budget[campaign_id]["clicks"] += campaign_clicks
        campaign_click_budget[campaign_id]["budget"] += campaign_budget

cost_per_click = []
for campaign, data in campaign_click_budget.items():
    cpc = round(data["budget"] / data["clicks"], 2) if data["clicks"] > 0 else 0

    cost_per_click.append({"campaign": campaign, "cpc": cpc})

cost_per_click.sort(key=lambda x: x["campaign"])

for campaign in cost_per_click:
    print(campaign)
