#!/usr/bin/env python3
"""
Write a function called filter_datum that returns the log message obfuscated
"""
import logging
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Arguments:
    fields: list of strings representing fields to obfuscate
    redaction: string representing by what field will be obfuscated
    message: string represented by log line
    separator: string represented by which character is separating fields

    Function uses a regex to replace occurences of certain field values
    Function uses re.sub to perform substitution with single regex
    """
    for field in fields:
        regexStr = f"(?<={field}=).*?(?={separator})"
        message = re.sub(regexStr, redaction, message)
    return message
