import os
from dotenv import load_dotenv

print("📂 Current Directory:", os.getcwd())

if load_dotenv():
    print("✅ .env file loaded")
else:
    print("❌ .env file not found")

print("🔑 API Key:", os.getenv("UMICO_API_KEY"))
