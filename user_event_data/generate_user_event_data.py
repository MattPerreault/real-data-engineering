import json
import random
import time
from datetime import datetime, timedelta
from typing import TypedDict


class UserEvent(TypedDict):
    timestamp: time
    user_id: int
    event_type: str
    metadata: dict


event_types = ["map_download", "trail_started", "trail_completed"]
map_types = ["satalite", "hybrid", "topo"]

event_date = datetime.now()

for i in range(0, 90):
    event_date_str = event_date.strftime("%Y-%m-%d")
    file = f"./user_events_daily_data/activity-log-{event_date}.json"

    with open(file, "w") as user_event_file:
        for _ in range(0, random.randint(10, 30)):
            user_id = random.randint(1, 100)
            event_type = random.choice(event_types)

            metadata = {}
            if event_type in ["trail_started", "trail_completed"]:
                metadata["duration"] = random.randint(
                    300, 28800
                )  # Duration in seconds (5 min to 8 hours)
            else:
                metadata["size"] = round(
                    random.uniform(1, 500), 2
                )  # Size in MD (1MB to 500MB)
                metadata["map_type"] = random.choice(map_types)

            event = UserEvent(
                timestamp=datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
                user_id=user_id,
                event_type=event_type,
                metadata=metadata,
            )
            # new-line delimeted json to make parsing less error prone.
            user_event_file.write(json.dumps(event) + "\n")

    event_date += timedelta(days=1)
