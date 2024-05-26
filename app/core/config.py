from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Application settings.
    """
    DATABASE_TYPE: int
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_NAME: str
    DATABASE_HOST: str

    MYSQL_DATABASE_URL: str
    POSTGRES_DATABASE_URL: str
    MSSQL_DATABASE_URL: str

    HOST: str
    PORT: int

    PROMETHEUS_PORT: int
    GRAFANA_PORT: int

    @property
    def DATABASE_URL(self) -> str:
        if self.DATABASE_TYPE == 0:
            return self.MYSQL_DATABASE_URL
        elif self.DATABASE_TYPE == 1:
            return self.MSSQL_DATABASE_URL
        elif self.DATABASE_TYPE == 2:
            return self.POSTGRES_DATABASE_URL
        else:
            raise ValueError("Invalid DATABASE_TYPE specified.")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
