import pandas as pd
from basketball.game import simulate_game
from basketball.team import Team
from basketball.round_robin import roundRobin
from .constants import reset

def simulate_season(teams: list[Team], records: dict, year: int = 1):
    df = pd.DataFrame(columns=['Team','W','L'])
    for i in teams:
      df.loc[len(df)] = [f"{i.color}{i.name}{reset}", 0, 0]
    schedule = roundRobin(teams)
    for gameday in schedule:
      for game in gameday:
        winner,summary = simulate_game(game[0],game[1],0.01,records)
        if winner:
          df.loc[game[0].id,'W'] += 1
          df.loc[game[1].id,'L'] += 1
        else:
          df.loc[game[0].id,'L'] += 1
          df.loc[game[1].id,'W'] += 1
    df = df.sort_values(by=['W'], ascending=False)

    bonus_points = df.head(8)['Team']
    super_bonus_points = df.head(3)['Team']

    player_df = pd.DataFrame(columns=['Player','Country','Team','Position','Age','Height','OVR','PTS','REB','AST','BLK','STL','TOV','PM','MIN','GP'])
    seasonal_stats = {'PTS','REB','AST','BLK','STL'}
    best = 0
    best_player = None
    best_stats_pts = {'PTS':0, 'REB':0, 'AST':0, 'BLK':0, 'STL':0}
    best_stats_plr = {'PTS':None, 'REB':None, 'AST':None, 'BLK':None, 'STL':None}
    best_pos_pts = {'C': 0, 'PG': 0, 'SG': 0, 'PF': 0, 'SF': 0}
    best_pos_plr = {'C': None, 'PG': None, 'SG': None, 'PF': None, 'SF': None}
    for team in teams:
      for player in team.get_players():
        score = ((player.season_stats['PTS']*4/3) + (player.season_stats['AST']*3/2) + (player.season_stats['REB']) + (player.season_stats['BLK']*2) + (player.season_stats['STL']*2) - (player.season_stats['TOV']*2)-(player.season_stats['MIN']/3))
        if team.name in bonus_points:
          score += 150
        if team.name in super_bonus_points:
          score += 250
        if score > best and player.season_stats['MIN']>600:
          best = score
          best_player = player
          best_pos_pts[player.position] = score
          best_pos_plr[player.position] = player
        elif score > best_pos_pts[player.position]:
          best_pos_pts[player.position] = score
          best_pos_plr[player.position] = player
        for stat in seasonal_stats:
          if player.season_stats[stat] > best_stats_pts[stat]:
            best_stats_pts[stat] = player.season_stats[stat]
            best_stats_plr[stat] = player
        player_df.loc[len(player_df)] = [player.name, f"{player.country.color}{player.country.name}{reset}", f"{team.color}{team.name}{reset}", player.position, player.age, player.print_height, round(player.ovr,1),
                                         player.season_stats['PTS'],player.season_stats['REB'],player.season_stats['AST'],player.season_stats['BLK'],player.season_stats['STL'],player.season_stats['TOV'],
                                         player.season_stats['PM'],player.season_stats['MIN'],player.season_stats['GP']]
    player_df = player_df.sort_values(by='PTS',ascending=False)
    print("Golden Awards:")
    best_stats_plr['PTS'].awards['Golden Bucket'] += 1
    print(f"Golden Bucket: {best_stats_plr['PTS'].name} ({best_stats_plr['PTS'].season_stats['PTS']})")
    best_stats_plr['REB'].awards['Golden Board'] += 1
    print(f"Golden Board: {best_stats_plr['REB'].name} ({best_stats_plr['REB'].season_stats['REB']})")
    best_stats_plr['AST'].awards['Golden Dime'] += 1
    print(f"Golden Dime: {best_stats_plr['AST'].name} ({best_stats_plr['AST'].season_stats['AST']})")
    best_stats_plr['BLK'].awards['Golden Stuff'] += 1
    print(f"Golden Stuff: {best_stats_plr['BLK'].name} ({best_stats_plr['BLK'].season_stats['BLK']})")
    best_stats_plr['STL'].awards['Golden Hands'] += 1
    print(f"Golden Hands: {best_stats_plr['STL'].name} ({best_stats_plr['STL'].season_stats['STL']})")
    print("\nTeam of the Season:")
    for pos in {'C','PF','SF','PG','SG'}:
      best_pos_plr[pos].awards['TOTS'] += 1
      print(pos + ': ' + best_pos_plr[pos].name)
    best_player.awards['MVP'] += 1
    print(best_player.name, "wins MVP!")

    # season records
    for team in teams:
      if team.season_wins > records['most_season_games_won_team'][0]:
        records['most_season_games_won_team'] = (team.season_wins, team.name, year)
      if team.season_wins < records['least_season_games_won_team'][0]:
        records['least_season_games_won_team'] = (team.season_wins, team.name, year)
      team_triple_doubles = 0
      team_double_doubles = 0
      for player in team.get_players():
        if player.season_stats['PTS'] > records['most_season_points_indi'][0]:
          records['most_season_points_indi'] = (player.season_stats['PTS'], player.name, year)
        if player.season_stats['AST'] > records['most_season_assists_indi'][0]:
          records['most_season_assists_indi'] = (player.season_stats['AST'], player.name, year)
        if player.season_stats['REB'] > records['most_season_rebounds_indi'][0]:
          records['most_season_rebounds_indi'] = (player.season_stats['REB'], player.name, year)
        if player.season_stats['BLK'] > records['most_season_blocks_indi'][0]:
          records['most_season_blocks_indi'] = (player.season_stats['BLK'], player.name, year)
        if player.season_stats['STL'] > records['most_season_steals_indi'][0]:
          records['most_season_steals_indi'] = (player.season_stats['STL'], player.name, year)
        if player.season_stats['TD'] > records['most_season_triple_doubles_indi'][0]:
          records['most_season_triple_doubles_indi'] = (player.season_stats['TD'], player.name, year)
        # if player.season_stats['DD'] > records['most_season_double_doubles_indi'][0]:
        #   records['most_season_double_doubles_indi'] = (player.season_stats['DD'], player.name, f"{team.name} {team.points}-{team.opp_points} {team.opp_name}", year)
        team_triple_doubles += player.season_stats['TD']
        # team_double_doubles += player.season_stats['DD']
      if team_triple_doubles > records['most_season_triple_doubles_team'][0]:
        records['most_season_triple_doubles_team'] = (team_triple_doubles, team.name, year)

    # award MVP, TOTS, Golden awards
    return df, player_df