from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class PostgresConfig(BaseModel):
    driver: str
    user: str
    password: str
    host: str
    port: str
    db: str

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


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="../../.env",
        env_prefix="APP_",
        case_sensitive=False,
        env_nested_delimiter="__",
        extra="ignore",
    )

    postgres: PostgresConfig
    mongodb: MongoDBConfig


config = Config()
