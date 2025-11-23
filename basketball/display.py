import matplotlib.pyplot as plt
from basketball.constants import reset

def plot_scoring_trend(team1, team2, game_seconds):
    # Unpack the tuples into separate lists
    times1, scores1 = zip(*team1.scoring_trend)
    times2, scores2 = zip(*team2.scoring_trend)

    plt.figure(figsize=(12, 6))

    plt.plot(times1, scores1, label="Team 1", color="blue")
    plt.plot(times2, scores2, label="Team 2", color="red")

    # Draw vertical lines at 720, 1440, 2160 seconds
    quarter_times = [0, 720, 1440, 2160]
    cur = 2880
    while game_seconds > cur:
        quarter_times.append(cur)
        cur += 300
    for quarter_time in quarter_times:
        plt.axvline(x=quarter_time, color='gray', linestyle='--', linewidth=1)
        plt.text(quarter_time + 10, max(max(scores1), max(scores2)) * 0.95,
                 f"Q{quarter_time // 720 + 1}", rotation=90, color='gray')

    plt.xlim(0, game_seconds)
    plt.ylim(0, max(max(scores1), max(scores2)) * 1.1)
    plt.xlabel("Elapsed Time (seconds)")
    plt.ylabel("Score")
    plt.title("Scoring Trend Over Game")
    plt.legend()
    plt.grid(True, which='both', linestyle=':', linewidth=0.5)

    plt.show()

def print_summary(team1, team2):
    fga1 = team1.shots2 + team1.shots3
    fga2 = team2.shots2 + team2.shots3
    fg1 = team1.shots2_made + team1.shots3_made
    fg2 = team2.shots2_made + team2.shots3_made

    tpa1 = team1.shots3
    tpa2 = team2.shots3
    tpp1 = team1.shots3_made * 3
    tpp2 = team2.shots3_made * 3

    ftp1 = team1.fts_made
    ftp2 = team2.fts_made
    fta1 = team1.fts
    fta2 = team2.fts

    summary = f'''
Summary:
        {team1.color}{team1.points}{reset} - {team2.color}{team2.points}{reset}
{fg1}/{fga1}   Field goals   {fg2}/{fga2}
{round(100*fg1/max(fga1,1),1)}       %       {round(100*fg2/max(fga2,1),1)}
{int(tpp1/3)}/{tpa1}   3 pointers   {int(tpp2/3)}/{tpa2}
{round(100*tpp1/3/max(tpa1,1),1)}       %       {round(100*tpp2/3/max(tpa2,1),1)}
{ftp1}/{fta1}   Free throws  {ftp2}/{fta2}
{round(100*ftp1/max(fta1,1),1)}       %       {round(100*ftp2/max(fta2,1),1)}
{team1.rebounds}     Rebounds   {team2.rebounds}
{team1.assists}     Assists    {team2.assists}
{team1.blocks}      Blocks    {team2.blocks}
{team1.steals}      Steals    {team2.steals}
{team1.turnovers}    Turnovers   {team2.turnovers}
{team1.fouls}      Fouls     {team2.fouls}
'''
    return summary

def print_box_score_line(player):
    return f'{player.name:<16}  {round(player.game_stats["MIN"],1):>4}  {player.game_stats["PTS"]:>3}  {player.game_stats["FGM"]:>3}  {player.game_stats["FGA"]:>3}\
 {0 if player.game_stats["FGA"] == 0 else int(100*player.game_stats["FGM"]/player.game_stats["FGA"]):>3}%  {player.game_stats["TPM"]:>3}  {player.game_stats["TPA"]:>3}\
 {0 if player.game_stats["TPA"] == 0 else int(100*player.game_stats["TPM"]/player.game_stats["TPA"]):>3}%  {player.game_stats["FTM"]:>3}  {player.game_stats["FTA"]:>3}\
 {0 if player.game_stats["FTA"] == 0 else int(100*player.game_stats["FTM"]/player.game_stats["FTA"]):>3}%  {player.game_stats["OREB"]:>3}  {player.game_stats["DREB"]:>3}\
  {player.game_stats["REB"]:>3}  {player.game_stats["AST"]:>3}  {player.game_stats["STL"]:>3}  {player.game_stats["BLK"]:>3}  {player.game_stats["TOV"]:>3}\
  {player.game_stats["PF"]:>3}  {player.game_stats["PM"]:>3}'

def print_box_score(team):
    print(f"""{team.color}{team.name}{reset}
Player             MIN  PTS  FGM  FGA  FG%  3PM  3PA  3P%  FTM  FTA  FT%  OREB  DREB  REB  AST  STL  BLK  TO  PF  +/-""")
    for player in team.get_players():
        print(print_box_score_line(player))