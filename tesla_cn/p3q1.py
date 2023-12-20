import json
from collections import defaultdict
import re

# testing data sting list
data = [
    "VIN:LRW03021, alerts: 'high_temp, low_soc', timestamp:1645442338",
    "VIN:LRW08090, alerts: '', timestamp:1645452319",
    "VIN:LRW03021, alerts: 'low_vol', timestamp:1645442349",
    "VIN:LRW03021, alerts: 'high_temp, low_soc', timestamp:1645442339",
    "VIN:LRW03021, alerts: '', timestamp:1645442351",
    "VIN:LRW08090, alerts: 'high_vol', timestamp:1645462319",
    "VIN:LRW03021, alerts: 'isolation', timestamp:1645442360",
    "VIN:LRW08090, alerts: 'crash', timestamp:1645462419"
]

vin_data = defaultdict(lambda: defaultdict(list))

for entry in data:
    # Extract VIN, alerts, and timestamp
    vin, alerts, timestamp = re.findall(r"VIN:(.*?), alerts: '(.*?)', timestamp:(\d+)", entry)[0]
    timestamp = int(timestamp)

    # If no alerts, add empty list to all known alerts for this VIN
    if not alerts:
        for known_alert in vin_data[vin].keys():
            vin_data[vin][known_alert].append(timestamp)
    else:
        for alert in alerts.split(', '):
            vin_data[vin][alert].append(timestamp)

json_output = {}

for vin, alerts in vin_data.items():
    json_output[vin] = {}
    for alert, timestamps in alerts.items():
        # Sort timestamps
        timestamps.sort()
        # Set start timestamp
        start = timestamps[0]
        # Set end timestamp to the last timestamp before an empty alert list or the last timestamp if no empty alert list follows
        end = next((timestamps[i] for i in range(len(timestamps) - 1) if timestamps[i + 1] in vin_data[vin] and not vin_data[vin][timestamps[i + 1]]), timestamps[-1])
        # Include end timestamp only if different from start timestamp
        json_output[vin][alert] = {'start': start, 'end': end if end != start else ''}

# Convert to JSON
json_data = json.dumps(json_output, indent=4)
print(json_data)


# Output
# {
#     "LRW03021": {
#         "high_temp": {
#             "start": 1645442338,
#             "end": 1645442351
#         },
#         "low_soc": {
#             "start": 1645442338,
#             "end": 1645442351
#         },
#         "low_vol": {
#             "start": 1645442349,
#             "end": 1645442351
#         },
#         "isolation": {
#             "start": 1645442360,
#             "end": ""
#         }
#     },
#     "LRW08090": {
#         "high_vol": {
#             "start": 1645462319,
#             "end": ""
#         },
#         "crash": {
#             "start": 1645462419,
#             "end": ""
#         }
#     }
# }


