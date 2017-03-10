import prettytable
import query_team
import db
import table_queries as queries


def print_table(query_result):
    table_headers = []
    data = query_result

    # If we have multiple results, then the loop is slightly different.
    if isinstance(query_result, list):
        data = query_result[0]
        # Get the table headers from the first row in dict
        for key, value in data.items():
            table_headers.append(key)

        table = prettytable.PrettyTable(table_headers)

        # For each row in the result we append its value to a row and then add that row to the table.
        for row in query_result:
            cur_row = []
            for key, value in row.items():
                cur_row.append(value)
            table.add_row(cur_row)
    else:
        cur_row = []
        # If we only have one item, then we can get the keys and values in the same loop
        for key, value in data.items():
            table_headers.append(key)
            cur_row.append(value)
        table = prettytable.PrettyTable(table_headers)
        table.add_row(cur_row)

    print(table)


def remove_cols_from_table(results, desired_cols):
    new_table = []
    for result in results:
        new_result = {key: value for key, value in result.items() if key in desired_cols}
        new_table.append(new_result)
    return new_table


if __name__ == '__main__':

    # game_headers = queries.get_table_col_names("game")
    # game_headers.append('succ')
    team1 = query_team.Team.from_team_id(8)
    # results = team1.get_all_games_played()
    # print(results)
    # results2 = team1.get_all_drives("and drive.succ > 8")
    # newTable = remove_cols_from_table(results2, game_headers)
    desiredGame = team1.get_game_from_season_and_week(2011,1)
    desiredGameID = desiredGame['gid']
    print_table(desiredGame)
    desiredStats = team1.get_stats_from_game(desiredGameID)
    print(desiredStats)
    db.close_connection()
