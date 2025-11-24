from .constants import get_country_color
from .country import Country
from .db import get_country, get_player, get_player_stats, get_player_awards, get_player_lifetime_boxscore, get_player_personal_bests_game, get_player_personal_bests_season, get_player_season_boxscore

class Player:
    def __init__(self, player_id: int, first_name: str, last_name: str, age: int, height: int, number: int, form: int, position: str, inner_attack: float, outer_attack: float,
                 inner_defense: float, outer_defense: float, iq: float, passing: float, physical: float, clutch: float, work_ethic: float, leadership: float, injury_tendency: float, luck: bool, country: Country):
        self.player_id = player_id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = 0
        self.age = age
        self.height = height
        self.print_height = self.get_print_height()
        self.number = number
        self.form = form
        self.position = position
        self.inner_attack = inner_attack
        self.outer_attack = outer_attack
        self.inner_defense = inner_defense
        self.outer_defense = outer_defense
        self.iq = iq
        self.passing = passing
        self.physical = physical
        self.injury_tendency = injury_tendency # 0.00005
        self.mins = 0
        self.luck = luck
        self.injured_games = 0
        self.current_seconds = 0
        self.active = False
        self.fouled_out = False
        self.game_stats = {"PTS":0,"REB":0,"AST":0,"BLK":0,"STL":0,"TOV":0,"MIN":0,
                           "FGM":0,"FGA":0,"TPM":0,"TPA":0,"FTM":0,"FTA":0,"OREB":0,"DREB":0,"REB":0,
                           "PF":0,"PM":0}
        self.season_stats = {"PTS":0,"REB":0,"AST":0,"BLK":0,"STL":0,"TOV":0,"MIN":0,"GP":0,
                           "FGM":0,"FGA":0,"TPM":0,"TPA":0,"FTM":0,"FTA":0,"OREB":0,"DREB":0,"REB":0,
                           "PF":0,"PM":0,"DD":0,"TD":0}
        self.lifetime_stats = {"PTS":0,"REB":0,"AST":0,"BLK":0,"STL":0,"TOV":0,"MIN":0,"GP":0,
                           "FGM":0,"FGA":0,"TPM":0,"TPA":0,"FTM":0,"FTA":0,"OREB":0,"DREB":0,"REB":0,
                           "PF":0,"PM":0,"DD":0,"TD":0}
        # top row is personal bests by game, triple double and games played are bests by season
        self.personal_bests = {"PTS":0,"REB":0,"AST":0,"BLK":0,"STL":0,"FGM":0,"TPM":0,"FTM":0,"PM":0,
                               "DD":0,"TD":0,"GP":0}
        self.awards = {"VBL Champion":0, "MVP":0, "Finals MVP":0, "TOTS":0, "TOF":0, "Golden Bucket":0, "Golden Board":0, "Golden Dime":0, "Golden Stuff":0, "Golden Hands":0}
        self.records = {}
        self.teams = []
        self.country = country

        # draft
        self.draft_year = 0
        self.draft_team_id = 0
        self.draft_pick = 0

        # mental
        self.clutch = clutch
        self.work_ethic = work_ethic
        self.leadership = leadership
        
        self.join_date = 0
        self.retire_date = 0
        self.championships = 0

    @staticmethod
    def load_player(player_id: int, year: int):
        _, first_name, last_name, birth_year, draft_year, draft_team_id, draft_pick, country_id, number, height, position, luck, injury_tendency, clutch, work_ethic, leadership, join_date, retire_date, championships = get_player(player_id)
        age = year - birth_year
        form = 3
        _, _, iq, physical, passing, inner_attack, outer_attack, inner_defense, outer_defense = get_player_stats(player_id, year)
        _, name, abbr, pcolor, scolor, tcolor, wins, losses, championships, = get_country(country_id)
        c_color = get_country_color(country_id)
        country = Country(id=country_id, name=name, abbr=abbr, color=c_color)
        return Player(player_id, first_name, last_name, age, height, number, form, position, inner_attack, outer_attack, inner_defense, outer_defense, iq, passing, physical, clutch, work_ethic, leadership, injury_tendency, luck, country)

    def to_tuple(self):
        return (self.first_name, self.last_name, self.birth_year, self.draft_year, self.draft_team_id, self.draft_pick, self.country.id, self.number, self.height, self.position, self.luck, self.injury_tendency, self.clutch, self.work_ethic, self.leadership, self.join_date, self.retire_date, self.championships)

    def stats_to_tuple(self, year: int):
        return (self.player_id, year, self.iq, self.physical, self.passing, self.inner_attack, self.outer_attack, self.inner_defense, self.outer_defense)

    def awards_to_tuple(self):
        return (self.player_id, *self.awards.values())

    def season_personal_bests_to_tuple(self):
        return (self.player_id, *self.personal_bests.values())
        
    def game_personal_bests_to_tuple(self):
        return (self.player_id, *self.personal_bests.values())
    
    def season_boxscore_to_tuple(self):
        return (self.player_id, *self.season_stats.values())
    
    def lifetime_boxscore_to_tuple(self):
        return (self.player_id, *self.lifetime_stats.values())

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def get_print_height(self):
        inches = round(self.height/2.54)
        feet = 0
        while inches >= 12:
            feet += 1
            inches -= 12
        return f"{feet}'{inches}"

    @property
    def ovr(self):
        if self.position == "C":
          return self.center_ovr
        if self.position == "PF":
          return self.power_forward_ovr
        if self.position == "SF":
          return self.small_forward_ovr
        if self.position == "SG":
          return self.shooting_guard_ovr
        if self.position == "PG":
          return self.point_guard_ovr

    @property
    def center_ovr(self):
        return (2*self.inner_attack)+self.outer_attack+(2*self.inner_defense)+self.outer_defense+(self.iq)+(2*self.physical)+(self.passing)

    @property
    def power_forward_ovr(self):
        return (1.7*self.inner_attack)+(1.3*self.outer_attack)+(1.7*self.inner_defense)+(1.3*self.outer_defense)+(self.iq)+(1.7*self.physical)+(1.3*self.passing)

    @property
    def small_forward_ovr(self):
        return (1.5*(self.inner_attack+self.outer_attack+self.inner_defense+self.outer_defense))+(1.33*(self.iq+self.physical+self.passing))

    @property
    def shooting_guard_ovr(self):
        return self.inner_attack+(2*self.outer_attack)+self.inner_defense+(2*self.outer_defense)+(1.5*self.iq)+(1.25*self.physical)+(1.25*self.passing)

    @property
    def point_guard_ovr(self):
        return self.inner_attack+(1.5*self.outer_attack)+self.inner_defense+(1.5*self.outer_defense)+(2*self.iq)+(self.physical)+(2*self.passing)

    def __str__(self):
        return f"""{self.name} Country:{self.country.name} Age:{self.age} Height:{self.print_height} OVR: {self.ovr} POS:{self.position}\n{self.lifetime_stats}\n{self.awards}"""

    def reset_season(self):
        self.season_stats = {"PTS":0,"REB":0,"AST":0,"BLK":0,"STL":0,"TOV":0,"MIN":0,"GP":0,
                           "FGM":0,"FGA":0,"TPM":0,"TPA":0,"FTM":0,"FTA":0,"OREB":0,"DREB":0,"REB":0,
                           "PF":0,"PM":0,"DD":0,"TD":0}
        self.injured_games = 0
        self.current_seconds = 0
        self.active = False
        self.fouled_out = False