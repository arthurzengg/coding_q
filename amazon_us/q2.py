from datetime import datetime, timedelta

class Event:
    def __init__(self, event_id, title, start_time, end_time, participants=None):
        self.event_id = event_id
        self.title = title
        self.start_time = start_time  # datetime object
        self.end_time = end_time      # datetime object
        self.participants = participants if participants else []

    def add_participant(self, user):
        if user not in self.participants:
            self.participants.append(user)
            user.add_event(self)

    def remove_participant(self, user):
        if user in self.participants:
            self.participants.remove(user)
            user.remove_event(self)


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.events = []  # List of Event objects

    def add_event(self, event):
        # Optionally check for time conflicts here
        self.events.append(event)

    def remove_event(self, event):
        if event in self.events:
            self.events.remove(event)

    def update_event(self, old_event, new_event):
        self.remove_event(old_event)
        self.add_event(new_event)

    def get_events_in_time_period(self, start_time, end_time):
        return [
            event for event in self.events
            if event.start_time < end_time and event.end_time > start_time
        ]

def create_event(event_id, title, start_time, end_time, participants):
    event = Event(event_id, title, start_time, end_time, participants)
    for user in participants:
        user.add_event(event)
    return event

def update_event(event, new_title=None, new_start_time=None, new_end_time=None):
    if new_title:
        event.title = new_title
    if new_start_time:
        event.start_time = new_start_time
    if new_end_time:
        event.end_time = new_end_time
    # Participants' schedules are updated automatically since they reference the same event object

def delete_event(event):
    for user in event.participants:
        user.remove_event(event)

def merge_intervals(intervals):
    # Sort intervals by start time
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    merged = []
    for current in sorted_intervals:
        if not merged or merged[-1][1] < current[0]:
            merged.append(list(current))
        else:
            merged[-1][1] = max(merged[-1][1], current[1])
    return merged

def compute_free_intervals(busy_intervals, start_time, end_time):
    free_intervals = []
    prev_end = start_time
    for interval in busy_intervals:
        if interval[0] > prev_end:
            free_intervals.append((prev_end, interval[0]))
        prev_end = max(prev_end, interval[1])
    if prev_end < end_time:
        free_intervals.append((prev_end, end_time))
    return free_intervals

def find_common_free_slots(users, start_time, end_time):
    busy_intervals = []
    for user in users:
        events = user.get_events_in_time_period(start_time, end_time)
        for event in events:
            busy_intervals.append((event.start_time, event.end_time))
    merged_busy = merge_intervals(busy_intervals)
    free_slots = compute_free_intervals(merged_busy, start_time, end_time)
    return free_slots

# Example Usage
if __name__ == "__main__":
    # Create some users
    alice = User(1, "Alice")
    bob = User(2, "Bob")
    carol = User(3, "Carol")

    # Define time intervals
    now = datetime.now()
    in_one_hour = now + timedelta(hours=1)
    in_two_hours = now + timedelta(hours=2)
    in_three_hours = now + timedelta(hours=3)
    in_four_hours = now + timedelta(hours=4)

    # Create events
    event1 = create_event(101, "Meeting A", now, in_two_hours, [alice, bob])
    event2 = create_event(102, "Meeting B", in_one_hour, in_three_hours, [bob, carol])
    event3 = create_event(103, "Meeting C", in_three_hours, in_four_hours, [alice, carol])

    # Get Alice's schedule for today
    start_of_day = datetime(now.year, now.month, now.day)
    end_of_day = start_of_day + timedelta(days=1)
    alices_events = alice.get_events_in_time_period(start_of_day, end_of_day)
    print("Alice's Schedule:")
    for event in alices_events:
        print(f"- {event.title} from {event.start_time} to {event.end_time}")

    # Find common free slots between Alice, Bob, and Carol today
    common_free_slots = find_common_free_slots([alice, bob, carol], start_of_day, end_of_day)
    print("\nCommon Free Time Slots:")
    for slot in common_free_slots:
        print(f"- From {slot[0]} to {slot[1]}")