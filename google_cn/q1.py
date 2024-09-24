data = [
    ('Abby', 10, 100),
    ('Ben', 50, 70),
    ('Carla', 60, 120),
    ('David', 150, 300)
]

# Create a list of all start and end events
events = []
for name, start, end in data:
    events.append((start, 'start', name))
    events.append((end, 'end', name))

print(events)

# Sort events by time; for same times, 'start' comes before 'end'
events.sort(key=lambda x: (x[0], 0 if x[1] == 'start' else 1))

print(events)

current_time = None
current_people = set()
intervals = []

for time, event_type, name in events:
    if current_time is not None and current_time != time:
        if current_people:
            intervals.append((current_time, time, sorted(current_people)))
        current_time = time
    else:
        current_time = time

    if event_type == 'start':
        current_people.add(name)
    elif event_type == 'end':
        current_people.remove(name)

print(intervals)
# Output the intervals
print("Start | End | Names")
for start, end, names in intervals:
    print(f"{start} {end} {', '.join(names)}")