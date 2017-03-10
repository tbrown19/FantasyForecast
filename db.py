import pymysql.cursors
import prettytable

_connection = None


def get_connection():
    connection_info = {'host': 'testing.cpylyaqsqppj.us-east-1.rds.amazonaws.com',
                       'port': 3306,
                       'user': 'tbrown19',
                       'password': 'password',
                       'db': 'testing',
                       }

    global _connection
    if not _connection:
        _connection = pymysql.connect(host=connection_info['host'],
                                      port=connection_info['port'],
                                      user=connection_info['user'],
                                      password=connection_info['password'],
                                      db=connection_info['db'],
                                      charset='utf8mb4',
                                      cursorclass=pymysql.cursors.DictCursor)
    return _connection


def run_query(query_string, fetch_all):
    print(query_string)
    # Get the connection from the database.
    connection = get_connection()
    results = ["No Results"]

    # Attempt to execute the provided query and then return the results.
    try:
        with connection.cursor() as cursor:
            sql = query_string
            cursor.execute(sql)

            if fetch_all:
                results = cursor.fetchall()
                # mytable = prettytable.from_db_cursor(cursor)
                # for data in results:
                #     mytable.add_row(data.values())

            else:
                results = cursor.fetchone()
                # mytable = prettytable.from_db_cursor(cursor)
                # mytable.add_row(results.values())

            # print(mytable)

    except pymysql.err.ProgrammingError as e:
        results = ['Error {!r}, errno {}'.format(e, e.args[0])]

    finally:
        return results


def close_connection():
    if _connection:
        _connection.close()


__all__ = ['get_connection', 'run_query']
