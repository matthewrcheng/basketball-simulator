import random
from .constants import default_color, reset, get_color
from .db import get_team

class Team:
    def __init__(self, id, city = 0, name='Default Team', abbr='DEF', players=None,
                 color=default_color, wins = 0, losses = 0, championships = 0, 
                 stadium = "Default Stadium", conference = "Default Conference",
                 division = "Default Division", budget = 0):
        # team identity
        self.id = id
        self.city = city
        self.name = name
        self.abbr = abbr
        self.color = color
        self.stadium = stadium
        self.conference = conference
        self.division = division

        # financials
        self.budget = budget
        
        # historical stats
        self.championships = championships
        self.playoff_appearances = 0
        self.wins = wins
        self.losses = losses
        self.net_points = 0

        # season stats
        self.season_wins = 0
        self.season_losses = 0
        self.season_net_points = 0

        # game stats
        self.shots = 0
        self.shots2 = 0
        self.shots2_made = 0
        self.shots3 = 0
        self.shots3_made = 0
        self.fouls = 0
        self.quarter_fouls = 0
        self.turnovers = 0
        self.fts = 0
        self.fts_made = 0
        self.blocks = 0
        self.assists = 0
        self.rebounds = 0
        self.steals = 0
        self.points = 0
        self.scoring_trend = []
        self.consecutive_points = 0
        self.most_consecutive_points = 0

        self.active_players = {
            'C': None,
            'PF': None,
            'SF': None,
            'SG': None,
            'PG': None
        }
        if not players:
            self.players = {
                'C': [],
                'PF': [],
                'SF': [],
                'SG': [],
                'PG': []
            }
        else:
            self.players = players
        # self.players = players if players is not None else {
        #     'C': [
        #         Player(1001, "Center 1", 25, 215, 1, 3, 'C', 9, 5, 8, 6, 7, 5, 7, False),
        #         Player(1002, "Center 2", 25, 210, 11, 3, 'C', 6, 4, 6, 5, 5, 4, 6, False),
        #         Player(1003, "Center 3", 25, 220, 21, 3, 'C', 4, 2, 4, 4, 3, 3, 5, False)
        #     ],
        #     'PF': [
        #         Player(1004, "Power Forward 1", 25, 203, 2, 3, 'PF', 8, 6, 7, 6, 7, 6, 6, False),
        #         Player(1005, "Power Forward 2", 25, 210, 12, 3, 'PF', 6, 5, 6, 4, 5, 5, 5, False),
        #         Player(1006, "Power Forward 3", 25, 205, 22, 3, 'PF', 4, 3, 3, 4, 3, 4, 4, False)
        #     ],
        #     'SF': [
        #         Player(1007, "Small Forward 1", 25, 204, 3, 3, 'SF', 7, 7, 7, 7, 7, 7, 6, False),
        #         Player(1008, "Small Forward 2", 25, 200, 13, 3, 'SF', 5, 5, 5, 5, 5, 5, 5, False),
        #         Player(1009, "Small Forward 3", 25, 202, 23, 3, 'SF', 3, 3, 3, 3, 4, 4, 4, False)
        #     ],
        #     'SG': [
        #         Player(1010, "Shooting Guard 1", 25, 195, 4, 3, 'SG', 6, 9, 6, 7, 7, 7, 6, False),
        #         Player(1011, "Shooting Guard 2", 25, 193, 14, 3, 'SG', 4, 6, 4, 6, 5, 5, 5, False),
        #         Player(1012, "Shooting Guard 3", 25, 197, 24, 3, 'SG', 3, 4, 3, 4, 3, 3, 4, False)
        #     ],
        #     'PG': [
        #         Player(1013, "Point Guard 1", 25, 185, 5, 3, 'PG', 5, 8, 5, 8, 8, 9, 5, False),
        #         Player(1014, "Point Guard 2", 25, 190, 15, 3, 'PG', 4, 7, 3, 6, 6, 7, 4, False),
        #         Player(1015, "Point Guard 3", 25, 192, 25, 3, 'PG', 2, 5, 2, 5, 5, 5, 3, False)
        #     ]
        # }
        self.position_orders = {
            'C': ['PF', 'SF', 'SG', 'PG'],
            'PF': ['SF', 'C', 'SG', 'PG'],
            'SF': ['PF', 'SG', 'C', 'PG'],
            'SG': ['PG', 'SF', 'PF', 'C'],
            'PG': ['SG', 'SF', 'PF', 'C']
        }
        self.adv = 0

    @staticmethod
    def load_team(team_name: str):
        team_data = get_team(name=team_name)
        if team_data:
            id, city, name, abbr, pcolor, scolor, tcolor, wins, losses, championships, stadium, conference, division, budget = team_data
            color = get_color(pcolor)
            return Team(id=id, city=city, name=name, abbr=abbr, color=color, wins=wins, losses=losses,
                        championships=championships, stadium=stadium, conference=conference,
                        division=division, budget=budget)
        else:
            return None

    def __str__(self):
        return f"{self.color}{self.name}{reset}\n{self.get_players()}"

    def reset(self):
        self.shots = 0
        self.shots2 = 0
        self.shots2_made = 0
        self.shots3 = 0
        self.shots3_made = 0
        self.fouls = 0
        self.quarter_fouls = 0
        self.turnovers = 0
        self.fts = 0
        self.fts_made = 0
        self.blocks = 0
        self.assists = 0
        self.rebounds = 0
        self.steals = 0
        self.points = 0
        self.scoring_trend = []
        self.consecutive_points = 0
        self.most_consecutive_points = 0
        self.active_players = {
            'C': None,
            'PF': None,
            'SF': None,
            'SG': None,
            'PG': None
        }

    def __str__(self) -> str:
        return self.name

    def sort_players_by_ovr(self):
        for position, players in self.players.items():
            players.sort(key=lambda x: x.ovr, reverse=True)

    def set_starting_lineup(self):
        # choose the best non-injured player to start the game
        players = self.get_players()
        for i in range(5):
            best_ovr = 0
            best_player = None
            best_position = None
            best_center = None
            best_center_ovr = 0
            best_power_forward = None
            best_power_forward_ovr = 0
            best_small_forward = None
            best_small_forward_ovr = 0
            best_shooting_guard = None
            best_shooting_guard_ovr = 0
            best_point_guard = None
            best_point_guard_ovr = 0
            for player in players:
                if player.center_ovr > best_center_ovr and not player.injured_games and not player.active:
                    best_center = player
                    best_center_ovr = player.center_ovr
                    if player.position == 'C':
                        best_center_ovr *= 1.2
                    if best_center_ovr > best_ovr and not self.active_players['C']:
                        best_ovr = best_center_ovr
                        best_player = player
                        best_position = 'C'
                if player.power_forward_ovr > best_power_forward_ovr and not player.injured_games and not player.active:
                    best_power_forward = player
                    best_power_forward_ovr = player.power_forward_ovr
                    if player.position == 'PF':
                        best_power_forward_ovr *= 1.2
                    if best_power_forward_ovr > best_ovr and not self.active_players['PF']:
                        best_ovr = best_power_forward_ovr
                        best_player = player
                        best_position = 'PF'
                if player.small_forward_ovr > best_small_forward_ovr and not player.injured_games and not player.active:
                    best_small_forward = player
                    best_small_forward_ovr = player.small_forward_ovr
                    if player.position == 'SF':
                        best_small_forward_ovr *= 1.2
                    if best_small_forward_ovr > best_ovr and not self.active_players['SF']:
                        best_ovr = best_small_forward_ovr
                        best_player = player
                        best_position = 'SF'
                if player.shooting_guard_ovr > best_shooting_guard_ovr and not player.injured_games and not player.active:
                    best_shooting_guard = player
                    best_shooting_guard_ovr = player.shooting_guard_ovr
                    if player.position == 'SG':
                        best_shooting_guard_ovr *= 1.2
                    if best_shooting_guard_ovr > best_ovr and not self.active_players['SG']:
                        best_ovr = best_shooting_guard_ovr
                        best_player = player
                        best_position = 'SG'
                if player.point_guard_ovr > best_point_guard_ovr and not player.injured_games and not player.active:
                    best_point_guard = player
                    best_point_guard_ovr = player.point_guard_ovr
                    if player.position == 'PG':
                        best_point_guard_ovr *= 1.2
                    if best_point_guard_ovr > best_ovr and not self.active_players['PG']:
                        best_ovr = best_point_guard_ovr
                        best_player = player
                        best_position = 'PG'

            self.active_players[best_position] = best_player
            best_player.active = True

        # for position, players in self.players.items():
        #     for player in players:
        #         if player.injured_games > 0:
        #             continue
        #         self.active_players[position] = player
        #         player.active = True
        #         break
        # if all players in the position are injured (player is None)
        for position, player in self.active_players.items():
            if player is None:
                # choose a player from a different position
                positions = self.position_orders[position]
                # as long as a player hasn't been chosen, keep looking for a player to start as center
                while self.active_players[position] is None:
                    if len(positions) == 0:
                        # if no player
                        return False
                    cur_pos = positions[0]
                    for alt_player in self.players[cur_pos]:
                        if alt_player.injured_games == 0 and alt_player.active == False:
                            self.active_players[position] = alt_player
                            break
                    positions.remove(cur_pos)
        return True

    def make_substitution(self, player, position, show_pbp):
        # find best replacement
        replacement = None
        best_ovr = 0
        best_player = None
        for repl_player in self.get_players():
            if repl_player != player and repl_player.injured_games == 0 and repl_player.active == False and repl_player.fouled_out == False:
                if position == 'C':
                    center_ovr = repl_player.center_ovr
                    if repl_player.position == 'C':
                        center_ovr *= 1.2
                    if center_ovr > best_ovr:
                        best_ovr = repl_player.center_ovr
                        best_player = repl_player
                elif position == 'PF':
                    power_forward_ovr = repl_player.power_forward_ovr
                    if repl_player.position == 'PF':
                        power_forward_ovr *= 1.2
                    if power_forward_ovr > best_ovr:
                        best_ovr = repl_player.power_forward_ovr
                        best_player = repl_player
                elif position == 'SF':
                    small_forward_ovr = repl_player.small_forward_ovr
                    if repl_player.position == 'SF':
                        small_forward_ovr *= 1.2
                    if small_forward_ovr > best_ovr:
                        best_ovr = repl_player.small_forward_ovr
                        best_player = repl_player
                elif position == 'SG':
                    shooting_guard_ovr = repl_player.shooting_guard_ovr
                    if repl_player.position == 'SG':
                        shooting_guard_ovr *= 1.2
                    if shooting_guard_ovr > best_ovr:
                        best_ovr = repl_player.shooting_guard_ovr
                        best_player = repl_player
                elif position == 'PG':
                    point_guard_ovr = repl_player.point_guard_ovr
                    if repl_player.position == 'PG':
                        point_guard_ovr *= 1.2
                    if point_guard_ovr > best_ovr:
                        best_ovr = repl_player.point_guard_ovr
                        best_player = repl_player
        replacement = best_player
        # for same_pos_player in self.players[position]:
        #     if same_pos_player != player and same_pos_player.injured_games == 0 and same_pos_player.active == False and same_pos_player.fouled_out == False:
        #         replacement = same_pos_player
        #         break
        if replacement is None:
            positions = self.position_orders[position]
            while replacement is None:
                if len(positions) == 0:
                    return False
                cur_pos = positions[0]
                for alt_player in self.players[cur_pos]:
                    if alt_player != player and alt_player.injured_games == 0 and alt_player.active == False and alt_player.fouled_out == False:
                        replacement = alt_player
                        break
                positions.remove(cur_pos)
        self.active_players[position] = replacement
        player.active = False
        player.current_seconds = 0
        replacement.active = True
        if show_pbp:
          print(f"{self.color}{replacement.name}{reset} in for {self.color}{player.name}{reset} at {position}")
        return True

    def decide_substitutions(self, show_pbp):
        for position, player in self.active_players.items():
            if not player:
                print(f"Team: {self.name}")
                print(f"Position: {position}")
                print(self.active_players)
                print(player for player in self.active_players.values())
                print(player for player in self.players.values())
            if (random.random()/10+0.95)*(player.ovr*6) < player.current_seconds or player.fouled_out or player.injured_games > 0:
                self.make_substitution(player, position, show_pbp)

    def get_active_players(self):
        players = []
        for position, player in self.active_players.items():
            if player is not None:
                players.append(player)
        return players

    def get_players(self):
        players = []
        for position, players_list in self.players.items():
            for player in players_list:
                players.append(player)
        # sort players by most game seconds
        players.sort(key=lambda x: x.game_stats["MIN"], reverse=True)
        return players

    def calculate_playstyle(self):
        inner_attack_sum = 0
        outer_attack_sum = 0
        for player in self.get_players():
            inner_attack_sum += player.inner_attack
            outer_attack_sum += player.outer_attack
        self.distance_playstyle = .58+(outer_attack_sum - inner_attack_sum)/1000

    def clear_season_stats(self):
        self.season_wins = 0
        self.season_losses = 0
        self.season_net_points = 0
        for player in self.get_players():
            player.reset_season()