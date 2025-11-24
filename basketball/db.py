import os
import sqlite3
from .player import Player

root_dir = os.path.dirname(os.path.abspath(__file__))
db_url = os.path.join(root_dir, '..', 'basketball.db')

def execute_query(query, params=()):
    conn = sqlite3.connect(db_url)
    cursor = conn.cursor()

    cursor.execute(query, params)
    results = cursor.fetchall()

    conn.commit()
    conn.close()

    return results

def get_city(id: int = None, name: str = None):
    if not id and not name:
        raise ValueError("Either id or name must be provided")
    if name:
        query = "SELECT name FROM cities WHERE name = ?"
        result = execute_query(query, (name,))
        if result:
            return result[0][0]
        return None
    if id:
        query = "SELECT name FROM cities WHERE id = ?"
        result = execute_query(query, (id,))
        if result:
            return result[0][0]
        return None
    
def get_country(id: int):
    query = "SELECT * FROM countries WHERE id = ?"
    result = execute_query(query, (id,))
    if result:
        return list(result[0])
    return None
    
def get_stadium(id: int):
    query = "SELECT name FROM stadiums WHERE id = ?"
    result = execute_query(query, (id,))
    if result:
        return result[0][0]
    return None

def get_player(id: int):
    query = "SELECT * FROM players WHERE id = ?"
    result = execute_query(query, (id,))
    if result:
        return list(result[0])
    return None

def get_player_stats(id: int, year: int):
    query = "SELECT * FROM player_stats WHERE player_id = ? AND year = ?"
    result = execute_query(query, (id, year))
    if result:
        return list(result[0])
    return None

def get_award(id: int):
    query = "SELECT * FROM awards WHERE id = ?"
    result = execute_query(query, (id,))
    if result:
        return list(result[0])
    return None

def get_player_awards(id: int):
    query = "SELECT * FROM player_awards WHERE player_id = ?"
    result = execute_query(query, (id,))
    return result

def get_player_personal_bests_season(id: int):
    query = "SELECT * FROM player_personal_bests_season WHERE player_id = ?"
    result = execute_query(query, (id,))
    return result

def get_player_personal_bests_game(id: int):
    query = "SELECT * FROM player_personal_bests_game WHERE player_id = ?"
    result = execute_query(query, (id,))
    return result

def get_player_season_boxscore(id: int):
    query = "SELECT * FROM player_season_boxscore WHERE player_id = ?"
    result = execute_query(query, (id,))
    return result

def get_player_lifetime_boxscore(id: int):
    query = "SELECT * FROM player_lifetime_boxscore WHERE player_id = ?"
    result = execute_query(query, (id,))
    return result

def get_team_players(id: int):
    query = "SELECT player_id FROM player_teams WHERE team_id = ?"
    result = execute_query(query, (id,))
    players = [player[0] for player in result]
    result = [get_player(player) for player in players]
    return result

def get_team(id: int = None, name: str = None):
    if not id and not name:
        raise ValueError("Either id or name must be provided")
    if id:
        query = "SELECT * FROM teams WHERE id = ?"
        result = execute_query(query, (id,))
        if result:
            team = list(result[0])
            city_id = team[1]
            stadium_id = team[10]
            city = get_city(id=city_id)
            stadium = get_stadium(id=stadium_id)
            team[1] = city
            team[10] = stadium
    elif name:
        query = "SELECT * FROM teams WHERE name = ?"
        result = execute_query(query, (name,))
        if result:
            team = list(result[0])
            city_id = team[1]
            stadium_id = team[10]
            city = get_city(id=city_id)
            stadium = get_stadium(id=stadium_id)
            team[1] = city
            team[10] = stadium
    if team:
        return team
    return None

def get_next_player_id():
    query = "SELECT MAX(id) FROM players"
    result = execute_query(query)
    if result:
        return result[0][0] + 1
    return 1

def store_player(player):
    query = "INSERT INTO players (first_name, last_name, birth_year, draft_year, draft_team_id, draft_pick, country_id, number, height, position, luck, injury_tendency, clutch, work_ethic, leadership, join_date, retire_date, championships) VALUES (?, ?, ?, ?, ?, ?, ?)"
    return execute_query(query, player)

def store_player_awards(player_awards):
    query = "INSERT INTO player_awards (player_id, award_id, year) VALUES (?, ?, ?) ON CONFLICT (player_id, award_id) DO UPDATE SET year = EXCLUDED.year"
    return execute_query(query, player_awards)

def store_player_season_boxscore(player_season_boxscore):
    query = "INSERT INTO player_season_boxscore (player_id, year, games, minutes, points, rebounds, rebounds_offensive, rebounds_defensive, assists, steals, blocks, turnovers, field_goals_made, field_goals_attempted, three_pt_made, three_pt_attempted, ft_made, ft_attempted, personal_fouls, plus_minus) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    return execute_query(query, player_season_boxscore)

def store_player_lifetime_boxscore(player_lifetime_boxscore):
    # overwrite if already exists
    query = "INSERT INTO player_lifetime_boxscore (player_id, games, minutes, points, rebounds, rebounds_offensive, rebounds_defensive, assists, steals, blocks, turnovers, field_goals_made, field_goals_attempted, three_pt_made, three_pt_attempted, ft_made, ft_attempted, personal_fouls, plus_minus) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    return execute_query(query, player_lifetime_boxscore)

def store_player_stats(player_stats):
    query = "INSERT INTO player_stats (player_id, year, iq, physical, passing, inner_attack, outer_attack, inner_defense, outer_defense) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
    return execute_query(query, player_stats)

def store_player_personal_bests_game(player_game_personal_bests):
    query = "INSERT INTO player_game_personal_bests (player_id, year, game_id, personal_bests) VALUES (?, ?, ?, ?)"
    return execute_query(query, player_game_personal_bests)

def store_player_personal_bests_season(player_season_personal_bests):
    query = "INSERT INTO player_season_personal_bests (player_id, year, personal_bests) VALUES (?, ?, ?)"
    return execute_query(query, player_season_personal_bests)

def player_to_db(player: Player):
    player_tuple = player.to_tuple()
    store_player(player_tuple)

    player_stats = player.stats_to_tuple()
    store_player_stats(player_stats)

    player_awards = player.awards_to_tuple()
    store_player_awards(player_awards)

    player_season_boxscore = player.season_boxscore_to_tuple()
    store_player_season_boxscore(player_season_boxscore)

    player_lifetime_boxscore = player.lifetime_boxscore_to_tuple()
    store_player_lifetime_boxscore(player_lifetime_boxscore)

    player_game_personal_bests = player.game_personal_bests_to_tuple()
    store_player_personal_bests_game(player_game_personal_bests)

    player_season_personal_bests = player.season_personal_bests_to_tuple()
    store_player_personal_bests_season(player_season_personal_bests)
