import prettytable
import query_team
import db


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
        #print(new_result)
        new_table.append(new_result)
    return new_table


if __name__ == '__main__':
    # game = queries.get_plays_from_game(2922, {'and qtr': 1})
    # for play in game:
    #     print(play['pid'])
    # oline = queries.get_oline_from_play(474435)
    # print(oline[1])
    # for member in oline[1]:
    #     player = queries.get_player(oline[1][member])
    #     print(player['pname'])
    #
    # weeklyGames = queries.get_all_games(["sprv < -25"/, " or sprv > 25"])
    # print_table(weeklyGames)
    #
    # game_headers = queries.get_table_col_names("game")
    # game_headers.append('ry')
    #
    # results = queries.get_all_games_by_team_stat({}, {"ry/ra": "> 10"}, "ry/ra")
    #
    # newTable = remove_cols_from_table(results, game_headers)
    # print_table(newTable)
    #
    # results = queries.team.get_team('GB')
    # # newTable2 = remove_cols_from_table(results, game_headers)
    # print(results)
    # print_table(results)

    team1 = query_team.Team.from_team_id(8)
    results = team1.get_all_games_played()
    print(results)
    results2 = team1.get_game_from_season(2011, 1)
    print(results2)
    db.close_connection()
