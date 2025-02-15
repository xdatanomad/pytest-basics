import logging
import json
from pydantic import BaseModel, Field, field_validator
from datetime import datetime
import traceback

# List of known logging field names
KNOWN_LOGGING_FIELDS = {
    'name', 'msg', 'args', 'levelname', 'levelno', 'pathname', 'filename',
    'module', 'exc_info', 'exc_text', 'stack_info', 'lineno', 'funcName',
    'created', 'msecs', 'relativeCreated', 'thread', 'threadName', 'processName', 
    'process', 'taskName',
}


class JsonFormatter(BaseModel, logging.Formatter):
    datefmt: str = Field(default="%Y-%m-%dT%H:%M:%S", alias="date_format")


    @field_validator("datefmt", mode="before")
    @classmethod
    def validate_date_format(cls, value):
        if not value:
            return "%Y-%m-%dT%H:%M:%S"
        else:
            # Check if the value is a valid date format
            datetime.now().strftime(value)
        return value

    def get_additional_fields(self, record):
        return {key: value for key, value in record.items() if key not in KNOWN_LOGGING_FIELDS}

    def format(self, record):
        log_record = {
            "timestamp": self.formatTime(record, self.datefmt) + f" {round(record.msecs):03d}",
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "funcName": record.funcName,
            "lineno": record.lineno,
            # "user_id": getattr(record, "user_id", None),
        }
        # Get additional fields from the extra attribute
        extra_fields = self.get_additional_fields(record.__dict__)
        log_record.update(extra_fields)
        # Check if exception info is present
        if record.exc_info:
            log_record["exception"] = self.formatException(record.exc_info)
            # Add the entire stack trace
            log_record["stack_trace"] = traceback.format_exc()

        return json.dumps(log_record)

    

logger = logging.getLogger("main")
handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter(datefmt=r"%Y-%m-%d %H:%M:%S"))
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

# Example usage
logger.info("User login successful", extra={"user_id": "12345", "request_id": "xyz789"})
logger.debug("User login successful", extra={"user_id": "12345", "request_id": "xyz789"})
