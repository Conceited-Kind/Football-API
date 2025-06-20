from flask import Flask
from flask_restful import Api
from flasgger import Swagger
from resources.player import PlayerResource, PlayerListResource
from resources.team import TeamResource, TeamListResource

app = Flask(__name__)
api = Api(app)

# Configure Swagger
app.config['SWAGGER'] = {
    'title': 'Football API',
    'uiversion': 3,
    'description': 'A RESTful API for managing football players and teams',
    'version': '1.0.0'
}
swagger = Swagger(app)

# In-memory data stores
players = []
teams = []

# Register API resources with data stores
api.add_resource(PlayerListResource, '/players', resource_class_kwargs={'players': players})
api.add_resource(PlayerResource, '/players/<int:player_id>', resource_class_kwargs={'players': players})
api.add_resource(TeamListResource, '/teams', resource_class_kwargs={'teams': teams})
api.add_resource(TeamResource, '/teams/<int:team_id>', resource_class_kwargs={'teams': teams})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)