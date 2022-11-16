# flask-how-to-architect-the-project-with-multiple-apps
# 참고
# 1) https://stackoverflow.com/questions/15583671/flask-how-to-architect-the-project-with-multiple-apps
# 2) https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications

from flask import Flask, render_template, request
from apps.user import user
from apps.user_squad import squad
from apps.user_hero import hero
from apps.match import match

# 1) Create App
app = Flask(__name__, static_url_path='/static')

# 2) Configurations
# app.config.from_object('settings')
print( "config = ", app.config )

# 3) Register blueprint(s)
app.register_blueprint(user, url_prefix = "/api/v1/user")
app.register_blueprint(hero, url_prefix = "/api/v1/user/<int:user_id>/hero")
app.register_blueprint(squad, url_prefix = "/api/v1/user/<int:user_id>/squad")
app.register_blueprint(match, url_prefix = "/api/v1/match")

# 4) Build the database:
# This will create the database file using SQLAlchemy
# db.create_all()

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    app.logger.error('Page Not Found: %s', (request.path))
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error('Server Error: %s', (error))
    return render_template('500.html'), 500


@app.errorhandler(Exception)
def unhandled_exception(error):
    app.logger.error('Unhandled Exception: %s', (error))
    return render_template('500.htm'), 500

@app.route('/', methods=['GET'])
def index():
    return "this is test"
#     return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
