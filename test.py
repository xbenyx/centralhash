from sqlalchemy import create_engine, text
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_connection():
    # Database connection string
    DATABASE_USER = 'root'
    DATABASE_PASSWORD = 'Emyvale12'
    DATABASE_HOST = 'localhost'
    DATABASE_NAME = 'test2'

    # Create the database URL
    database_url = f"mysql+mysqlconnector://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"

    # Create the engine
    engine = create_engine(database_url)

    # Test the connection
    try:
        with engine.connect() as connection:
            logger.info("Connection to the database established.")
            result = connection.execute(text("SELECT 1"))
            for row in result:
                logger.info(f"Query result: {row}")
    except Exception as e:
        logger.error(f"Failed to connect to the database: {e}")

if __name__ == "__main__":
    test_connection()
