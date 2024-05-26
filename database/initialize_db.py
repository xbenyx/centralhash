import logging
from sqlalchemy import text

logger = logging.getLogger(__name__)

def load_schema(engine, schema_file):
    """
    Load the database schema from a file.
    """
    try:
        with engine.connect() as connection:
            logger.info("Connection to the database established.")
            connection.execute(text(schema_file))
    except FileNotFoundError as e:
        logger.error(f"Schema file not found: {e}")
    except PermissionError as e:
        logger.error(f"Permission denied while accessing schema file: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
