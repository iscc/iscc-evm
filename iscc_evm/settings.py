"""App Settings."""
from pydantic import BaseSettings


class Settings(BaseSettings):
    ipfs_address: str = "/ip4/127.0.0.1/tcp/5001/http"
    web3_address: str = "http://127.0.0.1:7545"
    hub_address: str = ""
    registrar_address: str = ""

    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"


settings = Settings()
