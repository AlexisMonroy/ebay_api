from datetime import datetime, timedelta

def schedule_listings(num_items: int):
    scheduled_times = []
    now = datetime.utcnow() + timedelta(minutes=5)
    full_hours, remainder = divmod(num_items, 10)
    for hour in range(full_hours):
        for i in range(10):
            scheduled_time = now + timedelta(hours=hour) + timedelta(minutes=6 * i)
            scheduled_times.append(scheduled_time.isoformat())
            print(f"Item {hour * 10 + i + 1} scheduled for {scheduled_time.isoformat()}")
    for i in range(remainder):
        scheduled_time = now + timedelta(hours=full_hours) + timedelta(minutes=60 / remainder * i)
        scheduled_times.append(scheduled_time.isoformat())
        print(f"Item {full_hours * 10 + i + 1} scheduled for {scheduled_time.isoformat()}")
    print(scheduled_times)
    return scheduled_times

schedule_listings(11)