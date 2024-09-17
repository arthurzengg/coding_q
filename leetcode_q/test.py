def detect_fraudulent_merchants(not_fraudulent, fraudulent, mcc_thresholds, merchants_info, min_transactions, charges):
    # Parse and set up data structures
    not_fraudulent_codes = set(not_fraudulent.split(","))
    fraudulent_codes = set(fraudulent.split(","))

    # MCC and their fraud thresholds
    mcc_threshold_dict = {}
    for line in mcc_thresholds.split("\n"):
        mcc, threshold = line.split(",")
        mcc_threshold_dict[mcc] = int(threshold)

    # Merchant accounts and their MCCs
    merchant_mcc_map = {}
    for line in merchants_info.split("\n"):
        account_id, mcc = line.split(",")
        merchant_mcc_map[account_id] = mcc

    # Processing charges
    merchant_transactions = {account_id: [] for account_id in merchant_mcc_map}
    merchant_fraud_counts = {account_id: 0 for account_id in merchant_mcc_map}

    for line in charges.split("\n"):
        if line.startswith("CHARGE"):
            _, charge_id, account_id, amount, code = line.split(",")
            if account_id in merchant_transactions:
                merchant_transactions[account_id].append((float(amount), code))
                if code in fraudulent_codes:
                    merchant_fraud_counts[account_id] += 1

    # Determine fraudulent merchants
    fraudulent_merchants = []
    for account_id in merchant_mcc_map:
        total_transactions = len(merchant_transactions[account_id])
        if total_transactions >= min_transactions:
            mcc = merchant_mcc_map[account_id]
            fraud_threshold = mcc_threshold_dict[mcc]
            fraud_count = merchant_fraud_counts[account_id]
            if fraud_count >= fraud_threshold:
                fraudulent_merchants.append(account_id)

    # Return sorted list of fraudulent merchants
    fraudulent_merchants.sort()
    return ",".join(fraudulent_merchants)


# Example usage
not_fraudulent = "approved,invalid_pin,expired_card"
fraudulent = "do_not_honor,stolen_card,lost_card"
mcc_thresholds = "retail,5\nairline,2\nvenue,3"
merchants_info = "acct_1,airline\nacct_2,venue\nacct_3,retail"
min_transactions = 0
charges = "CHARGE,ch_1,acct_1,100,do_not_honor\nCHARGE,ch_2,acct_1,200,approved\nCHARGE,ch_3,acct_1,300,do_not_honor\nCHARGE,ch_4,acct_2,100,lost_card\nCHARGE,ch_5,acct_2,200,lost_card\nCHARGE,ch_6,acct_2,300,lost_card\nCHARGE,ch_7,acct_3,100,lost_card\nCHARGE,ch_8,acct_2,200,stolen_card\nCHARGE,ch_9,acct_3,100,approved"

print(detect_fraudulent_merchants(not_fraudulent, fraudulent, mcc_thresholds, merchants_info, min_transactions, charges))