User activity logs are stored in multiple log files. Each log contains:

- `timestamp`
- `user_id`
- `event_type` (`map_download`, `trail_started`, `trail_completed`)
- `metadata` (JSON containing event-specific details like `duration`, `size`, etc.)

**Questions:**

1. Count the total number of unique users who completed at least one trail in the last 60 days.
2. Calculate the average duration of a `trail_completed` event grouped by user.
3. Identify the most frequently downloaded map in the last 7 days.