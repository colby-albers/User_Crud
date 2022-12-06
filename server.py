from flask_app import app
from flask_app.models.users_model import User
from flask_app.controllers import user_crud_controller



if __name__=="__main__":
    app.run(debug=True,)