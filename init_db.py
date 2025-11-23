import sqlite3

db_url = "basketball.db"

def init_db():
    conn = sqlite3.connect(db_url)
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")

    # --------------------------
    # Countries
    # --------------------------
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        abbr TEXT,
        primary_color TEXT,
        secondary_color TEXT,
        tertiary_color TEXT,
        wins INTEGER DEFAULT 0,
        losses INTEGER DEFAULT 0,
        trophies INTEGER DEFAULT 0
    );
    ''')

    # --------------------------
    # Cities
    # --------------------------
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cities (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        population INTEGER,
        wealth_index REAL,
        stability_index REAL
    );
    ''')    

    # --------------------------
    # Awards
    # --------------------------
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS awards (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    );
    ''')

    # --------------------------
    # Stadium
    # --------------------------
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS stadiums (
        id INTEGER PRIMARY KEY,
        city_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        capacity INTEGER,
        base_capacity INTEGER,
        courtside_capacity INTEGER,
        base_tickets_price REAL,
        courtside_price REAL,
        year_opened INTEGER,
        FOREIGN KEY(city_id) REFERENCES cities(id)
    );
    ''')

    # --------------------------
    # Teams
    # --------------------------
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS teams (
        id INTEGER PRIMARY KEY,
        city_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        abbr TEXT NOT NULL,
        primary_color TEXT,
        secondary_color TEXT,
        tertiary_color TEXT,
        wins INTEGER DEFAULT 0,
        losses INTEGER DEFAULT 0,
        championships INTEGER DEFAULT 0,
        stadium_id INTEGER NOT NULL,
        conference TEXT,
        division TEXT,
        budget REAL DEFAULT 0,
        FOREIGN KEY(city_id) REFERENCES cities(id),
        FOREIGN KEY(stadium_id) REFERENCES stadiums(id)
    );
    ''')

    # --------------------------
    # Team Season Summary
    # --------------------------
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS team_season (
        team_id INTEGER,
        season INTEGER,
        wins INTEGER DEFAULT 0,
        losses INTEGER DEFAULT 0,
        seed INTEGER,
        points_for INTEGER DEFAULT 0,
        points_against INTEGER DEFAULT 0,
        made_playoff INTEGER,
        PRIMARY KEY(team_id, season),
        FOREIGN KEY(team_id) REFERENCES teams(id)
    );
    ''')

    # --------------------------
    # Team Playoffs
    # --------------------------
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS team_playoffs (
        team_id INTEGER,
        season INTEGER,
        wins INTEGER DEFAULT 0,
        losses INTEGER DEFAULT 0,
        seed INTEGER,
        points_for INTEGER DEFAULT 0,
        points_against INTEGER DEFAULT 0,
        placement TEXT,
        PRIMARY KEY(team_id, season),
        FOREIGN KEY(team_id) REFERENCES teams(id)
    );
    ''')

    # --------------------------
    # Games
    # --------------------------
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS games (
        id INTEGER PRIMARY KEY,
        home_team INTEGER NOT NULL,
        away_team INTEGER NOT NULL,
        home_score INTEGER,
        away_score INTEGER,
        year INTEGER,
        date TEXT,
        is_playoff INTEGER,
        overtimes INTEGER,
        attendance INTEGER,
        lead_changes INTEGER,
        home_rebounds INTEGER,
        away_rebounds INTEGER,
        home_orebs INTEGER,
        away_orebs INTEGER,
        home_drebs INTEGER,
        away_drebs INTEGER,
        home_assists INTEGER,
        away_assists INTEGER,
        home_steals INTEGER,
        away_steals INTEGER,
        home_blocks INTEGER,
        away_blocks INTEGER,
        home_turnovers INTEGER,
        away_turnovers INTEGER,
        home_ptoffto INTEGER,
        away_ptoffto INTEGER,
        home_fbpts INTEGER,
        away_fbpts INTEGER,
        home_pitp INTEGER,
        away_pitp INTEGER,
        home_ptperpos REAL,
        away_ptperpos REAL,
        home_largest_lead INTEGER,
        away_largest_lead INTEGER,
        home_fgm INTEGER,
        away_fgm INTEGER,
        home_fga INTEGER,
        away_fga INTEGER,
        home_3pm INTEGER,
        away_3pm INTEGER,
        home_3pa INTEGER,
        away_3pa INTEGER,
        home_ftm INTEGER,
        away_ftm INTEGER,
        home_fta INTEGER,
        away_fta INTEGER,
        FOREIGN KEY(home_team) REFERENCES teams(id),
        FOREIGN KEY(away_team) REFERENCES teams(id)
    );
    ''')

    # --------------------------
    # Player
    # --------------------------
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS player (
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        birth_year INTEGER,
        draft_year INTEGER,
        draft_team_id INTEGER,
        draft_pick INTEGER,
        country_id INTEGER,
        number INTEGER,
        height REAL,
        position TEXT,
        luck INTEGER,
        injury_tendency REAL,
        clutch REAL,
        work_ethic REAL,
        leadership REAL,
        join_date TEXT,
        retire_date TEXT,
        championships INTEGER DEFAULT 0,
        FOREIGN KEY(draft_team_id) REFERENCES teams(id),
        FOREIGN KEY(country_id) REFERENCES countries(id)
    );
    ''')

    # --------------------------
    # Player Personal Bests (Season)
    # --------------------------
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS player_personal_bests_season (
        player_id INTEGER, 
        year INTEGER,
        pts INTEGER,
        reb INTEGER,
        ast INTEGER,
        blk INTEGER,
        stl INTEGER,
        fgm INTEGER,
        tpm INTEGER,
        ftm INTEGER,
        plus_minus INTEGER,
        double_doubles INTEGER,
        triple_doubles INTEGER,
        games_played INTEGER,
        PRIMARY KEY(player_id, year),
        FOREIGN KEY(player_id) REFERENCES player(id)
    );
    ''')
                   
    # --------------------------
    # Player Personal Bests (Game)
    # --------------------------
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS player_personal_bests_game (
        player_id INTEGER,
        game_id INTEGER,
        pts INTEGER,
        reb INTEGER,
        oreb INTEGER,
        dreb INTEGER,
        ast INTEGER,
        blk INTEGER,
        stl INTEGER,
        fgm INTEGER,
        tpm INTEGER,
        ftm INTEGER,
        plus_minus INTEGER,
        double_doubles INTEGER,
        triple_doubles INTEGER,
        PRIMARY KEY(player_id, game_id),
        FOREIGN KEY(player_id) REFERENCES player(id),
        FOREIGN KEY(game_id) REFERENCES games(id)
    );
    ''')

    # --------------------------
    # Player Awards
    # --------------------------
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS player_awards (
        player_id INTEGER,
        award_id INTEGER,
        year INTEGER,
        FOREIGN KEY(player_id) REFERENCES player(id),
        FOREIGN KEY(award_id) REFERENCES awards(id)
    );
    ''')

    # --------------------------
    # Player Stats (Attributes)
    # --------------------------
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS player_stats (
        player_id INTEGER PRIMARY KEY,
        year INTEGER,
        iq INTEGER,
        physical INTEGER,
        passing INTEGER,
        inner_attack INTEGER,
        outer_attack INTEGER,
        inner_defense INTEGER,
        outer_defense INTEGER,
        FOREIGN KEY(player_id) REFERENCES player(id)
    );
    ''')

    # --------------------------
    # Player Team Assignments
    # --------------------------
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS player_teams (
        id INTEGER PRIMARY KEY,
        player_id INTEGER,
        team_id INTEGER,
        join_date TEXT,
        leave_date TEXT,
        games INTEGER DEFAULT 0,
        contract_value REAL DEFAULT 0,
        contract_expires INTEGER,
        acquired_by TEXT,
        reason_left TEXT,
        FOREIGN KEY(player_id) REFERENCES player(id),
        FOREIGN KEY(team_id) REFERENCES teams(id)
    );
    ''')

    # --------------------------
    # Player Game Boxscore
    # --------------------------
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS player_game_boxscore (
        player_id INTEGER NOT NULL,
        game_id INTEGER NOT NULL,
        minutes INTEGER,
        points INTEGER,
        rebounds INTEGER,
        rebounds_offensive INTEGER,
        rebounds_defensive INTEGER,
        assists INTEGER,
        steals INTEGER,
        blocks INTEGER,
        turnovers INTEGER,
        field_goals_made INTEGER,
        field_goals_attempted INTEGER,
        three_pt_made INTEGER,
        three_pt_attempted INTEGER,
        ft_made INTEGER,
        ft_attempted INTEGER,
        personal_fouls INTEGER,
        plus_minus INTEGER,
        PRIMARY KEY(player_id, game_id),
        FOREIGN KEY(player_id) REFERENCES player(id),
        FOREIGN KEY(game_id) REFERENCES games(id)
    );
    ''')

    # --------------------------
    # Player Season Boxscore
    # --------------------------
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS player_season_boxscore (
        player_id INTEGER NOT NULL,
        year INTEGER NOT NULL,
        games INTEGER,
        minutes INTEGER,
        points INTEGER,
        rebounds INTEGER,
        rebounds_offensive INTEGER,
        rebounds_defensive INTEGER,
        assists INTEGER,
        steals INTEGER,
        blocks INTEGER,
        turnovers INTEGER,
        field_goals_made INTEGER,
        field_goals_attempted INTEGER,
        three_pt_made INTEGER,
        three_pt_attempted INTEGER,
        ft_made INTEGER,
        ft_attempted INTEGER,
        personal_fouls INTEGER,
        plus_minus INTEGER,
        PRIMARY KEY(player_id, year),
        FOREIGN KEY(player_id) REFERENCES player(id)
    );
    ''')

    # --------------------------
    # Player Lifetime Boxscore
    # --------------------------
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS player_lifetime_boxscore (
        player_id INTEGER PRIMARY KEY,
        games INTEGER,
        minutes INTEGER,
        points INTEGER,
        rebounds INTEGER,
        rebounds_offensive INTEGER,
        rebounds_defensive INTEGER,
        assists INTEGER,
        steals INTEGER,
        blocks INTEGER,
        turnovers INTEGER,
        field_goals_made INTEGER,
        field_goals_attempted INTEGER,
        three_pt_made INTEGER,
        three_pt_attempted INTEGER,
        ft_made INTEGER,
        ft_attempted INTEGER,
        personal_fouls INTEGER,
        plus_minus INTEGER,
        FOREIGN KEY(player_id) REFERENCES player(id)
    );
    ''')

    # --------------------------
    # Draft Picks
    # --------------------------
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS draft_picks (
        id INTEGER PRIMARY KEY,
        year INTEGER NOT NULL,
        round INTEGER NOT NULL,
        pick_number INTEGER NOT NULL,
        original_team_id INTEGER NOT NULL,
        current_team_id INTEGER NOT NULL,
        player_id INTEGER,
        FOREIGN KEY(original_team_id) REFERENCES teams(id),
        FOREIGN KEY(current_team_id) REFERENCES teams(id),
        FOREIGN KEY(player_id) REFERENCES player(id)
    );
    ''')

    # --------------------------
    # Trades
    # --------------------------
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS trades (
        id INTEGER PRIMARY KEY,
        trade_date TEXT,
        from_team_id INTEGER,
        to_team_id INTEGER,
        FOREIGN KEY(from_team_id) REFERENCES teams(id),
        FOREIGN KEY(to_team_id) REFERENCES teams(id)
    );
    ''')

    # --------------------------
    # Trade Pieces
    # --------------------------
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS trade_pieces (
        id INTEGER PRIMARY KEY,
        trade_id INTEGER,
        player_id INTEGER,
        draft_pick_id INTEGER,
        FOREIGN KEY(player_id) REFERENCES player(id),
        FOREIGN KEY(draft_pick_id) REFERENCES draft_picks(id)
    );
    ''')

    # --------------------------
    # Injuries
    # -------------------------
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS injuries (
        id INTEGER PRIMARY KEY,
        player_id INTEGER NOT NULL,
        injury_type TEXT NOT NULL,
        severity TEXT NOT NULL,
        start_date TEXT NOT NULL,
        end_date TEXT,
        games_missed INTEGER,
        FOREIGN KEY(player_id) REFERENCES player(id)
    );
    ''')

    #-----------------------------------
    # Records
    #-----------------------------------
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS records (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        team_id INTEGER NOT NULL,
        opponent_id INTEGER NOT NULL,
        player_id INTEGER,
        value REAL NOT NULL,
        year INTEGER NOT NULL,
        date TEXT NOT NULL,
        result TEXT NOT NULL,
        is_active INTEGER DEFAULT 1,
        FOREIGN KEY(team_id) REFERENCES teams(id),
        FOREIGN KEY(opponent_id) REFERENCES teams(id),
        FOREIGN KEY(player_id) REFERENCES player(id)
    );
    ''')

    # --------------------------
    # Results (Championship outcomes)
    # --------------------------
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY,
        year INTEGER NOT NULL,
        winner INTEGER NOT NULL,
        winner_seed INTEGER,
        runner_up INTEGER NOT NULL,
        runner_up_seed INTEGER,
        winner_wins INTEGER,
        runner_up_wins INTEGER,
        semifinalist1 INTEGER,
        semifinalist1_seed INTEGER,
        semifinalist2 INTEGER,
        semifinalist2_seed INTEGER,
        mvp_player_id INTEGER,
        notes TEXT,
        FOREIGN KEY(mvp_player_id) REFERENCES player(id),
        FOREIGN KEY(winner) REFERENCES teams(id),
        FOREIGN KEY(runner_up) REFERENCES teams(id),
        FOREIGN KEY(semifinalist1) REFERENCES teams(id),
        FOREIGN KEY(semifinalist2) REFERENCES teams(id)
    );
    ''')

    conn.commit()
    conn.close()

def populate_countries():
    conn = sqlite3.connect(db_url)
    cursor = conn.cursor()

    # add

    conn.commit()
    conn.close()

def populate_cities():
    conn = sqlite3.connect(db_url)
    cursor = conn.cursor()

    cursor.execute('''
    INSERT OR IGNORE INTO cities (name, population, wealth_index, stability_index) VALUES
        ('Silent Rock', 10000, 0.5, 0.9),
        ('Mistbourne', 20000, 0.5, 0.95),
        ('Aerilon', 210000, 0.88, 0.53),
        ('Coalfell', 12500, 0.48, 0.45),
        ('Aquarin', 450000, 1.0, 0.25),
        ('Amberfall', 22500, 0.55, 0.83),
        ('Wintervale', 18000, 0.69, 0.79),
        ('Ironforge', 40000, 0.63, 0.80),
        ('Willowbrook', 60000, 0.43, 0.68),
        ('Goldenleaf', 22000, 0.43, 0.93),
        ('Sunhaven', 290000, 0.69, 0.48),
        ('Rosewood', 27000, 0.56, 0.89),
        ('Cedarcrest', 38000, 0.53, 0.82),
        ('Fogrend', 14000, 0.36, 0.65),
        ('Black Crystal', 9000, 0.44, 0.71),
        ('Shadowfen', 32000, 0.45, 0.63),
        ('Oakheart', 25000, 0.7, 0.78),
        ('Stormridge', 43000, 0.58, 0.81),
        ('Silverlake', 120000, 0.54, 0.84),
        ('Emberlyn', 19000, 0.52, 0.86);
    ''')

    conn.commit()
    conn.close()

def populate_awards():
    conn = sqlite3.connect(db_url)
    cursor = conn.cursor()

    cursor.execute('''
    INSERT OR IGNORE INTO awards (name) VALUES
        ('VBL Champion'),
        ('MVP'),
        ('Finals MVP'),
        ('TOTS'),
        ('TOF'),
        ('Golden Bucket'),
        ('Golden Board'),
        ('Golden Dime'),
        ('Golden Stuff'),
        ('Golden Hands');
    ''')

    conn.commit()
    conn.close()

def populate_stadiums():
    conn = sqlite3.connect(db_url)
    cursor = conn.cursor()

    cursor.execute('''
    INSERT OR IGNORE INTO stadiums (city_id, name, capacity, base_capacity, courtside_capacity, base_tickets_price, courtside_price, year_opened) VALUES
        (1, 'Shadow Stadium', 1000, 900, 100, 50.0, 200.0, 1995),
        (2, 'Mystery Dome', 1200, 1080, 120, 55.0, 220.0, 2000),
        (3, 'Skyline Stadium', 3200, 3000, 200, 60.0, 450.0, 1985),
        (4, 'Flame Pit', 1200, 1100, 100, 45.0, 200.0, 1998),
        (5, 'Nebula Arena', 4000, 3700, 300, 70.0, 600.0, 2003),
        (6, 'Dojo', 1500, 1350, 150, 52.0, 250.0, 1992),
        (7, 'Wolf Den', 1800, 1600, 200, 58.0, 300.0, 2001),
        (8, 'Titanium Coliseum', 2800, 2600, 200, 65.0, 400.0, 1997),
        (9, 'Adventure Park', 1400, 1300, 100, 48.0, 220.0, 2004),
        (10, 'Griffin''s Roost', 2300, 2100, 200, 62.0, 350.0, 1993),
        (11, 'Radiant Arena', 3350, 3150, 200, 65.0, 500.0, 1990),
        (12, 'Rebel Grounds', 1600, 1450, 150, 54.0, 280.0, 2002),
        (13, 'Stallion Stable', 2200, 2000, 200, 60.0, 320.0, 1996),
        (14, 'Flight Center', 1300, 1200, 100, 50.0, 210.0, 2006),
        (15, 'Crystal Cavern', 900, 800, 100, 45.0, 190.0, 2012),
        (16, 'Wasteland', 1700, 1550, 150, 53.0, 270.0, 1999),
        (17, 'Guardian Arena', 2400, 2200, 200, 63.0, 360.0, 1994),
        (18, 'Thunder Dome', 2600, 2450, 150, 62.0, 480.0, 2005),
        (19, 'Aquatic Center', 3000, 2800, 200, 68.0, 520.0, 2008),
        (20, 'Apex Arena', 1100, 1000, 100, 50.0, 250.0, 2010);
    ''')

    conn.commit()
    conn.close()

def populate_teams():
    conn = sqlite3.connect(db_url)
    cursor = conn.cursor()

    cursor.execute('''
    INSERT OR IGNORE INTO teams (city_id, name, abbr, primary_color, secondary_color, tertiary_color, stadium_id, conference, division) VALUES
        (1, 'Silent Rock Shadows', 'SRS', 'Midnight Black', 'Shadow Gray', 'Whispering White', 1, 'Eastern', 'Southeast'),
        (2, 'Mistbourne Mystery', 'MM', 'Mysterious Purple', 'Enigmatic Blue', 'Secret Silver', 2, 'Eastern', 'Southeast'),
        (3, 'Aerilon Aces', 'AA', 'Sky Blue', 'Radiant White', 'Sunny Yellow', 3, 'Eastern', 'Southeast'),
        (4, 'Coalfell Inferno', 'CFI', 'Coal Black', 'Smoldering Orange', 'Ashen Gray', 4, 'Eastern', 'Southeast'),
        (5, 'Aquarin Currents', 'AC', 'Teal', 'Pearl White', 'Dark Blue', 5, 'Eastern', 'Southeast'),
        (6, 'Amberfall Blaze', 'AB', 'Amber Orange', 'Fiery Yellow', 'White', 6, 'Eastern', 'Southeast'),
        (7, 'Wintervale Wolves', 'WW', 'Arctic Blue', 'Frost White', 'Winter Gray', 7, 'Western', 'Northwest'),
        (8, 'Ironforge Titans', 'IT', 'Steel Gray', 'Fiery Red', 'Molten Gold', 8, 'Western', 'Northwest'),
        (9, 'Willowbrook Wanderers', 'WBW', 'Brown', 'Whispering Blue', 'Gray', 9, 'Western', 'Northwest'),
        (10, 'Goldenleaf Griffins', 'GG', 'Royal Gold', 'Verdant Green', 'Majestic Maroon', 10, 'Western', 'Northwest'),
        (11, 'Sunhaven Rays', 'SR', 'Radiant Yellow', 'Burning Red', 'Black', 11, 'Western', 'Sunborn'),
        (12, 'Rosewood Rebels', 'RR', 'Crimson Red', 'Rebel Pink', 'Thorny Green', 12, 'Western', 'Sunborn'),
        (13, 'Cedarcrest Stallions', 'CS', 'Rich Chestnut', 'Earthy Green', 'Strong Silver', 13, 'Western', 'Sunborn'),
        (14, 'Fogrend Falcons', 'FF', 'Misty Gray', 'Sky Blue', 'Feathered White', 14, 'Western', 'Southwest'),
        (15, 'Black Crystal Geodes', 'BCG', 'Onyx Black', 'Obsidian Gray', 'Obsidian White', 15, 'Western', 'Southwest'),
        (16, 'Shadowfen Scorpions', 'SFS', 'Venomous Purple', 'Poison Green', 'Radioactive Yellow', 16, 'Western', 'Southwest'),
        (17, 'Oakheart Guardians', 'OG', 'Deep Green', 'Earth Brown', 'Noble Gold', 17, 'Eastern', 'Northeast'),
        (18, 'Stormridge Lightning', 'SL', 'Electric Blue', 'Thunder Yellow', 'Striking Silver', 18, 'Eastern', 'Northeast'),
        (19, 'Silverlake Stingrays', 'SS', 'Silver Metallic', 'Electric Blue', 'Singing Gold', 19, 'Eastern', 'Northeast'),
        (20, 'Emberlyn Crests', 'EC', 'Ember Red', 'Fiery Orange', 'Burnished Gold', 20, 'Eastern', 'Northeast');
    ''')

    conn.commit()
    conn.close()

def reset():
    conn = sqlite3.connect(db_url)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM player;")
    cursor.execute("DELETE FROM teams;")
    cursor.execute("DELETE FROM stadiums;")
    cursor.execute("DELETE FROM cities;")
    cursor.execute("DELETE FROM countries;")
    cursor.execute("DELETE FROM awards;")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    reset()
    # populate_countries()
    populate_cities()
    populate_awards()
    populate_stadiums()
    populate_teams()