import pandas as pd
from basketball.offseason import simulate_offseason
from basketball.playoffs import simulate_playoffs
from basketball.season import simulate_season
from basketball.team import Team
from basketball.util import generate_new_players, determine_draft_order
from basketball.constants import reset

def simulate_full(teams: list[Team], seasons: int, next_id: int, draft_order: list[int] = None, retired: list = [], year: int = 1, records: dict = {}):
  full_player_df = pd.DataFrame(columns=['Player','Country','Position','Age','Status','OVR','PTS','REB','AST','BLK','STL','TOV','PM','MIN','GP','MVP',"FMVP",'Championships','Luck'])

  # initial pre-season
  print("\nPre-season:")
  if not draft_order:
    draft_order = list(range(len(teams)))
    draft_order.extend(list(range(len(teams)-1, -1, -1)))

  next_id = generate_new_players(draft_order, teams, next_id, range(20,35))

  while min([len(team.get_players()) for team in teams]) < 15:
    next_id = generate_new_players(draft_order, teams, next_id, range(20,35))

  for i in range(seasons):
    print(f"Season {i}:")
    df,player_df = simulate_season(teams, records, year)
    print("")
    print(df)
    print("")
    print("Top Scorers:")
    print(player_df.head(10))
    print("")
    print("Playoffs:")
    finals_players = simulate_playoffs(df, teams, records, year)
    print("")
    print("Top Scorers:")
    print(finals_players.head(10))
    print("\nOff-season:")
    retiring, next_id = simulate_offseason(teams, next_id, df)
    print("\nRetiring Players:")
    for player in retiring:
      print(player)
      retired.append(player)
    year += 1

  print("\nAll-time Results\nTeams:")
  for team in teams:
    print(f"{team.color}{team.name}{reset}", team.championships, team.playoff_appearances)

  for player in retired:
    full_player_df.loc[len(full_player_df)] = [player.name, f"{player.country.color}{player.country.name}{reset}", player.position, player.age, 'Retired', player.ovr, player.lifetime_stats['PTS'],player.lifetime_stats['REB'],player.lifetime_stats['AST'],player.lifetime_stats['BLK'],\
                                    player.lifetime_stats['STL'],player.lifetime_stats['TOV'],player.lifetime_stats['PM'],player.lifetime_stats['MIN'],player.lifetime_stats['GP'],player.awards['MVP'],player.awards['Finals MVP'],\
                                               player.awards['VBL Champion'],player.luck]

  for team in teams:
    for player in team.get_players():
      full_player_df.loc[len(full_player_df)] = [player.name, f"{player.country.color}{player.country.name}{reset}", player.position, player.age, 'Active', player.ovr, player.lifetime_stats['PTS'],player.lifetime_stats['REB'],player.lifetime_stats['AST'],player.lifetime_stats['BLK'],\
                                         player.lifetime_stats['STL'],player.lifetime_stats['TOV'],player.lifetime_stats['PM'],player.lifetime_stats['MIN'],player.lifetime_stats['GP'],player.awards['MVP'],player.awards['Finals MVP'],\
                                                 player.awards['VBL Champion'],player.luck]
  full_player_df = full_player_df.sort_values(by='PTS',ascending=False)
  print("\nPlayers:")
  print(full_player_df.head(50))
  draft_order = determine_draft_order(df, teams)
  for team in teams:
    team.clear_season_stats()
    team.reset()
  return full_player_df, retired, draft_order