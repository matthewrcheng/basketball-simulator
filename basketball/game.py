import numpy as np
import random
from basketball.team import Team
from basketball.util import *
from .constants import *
from .display import *

def simulate_game(team1: Team, team2: Team, adv, records, show_summary=False, show_box_score=False, show_scoring_trend=False, show_pbp=False, year: int = 1):
    team1.adv = adv

    team1_ready = team1.set_starting_lineup()
    team2_ready = team2.set_starting_lineup()

    if not team1_ready:
      print(f"{team1.name} forfeited due to squad size!")
      return False, None
    if not team2_ready:
      print(f"{team2.name} forfeited due to squad size!")
      return True, None

    current_team = team1
    opposing_team = team2

    # 4 quarters
    i = 0
    game_seconds = 0
    while True:
      current_team.quarter_fouls = 0
      opposing_team.quarter_fouls = 0
      if i > 3:
        total_seconds = 300
        if show_pbp:
          print(f"------------Starting Overtime {i-3}-------------")
      else:
        total_seconds = 720
        if show_pbp:
          print(f"------------Starting Quarter {i+1}-------------")
      game_seconds += total_seconds
      while total_seconds > 0:
        # decide outcome
        if total_seconds < 24:
          seconds = np.random.normal(total_seconds/2 + 1, total_seconds/4)
        else:
          seconds = np.random.normal(14, 7)

        if seconds < 2 or seconds > min(24, total_seconds):
            seconds = max(0, min(min(24, total_seconds), seconds))
            result = PossessionResult.TURNOVER
        else:
            result = random.choices(
                [PossessionResult.SHOT, PossessionResult.TURNOVER, PossessionResult.FOUL],
                weights=[89.5, 1, 18.5],
                k=1
            )[0]
        total_seconds -= seconds

        for player in current_team.get_active_players():
          player.current_seconds += seconds
          player.game_stats['MIN'] += seconds/60

        for player in opposing_team.get_active_players():
          player.current_seconds += seconds
          player.game_stats['MIN'] += seconds/60

        # play out result
        if result == PossessionResult.SHOT:
            current_team.shots += 1
            if np.random.random() < current_team.distance_playstyle:
                # 2 point attempt
                current_team.shots2 += 1
                shooter = decide_shooter(2, current_team)
                shooter.game_stats['FGA'] += 1
                outcome = np.random.random()
                if outcome < 0.07:
                    opposing_team.blocks += 1
                    blocker = decide_blocker(2, opposing_team)
                    blocker.game_stats["BLK"] += 1
                    if np.random.random() < 0.4:
                        if show_pbp:
                          print(f"{current_team.color}{shooter.name}'s ({current_team.name}){reset} 2 point shot blocked by {opposing_team.color}{blocker.name} ({opposing_team.name}){reset}! {opposing_team.color}{opposing_team.name}{reset} with possession.")
                        current_team,opposing_team = opposing_team,current_team
                    else:
                        if show_pbp:
                          print(f"{current_team.color}{shooter.name}'s ({current_team.name}){reset} 2 point shot blocked by {opposing_team.color}{blocker.name} ({opposing_team.name}){reset}! Possession maintained by {current_team.color}{current_team.name}{reset}.")
                elif outcome < 0.07 + (0.38 - (shooter.inner_attack/100) + 0.05 - current_team.adv):
                    rebounder, off_reb = decide_rebounder(current_team, opposing_team)
                    rebounder.game_stats["REB"] += 1
                    if off_reb:
                        rebounder.game_stats["OREB"] += 1
                        current_team.rebounds += 1
                        if show_pbp:
                          print(f"{current_team.color}{shooter.name} ({current_team.name}){reset} misses 2 point shot. Offensive rebound by {current_team.color}{rebounder.name} ({current_team.name}){reset}!")
                    else:
                        rebounder.game_stats["DREB"] += 1
                        opposing_team.rebounds += 1
                        if show_pbp:
                          print(f"{current_team.color}{shooter.name} ({current_team.name}){reset} misses 2 point shot. Rebound by {opposing_team.color}{rebounder.name} ({opposing_team.name}){reset}!")
                        current_team,opposing_team = opposing_team,current_team
                else:
                    shooter.game_stats['PTS'] += 2
                    shooter.game_stats['FGM'] += 1
                    current_team.points += 2
                    current_team.shots2_made += 1
                    for player in current_team.get_active_players():
                        player.game_stats['PM'] += 2
                    for player in opposing_team.get_active_players():
                        player.game_stats['PM'] -= 2
                    if np.random.random() < 0.63:
                        assister = decide_assister(shooter, current_team)
                        assister.game_stats['AST'] += 1
                        current_team.assists += 1
                        if show_pbp:
                          print(f"{current_team.color}{shooter.name} ({current_team.name}){reset} scored a 2 point shot with an assist!")
                    else:
                        if show_pbp:
                          print(f"{current_team.color}{shooter.name} ({current_team.name}){reset} scored a 2 point shot!")
                    points_streak = check_streak(2, current_team, team1, team2)
                    if points_streak > 3:
                        if show_pbp:
                          print(f"{current_team.color}{current_team.name}{reset} has scored {orange}{points_streak}{reset} points in a row!")
                    current_team,opposing_team = opposing_team,current_team
            else:
                # 3 point attempt
                current_team.shots3 += 1
                shooter = decide_shooter(3, current_team)
                shooter.game_stats['FGA'] += 1
                shooter.game_stats['TPA'] += 1
                outcome = np.random.random()
                if outcome < 0.04:
                    opposing_team.blocks += 1
                    blocker = decide_blocker(2, opposing_team)
                    blocker.game_stats["BLK"] += 1
                    if np.random.random() < 0.4:
                        if show_pbp:
                          print(f"{current_team.color}{shooter.name}'s ({current_team.name}){reset} 3 point shot blocked by {opposing_team.color}{blocker.name} ({opposing_team.name}){reset}! {opposing_team.color}{opposing_team.name}{reset} with possession.")
                        current_team,opposing_team = opposing_team,current_team
                    else:
                        if show_pbp:
                          print(f"{current_team.color}{shooter.name}'s ({current_team.name}){reset} 3 point shot blocked by {opposing_team.color}{blocker.name} ({opposing_team.name}){reset}! Possession maintained by {current_team.color}{current_team.name}{reset}.")
                elif outcome < 0.04 + (0.595 - (shooter.outer_attack/100) + 0.05 - current_team.adv):
                    rebounder, off_reb = decide_rebounder(current_team, opposing_team)
                    rebounder.game_stats["REB"] += 1
                    if off_reb:
                        rebounder.game_stats["OREB"] += 1
                        current_team.rebounds += 1
                        if show_pbp:
                          print(f"{current_team.color}{shooter.name} ({current_team.name}){reset} misses 3 point shot. Offensive rebound by {current_team.color}{rebounder.name} ({current_team.name}){reset}!")
                    else:
                        rebounder.game_stats["DREB"] += 1
                        opposing_team.rebounds += 1
                        if show_pbp:
                          print(f"{current_team.color}{shooter.name} ({current_team.name}){reset} misses 3 point shot. Rebound by {opposing_team.color}{rebounder.name} ({opposing_team.name}){reset}!")
                        current_team,opposing_team = opposing_team,current_team
                else:
                    current_team.points += 3
                    current_team.shots3_made += 1
                    shooter.game_stats['PTS'] += 3
                    shooter.game_stats['FGM'] += 1
                    shooter.game_stats['TPM'] += 1
                    for player in current_team.get_active_players():
                        player.game_stats['PM'] += 3
                    for player in opposing_team.get_active_players():
                        player.game_stats['PM'] -= 3
                    if np.random.random() < 0.63:
                        assister = decide_assister(shooter, current_team)
                        assister.game_stats['AST'] += 1
                        current_team.assists += 1
                        if show_pbp:
                          print(f"{current_team.color}{shooter.name} ({current_team.name}){reset} scored a 3 point shot with an assist!")
                    else:
                        if show_pbp:
                          print(f"{current_team.color}{shooter.name} ({current_team.name}){reset} scored a 3 point shot!")
                    points_streak = check_streak(3, current_team, team1, team2)
                    if points_streak > 3:
                        if show_pbp:
                          print(f"{current_team.color}{current_team.name}{reset} has scored {orange}{points_streak}{reset} points in a row!")
                    current_team,opposing_team = opposing_team,current_team

        elif result == PossessionResult.FOUL:
            opposing_team.fouls += 1
            opposing_team.quarter_fouls += 1
            fouler = decide_fouler(opposing_team)
            fouler.game_stats['PF'] += 1
            if fouler.game_stats['PF'] == 6:
                fouler.fouled_out = True
                if show_pbp:
                  print(f"{opposing_team.color}{fouler.name}{reset} fouled out of the game!")
                opposing_team.decide_substitutions(show_pbp)
            if np.random.random() < 0.7 or opposing_team.quarter_fouls > 4:
                shooter = decide_shooter(2, current_team)
                if np.random.random() < 0.282:
                    current_team.shots += 1
                    current_team.fts += 1
                    shooter.game_stats['FGA'] += 1
                    shooter.game_stats['FGM'] += 1
                    if np.random.random() < current_team.distance_playstyle:
                        current_team.shots2 += 1
                        current_team.points += 2
                        current_team.shots2_made += 1
                        shooter.game_stats['PTS'] += 2
                        for player in current_team.get_active_players():
                            player.game_stats['PM'] += 2
                        for player in opposing_team.get_active_players():
                            player.game_stats['PM'] -= 2
                        points_streak = check_streak(2, current_team, team1, team2)
                        if points_streak > 3:
                            if show_pbp:
                              print(f"{current_team.color}{current_team.name}{reset} has scored {orange}{points_streak}{reset} points in a row!")
                        if show_pbp:
                          print(f"And-1 for {current_team.color}{shooter.name} ({current_team.name}){reset} off a 2 point shot!")
                        if np.random.random() < 0.63:
                            current_team.assists += 1
                            assister = decide_assister(shooter, current_team)
                            assister.game_stats['AST'] += 1
                    else:
                        current_team.shots3 += 1
                        current_team.points += 3
                        current_team.shots3_made += 1
                        shooter.game_stats['PTS'] += 3
                        shooter.game_stats['TPA'] += 1
                        shooter.game_stats['TPM'] += 1
                        for player in current_team.get_active_players():
                            player.game_stats['PM'] += 3
                        for player in opposing_team.get_active_players():
                            player.game_stats['PM'] -= 3
                        points_streak = check_streak(3, current_team, team1, team2)
                        if points_streak > 3:
                            if show_pbp:
                              print(f"{current_team.color}{current_team.name}{reset} has scored {orange}{points_streak}{reset} points in a row!")
                        if show_pbp:
                          print(f"And-1 for {current_team.color}{shooter.name} ({current_team.name}){reset} off a 3 point shot!")
                        if np.random.random() < 0.63:
                            current_team.assists += 1
                            assister = decide_assister(shooter, current_team)
                            assister.game_stats['AST'] += 1
                    if decide_free_throw(shooter, current_team.adv):
                        shooter.game_stats['FTM'] += 1
                        shooter.game_stats['FTA'] += 1
                        shooter.game_stats['PTS'] += 1
                        current_team.points += 1
                        current_team.fts_made += 1
                        for player in current_team.get_active_players():
                            player.game_stats['PM'] += 1
                        for player in opposing_team.get_active_players():
                            player.game_stats['PM'] -= 1
                        points_streak = check_streak(1, current_team, team1, team2)
                        if points_streak > 3:
                            if show_pbp:
                              print(f"{current_team.color}{current_team.name}{reset} has scored {orange}{points_streak}{reset} points in a row!")
                        if show_pbp:
                          print(f"{current_team.color}{shooter.name} ({current_team.name}){reset} scored the free throw!")
                        current_team,opposing_team = opposing_team,current_team
                    else:
                        shooter.game_stats['FTA'] += 1
                        rebounder, off_reb = decide_rebounder(current_team, opposing_team)
                        rebounder.game_stats["REB"] += 1
                        if off_reb:
                            rebounder.game_stats["OREB"] += 1
                            current_team.rebounds += 1
                            if show_pbp:
                              print(f"{current_team.color}{shooter.name} ({current_team.name}){reset} missed the free throw. Offensive rebound by {current_team.color}{rebounder.name} ({current_team.name}){reset}!")
                        else:
                            rebounder.game_stats["DREB"] += 1
                            opposing_team.rebounds += 1
                            if show_pbp:
                              print(f"{current_team.color}{shooter.name} ({current_team.name}){reset} missed the free throw. Rebound by {opposing_team.color}{rebounder.name} ({opposing_team.name}){reset}!")
                            current_team,opposing_team = opposing_team,current_team
                else:
                    if opposing_team.quarter_fouls > 4:
                        if show_pbp:
                          print(f"Foul by {opposing_team.color}{fouler.name} ({opposing_team.name}){reset}. {current_team.color}{current_team.name}{reset} is in the bonus. Shooting 2 free throws.")
                    else:
                        if show_pbp:
                          print(f"Shooting foul by {opposing_team.color}{fouler.name} ({opposing_team.name}){reset}. Shooting 2 free throws.")
                    current_team.fts += 2
                    # first shot
                    if decide_free_throw(shooter, current_team.adv):
                        current_team.points += 1
                        current_team.fts_made += 1
                        shooter.game_stats['FTM'] += 1
                        shooter.game_stats['FTA'] += 1
                        shooter.game_stats['PTS'] += 1
                        for player in current_team.get_active_players():
                            player.game_stats['PM'] += 1
                        for player in opposing_team.get_active_players():
                            player.game_stats['PM'] -= 1
                        points_streak = check_streak(1, current_team, team1, team2)
                        if points_streak > 3:
                            if show_pbp:
                              print(f"{current_team.color}{current_team.name}{reset} has scored {orange}{points_streak}{reset} points in a row!")
                        if show_pbp:
                          print(f"{current_team.color}{shooter.name} ({current_team.name}){reset} scored the first free throw!")
                    else:
                        shooter.game_stats['FTA'] += 1
                        if show_pbp:
                          print(f"{current_team.color}{shooter.name} ({current_team.name}){reset} missed the first free throw.")
                    # second shot
                    if decide_free_throw(shooter, current_team.adv):
                        shooter.game_stats['FTM'] += 1
                        shooter.game_stats['FTA'] += 1
                        shooter.game_stats['PTS'] += 1
                        current_team.points += 1
                        current_team.fts_made += 1
                        for player in current_team.get_active_players():
                            player.game_stats['PM'] += 1
                        for player in opposing_team.get_active_players():
                            player.game_stats['PM'] -= 1
                        points_streak = check_streak(1, current_team, team1, team2)
                        if points_streak > 3:
                            if show_pbp:
                              print(f"{current_team.color}{current_team.name}{reset} has scored {orange}{points_streak}{reset} points in a row!")
                        if show_pbp:
                          print(f"{current_team.color}{shooter.name} ({current_team.name}){reset} scored the second free throw!")
                        current_team,opposing_team = opposing_team,current_team
                    else:
                        shooter.game_stats['FTA'] += 1
                        rebounder, off_reb = decide_rebounder(current_team, opposing_team)
                        rebounder.game_stats["REB"] += 1
                        if off_reb:
                            rebounder.game_stats["OREB"] += 1
                            current_team.rebounds += 1
                            if show_pbp:
                              print(f"{current_team.color}{shooter.name} ({current_team.name}){reset} missed the second free throw. Offensive rebound by {current_team.color}{rebounder.name} {current_team.name}{reset}!")
                        else:
                            rebounder.game_stats["DREB"] += 1
                            opposing_team.rebounds += 1
                            if show_pbp:
                              print(f"{current_team.color}{shooter.name} ({current_team.name}){reset} missed the second free throw. Rebound by {opposing_team.color}{rebounder.name} {opposing_team.name}{reset}!")
                            current_team,opposing_team = opposing_team,current_team
            else:
                if show_pbp:
                  print(f"Foul by {opposing_team.color}{fouler.name} ({opposing_team.name}){reset}.")
        elif result == PossessionResult.TURNOVER:
            current_team.turnovers += 1
            turnoverer = decide_turnoverer(current_team)
            turnoverer.game_stats['TOV'] += 1
            if np.random.random() < 0.4:
                opposing_team.steals += 1
                stealer = decide_stealer(2, opposing_team)
                stealer.game_stats['STL'] += 1
                if show_pbp:
                  print(f"Steal by {opposing_team.color}{stealer.name} ({opposing_team.name}){reset}!")
            else:
                if show_pbp:
                  print(f"Turnover by {current_team.color}{turnoverer.name} ({current_team.name}){reset}!")
            current_team,opposing_team = opposing_team,current_team
        if show_pbp:
          print(f"{round(seconds,1)} seconds elapsed during possession, {int(total_seconds//60)}:{total_seconds%60:04.1f} remaining. {team1.color}{team1.name}{reset} {team1.points} - {team2.points} {team2.color}{team2.name}{reset}")
        current_team.scoring_trend.append(((720*i)+720-total_seconds, current_team.points))
        opposing_team.scoring_trend.append(((720*i)+720-total_seconds,opposing_team.points))
        team1.decide_substitutions(show_pbp)
        team2.decide_substitutions(show_pbp)
        injured_player1 = check_injury(current_team, current_team.get_active_players(), show_pbp)
        injured_player2 = check_injury(opposing_team, opposing_team.get_active_players(), show_pbp)
        if injured_player1 is not None:
          current_team.decide_substitutions(show_pbp)
        if injured_player2 is not None:
          opposing_team.decide_substitutions(show_pbp)
      i += 1
      if i >= 4 and team1.points != team2.points:
        break

    winner = 1
    # decide winner
    if team1.points > team2.points:
      winner = 1
      team1.wins += 1
      team1.season_wins += 1
      team2.losses += 1
      team2.season_losses += 1
      if show_pbp:
        print(f"{team1.color}{team1.name}{reset} wins!")
    else:
      winner = 0
      team2.wins += 1
      team2.season_wins += 1
      team1.losses += 1
      team1.season_losses += 1
      if show_pbp:
        print(f"{team2.color}{team2.name}{reset} wins!")
    team1.season_net_points += team1.points - team2.points
    team2.season_net_points -= team1.points + team2.points

    # Print summary
    summary = print_summary(team1, team2)
    # if show_summary:
    #   print(summary)
    if show_box_score:
      print_box_score(team1)
      print_box_score(team2)
    if show_scoring_trend:
      plot_scoring_trend(team1, team2, game_seconds)

    # team records
    if team1.points > records['most_points_team'][0]:
      records['most_points_team'] = (team1.points, team1.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
    elif team2.points > records['most_points_team'][0]:
      records['most_points_team'] = (team2.points, team2.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
    elif team1.points < records['least_points_team'][0]:
      records['least_points_team'] = (team1.points, team1.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
    elif team2.points < records['least_points_team'][0]:
      records['least_points_team'] = (team2.points, team2.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)

    if team1.rebounds > records['most_rebounds_team'][0]:
      records['most_rebounds_team'] = (team1.rebounds, team1.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
    elif team2.rebounds > records['most_rebounds_team'][0]:
      records['most_rebounds_team'] = (team2.rebounds, team2.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
    elif team1.rebounds < records['least_rebounds_team'][0]:
      records['least_rebounds_team'] = (team1.rebounds, team1.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
    elif team2.rebounds < records['least_rebounds_team'][0]:
      records['least_rebounds_team'] = (team2.rebounds, team2.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)

    if team1.assists > records['most_assists_team'][0]:
      records['most_assists_team'] = (team1.assists, team1.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
    elif team2.assists > records['most_assists_team'][0]:
      records['most_assists_team'] = (team2.assists, team2.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
    elif team1.assists < records['least_assists_team'][0]:
      records['least_assists_team'] = (team1.assists, team1.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
    elif team2.assists < records['least_assists_team'][0]:
      records['least_assists_team'] = (team2.assists, team2.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)

    if team1.blocks > records['most_blocks_team'][0]:
      records['most_blocks_team'] = (team1.blocks, team1.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
    elif team2.blocks > records['most_blocks_team'][0]:
      records['most_blocks_team'] = (team2.blocks, team2.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
    elif team1.blocks < records['least_blocks_team'][0]:
      records['least_blocks_team'] = (team1.blocks, team1.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
    elif team2.blocks < records['least_blocks_team'][0]:
      records['least_blocks_team'] = (team2.blocks, team2.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)

    if team1.steals > records['most_steals_team'][0]:
      records['most_steals_team'] = (team1.steals, team1.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
    elif team2.steals > records['most_steals_team'][0]:
      records['most_steals_team'] = (team2.steals, team2.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
    elif team1.steals < records['least_steals_team'][0]:
      records['least_steals_team'] = (team1.steals, team1.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
    elif team2.steals < records['least_steals_team'][0]:
      records['least_steals_team'] = (team2.steals, team2.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)

    if team1.turnovers > records['most_turnovers_team'][0]:
      records['most_turnovers_team'] = (team1.turnovers, team1.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
    elif team2.turnovers > records['most_turnovers_team'][0]:
      records['most_turnovers_team'] = (team2.turnovers, team2.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
    elif team1.turnovers < records['least_turnovers_team'][0]:
      records['least_turnovers_team'] = (team1.turnovers, team1.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
    elif team2.turnovers < records['least_turnovers_team'][0]:
      records['least_turnovers_team'] = (team2.turnovers, team2.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)

    if team1.shots3_made > records['most_3pt_team'][0]:
      records['most_3pt_team'] = (team1.shots3_made, team1.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
    elif team2.shots3_made > records['most_3pt_team'][0]:
      records['most_3pt_team'] = (team2.shots3_made, team2.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
    elif team1.shots3_made < records['least_3pt_team'][0]:
      records['least_3pt_team'] = (team1.shots3_made, team1.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
    elif team2.shots3_made < records['least_3pt_team'][0]:
      records['least_3pt_team'] = (team2.shots3_made, team2.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)

    if team1.shots2_made + team1.shots3_made > records['most_fg_team'][0]:
      records['most_fg_team'] = (team1.shots2_made + team1.shots3_made, team1.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
    elif team2.shots2_made + team2.shots3_made > records['most_fg_team'][0]:
      records['most_fg_team'] = (team2.shots2_made + team2.shots3_made, team2.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
    elif team1.shots2_made + team1.shots3_made < records['least_fg_team'][0]:
      records['least_fg_team'] = (team1.shots2_made + team1.shots3_made, team1.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
    elif team2.shots2_made + team2.shots3_made < records['least_fg_team'][0]:
      records['least_fg_team'] = (team2.shots2_made + team2.shots3_made, team2.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)

    if team1.fts_made > records['most_ft_team'][0]:
      records['most_ft_team'] = (team1.fts_made, team1.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
    elif team2.fts_made > records['most_ft_team'][0]:
      records['most_ft_team'] = (team2.fts_made, team2.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
    elif team1.fts_made < records['least_ft_team'][0]:
      records['least_ft_team'] = (team1.fts_made, team1.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
    elif team2.fts_made < records['least_ft_team'][0]:
      records['least_ft_team'] = (team2.fts_made, team2.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)

    if team1.fouls > records['most_fouls_team'][0]:
      records['most_fouls_team'] = (team1.fouls, team1.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
    elif team2.fouls > records['most_fouls_team'][0]:
      records['most_fouls_team'] = (team2.fouls, team2.name, f"{team2.name} {team2.points}-{team1.points} {team1.name}", year)
    elif team1.fouls < records['least_fouls_team'][0]:
      records['least_fouls_team'] = (team1.fouls, team1.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
    elif team2.fouls < records['least_fouls_team'][0]:
      records['least_fouls_team'] = (team2.fouls, team2.name, f"{team2.name} {team2.points}-{team1.points} {team1.name}", year)

    if team1.points - team2.points > records['biggest_win'][0]:
      records['biggest_win'] = (team1.points - team2.points, team1.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
    elif team2.points - team1.points > records['biggest_win'][0]:
      records['biggest_win'] = (team2.points - team1.points, team2.name, f"{team2.name} {team2.points}-{team1.points} {team1.name}", year)

    if team1.most_consecutive_points > records['most_consecutive_points_team'][0]:
      records['most_consecutive_points_team'] = (team1.most_consecutive_points, team1.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
    elif team2.most_consecutive_points > records['most_consecutive_points_team'][0]:
      records['most_consecutive_points_team'] = (team2.most_consecutive_points, team2.name, f"{team2.name} {team2.points}-{team1.points} {team1.name}", year)

    # individual records
    for player in team1.get_players():
      if player.game_stats['PTS'] > records['most_points_indi'][0]:
        records['most_points_indi'] = (player.game_stats['PTS'], player.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
      if player.game_stats['PTS'] > player.personal_bests['PTS']:
        player.personal_bests['PTS'] = player.game_stats['PTS']
      if player.game_stats['AST'] > records['most_assists_indi'][0]:
        records['most_assists_indi'] = (player.game_stats['AST'], player.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
      if player.game_stats['AST'] > player.personal_bests['AST']:
        player.personal_bests['AST'] = player.game_stats['AST']
      if player.game_stats['REB'] > records['most_rebounds_indi'][0]:
        records['most_rebounds_indi'] = (player.game_stats['REB'], player.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
      if player.game_stats['REB'] > player.personal_bests['REB']:
        player.personal_bests['REB'] = player.game_stats['REB']
      if player.game_stats['BLK'] > records['most_blocks_indi'][0]:
        records['most_blocks_indi'] = (player.game_stats['BLK'], player.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
      if player.game_stats['BLK'] > player.personal_bests['BLK']:
        player.personal_bests['BLK'] = player.game_stats['BLK']
      if player.game_stats['STL'] > records['most_steals_indi'][0]:
        records['most_steals_indi'] = (player.game_stats['STL'], player.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
      if player.game_stats['STL'] > player.personal_bests['STL']:
        player.personal_bests['STL'] = player.game_stats['STL']
      if player.game_stats['TOV'] > records['most_turnovers_indi'][0]:
        records['most_turnovers_indi'] = (player.game_stats['TOV'], player.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
      # if player.game_stats['TOV'] > player.personal_bests['TOV']:
      #   player.personal_bests['TOV'] = player.game_stats['TOV']
      if player.game_stats['FGM'] > records['most_fg_indi'][0]:
        records['most_fg_indi'] = (player.game_stats['FGM'], player.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
      if player.game_stats['FGM'] > player.personal_bests['FGM']:
        player.personal_bests['FGM'] = player.game_stats['FGM']
      if player.game_stats['TPM'] > records['most_3pt_indi'][0]:
        records['most_3pt_indi'] = (player.game_stats['TPM'], player.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
      if player.game_stats['TPM'] > player.personal_bests['TPM']:
        player.personal_bests['TPM'] = player.game_stats['TPM']
      if player.game_stats['FTM'] > records['most_ft_indi'][0]:
        records['most_ft_indi'] = (player.game_stats['FTM'], player.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
      if player.game_stats['FTM'] > player.personal_bests['FTM']:
        player.personal_bests['FTM'] = player.game_stats['FTM']
      if player.game_stats['PM'] > records['most_pm_indi'][0]:
        records['most_pm_indi'] = (player.game_stats['PM'], player.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
      if player.game_stats['PM'] > player.personal_bests['PM']:
        player.personal_bests['PM'] = player.game_stats['PM']

      double_digit_stats = 0
      if player.game_stats['PTS'] >= 10:
        double_digit_stats += 1
      if player.game_stats['REB'] >= 10:
        double_digit_stats += 1
      if player.game_stats['AST'] >= 10:
        double_digit_stats += 1
      if player.game_stats['BLK'] >= 10:
        double_digit_stats += 1
      if player.game_stats['STL'] >= 10:
        double_digit_stats += 1

      if double_digit_stats >= 3:
        player.season_stats['TD'] += 1
        player.lifetime_stats['TD'] += 1
      elif double_digit_stats >= 2:
        player.season_stats['DD'] += 1
        player.lifetime_stats['DD'] += 1

    for player in team2.get_players():
      if player.game_stats['PTS'] > records['most_points_indi'][0]:
        records['most_points_indi'] = (player.game_stats['PTS'], player.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
      if player.game_stats['PTS'] > player.personal_bests['PTS']:
        player.personal_bests['PTS'] = player.game_stats['PTS']
      if player.game_stats['AST'] > records['most_assists_indi'][0]:
        records['most_assists_indi'] = (player.game_stats['AST'], player.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
      if player.game_stats['AST'] > player.personal_bests['AST']:
        player.personal_bests['AST'] = player.game_stats['AST']
      if player.game_stats['REB'] > records['most_rebounds_indi'][0]:
        records['most_rebounds_indi'] = (player.game_stats['REB'], player.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
      if player.game_stats['REB'] > player.personal_bests['REB']:
        player.personal_bests['REB'] = player.game_stats['REB']
      if player.game_stats['BLK'] > records['most_blocks_indi'][0]:
        records['most_blocks_indi'] = (player.game_stats['BLK'], player.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
      if player.game_stats['BLK'] > player.personal_bests['BLK']:
        player.personal_bests['BLK'] = player.game_stats['BLK']
      if player.game_stats['STL'] > records['most_steals_indi'][0]:
        records['most_steals_indi'] = (player.game_stats['STL'], player.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
      if player.game_stats['STL'] > player.personal_bests['STL']:
        player.personal_bests['STL'] = player.game_stats['STL']
      if player.game_stats['TOV'] > records['most_turnovers_indi'][0]:
        records['most_turnovers_indi'] = (player.game_stats['TOV'], player.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
      # if player.game_stats['TOV'] > player.personal_bests['TOV']:
      #   player.personal_bests['TOV'] = player.game_stats['TOV']
      if player.game_stats['FGM'] > records['most_fg_indi'][0]:
        records['most_fg_indi'] = (player.game_stats['FGM'], player.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
      if player.game_stats['FGM'] > player.personal_bests['FGM']:
        player.personal_bests['FGM'] = player.game_stats['FGM']
      if player.game_stats['TPM'] > records['most_3pt_indi'][0]:
        records['most_3pt_indi'] = (player.game_stats['TPM'], player.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
      if player.game_stats['TPM'] > player.personal_bests['TPM']:
        player.personal_bests['TPM'] = player.game_stats['TPM']
      if player.game_stats['FTM'] > records['most_ft_indi'][0]:
        records['most_ft_indi'] = (player.game_stats['FTM'], player.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
      if player.game_stats['FTM'] > player.personal_bests['FTM']:
        player.personal_bests['FTM'] = player.game_stats['FTM']
      if player.game_stats['PM'] > records['most_pm_indi'][0]:
        records['most_pm_indi'] = (player.game_stats['PM'], player.name, f"{team1.name} {team1.points}-{team2.points} {team2.name}", year)
      if player.game_stats['PM'] > player.personal_bests['PM']:
        player.personal_bests['PM'] = player.game_stats['PM']

      double_digit_stats = 0
      if player.game_stats['PTS'] >= 10:
        double_digit_stats += 1
      if player.game_stats['REB'] >= 10:
        double_digit_stats += 1
      if player.game_stats['AST'] >= 10:
        double_digit_stats += 1
      if player.game_stats['BLK'] >= 10:
        double_digit_stats += 1
      if player.game_stats['STL'] >= 10:
        double_digit_stats += 1

      if double_digit_stats >= 3:
        player.season_stats['TD'] += 1
        player.lifetime_stats['TD'] += 1
      elif double_digit_stats >= 2:
        player.season_stats['DD'] += 1
        player.lifetime_stats['DD'] += 1

    # reset player minutes
    for player in team1.get_players():
      player.mins = 0
      player.current_seconds = 0
      player.active = False
      player.fouled_out = False
      player.season_stats['GP'] += 1
      for key, value in player.game_stats.items():
        player.season_stats[key] += value
        player.lifetime_stats[key] += value
        player.game_stats[key] = 0
      player.lifetime_stats['GP'] += 1
      if player.injured_games > 0:
        player.injured_games -= 1

    # player.game_stats = {"PTS":0,"REB":0,"AST":0,"BLK":0,"STL":0,"TOV":0,"MIN":0,
    #                           "FGM":0,"FGA":0,"TPM":0,"TPA":0,"FTM":0,"FTA":0,"OREB":0,"DREB":0,"REB":0,
    #                           "PF":0,"PM":0}

    for player in team2.get_players():
      player.mins = 0
      player.current_seconds = 0
      player.active = False
      player.fouled_out = False
      player.season_stats['GP'] += 1
      for key, value in player.game_stats.items():
        player.season_stats[key] += value
        player.lifetime_stats[key] += value
        player.game_stats[key] = 0
      player.lifetime_stats['GP'] += 1
      if player.injured_games > 0:
        player.injured_games -= 1

    team1.reset()
    team2.reset()

    # return game result (home win or home loss) and game summary
    return winner, summary