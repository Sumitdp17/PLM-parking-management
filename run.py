# run.py
import os
import sys
from flask import Flask, jsonify
from config import Config, init_app, get_tls_context
from app.routes.validate import validate_bp

# Ensure project imports work
sys.path.append(os.path.abspath(os.path.dirname(__file__)))


def create_app():
    """Initialize and configure the Flask app."""
    app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

    # Apply configuration settings
    init_app(app)

    # --- Import routes ---
    from app.routes.auth import auth_bp
    from app.routes.entry import entry_bp
    from app.routes.exit import exit_bp
    from app.routes.dashboard import dashboard_bp
    from app.routes.maintenance import maintenance_bp

    # ✅ NEW Sprint-2 module
    from app.routes.payment import payment_bp

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(entry_bp, url_prefix="/entry")
    app.register_blueprint(exit_bp, url_prefix="/exit")
    app.register_blueprint(dashboard_bp, url_prefix="/dashboard")
    app.register_blueprint(validate_bp, url_prefix="/")
    app.register_blueprint(maintenance_bp, url_prefix="/")

    # ✅ Register Sprint-2 payment blueprint
    app.register_blueprint(payment_bp, url_prefix="/payment")

    @app.route("/")
    def index():
        return jsonify({
            "status": "ok",
            "app": Config.APP_NAME,
            "message": "🚗 Smart Parking Management System running successfully!"
        })

    return app


if __name__ == "__main__":
    app = create_app()
    tls_context = get_tls_context()

    # If TLS is configured and available, start HTTPS
    if tls_context:
        print("🔒 Running with HTTPS enabled...")
        app.run(host="0.0.0.0", port=5000, ssl_context=tls_context, debug=(Config.FLASK_ENV == "development"))
    else:
        print("🌐 Running in HTTP mode...")
        app.run(host="0.0.0.0", debug=(Config.FLASK_ENV == "development"))
