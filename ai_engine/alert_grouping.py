from collections import defaultdict

def group_signals_by_account(signals):
    """
    Groups multiple signals into a single case
    per account to reduce alert fatigue.
    """

    grouped = defaultdict(list)

    for signal in signals:
        grouped[signal["account_id"]].append(signal)

    return grouped
