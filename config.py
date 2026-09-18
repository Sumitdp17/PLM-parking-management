import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


class Config:
    """Base configuration class for the Flask app."""

    # ===== Flask Core Settings =====
    SECRET_KEY = os.getenv("SECRET_KEY", "defaultsecret")
    FLASK_ENV = os.getenv("FLASK_ENV", "production")

    # ===== Application Metadata =====
    APP_NAME = os.getenv("APP_NAME", "Smart Parking Management System")
    TOTAL_SLOTS = int(os.getenv("TOTAL_SLOTS", 10))

    # ===== Security & TLS =====
    USE_TLS = os.getenv("USE_TLS", "False").lower() == "true"
    CERT_PATH = os.getenv("CERT_PATH", "certs/server.crt")
    KEY_PATH = os.getenv("KEY_PATH", "certs/server.key")

    # ===== Logging =====
    LOG_FILE = os.getenv("LOG_FILE", "data/admin_logs.json")

    # ===== Mock Payment Settings =====
    PAYMENT_GATEWAY_MODE = os.getenv("PAYMENT_GATEWAY_MODE", "test")
    DEFAULT_RATE_PER_HOUR = float(os.getenv("DEFAULT_RATE_PER_HOUR", 10))

    # ===== Admin Credentials =====
    ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")


def init_app(app):
    """
    Apply configuration to the Flask app.
    This function is called inside app/__init__.py
    """
    app.config.from_object(Config)

    # Log startup info for verification
    print(f"\n🚗 {Config.APP_NAME} Starting...")
    print(f"Environment : {Config.FLASK_ENV}")
    print(f"TLS Enabled : {Config.USE_TLS}")
    print(f"Total Slots : {Config.TOTAL_SLOTS}")
    print(f"Payment Mode: {Config.PAYMENT_GATEWAY_MODE}\n")

    return app


def get_tls_context():
    """
    Returns SSL context if TLS is enabled, else None.
    Used in run.py to start HTTPS server.
    """
    if Config.USE_TLS and os.path.exists(Config.CERT_PATH) and os.path.exists(Config.KEY_PATH):
        return (Config.CERT_PATH, Config.KEY_PATH)
    return None
