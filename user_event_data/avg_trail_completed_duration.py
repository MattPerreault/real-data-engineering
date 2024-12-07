import glob
import json
from collections import defaultdict


trail_completed_by_user = defaultdict(
    lambda: {"trail_completed_duration": 0.0, "number_of_completed_trails": 0}
)
for file in glob.glob("./user_events_daily_data/*.json"):
    with open(file, "r") as daily_user_event:
        # you can do this and load all the lines into memory however if the file is huge you can just iterate
        # through each line in the file object directly
        # daily_event_list = daily_user_event.readlines()
        # for daily_event in daily_event_list:

        for daily_event in daily_user_event:
            daily_json_event = json.loads(daily_event)

            if daily_json_event["event_type"] == "trail_completed":
                user_id = daily_json_event["user_id"]
                trail_completed_by_user[user_id][
                    "trail_completed_duration"
                ] += daily_json_event["metadata"].get("duration", 0)
                trail_completed_by_user[user_id]["number_of_completed_trails"] += 1

for user_id, data in trail_completed_by_user.items():
    avg_duration = round(
        data["trail_completed_duration"] / data["number_of_completed_trails"], 2
    )
    print(f"Average trail completed duration for {user_id} is {avg_duration} seconds")
