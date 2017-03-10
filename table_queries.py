import db



def get_team(game_id, team_name):
    """
    :param game_id:
    :param team_name:
    :return:
    """
    query = ('SELECT * '
             'FROM team '
             "WHERE team.gid = '{0}' and team.tname = '{1}'"
             ).format(game_id, team_name)
    return db.run_query(query, False)


def get_player(player_id):
    query = ('SELECT * '
             'FROM player '
             "WHERE player = '{0}'"
             ).format(player_id)
    return db.run_query(query, False)


def get_game(game_id):
    query = ('SELECT * '
             'FROM game '
             "WHERE game.gid = '{0}'"
             ).format(game_id)
    return db.run_query(query, False)


def get_drive(drive_id):
    query = ('SELECT * '
             'FROM drive '
             "WHERE drive.uid = '{0}'"
             ).format(drive_id)
    return db.run_query(query, False)


def get_play(play_id):

    query = ('SELECT * '
             'FROM play '
             "WHERE play.id = '{0}'"
             ).format(play_id)
    return db.run_query(query, False)


def get_all_games(limiters=None):
    limits = limiters_to_sql(limiters)

    query = ('SELECT * '
             'FROM game '
             "WHERE {0}"
             ).format(limits)
    print(query)
    return db.run_query(query, True)


def get_team_season_stat_from_all_games():
    query = ('SELECT * '
             'FROM game '
             "JOIN team "
             "ON team.gid = game.gid "
             "WHERE team.tname = 'GB' and game.seas = 2011 "
             ).format()
    return db.run_query(query, True)


def get_all_games_by_team_stat(game_limiters=None, team_limiters=None, headers=None):
    game_limits = limiters_to_sql(game_limiters)
    team_limits = limiters_to_sql(team_limiters)

    query = ('SELECT *, {2} '
             'FROM game '
             "JOIN team "
             "ON team.gid = game.gid "
             "WHERE {0} {1}"
             ).format(game_limits, team_limits, headers)
    return db.run_query(query, True)


def get_all_games_from_season(season, limiters=None):
    limits = limiters_to_sql(limiters)

    query = ('SELECT * '
             'FROM game '
             "WHERE game.seas = '{0}' {1}"
             ).format(season, limits)
    print(query)
    return db.run_query(query, True)


def get_teams_games_from_season(season, team_name, limiters=None):
    limits = limiters_to_sql(limiters)

    query = ('SELECT * '
             'FROM game '
             "WHERE game.seas = '{0}' and (game.v = '{1}' or game.h = '{1}') {2}"
             ).format(season, team_name, limits)
    return db.run_query(query, True)


def get_all_games_from_week(week, limiters=None):
    limits = limiters_to_sql(limiters)

    query = ('SELECT * '
             'FROM game '
             "WHERE game.wk = '{0}' {1}"
             ).format(week, limits)
    print(query)
    return db.run_query(query, True)


def get_teams_games_from_week(week, team_name, limiters=None):
    limits = limiters_to_sql(limiters)

    query = ('SELECT * '
             'FROM game '
             "WHERE game.wk = '{0}' and (game.v = '{1}' or game.h = '{1}') {2}"
             ).format(week, team_name, limits)
    print(query)
    return db.run_query(query, True)


def get_plays_from_game(game_id, limiters=None):
    limits = limiters_to_sql(limiters)

    query = ('SELECT * '
             'FROM play '
             "WHERE play.gid = '{0}' {1}"
             ).format(game_id, limits)
    return db.run_query(query, True)


def get_drives_from_game(game_id, limiters=None):
    limits = limiters_to_sql(limiters)
    print(limits)
    query = ('SELECT * '
             'FROM drive '
             "WHERE drive.gid = '{0}' {1}"
             ).format(game_id, limits)
    return db.run_query(query, True)


def get_oline_from_play(play_id):
    query = ('SELECT oline.* '
             'FROM oline '
             'JOIN play '
             'ON play.olid = oline.olid '
             "WHERE pid = '{0}'"
             ).format(play_id)
    # We remove the olid from the begining of the dict,
    # and instead make it its own element in a list, for easier parsing.
    oline = db.run_query(query, False)
    olid = oline.pop('olid')
    return [olid, oline]


def get_table_col_names(table_name):
    col_names = []

    query = ('SELECT column_name '
             'FROM INFORMATION_SCHEMA.COLUMNS '
             "WHERE TABLE_NAME = '{0}'"
             ).format(table_name)
    col_names_result = db.run_query(query, True)
    # For each column in the results,
    for col_name in col_names_result:
        # We append its column name information to the list of column names.
        col_names.append(col_name['column_name'])
    return col_names


def limiters_to_sql(limiters):
    sqlized_limits = ""
    print(limiters)
    if limiters is not None:
        for key,value in limiters.items():
            sqlized_limits += key + " " + value

    return sqlized_limits
