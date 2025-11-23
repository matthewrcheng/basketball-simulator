import os
import sqlite3

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
    
def get_stadium(id: int):
    query = "SELECT name FROM stadiums WHERE id = ?"
    result = execute_query(query, (id,))
    if result:
        return result[0][0]
    return None

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
            return team
    if name:
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
            return team
    return None


