from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent.parent


class PostgresConfig(BaseModel):
    driver: str
    user: str
    password: str
    host: str
    port: str
    db: str
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }

    @property
    def uri(self) -> str:
        return "{}://{}:{}@{}:{}/{}".format(
            self.driver,
            self.user,
            self.password,
            self.host,
            self.port,
            self.db,
        )


class MongoDBConfig(BaseModel):
    driver: str
    host: str
    port: str
    db: str

    @property
    def uri(self) -> str:
        return "{}://{}:{}".format(self.driver, self.host, self.port)


class DatabaseConfig(BaseModel):
    postgres: PostgresConfig
    mongo: MongoDBConfig


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=f"{BASE_DIR}/.env",
        env_prefix="APP_",
        case_sensitive=False,
        env_nested_delimiter="__",
        extra="ignore",
    )

    db: DatabaseConfig


config = Config()

if __name__ == "__main__":
    print(BASE_DIR)
