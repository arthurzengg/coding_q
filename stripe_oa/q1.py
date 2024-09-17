def find_fraudulent_merchants(non_fraud_codes, fraud_codes, mcc_thresholds, merchant_mcc_map, min_charges, entries):
    # Define sets for quick lookup
    # non_fraudulent_codes = set(non_fraud_codes.replace(' ', '').split(","))
    # fraudulent_codes = set(fraud_codes.replace(' ', '').split(","))
    #
    # # Parse MCC thresholds into a dictionary with float values for percentage
    # mcc_threshold_dict = {}
    # for entry in mcc_thresholds:
    #     mcc, threshold = [x.strip() for x in entry.split(',')]
    #     mcc_threshold_dict[mcc] = float(threshold)
    #
    # # Parse merchant data into a dictionary mapping account to MCC
    # merchant_mcc_dict = {}
    # for entry in merchant_mcc_map:
    #     account_id, mcc = [x.strip() for x in entry.split(',')]
    #     merchant_mcc_dict[account_id] = mcc
    #
    # min_charges = int(min_charges.strip())

    non_fraudulent_codes = set(non_fraud_codes.replace(' ', '').split(","))
    fraudulent_codes = set(fraud_codes.replace(' ', '').split(","))

    # Parse MCC thresholds into a dictionary with float values for percentage
    mcc_threshold_dict = {}
    for entry in mcc_thresholds:
        mcc, threshold = [x.strip() for x in entry.split(',')]
        mcc_threshold_dict[mcc] = float(threshold)

    # Parse merchant data into a dictionary mapping account to MCC
    merchant_mcc_dict = {}
    for entry in merchant_mcc_map:
        account_id, mcc = [x.strip() for x in entry.split(',')]
        merchant_mcc_dict[account_id] = mcc

    min_charges = int(min_charges.strip())

    # print(fraudulent_codes)
    # print(mcc_threshold_dict)
    # print(merchant_mcc_dict)

    # Initialize transaction tracking
    merchant_transactions = {merchant: [] for merchant in merchant_mcc_dict}
    merchant_fraud_counts = {merchant: 0 for merchant in merchant_mcc_dict}
    merchant_status = {merchant: 'not_fraudulent' for merchant in merchant_mcc_dict}

    # Initialize charges_dict to keep track of individual charges
    charges_dict = {}

    # Process entries
    for entry in entries:
        entry = entry.strip()
        if entry.startswith("CHARGE"):
            # Process charge
            parts = entry.split(',')
            _, charge_id, account_id, amount, code = [x.strip() for x in parts]
            if account_id in merchant_transactions:
                merchant_transactions[account_id].append(code)
                is_fraudulent = False
                if code in fraudulent_codes:
                    is_fraudulent = True
                    merchant_fraud_counts[account_id] += 1
                charges_dict[charge_id] = {'account_id': account_id, 'code': code, 'fraudulent': is_fraudulent}

                # Evaluate merchant status if necessary
                total_transactions = len(merchant_transactions[account_id])
                if total_transactions >= min_charges and merchant_status[account_id] != 'fraudulent':
                    fraud_count = merchant_fraud_counts[account_id]
                    fraud_percentage = fraud_count / total_transactions if total_transactions > 0 else 0
                    mcc = merchant_mcc_dict[account_id]
                    threshold = mcc_threshold_dict[mcc]
                    if fraud_percentage >= threshold:
                        merchant_status[account_id] = 'fraudulent'
        elif entry.startswith("DISPUTE"):
            # Process dispute
            _, charge_id = [x.strip() for x in entry.split(',')]
            if charge_id in charges_dict:
                charge = charges_dict[charge_id]
                if charge['fraudulent']:
                    account_id = charge['account_id']
                    charge['fraudulent'] = False
                    # Adjust fraud count
                    merchant_fraud_counts[account_id] -= 1

                    # Re-evaluate merchant status if they are currently 'fraudulent'
                    if merchant_status[account_id] == 'fraudulent':
                        total_transactions = len(merchant_transactions[account_id])
                        fraud_count = merchant_fraud_counts[account_id]
                        fraud_percentage = fraud_count / total_transactions if total_transactions > 0 else 0
                        mcc = merchant_mcc_dict[account_id]
                        threshold = mcc_threshold_dict[mcc]
                        if fraud_percentage < threshold:
                            merchant_status[account_id] = 'not_fraudulent'

    # After processing all entries, collect merchants who are 'fraudulent'
    fraudulent_merchants = [account_id for account_id, status in merchant_status.items() if status == 'fraudulent']

    # Return sorted list of fraudulent merchants
    return ",".join(sorted(fraudulent_merchants))


non_fraud_codes = "approved,invalid_pin,expired_card"
fraud_codes = "do_not_honor,stolen_card,lost_card"
mcc_thresholds = [
    "retail,5",
    "airline,2",
    "restaurant,10",
    "venue,3"
]
merchant_mcc_map = [
    "acct_1,airline",
    "acct_2,venue",
    "acct_3,retail"
]
min_charges = "0"
charges = [
    "CHARGE,ch_1,acct_1,100,do_not_honor",
    "CHARGE,ch_2,acct_1,200,approved",
    "CHARGE,ch_3,acct_1,300,do_not_honor",
    "CHARGE,ch_4,acct_2,100,lost_card",
    "CHARGE,ch_5,acct_2,200,lost_card",
    "CHARGE,ch_6,acct_2,300,lost_card",
    "CHARGE,ch_7,acct_3,100,lost_card",
    "CHARGE,ch_8,acct_2,200,stolen_card",
    "CHARGE,ch_9,acct_3,100,approved"
]


print(find_fraudulent_merchants(non_fraud_codes, fraud_codes, mcc_thresholds, merchant_mcc_map, min_charges, charges))