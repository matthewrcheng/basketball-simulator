import random
import math
import numpy as np
from enum import Enum
from basketball.player import Player
from .name_generator import random_name
from .display import reset

class PossessionResult(Enum):
  SHOT = 1
  TURNOVER = 2
  FOUL = 3

def decide_free_throw(player, adv):
  # does the player succeed?
  return np.random.random() < 0.73 + (2*player.outer_attack/100) + adv

def decide_shooter(points, team):
  # randomly choose a player using corresponding attack as weights
  active_players = list(team.active_players.values())
  if points == 2:
    weights = [player.inner_attack**1.5 for player in active_players]
  else:
    weights = [player.outer_attack**1.5 for player in active_players]
  return random.choices(active_players, weights=weights, k=1)[0]

def decide_rebounder(off_team, def_team):
  # randomly choose a player using height and physicality as weights
  active_off_players = off_team.get_active_players()
  active_def_players = def_team.get_active_players()
  active_players = active_off_players + active_def_players
  off_weights = [player.physical * player.height * (.25+off_team.adv) for player in active_off_players]
  def_weights = [player.physical * player.height * (.75+def_team.adv) for player in active_def_players]
  weights = off_weights + def_weights
  rebounder = random.choices(active_players, weights=weights, k=1)[0]
  off_reb = rebounder in active_off_players
  return rebounder, off_reb

def decide_assister(shooter, team):
  # randomly choose a player using passing and iq as weights
  active_players = list(team.active_players.values())
  # remove shooter from the list of active players (can't assist self)
  active_players.remove(shooter)
  weights = [player.iq * player.passing for player in active_players]
  return random.choices(active_players, weights=weights, k=1)[0]

def decide_stealer(position, team):
  # randomly choose a player using inner and outer defense as weights
  active_players = list(team.active_players.values())
  weights = [player.inner_defense + player.outer_defense for player in active_players]
  return random.choices(active_players, weights=weights, k=1)[0]

def decide_blocker(points, team):
  # randomly choose a player using height and physicality as weights
  active_players = list(team.active_players.values())
  if points == 2:
    weights = [player.height * player.inner_defense for player in active_players]
  else:
    weights = [player.height * player.outer_defense for player in active_players]
  return random.choices(active_players, weights=weights, k=1)[0]

def decide_fouler(team):
  # choose random active player
  active_players = list(team.active_players.values())
  weights = [10 + player.physical for player in active_players]
  return random.choices(active_players, weights=weights, k=1)[0]

def decide_turnoverer(team):
  # choose random active player
  active_players = list(team.active_players.values())
  weights = [10 + player.passing - player.iq for player in active_players]
  return random.choices(active_players, weights=weights, k=1)[0]

def check_streak(points, scoring_team, team1, team2):
  if scoring_team == team1:
    team1.consecutive_points += points
    if team1.consecutive_points > team1.most_consecutive_points:
      team1.most_consecutive_points = team1.consecutive_points
    team2.consecutive_points = 0
    return team1.consecutive_points
  else:
    team2.consecutive_points += points
    if team2.consecutive_points > team2.most_consecutive_points:
      team2.most_consecutive_points = team2.consecutive_points
    team1.consecutive_points = 0
    return team2.consecutive_points

def check_injury(team, players, show_pbp):
  for player in players:
    chance = np.random.random()
    if chance < player.injury_tendency:
      days = max(int(np.random.exponential(scale=5, size=1)[0]),1)
      player.injured_games += days
      # if show_pbp:
      print(f"{team.color}{player.name} ({team.name}){reset} was injured! Injury will last for {days} games.")
      return player
  return None

def random_stat(luck = 0):
  if luck:
    val = np.round(np.random.normal(8,.75),1)
  else:
    val = np.round(np.random.normal(5,1.5),1)
    if val<1:
      val = 1
    elif val>10:
      val = 10
  return val

def random_outer_stat(quality = 5, pos = 'PG'):
  base = {'C':-1,'PF':-0.5,'SF':0,'SG':0.5,'PG':1}
  val = np.round(np.random.normal(base[pos]+quality,.75),1)
  if val<1:
    val = 1
  elif val>10:
    val = 10
  return val

def random_inner_stat(quality = 5, pos = 'C'):
  base = {'C':1,'PF':0.5,'SF':0,'SG':-0.5,'PG':-1}
  val = np.round(np.random.normal(base[pos]+quality,.75),1)
  if val<1:
    val = 1
  elif val>10:
    val = 10
  return val

def decide_retirement(player):
  age = 35 if player.position in {'PG','SF','PF'} else 34
  age += max(player.inner_attack, player.outer_attack, player.inner_defense, player.outer_defense, player.passing)-6
  return True if player.age>np.random.normal(age, 1.5) else False

