from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

# Added serverSelectionTimeoutMS for better fail-fast on Render
client = AsyncIOMotorClient(
    settings.MONGODB_URL,
    serverSelectionTimeoutMS=5000,
    connectTimeoutMS=10000,
    tlsAllowInvalidCertificates=True # Temporary to debug SSL Handshake on Render
)
db = client.get_database()
