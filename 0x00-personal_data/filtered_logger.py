#!/usr/bin/env python3
"""function filter_datum"""
import re


def filter_datum(fields : str,
                redaction : str,
                message : str,
                separator : str):
    """ returns the log message obfuscated"""
    pattern = r"(?i)\b(" + "|".join(fields) + r")\b"
    return re.sub(pattern, redaction, message)
