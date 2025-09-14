from flask import Flask
from flask_login import LoginManager
from models import db, User
from routes import main_bp

import sys

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

# 初始化数据库
db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = "main.login"


@login_manager.user_loader
def load_user(user_id):
    # return User.query.get(int(user_id))
    return db.session.get(User, int(user_id))


# 注册蓝图
app.register_blueprint(main_bp)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)