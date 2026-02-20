from loguru import logger
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

from core.settings import settings


class MongoDatabseConnector:
    _instance: MongoClient | None = None

    def __new__(cls, *args, **kwargs) -> MongoClient:
        if not cls._instance:
            try:
                cls._instance = MongoClient(settings.DATABASE_HOST)
            except ConnectionFailure as e:
                logger.error(f"Couldn't connect to the database: {e!s}")
                raise
        logger.info(
            "connection to MongoDB with URI successful: {settings.DATABASE_HOST}"
        )

        return cls._instance


connection = MongoDatabseConnector()
