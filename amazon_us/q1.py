def pair_orders_with_ads(orders, ad_events):
    # Initialize pointers for orders and ad_events
    i, j = 0, 0
    # Initialize the last ad event dictionary
    last_ad_event = {}
    # Initialize the result list
    result = []
    # Merge the lists and process events in chronological order
    events = []
    for order in orders:
        events.append((order[0], 'order', order))
    for ad_event in ad_events:
        events.append((ad_event[0], 'ad_event', ad_event))
    # Sort the merged list by timestamp
    events.sort(key=lambda x: x[0])
    # Process each event
    for _, event_type, event in events:
        if event_type == 'ad_event':
            timestamp, ad_event_id, customer_id = event
            # Update the last ad event for the customer
            last_ad_event[customer_id] = event
        elif event_type == 'order':
            timestamp, order_id, customer_id = event
            # Get the last ad event for the customer
            ad_event = last_ad_event.get(customer_id)
            # Append the order and its corresponding ad event to the result
            result.append((event, ad_event))
    return result

# Example usage:
orders = [
    (2, 'order1', 'cust1'),
    (5, 'order2', 'cust1'),
    (7, 'order3', 'cust2'),
]

ad_events = [
    (1, 'ad1', 'cust1'),
    (3, 'ad2', 'cust2'),
    (4, 'ad3', 'cust1'),
    (6, 'ad4', 'cust3'),
]

paired_orders = pair_orders_with_ads(orders, ad_events)
for order, ad_event in paired_orders:
    print(f"Order: {order}, Previous Ad Event: {ad_event}")