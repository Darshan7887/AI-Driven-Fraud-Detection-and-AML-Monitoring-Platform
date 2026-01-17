from datetime import datetime

def detect_velocity_spike(transactions, window_minutes=10):
    """
    Detects rapid bursts of transactions within a short time window.
    """

    signals = []
    transactions_sorted = sorted(
        transactions,
        key=lambda x: x["timestamp"]
    )

    for i in range(len(transactions_sorted)):
        count = 1
        base_time = datetime.fromisoformat(
            transactions_sorted[i]["timestamp"]
        )

        for j in range(i + 1, len(transactions_sorted)):
            next_time = datetime.fromisoformat(
                transactions_sorted[j]["timestamp"]
            )

            if (next_time - base_time).seconds <= window_minutes * 60:
                count += 1
            else:
                break

        if count >= 3:
            signals.append({
                "signal_type": "VELOCITY_SPIKE",
                "strength": "HIGH",
                "reason": (
                    f"{count} transactions occurred within "
                    f"{window_minutes} minutes, indicating abnormal velocity."
                )
            })

    return signals
