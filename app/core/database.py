from sqlalchemy import create_engine, exc
from sqlalchemy.ext.asyncio import create_async_engine
from app.core.config import settings

def create_database_engine():
    """
    Create a database engine based on the configured database URL.
    """
    database_urls = [
        f"mysql+mysqlconnector://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}/{settings.DATABASE_NAME}",
        f"mssql+pyodbc://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}/{settings.DATABASE_NAME}",
        f"postgresql+psycopg2://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}/{settings.DATABASE_NAME}"
    ]

    if settings.DATABASE_TYPE in [0, 1, 2]:
        try:
            engine = create_engine(database_urls[settings.DATABASE_TYPE])
            # Test the connection
            with engine.connect():
                pass  # Connection successful
            return engine
        except exc.SQLAlchemyError as e:
            raise ValueError(f"Failed to connect to the database: {e}")
    else:
        raise ValueError("Unsupported database type. Use 0 for MySQL, 1 for MSSQL, or 2 for PostgreSQL.")

def create_async_database_engine():
    """
    Create an asynchronous database engine based on the configured database URL.
    """
    database_urls = [
        f"mysql+mysqlconnector://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}/{settings.DATABASE_NAME}",
        f"mssql+pyodbc://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}/{settings.DATABASE_NAME}",
        f"postgresql+psycopg2://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}/{settings.DATABASE_NAME}"
    ]

    if settings.DATABASE_TYPE in [0, 1, 2]:
        try:
            engine = create_async_engine(database_urls[settings.DATABASE_TYPE])
            # Test the connection
            with engine.connect():
                pass  # Connection successful
            return engine
        except exc.SQLAlchemyError as e:
            raise ValueError(f"Failed to connect to the database: {e}")
    else:
        raise ValueError("Unsupported database type. Use 0 for MySQL, 1 for MSSQL, or 2 for PostgreSQL.")