def simulate_trades(teams):
  player_count = 0
  team_most_pos = []
  team_least_pos = []
  trades = []
  chosen = set()
  for i in range(len(teams)):
    temp = dict()
    positions = ['C','PF','SF','PG','SG']
    for player in teams[i].get_players():
      player_count += 1
      if not player.position in temp:
        temp[player.position] = 1
        positions.remove(player.position)
      else:
        temp[player.position] += 1
    for p in positions:
      temp[p] = 0
    team_most_pos.append(max(temp, key=temp.get))
    team_least_pos.append(min(temp, key=temp.get))
  for i in range(len(team_least_pos)):
    for j in range(len(team_most_pos)):
      if team_least_pos[i] == team_most_pos[j] and j not in chosen and i != j:
        trades.append((i,j,team_least_pos[i]))
        chosen.add(j)
        break
  count = 0
  for trade in trades:
    for player1 in teams[trade[1]].get_players():
      if player1.position == trade[2]:
        str1 = calculate_player_value(player1)
        for player2 in teams[trade[0]].get_players():
          str2 = calculate_player_value(player2)
          if math.isclose(str1,str2,rel_tol=.1):
            count += 1
            player1.teams.append(teams[trade[1]].name)
            player2.teams.append(teams[trade[0]].name)
            teams[trade[0]].players[player1.position].append(player1)
            teams[trade[1]].players[player1.position].remove(player1)
            teams[trade[1]].players[player2.position].append(player2)
            teams[trade[0]].players[player2.position].remove(player2)
            print(f'{player1.name} -> {teams[trade[0]].color}{teams[trade[0]].name}{reset}')
            print(f'{teams[trade[1]].color}{teams[trade[1]].name}{reset} <- {player2.name}')
            break
        break
  print("Trades:", count)

def calculate_player_value(player):
  return (player.ovr**1.5) * (28/player.age)

def simulate_aging(teams, retiring):
  for team in teams:
    for player in team.get_players():
      player.age += 1
      if decide_retirement(player):
        player.teams.append(team.name)
        retiring.append(player)
        team.players[player.position].remove(player)
      else:
        if player.luck:
          age_boost = (30-player.age)/12
        else:
          age_boost = (28-player.age)/20
        player.inner_attack+=np.random.normal(age_boost, .25)
        player.outer_attack+=np.random.normal(age_boost, .25)
        player.inner_defense+=np.random.normal(age_boost, .25)
        player.outer_defense+=np.random.normal(age_boost, .25)
        player.passing+=np.random.normal(age_boost, .25)
        player.physical+=np.random.normal(age_boost, .125)
        player.form = random.choice(range(1,6))
        player.inner_attack = max(1, player.inner_attack)
        player.outer_attack = max(1, player.outer_attack)
        player.inner_defense = max(1, player.inner_defense)
        player.outer_defense = max(1, player.outer_defense)
        player.passing = max(1, player.passing)
        player.physical = max(1, player.physical)

def generate_new_players(draft_order, teams, next_id, ages=range(18,26)):
  new_players = []
  for i in range(len(draft_order)):
    luck = random.choices(range(2), weights=[250,1], k=1)[0]
    if luck:
      quality = 8
    else:
      quality = random.random()*6 + 2
    pos = random.choice(['C','PF','SF','SG','PG'])
    heights = {'C':211,'PF':205,'SF':202,'SG':198,'PG':189}
    name, country = random_name()
    height = int(np.random.normal(heights[pos],7))
    player = Player(player_id=next_id, name=name, age=random.choice(ages), height=height, number=random.choice(range(100)), 
                    form=random.choice(range(1,6)), position=pos, inner_attack=random_inner_stat(quality, pos), 
                    outer_attack=random_outer_stat(quality, pos), inner_defense=random_inner_stat(quality, pos), 
                    outer_defense=random_outer_stat(quality, pos), iq=random_stat(quality), passing=random_outer_stat(quality, pos), 
                    physical=random_inner_stat(quality, pos), luck=luck, country=country)
    country.potential_players[player.position].append(player)
    new_players.append(player)
    next_id += 1
  print('\nVBL Draft')
  for i in range(len(draft_order)):
    player_weight = []
    position_scores = {'C':0,'PF':0,'SF':0,'SG':0,'PG':0}
    for player in teams[draft_order[i]].get_players():
      position_scores[player.position] += player.ovr
    player_scores = []
    for player in new_players:
      player_scores.append(player.ovr + (player.luck*10) - (position_scores[player.position]/10))
    idx = player_scores.index(max(player_scores))
    player = new_players[idx]
    teams[draft_order[i]].players[player.position].append(player)
    new_players.pop(idx)
    print(f'Pick {i+1}: {player.name} {player.country.color}{player.country.name}{reset} {player.position} {player.print_height} ({player.age}) to {teams[draft_order[i]].color}{teams[draft_order[i]].name}{reset}, Stats: {player.inner_attack} {player.outer_attack} {player.inner_defense} {player.outer_defense} {player.iq} {player.passing} {player.physical}')
  return next_id

def determine_draft_order(df, teams: list):
  order = list(df['Team'])
  pick_weights = []
  for i in range(len(order)):
    pick_weights.append(int(np.around(100*(2**(i-7)))))

  draft_order = []
  for i in range(len(order)):
    c = random.choices(range(len(order)), weights=pick_weights, k=1)[0]
    draft_order.append(order[c])
    order.pop(c)
    pick_weights.pop(c)

  order = list(df['Team'])
  for i in range(len(order)):
    pick_weights.append(int(np.around(100*(2**(i-7)))))

  for i in range(len(order)):
    c = random.choices(range(len(order)), weights=pick_weights, k=1)[0]
    draft_order.append(order[c])
    order.pop(c)
    pick_weights.pop(c)

  new_draft_order = [None]*len(draft_order)
  for team in teams:
    pattern = f"{team.color}{team.name}{reset}"
    for i in range(len(draft_order)):
      if draft_order[i] == pattern:
        new_draft_order[i] = team.id
  return new_draft_order