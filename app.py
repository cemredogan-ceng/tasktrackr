from flask import Flask
from config import Config
from db import db, jwt


from routes.auth_routes import auth_bp
from routes.task_routes import task_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(task_bp, url_prefix="/api/tasks")

    @app.route("/")
    def home():
        return "🎯 TaskTrackr Backend Running!"

    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    print("💡 Flask server başlatılıyor...")
    app.run(debug=True)



