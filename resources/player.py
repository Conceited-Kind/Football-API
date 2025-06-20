from flask_restful import Resource, reqparse, abort
from flasgger import swag_from

class PlayerListResource(Resource):
    def __init__(self, players):
        self.players = players
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str, required=True, help='Player name is required')
        self.parser.add_argument('position', type=str, required=True, help='Player position is required')
        self.parser.add_argument('team_id', type=int, required=False, help='Team ID (optional)')

    @swag_from({
        'responses': {
            200: {
                'description': 'List of all players',
                'content': {
                    'application/json': {
                        'examples': {
                            'example1': {
                                'summary': 'Sample player list',
                                'value': [
                                    {'id': 1, 'name': 'Lionel Messi', 'position': 'Forward', 'team_id': 1},
                                    {'id': 2, 'name': 'Cristiano Ronaldo', 'position': 'Forward', 'team_id': 2}
                                ]
                            }
                        }
                    }
                }
            }
        }
    })
    def get(self):
        """Get a list of all players"""
        return {'players': self.players}, 200

    @swag_from({
        'parameters': [
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'name': {'type': 'string', 'example': 'Lionel Messi'},
                        'position': {'type': 'string', 'example': 'Forward'},
                        'team_id': {'type': 'integer', 'example': 1}
                    },
                    'required': ['name', 'position']
                }
            }
        ],
        'responses': {
            201: {
                'description': 'Player created successfully',
                'content': {
                    'application/json': {
                        'examples': {
                            'example1': {
                                'summary': 'Created player',
                                'value': {'id': 1, 'name': 'Lionel Messi', 'position': 'Forward', 'team_id': 1}
                            }
                        }
                    }
                }
            },
            400: {'description': 'Invalid input'}
        }
    })
    def post(self):
        """Create a new player"""
        args = self.parser.parse_args()
        player_id = len(self.players) + 1
        player = {'id': player_id, 'name': args['name'], 'position': args['position'], 'team_id': args['team_id']}
        self.players.append(player)
        return player, 201

class PlayerResource(Resource):
    def __init__(self, players):
        self.players = players
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str, required=False)
        self.parser.add_argument('position', type=str, required=False)
        self.parser.add_argument('team_id', type=int, required=False)

    @swag_from({
        'parameters': [
            {
                'name': 'player_id',
                'in': 'path',
                'type': 'integer',
                'required': True,
                'description': 'ID of the player to retrieve'
            }
        ],
        'responses': {
            200: {
                'description': 'Player details',
                'content': {
                    'application/json': {
                        'examples': {
                            'example1': {
                                'summary': 'Sample player',
                                'value': {'id': 1, 'name': 'Lionel Messi', 'position': 'Forward', 'team_id': 1}
                            }
                        }
                    }
                }
            },
            404: {'description': 'Player not found'}
        }
    })
    def get(self, player_id):
        """Get a specific player by ID"""
        player = next((p for p in self.players if p['id'] == player_id), None)
        if not player:
            abort(404, message='Player not found')
        return player, 200

    @swag_from({
        'parameters': [
            {
                'name': 'player_id',
                'in': 'path',
                'type': 'integer',
                'required': True,
                'description': 'ID of the player to update'
            },
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'name': {'type': 'string', 'example': 'Lionel Messi'},
                        'position': {'type': 'string', 'example': 'Forward'},
                        'team_id': {'type': 'integer', 'example': 1}
                    }
                }
            }
        ],
        'responses': {
            200: {'description': 'Player updated successfully'},
            404: {'description': 'Player not found'},
            400: {'description': 'Invalid input'}
        }
    })
    def put(self, player_id):
        """Update a player's details"""
        args = self.parser.parse_args()
        player = next((p for p in self.players if p['id'] == player_id), None)
        if not player:
            abort(404, message='Player not found')
        if args['name']:
            player['name'] = args['name']
        if args['position']:
            player['position'] = args['position']
        if args['team_id'] is not None:
            player['team_id'] = args['team_id']
        return player, 200

    @swag_from({
        'parameters': [
            {
                'name': 'player_id',
                'in': 'path',
                'type': 'integer',
                'required': True,
                'description': 'ID of the player to delete'
            }
        ],
        'responses': {
            204: {'description': 'Player deleted successfully'},
            404: {'description': 'Player not found'}
        }
    })
    def delete(self, player_id):
        """Delete a player"""
        player = next((p for p in self.players if p['id'] == player_id), None)
        if not player:
            abort(404, message='Player not found')
        self.players.remove(player)
        return '', 204