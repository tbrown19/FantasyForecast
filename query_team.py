import db


class Team:
    def __init__(self, team_name, team_id):
        self.team_id = team_id
        self.team_name = team_name

    @classmethod
    def from_team_name(cls, team_name):
        print(team_name)
        id = get_id_from_team_name(team_name)
        return cls(team_name, id)

    @classmethod
    def from_team_id(cls, team_id):
        print(team_id)
        name = get_name_from_team_id(team_id)
        return cls(name, team_id)

    def get_all_games_played(self):
        """
        Get all the games a team has played using the team's name
        :return: List version of the SQL Query
        """
        query = ('SELECT COUNT(gid) '
                 'FROM team '
                 "WHERE team.tname = '{0}'"
                 ).format(self.team_name)
        return db.run_query(query, True)

    def get_games_from_season(self, season):
        query = ('SELECT * '
                 'FROM game '
                 "WHERE (game.v = '{0}' or game.h = '{0}') and game.seas = {1}"
                 ).format(self.team_name, season)
        return db.run_query(query, True)

    def get_game_from_season_and_week(self, season, week):
        query = ('SELECT * '
                 'FROM game '
                 "WHERE (game.v = '{0}' or game.h = '{0}') and game.seas = {1} and game.wk = {2}"
                 ).format(self.team_name, season, week)
        return db.run_query(query, False)

    def get_all_drives(self, drive_limits="", game_limits=""):
        query = ('SELECT * '
                 'FROM drive '
                 'JOIN game '
                 'ON game.gid = drive.gid {1} '
                 "WHERE (game.v = '{0}' or game.h = '{0}') {2}"
                 ).format(self.team_name, drive_limits, game_limits)
        return db.run_query(query, True)

    def get_all_drives_from_season(self, season,  drive_limits="", game_limits=""):

        query = ('SELECT * '
                 'FROM drive '
                 'JOIN game '
                 'ON game.gid = drive.gid {2} '
                 "WHERE (game.v = '{0}' or game.h = '{0}') and game.seas={1} {3}"
                 ).format(self.team_name, season, drive_limits, game_limits)
        return db.run_query(query, True)

    def get_stats_from_game(self, game):
        query = ('SELECT * '
                 'FROM team '
                 "WHERE team.tname = '{0}' and team.gid = {1}"
                 ).format(self.team_name, game)
        return db.run_query(query, True)

    def get_stats_from_season(self, season):
        query = ('SELECT * '
                 'FROM team '
                 "WHERE team.tname = '{0}' and team.gid = {1}"
                 ).format(self.team_name, game)
        return db.run_query(query, True)


def get_id_from_team_name(team_name):
    query = ('SELECT tid '
             'FROM team '
             "WHERE team.tname = '{0}'"
             ).format(team_name)
    return db.run_query(query, False)['tid']


def get_name_from_team_id(team_id):
    query = ('SELECT tname '
             'FROM team '
             "WHERE team.tid = '{0}'"
             ).format(team_id)
    return db.run_query(query, False)['tname']
