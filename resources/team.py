from flask_restful import Resource, reqparse, abort
from flasgger import swag_from

class TeamListResource(Resource):
    def __init__(self, teams):
        self.teams = teams
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str, required=True, help='Team name is required')
        self.parser.add_argument('city', type=str, required=True, help='Team city is required')

    @swag_from({
        'responses': {
            200: {
                'description': 'List of all teams',
                'content': {
                    'application/json': {
                        'examples': {
                            'example1': {
                                'summary': 'Sample team list',
                                'value': [
                                    {'id': 1, 'name': 'FC Barcelona', 'city': 'Barcelona'},
                                    {'id': 2, 'name': 'Real Madrid', 'city': 'Madrid'}
                                ]
                            }
                        }
                    }
                }
            }
        }
    })
    def get(self):
        """Get a list of all teams"""
        return {'teams': self.teams}, 200

    @swag_from({
        'parameters': [
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'name': {'type': 'string', 'example': 'FC Barcelona'},
                        'city': {'type': 'string', 'example': 'Barcelona'}
                    },
                    'required': ['name', 'city']
                }
            }
        ],
        'responses': {
            201: {
                'description': 'Team created successfully',
                'content': {
                    'application/json': {
                        'examples': {
                            'example1': {
                                'summary': 'Created team',
                                'value': {'id': 1, 'name': 'FC Barcelona', 'city': 'Barcelona'}
                            }
                        }
                    }
                }
            },
            400: {'description': 'Invalid input'}
        }
    })
    def post(self):
        """Create a new team"""
        args = self.parser.parse_args()
        team_id = len(self.teams) + 1
        team = {'id': team_id, 'name': args['name'], 'city': args['city']}
        self.teams.append(team)
        return team, 201

class TeamResource(Resource):
    def __init__(self, teams):
        self.teams = teams
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str, required=False)
        self.parser.add_argument('city', type=str, required=False)

    @swag_from({
        'parameters': [
            {
                'name': 'team_id',
                'in': 'path',
                'type': 'integer',
                'required': True,
                'description': 'ID of the team to retrieve'
            }
        ],
        'responses': {
            200: {
                'description': 'Team details',
                'content': {
                    'application/json': {
                        'examples': {
                            'example1': {
                                'summary': 'Sample team',
                                'value': {'id': 1, 'name': 'FC Barcelona', 'city': 'Barcelona'}
                            }
                        }
                    }
                }
            },
            404: {'description': 'Team not found'}
        }
    })
    def get(self, team_id):
        """Get a specific team by ID"""
        team = next((t for t in self.teams if t['id'] == team_id), None)
        if not team:
            abort(404, message='Team not found')
        return team, 200

    @swag_from({
        'parameters': [
            {
                'name': 'team_id',
                'in': 'path',
                'type': 'integer',
                'required': True,
                'description': 'ID of the team to update'
            },
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'name': {'type': 'string', 'example': 'FC Barcelona'},
                        'city': {'type': 'string', 'example': 'Barcelona'}
                    }
                }
            }
        ],
        'responses': {
            200: {'description': 'Team updated successfully'},
            404: {'description': 'Team not found'},
            400: {'description': 'Invalid input'}
        }
    })
    def put(self, team_id):
        """Update a team's details"""
        args = self.parser.parse_args()
        team = next((t for t in self.teams if t['id'] == team_id), None)
        if not team:
            abort(404, message='Team not found')
        if args['name']:
            team['name'] = args['name']
        if args['city']:
            team['city'] = args['city']
        return team, 200

    @swag_from({
        'parameters': [
            {
                'name': 'team_id',
                'in': 'path',
                'type': 'integer',
                'required': True,
                'description': 'ID of the team to delete'
            }
        ],
        'responses': {
            204: {'description': 'Team deleted successfully'},
            404: {'description': 'Team not found'}
        }
    })
    def delete(self, team_id):
        """Delete a team"""
        team = next((t for t in self.teams if t['id'] == team_id), None)
        if not team:
            abort(404, message='Team not found')
        self.teams.remove(team)
        return '', 204