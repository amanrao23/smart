from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from  flask_bootstrap import Bootstrap


db=SQLAlchemy()
bootstrap=Bootstrap()
login_manager=LoginManager()
login_manager.login_view = 'control.logincontrol'

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from app.control.routes import control
    from app.ngo.routes import ngo
    from app.main.routes import main

    app.register_blueprint(control)
    app.register_blueprint(ngo)
    app.register_blueprint(main)

    return app