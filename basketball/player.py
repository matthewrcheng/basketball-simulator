class Player:
    def __init__(self, player_id: int, name: str, age: int, height: int, number: int, form: int, position: str, inner_attack, outer_attack,
                 inner_defense, outer_defense, iq, passing, physical, luck, country):
        self.player_id = player_id
        self.name = name
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
        self.injury_tendency = 0.00005
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