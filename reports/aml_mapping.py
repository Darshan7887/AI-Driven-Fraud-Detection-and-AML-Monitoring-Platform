"""
This module conceptually maps detected behaviors
to common AML monitoring principles.
"""


def map_to_aml_principles(signals):
    """
    Maps signals to high-level AML concepts.
    """

    aml_flags = set()

    for signal in signals:
        if signal["signal_type"] in ["VELOCITY_SPIKE", "STRUCTURING"]:
            aml_flags.add("Suspicious Transaction Monitoring")

        if signal["signal_type"] == "GEO_ANOMALY":
            aml_flags.add("Geographic Risk Assessment")

        if signal["signal_type"] == "AMOUNT_ANOMALY":
            aml_flags.add("Unusual Transaction Pattern")

        if signal["signal_type"] == "BEHAVIOR_DRIFT":
            aml_flags.add("Customer Behavior Monitoring")

    return list(aml_flags)






