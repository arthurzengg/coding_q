import matplotlib.pyplot as plt
from collections import defaultdict
import re

# Testing data
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

# Counting total number of alerts triggered and occurrences of each alert
total_alerts_triggered = 0
alert_counts = defaultdict(int)

for entry in data:
    _, alerts, _ = re.findall(r"VIN:(.*?), alerts: '(.*?)', timestamp:(\d+)", entry)[0]
    if alerts:
        for alert in alerts.split(', '):
            alert_counts[alert] += 1
            total_alerts_triggered += 1

# Percentage
total_strings = len(data)
alert_percentages = {alert: (count / total_strings) * 100 for alert, count in alert_counts.items()}

# Plot for total time
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
ax1.bar(alert_counts.keys(), alert_counts.values())
ax1.set_title('Total Numbers of Times Each Alert is Triggered')
ax1.set_xlabel('Alerts')
ax1.set_ylabel('Number of Triggers')

# Plot for percentage
ax2.bar(alert_percentages.keys(), alert_percentages.values())
ax2.set_title('Percentage of Each Alert Triggered')
ax2.set_xlabel('Alerts')
ax2.set_ylabel('Percentage (%)')

plt.tight_layout()
plt.show()
