from flask import (Flask, render_template)
import connexion


# create the application instance
app = connexion.App(__name__, specification_dir='./')


# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')


# create a url route in our application for "/"
@app.route("/")
def home():
    """
    the function just respond to the browser ULR
    locolhost:5050/
    :return: the rendered template "home.html"
    """
    return render_template("home.html")


# if we"re running in stand alone mode, run the application
if __name__ == "__main__":
    app.run(debug=True)

