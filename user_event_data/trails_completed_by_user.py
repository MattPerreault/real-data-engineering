import glob
import json
from datetime import datetime, timedelta

# Count the total number of unique users who completed at least one trail in the last 60 days.

end_date = datetime.now()
start_date = end_date - timedelta(days=60)

end_date_str = end_date.strftime("%Y-%m-%d")
start_date_str = start_date.strftime("%Y-%m-%d")

# Use a set for unique items, faster lookup times O(1)
unique_users = set()

for file in glob.glob("./user_events_daily_data/*.json"):
    file_date_str = file.split()[0][-10:]

    if start_date_str <= file_date_str <= end_date_str:
        with open(file, "r") as daily_activity_log:
            records = daily_activity_log.readlines()

            for record in records:
                record_json = json.loads(record)

                if record_json["event_type"] == "trail_completed":
                    unique_users.add(record_json["user_id"])

print(len(unique_users))
