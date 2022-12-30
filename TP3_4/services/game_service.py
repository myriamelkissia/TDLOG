from dao.game_dao import *
from model.frigate import Frigate
from model.game import Game
from model.battlefield import Battlefield
from model.cruiser import Cruiser
from model.destroyer import Destroyer
from model.player import Player
from model.aircraft import Aircraft
from model.submarine import Submarine

class GameService:
    def __init__(self):
        self.game_dao = GameDao()

    def create_game(self, player_name: str, min_x: int, max_x: int, min_y: int,max_y: int, min_z: int, max_z: int) -> int:
        game = Game()
        battle_field = Battlefield(min_x, max_x, min_y, max_y, min_z, max_z)
        game.add_player(Player(player_name, battle_field))
        return self.game_dao.create_game(game)

    def join_game(self, game_id: int, player_name: str) -> bool:
        game=self.game_dao.find_game(game_id)
        player=Player(name=player_name)
        return game.add_player(player)

    def get_game(self, game_id: int) -> Game:
        return self.game_dao.find_game(game_id)

    def add_vessel(self, game_id: int, player_name: str, vessel_type: str, x: int, y: int, z: int) -> bool:
        game=GameService.get_game(self,game_id)
        l=[Cruiser,Destroyer,Submarine,Aircraft,Frigate]
        L=["cruiser","destroyer","submarine","aircraft","frigate"]
        for i in range(len(L)):
            if vessel_type.lower()==L[i]:
                ves_type=l[i]
        for e in range(len(game.players)):
            if game.players[e].name==player_name:
                vesselentity=map_to_vessel_entity(game.players[e].battle_field.id,ves_type(x,y,z))
                self.game_dao.db_session.add(vesselentity)
                game.players[e].battle_field.add_vessel(ves_type(x,y,z))
                return True
        else:
            return False

    def shoot_at(self, game_id: int, shooter_name: str, vessel_id: int, x: int, y: int, z: int) -> bool:
        game = self.get_game(game_id)
        vessel = self.game_dao.find_vessel(vessel_id)
        players = game.get_players()
        players_in_the_game=[]
        for i in range(len(players)):
            players_in_the_game.append(players[i].name)
        for k in range(len(players)):
            if players[k].name == shooter_name:
                for vessel in players[k].battle_field.vessels :
                    if vessel.id == vessel_id:
                        vessel.fire_at(x,y,z)
                        vessel_entity = map_to_vessel_entity(game.players[k].battlefield.id,vessel)
                        self.game_dao.db_session.add(vessel_entity)
            elif players[k].name != shooter_name and shooter_name in players_in_the_game:
                for vessel in players[k].battle_field.vessels :
                    if vessel.get_coordinates()==(x,y,z):
                        vessel_entity = map_to_vessel_entity(game.players[k].battlefield.id,vessel(x,y,z))
                        self.game_dao.db_session.add(vessel_entity)
                        return True
        return  False

    def get_game_status(self, game_id: int, shooter_name: str) -> str:
        game = self.get_game(game_id)
        player = Player(name=shooter_name)
        players = game.get_players
        if player in players :
            players.remove(player)
            player_2=players[0]
            if player.battle_field.get_power()==0:
                return "Perdu"
            elif player_2.battle_field.get_power()==0:
                return "Gagne"
            else :
                return "En cours"