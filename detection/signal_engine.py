import csv


from reports.technical_report import generate_technical_report
from reports.executive_summary import generate_executive_report
from reports.aml_mapping import map_to_aml_principles
from alerts.alert_generator import generate_alert
from alerts.case_manager import create_case
from alerts.analyst_actions import review_case
from ingestion.behavior_profiles import generate_account_profile
from detection.amount_rules import detect_amount_anomaly
from detection.geo_rules import detect_geo_anomaly
from detection.behavior_rules import detect_behavior_drift
from detection.velocity_rules import detect_velocity_spike
from detection.structuring_rules import detect_structuring

from risk_scoring.score_calculator import calculate_risk_score
from risk_scoring.prioritization import assign_priority

from ai_engine.ai_reasoner import run_ai_reasoning


def run_detection():
    # =========================
    # LOAD TRANSACTIONS
    # =========================
    with open("data/transactions.csv") as f:
        transactions = list(csv.DictReader(f))

    for txn in transactions:
        txn["amount"] = float(txn["amount"])

    # =========================
    # ACCOUNT PROFILE
    # =========================
    account_profile = generate_account_profile(
        transactions[0]["account_id"]
    )

    all_signals = []

    # =========================
    # PER-TRANSACTION SIGNALS
    # =========================
    for txn in transactions:
        for detector in [
            detect_amount_anomaly,
            detect_geo_anomaly,
            detect_behavior_drift
        ]:
            signal = detector(txn, account_profile)
            if signal:
                signal.update({
                    "transaction_id": txn["transaction_id"],
                    "account_id": txn["account_id"]
                })
                all_signals.append(signal)

    # =========================
    # CROSS-TRANSACTION SIGNALS
    # =========================
    account_id = account_profile["account_id"]

    for signal in detect_velocity_spike(transactions):
        signal["account_id"] = account_id
        all_signals.append(signal)

    for signal in detect_structuring(transactions):
        signal["account_id"] = account_id
        all_signals.append(signal)

    # =========================
    # OUTPUT: SIGNALS
    # =========================
    print("\n=== DETECTED RISK SIGNALS ===")
    for s in all_signals:
        print(s)

    # =========================
    # RISK SCORING
    # =========================
    risk_score, contributing_factors = calculate_risk_score(all_signals)
    priority = assign_priority(risk_score)

    print("\n=== RISK ASSESSMENT ===")
    print(f"Total Risk Score : {risk_score}")
    print(f"Priority Level  : {priority}")

    print("\n=== CONTRIBUTING FACTORS ===")
    for factor in contributing_factors:
        print(factor)

    # =========================
    # ALERTING & CASE MGMT
    # =========================
    if priority == "HIGH":
        alert = generate_alert(
            account_id=account_profile["account_id"],
            risk_score=risk_score,
            priority=priority,
            signals=all_signals
        )

        case = create_case(alert)

        # Simulate analyst decision
        case = review_case(case, decision="UNDER_REVIEW")

        print("\n=== ALERT GENERATED ===")
        print(alert)

        print("\n=== CASE CREATED ===")
        print(case)

    # =========================
    # COMPLIANCE & REPORTING
    # =========================
    technical_report = generate_technical_report(
        account_id=account_profile["account_id"],
        signals=all_signals,
        risk_score=risk_score,
        priority=priority
    )

    executive_report = generate_executive_report(
        account_id=account_profile["account_id"],
        risk_score=risk_score,
        priority=priority
    )

    aml_alignment = map_to_aml_principles(all_signals)

    print("\n=== TECHNICAL INVESTIGATION REPORT ===")
    print(technical_report)

    print("\n=== EXECUTIVE SUMMARY REPORT ===")
    print(executive_report)

    print("\n=== AML PRINCIPLE ALIGNMENT ===")
    for item in aml_alignment:
        print("-", item)


if __name__ == "__main__":
    run_detection()
