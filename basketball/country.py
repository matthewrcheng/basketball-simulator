from basketball.player import Player
from basketball.team import Team
from basketball.constants import *

class Country(Team):

    def __init__(self, id: int, name: str = 'Default Team', abbr: str = 'DEF', players: dict[str, list[Player]] = None, color: str = default_color):
        super().__init__(id, name, abbr, players, color)

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

        self.potential_players = {
            'C': [],
            'PF': [],
            'SF': [],
            'SG': [],
            'PG': []
        }

    def select_best_player(self, players: list[Player]) -> Player:
        best_player = None
        best_rating = 0
        for player in players:
            if player.ovr > best_rating:
                best_rating = player.ovr
                best_player = player
        return best_player

    def select_players(self) -> None:
        for position in self.potential_players:
            while len(self.players[position]) < 3 and len(self.potential_players[position]) > 0:
                best_player = self.select_best_player(self.potential_players[position])
                if not best_player.injured_games:
                    self.players[position].append(best_player)
                    self.potential_players[position].remove(best_player)

    def reset_potential_players(self) -> None:
        for position in self.players:
            for player in self.players[position]:
                self.potential_players[position].append(player)
            self.players[position] = []

USA = Country(101, 'United States', 'USA', None, blue)
CAN = Country(102, 'Canada', 'CAN', None, red)
AUS = Country(103, 'Australia', 'AUS', None, yellow)
NZL = Country(104, 'New Zealand', 'NZL', None, black)
ENG = Country(105, 'England', 'ENG', None, white)
RUS = Country(106, 'Russia', 'RUS', None, red)
UKR = Country(143, 'Ukraine', 'UKR', None, yellow)
SRB = Country(107, 'Serbia', 'SRB', None, dark_red)
CRO = Country(108, 'Croatia', 'CRO', None, blue)
BOS = Country(109, 'Bosnia and Herzegovina', 'BOS', None, dark_blue)
SLV = Country(110, 'Slovenia', 'SLV', None, white)
MON = Country(111, 'Montenegro', 'MON', None, dark_red)
TUR = Country(112, 'Turkey', 'TUR', None, red)
JOR = Country(132, 'Jordan', 'JOR', None, white)
ISR = Country(133, 'Israel', 'ISR', None, blue)
LBN = Country(113, 'Lebanon', 'LBN', None, light_red)
IRN = Country(139, 'Iran', 'IRN', None, white)
SAU = Country(114, 'Saudi Arabia', 'SAU', None, dark_green)
TUN = Country(115, 'Tunisia', 'TUN', None, white)
EGY = Country(116, 'Egypt', 'EGY', None, dark_red)
SSD = Country(117, 'South Sudan', 'SSD', None, white)
SEN = Country(118, 'Senegal', 'SEN', None, green)
NGA = Country(119, 'Nigeria', 'NGA', None, green)
CAM = Country(121, 'Cameroon', 'CAM', None, green)
DRC = Country(122, 'Democratic Republic of the Congo', 'DRC', None, light_blue)
CHN = Country(123, 'China', 'CHN', None, red)
JPN = Country(124, 'Japan', 'JPN', None, dark_blue)
KOR = Country(125, 'South Korea', 'KOR', None, white)
IND = Country(126, 'India', 'IND', None, orange)
LAT = Country(127, 'Latvia', 'LAT', None, dark_red)
LTH = Country(128, 'Lithuania', 'LTH', None, yellow)
POL = Country(129, 'Poland', 'POL', None, white)
FIN = Country(130, 'Finland', 'FIN', None, white)
SWE = Country(131, 'Sweden', 'SWE', None, yellow)
DEN = Country(150, 'Denmark', 'DEN', None, dark_red)
ARG = Country(136, 'Argentina', 'ARG', None, light_blue)
DOM = Country(137, 'Dominican Republic', 'DOM', None, dark_blue)
PUE = Country(138, 'Puerto Rico', 'PUE', None, light_red)
VEN = Country(140, 'Venezuela', 'VEN', None, dark_red)
MEX = Country(141, 'Mexico', 'MEX', None, green)
COL = Country(142, 'Colombia', 'COL', None, yellow)
URU = Country(144, 'Uruguay', 'URU', None, light_blue)
CHI = Country(151, 'Chile', 'CHI', None, red)
ESP = Country(145, 'Spain', 'ESP', None, red)
FRA = Country(146, 'France', 'FRA', None, blue)
BEL = Country(149, 'Belgium', 'BEL', None, black)
GER = Country(147, 'Germany', 'GER', None, white)
ITA = Country(148, 'Italy', 'ITA', None, blue)
BRA = Country(134, 'Brazil', 'BRA', None, yellow)
POR = Country(135, 'Portugal', 'POR', None, red)
ANG = Country(152, 'Angola', 'ANG', None, red)
CBV = Country(120, 'Cabo Verde', 'CBV', None, blue)
