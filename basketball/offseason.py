import random
from basketball.util import *

def simulate_offseason(teams, next_id, df):
  random.shuffle(teams)
  simulate_trades(teams)
  retiring = []
  simulate_aging(teams, retiring)
  def sort_crit(team):
    return team.id
  teams.sort(key=sort_crit)
  draft_order = determine_draft_order(df, teams)
  draft_numbers = []
  for d in draft_order:
    for team in teams:
      if team.name == d:
        draft_numbers.append(team.id)
        break
  next_id = generate_new_players(draft_numbers, teams, next_id)
  for i in range(len(teams)):
    pos_count = {'C':0,'PF':0,'SF':0,'SG':0,'PG':0}
    while len(teams[i].get_players()) < 10:
      luck = random.choices(range(2), weights=[250,1], k=1)
      name, country = random_name()
      player = Player(next_id, name, random.choice(range(20,35)), int(np.random.normal(200,7)), random.choice(range(100)), random.choice(range(1,6)),
                    random.choice(['C','PF','SF','SG','PG']), random_stat(luck[0]), random_stat(luck[0]), random_stat(luck[0]), random_stat(luck[0]),
                      random_stat(luck[0]),  random_stat(luck[0]),  random_stat(luck[0]), luck[0], country)
      country.potential_players[player.position].append(player)
      teams[i].players[player.position].append(player)
      print(f'{teams[i].color}{teams[i].name}{reset} sign unrestricted free agent {player.name} {country.color}{country.name}{reset} {player.position} {player.print_height}, Stats: {player.inner_attack} {player.outer_attack} {player.inner_defense} {player.outer_defense} {player.iq} {player.passing} {player.physical}')
      next_id += 1
    for curr_player in teams[i].get_players():
      pos_count[curr_player.position] += 1
    for pos in pos_count.keys():
      while pos_count[pos] < 2:
        pos_count[pos] += 1
        luck = random.choices(range(2), weights=[250,1], k=1)
        name, country = random_name()
        player = Player(next_id, name, random.choice(range(20,35)), int(np.random.normal(200,7)), random.choice(range(100)), random.choice(range(1,6)),
                    random.choice(['C','PF','SF','SG','PG']), random_stat(luck[0]), random_stat(luck[0]), random_stat(luck[0]), random_stat(luck[0]),
                      random_stat(luck[0]),  random_stat(luck[0]),  random_stat(luck[0]), luck[0], country)
        country.potential_players[player.position].append(player)
        teams[i].players[player.position].append(player)
        print(f'{teams[i].color}{teams[i].name}{reset} sign unrestricted free agent {player.name} {country.color}{country.name}{reset} {player.position} {player.print_height}, Stats: {player.inner_attack} {player.outer_attack} {player.inner_defense} {player.outer_defense} {player.iq} {player.passing} {player.physical}')
        next_id += 1
  for team in teams:
    for position, players in team.players.items():
      players.sort(key=lambda x: x.ovr, reverse=True)
  return retiring, next_id

def initial_draft(teams, next_id):
  draft_numbers = random.choices(range(20), k=300)
  next_id = generate_new_players(draft_numbers, teams, next_id, range(18, 35))
  for i in range(len(teams)):
    pos_count = {'C':0,'PF':0,'SF':0,'SG':0,'PG':0}
    while len(teams[i].get_players()) < 10:
      luck = random.choices(range(2), weights=[250,1], k=1)
      name, country = random_name()
      player = Player(next_id, name, random.choice(range(20,35)), int(np.random.normal(200,7)), random.choice(range(100)), random.choice(range(1,6)),
                    random.choice(['C','PF','SF','SG','PG']), random_stat(luck[0]), random_stat(luck[0]), random_stat(luck[0]), random_stat(luck[0]),
                      random_stat(luck[0]),  random_stat(luck[0]),  random_stat(luck[0]), luck[0], country)
      country.potential_players[player.position].append(player)
      teams[i].players[player.position].append(player)
      print(f'{teams[i].color}{teams[i].name}{reset} sign unrestricted free agent {player.name} {country.color}{country.name}{reset} {player.position} {player.print_height}, Stats: {player.inner_attack} {player.outer_attack} {player.inner_defense} {player.outer_defense} {player.iq} {player.passing} {player.physical}')
      next_id += 1
    for curr_player in teams[i].get_players():
      pos_count[curr_player.position] += 1
    for pos in pos_count.keys():
      while pos_count[pos] < 2:
        pos_count[pos] += 1
        luck = random.choices(range(2), weights=[250,1], k=1)
        name, country = random_name()
        player = Player(next_id, name, random.choice(range(20,35)), int(np.random.normal(200,7)), random.choice(range(100)), random.choice(range(1,6)),
                    random.choice(['C','PF','SF','SG','PG']), random_stat(luck[0]), random_stat(luck[0]), random_stat(luck[0]), random_stat(luck[0]),
                      random_stat(luck[0]),  random_stat(luck[0]),  random_stat(luck[0]), luck[0], country)
        teams[i].players[player.position].append(player)
        print(f'{teams[i].color}{teams[i].name}{reset} sign unrestricted free agent {player.name} {country.color}{country.name}{reset} {player.position} {player.print_height}, Stats: {player.inner_attack} {player.outer_attack} {player.inner_defense} {player.outer_defense} {player.iq} {player.passing} {player.physical}')
        next_id += 1

  for team in teams:
    for position, players in team.players.items():
      players.sort(key=lambda x: x.ovr, reverse=True)

  return next_id