import os

from flask import Flask

# Instead of creating a Flask instance globally, you will create it inside a function. 
# This function is known as the application factory. Any configuration, registration, and 
# other setup the application needs will happen inside the function, then the application will be returned.

# The Application Factory - Create the flaskr directory and add the __init__.py file. 
# The __init__.py serves double duty: it will contain the application factory, and 
# it tells Python that the flaskr directory should be treated as a package.

def create_app(test_config=None):
    # create the app
    app = Flask(__name__, instance_relative_config=True)


    # sets some default configuration to the app
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config:
        # load the test_config, if passed in
        app.config.from_mapping(test_config)
    else:
        # overrides the default configuration, 
        # loads the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
 
    # ensure the instance folder - app.instance_path exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route("/hello")
    def hello():
        return 'Hello, World!'




    from . import db
    db.init_app(app)

    # Import and register the blueprint from the factory
    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    
    return app

# from  the top-level flask-tutorial directory, not the flaskr package.
# run   $ flask --app flaskr run --debug
# Visit http://127.0.0.1:5000/hello in a browser
