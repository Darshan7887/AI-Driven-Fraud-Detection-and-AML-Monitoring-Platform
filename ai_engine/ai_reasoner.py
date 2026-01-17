from ai_engine.alert_grouping import group_signals_by_account
from ai_engine.summarizer import (
    generate_signal_explanations,
    generate_analyst_summary,
    generate_executive_summary
)

def run_ai_reasoning(signals, risk_score, priority):
    """
    Orchestrates AI-style explanations.
    """

    grouped_cases = group_signals_by_account(signals)

    for account_id, account_signals in grouped_cases.items():
        explanations = generate_signal_explanations(account_signals)

        analyst_view = generate_analyst_summary(explanations)
        executive_view = generate_executive_summary(risk_score, priority)

        print("\n=== AI EXPLANATION ENGINE ===")
        print(f"Account ID: {account_id}\n")

        print("--- Analyst Summary ---")
        print(analyst_view)

        print("--- Executive Summary ---")
        print(executive_view)
