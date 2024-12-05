import random
import time
from datetime import datetime
from typing import TypedDict


class UserEvent(TypedDict):
    timestamp: time
    user_id : int
    event_type: str
    metadata: dict

event_types = ['map_download', 'trail_started', 'trail_completed']
map_types = [''] #random map types

event_date = datetime.now()

for i in range(0, 90):
    event_date_str = datetime.strftime(event_date, '%Y-%m-%d')
    print(event_date_str)
    file = f'./user_events_daily_data/activity-log-{event_date}.json'
    with open(file, 'w') as user_even_file:
        for i in range(0, random.randint(0, 30)):
            user_id = random.randint(0, 100)
            event_type = random.choice(event_types)
            metadata = {}
            if event_type in ['trail_started', 'trail_completed']:
                # metadata['duration'] = # random duration
                metadata['size'] = 0
            else:
                metadata['duration'] = 0
                # metadata['size'] = # random size

    event_date += datetime.timedelta(days=1) 
    