"""Streamlit viewer that filters logs.log with real logging.Filter objects.

Run with: streamlit run log_viewer.py
"""

import logging
import re
from pathlib import Path

import streamlit as st

LEVEL_NAMES = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
# Matches the "standard" formatter in logging_config.json.
LINE_PATTERN = re.compile(
    r"^(?P<asctime>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) \| "
    r"(?P<levelname>\w+)\s* \| (?P<name>\S+) \| (?P<msg>.*)$"
)


def parse_log_records(log_text: str) -> list[logging.LogRecord]:
    level_numbers = logging.getLevelNamesMapping()
    records = []
    for line in log_text.splitlines():
        match = LINE_PATTERN.match(line)
        if match:
            fields = match.groupdict()
            fields["levelno"] = level_numbers[fields["levelname"]]
            records.append(logging.makeLogRecord(fields))
        elif records:
            # Tracebacks span several lines that belong to the record above them.
            records[-1].msg += f"\n{line}"
    return records


def build_filterer(
    levels: list[str], logger_name: str, message_substring: str
) -> logging.Filterer:
    """Filterer is the base class of Logger and Handler, so this runs filters exactly as logging does."""
    filterer = logging.Filterer()
    filterer.addFilter(lambda record: record.levelname in levels)
    # Passes logger_name and its children ("app.db" -> "app.db.query"), but not "app.dbx". Empty passes all.
    filterer.addFilter(logging.Filter(logger_name))
    if message_substring:
        filterer.addFilter(lambda record: message_substring in record.getMessage())
    return filterer


def main() -> None:
    st.title("Log viewer")

    log_path = Path(st.text_input("Log file", value="logs.log"))
    try:
        log_text = log_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        st.error(f"No log file at {log_path.resolve()}. Run generate_logs.py first.")
        st.stop()

    records = parse_log_records(log_text)

    with st.sidebar:
        st.header("Filters")
        levels = st.multiselect("Levels", LEVEL_NAMES, default=LEVEL_NAMES)
        logger_name = st.text_input("logging.Filter(name)", placeholder="app.db")
        message_substring = st.text_input("Message contains")

    filterer = build_filterer(levels, logger_name, message_substring)
    kept_records = [record for record in records if filterer.filter(record)]

    level_columns = st.columns(len(LEVEL_NAMES))
    for column, level_name in zip(level_columns, LEVEL_NAMES):
        kept_count = sum(record.levelname == level_name for record in kept_records)
        total_count = sum(record.levelname == level_name for record in records)
        column.metric(level_name, f"{kept_count}/{total_count}")

    st.dataframe(
        [
            {
                "time": record.asctime,
                "level": record.levelname,
                "logger": record.name,
                "message": record.getMessage(),
            }
            for record in kept_records
        ],
        width="stretch",
    )


if __name__ == "__main__":
    main()
