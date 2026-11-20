"""Load logging_config.json and write sample records so the viewer has something to parse."""

import json
import logging
import logging.config
from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "logging_config.json"


def configure_logging(config_path: Path) -> None:
    logging.config.dictConfig(json.loads(config_path.read_text()))


def emit_sample_logs() -> None:
    app_logger = logging.getLogger("app")
    db_logger = logging.getLogger("app.db")
    query_logger = logging.getLogger("app.db.query")
    # "app.dbx" shares a prefix with "app.db" but is not its child, so logging.Filter("app.db") rejects it.
    dbx_logger = logging.getLogger("app.dbx")
    api_logger = logging.getLogger("app.api")

    app_logger.info("Starting up")
    db_logger.debug("Opening connection pool with 4 connections")
    query_logger.debug("SELECT * FROM users WHERE id = 42")
    dbx_logger.info("Unrelated subsystem that only looks like app.db")
    api_logger.warning("Slow response from /users: 1.8s")
    try:
        int("A string that cannot be cast to an int")
    except ValueError:
        api_logger.exception("Failed to parse latency header")
    db_logger.critical("Connection pool exhausted")
    app_logger.info("Shutting down")


if __name__ == "__main__":
    configure_logging(CONFIG_PATH)
    emit_sample_logs()
