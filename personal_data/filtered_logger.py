#!/usr/bin/env python3
"""
Write a function called filter_datum that returns the log message obfuscated
"""
import logging
import re
from typing import List


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialization"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = list(fields)

    def format(self, record: logging.LogRecord) -> str:
        """Filters values in incoming log records using filter_datum"""
        msg = super().format(record)
        return filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
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


def get_logger() -> logging.Logger:
    """
    user_data: logs up to logging.INFO level, has a StreamHandler
    with RedactingFormatter as formatter
    PII_FIELDS: tuple constant at root of module with fields from csv file,
    only contains 5 fields that are considered important PII
    """
    user_data = logging.getLogger("user_data")
    user_data.setLevel(logging.INFO)
    user_data.propagate = False

    stream = logging.StreamHandler()
    stream.setFormatter(RedactingFormatter(PII_FIELDS))

    user_data.addHandler(stream)
    return user_data
