import logging
import logging.config
import os
from jinja2 import Environment, FileSystemLoader, TemplateNotFound
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.errors import ServerErrorMiddleware
from starlette_exporter import PrometheusMiddleware, handle_metrics
from app.core.database import create_database_engine
from app.core.config import settings
from database.initialize_db import load_schema
from app.api.v1.endpoints.router import api_router
from app.errors.handlers import http_exception_handler, validation_exception_handler

def create_app():
    app = FastAPI(
        title="Central Hash API",
        description="This API provides a central hash management",
        version="1.0.0",
        docs_url="/docs",  # Swagger UI
        redoc_url="/redoc"  # ReDoc
    )

    # Set up logging
    logging.config.fileConfig('app/logging.conf', disable_existing_loggers=False)
    logger = logging.getLogger(__name__)

    # Include middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
    app.add_middleware(ServerErrorMiddleware)
    app.add_middleware(PrometheusMiddleware)
    app.add_route("/metrics", handle_metrics)

    # Add exception handlers
    app.add_exception_handler(StarletteHTTPException, http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)

    # Initialize database
    db_engine = create_database_engine()

    # Load schema SQL template
    template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'database')
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template('schema.sql')

    # Render template with database type
    rendered_sql = template.render(DATABASE_TYPE=settings.DATABASE_TYPE)

    try:
        # logger.info(f"Render SQL: {db_engine} {rendered_sql}")
        load_schema(db_engine, rendered_sql)
        logger.info("Database initialized successfully.")
    except Exception as e:
        logger.error(f"Failed to initialize database: {e}")

    # Include API router
    app.include_router(api_router, prefix="/api/v1")

    return app

app = create_app()
