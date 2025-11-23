import pandas as pd
from basketball.team import Team
from basketball.game import simulate_game
from basketball.playoff_series import PlayoffSeries
from basketball.constants import reset

def simulate_playoffs(df, teams: list[Team], records: dict, year: int = 1):
    for team in teams:
      team.clear_season_stats()
    top8 = df.head(8).index.to_numpy()
    po_teams = []
    cur_teams = []
    for i in top8:
      po_teams.append(teams[i])
      cur_teams.append(teams[i])
      teams[i].playoff_appearances += 1
    schedule = []
    for i in range(4):
      schedule.append(PlayoffSeries(cur_teams[i],cur_teams[7-i]))

    for i in range(7):
      for s in schedule:
        if s.wins1 != 4 and s.wins2 != 4:
          if i%2:
            winner, summary = simulate_game(s.team2, s.team1, 0.01, records)
            if winner:
              s.wins2 += 1
            else:
              s.wins1 += 1
          else:
            winner, summary = simulate_game(s.team1, s.team2, 0.01, records)
            if winner:
              s.wins1 += 1
            else:
              s.wins2 += 1
          print(f'\n\nSeries Record {s.team1.color}{s.team1.abbr}{reset} {s.wins1}-{s.wins2} {s.team2.color}{s.team2.abbr}{reset}')
          print(summary)

    cur_teams = []
    for s in schedule:
      if s.wins1 == 4:
        cur_teams.append(s.team1)
      else:
        cur_teams.append(s.team2)

    schedule = []
    for i in range(2):
      schedule.append(PlayoffSeries(cur_teams[i],cur_teams[3-i]))

    for i in range(7):
      for s in schedule:
        if s.wins1 != 4 and s.wins2 != 4:
          if i%2:
            winner, summary = simulate_game(s.team2, s.team1, 0.01, records)
            if winner:
              s.wins2 += 1
            else:
              s.wins1 += 1
          else:
            winner, summary = simulate_game(s.team1, s.team2, 0.01, records)
            if winner:
              s.wins1 += 1
            else:
              s.wins2 += 1
          print(f'\n\nSeries Record {s.team1.color}{s.team1.abbr}{reset} {s.wins1}-{s.wins2} {s.team2.color}{s.team2.abbr}{reset}')
          print(summary)

    cur_teams = []
    for s in schedule:
      if s.wins1 == 4:
        cur_teams.append(s.team1)
      else:
        cur_teams.append(s.team2)

    final = PlayoffSeries(cur_teams[0],cur_teams[1])
    count = 0
    while(final.wins1 != 4 and final.wins2 != 4):
        if count%2:
          winner, summary = simulate_game(final.team2, final.team1, 0.01, records, True, True, True)
          if winner:
            final.wins2 += 1
          else:
            final.wins1 += 1
        else:
          winner, summary = simulate_game(final.team1, final.team2, 0.01, records, True, True, True)
          if winner:
            final.wins1 += 1
          else:
            final.wins2 += 1
        count += 1
        print(f'\n\nSeries Record {final.team1.color}{final.team1.abbr}{reset} {final.wins1}-{final.wins2} {final.team2.color}{final.team2.abbr}{reset}')
        print(summary)
    if final.wins1 == 4:
      winner = final.team1
    else:
      winner = final.team2

    winner.championships += 1
    for player in winner.get_players():
      player.awards['VBL Champion'] += 1
    print(f'{winner.color}{winner.name}{reset} wins the Valtara Basketball League!')

    # win record
    if winner.season_losses < records['best_playoff_record_team'][1]:
      records['best_playoff_record_team'] = (winner.season_wins, winner.season_losses, winner.name, year)

    player_df = pd.DataFrame(columns=['Player','Country','Team','Position','Age','Height','OVR','PTS','REB','AST','BLK','STL','TOV','PM','MIN','GP'])
    best = 0
    best_player = None
    best_pos_pts = {'C': 0, 'PG': 0, 'SG': 0, 'PF': 0, 'SF': 0}
    best_pos_plr = {'C': None, 'PG': None, 'SG': None, 'PF': None, 'SF': None}
    for team in po_teams:
      for player in team.get_players():
        score = ((player.season_stats['PTS']*4/3) + (player.season_stats['AST']*3/2) + (player.season_stats['REB']) + (player.season_stats['BLK']*2) + (player.season_stats['STL']*2) - (player.season_stats['TOV']*2)-(player.season_stats['MIN']/3))
        if team.name == winner.name:
          score += 500
        if score > best:
          best = score
          best_player = player
          best_pos_pts[player.position] = score
          best_pos_plr[player.position] = player
        elif score > best_pos_pts[player.position]:
          best_pos_pts[player.position] = score
          best_pos_plr[player.position] = player
        player_df.loc[len(player_df)] = [player.name, f"{player.country.color}{player.country.name}{reset}", f"{team.color}{team.name}{reset}", player.position, player.age, player.print_height, round(player.ovr,1),
                                         player.season_stats['PTS'],player.season_stats['REB'],player.season_stats['AST'],player.season_stats['BLK'],player.season_stats['STL'],player.season_stats['TOV'],
                                         player.season_stats['PM'],player.season_stats['MIN'],player.season_stats['GP']]
    player_df = player_df.sort_values(by='PTS',ascending=False)

    # award FMVP, Champion, TOF
    print("\nTeam of the Finals:")
    for pos in {'C','PF','SF','PG','SG'}:
      best_pos_plr[pos].awards['TOF'] += 1
      print(pos + ': ' + best_pos_plr[pos].name)
    best_player.awards['Finals MVP'] += 1
    print(best_player.name, "wins Finals MVP!")

    # records
    for team in po_teams:
      team_triple_doubles = 0
      team_double_doubles = 0
      for player in team.get_players():
        if player.season_stats['PTS'] > records['most_playoff_points_indi'][0]:
          records['most_playoff_points_indi'] = (player.season_stats['PTS'], player.name, team.name, year)
        if player.season_stats['AST'] > records['most_playoff_assists_indi'][0]:
          records['most_playoff_assists_indi'] = (player.season_stats['AST'], player.name, team.name, year)
        if player.season_stats['REB'] > records['most_playoff_rebounds_indi'][0]:
          records['most_playoff_rebounds_indi'] = (player.season_stats['REB'], player.name, team.name, year)
        if player.season_stats['BLK'] > records['most_playoff_blocks_indi'][0]:
          records['most_playoff_blocks_indi'] = (player.season_stats['BLK'], player.name, team.name, year)
        if player.season_stats['STL'] > records['most_playoff_steals_indi'][0]:
          records['most_playoff_steals_indi'] = (player.season_stats['STL'], player.name, team.name, year)
        if player.season_stats['TD'] > records['most_playoff_triple_doubles_indi'][0]:
          records['most_playoff_triple_doubles_indi'] = (player.season_stats['TD'], player.name, team.name, year)
        # if player.season_stats['DD'] > records['most_playoff_double_doubles_indi'][0]:
        #   records['most_playoff_double_doubles_indi'] = (player.season_stats['DD'], player.name, team.name, year)
        team_triple_doubles += player.season_stats['TD']
        # team_double_doubles += player.season_stats['DD']
      if team_triple_doubles > records['most_playoff_triple_doubles_team'][0]:
        records['most_playoff_triple_doubles_team'] = (team_triple_doubles, team.name, year)
      # if team_double_doubles > records['most_playoff_double_doubles_team'][0]:
      #   records['most_playoff_double_doubles_team'] = (team_double_doubles, team.name, year)

    for team in teams:
      team.clear_season_stats()
    return player_df