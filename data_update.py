import pymysql
import time
import traceback
import dao


def getConnection():
    connection = pymysql.connect(host="localhost",
                                 user="root",
                                 password="EllaSun-521",
                                 database="covid")
    cursor = connection.cursor()
    return connection, cursor


def closeConection(connection, cursor):
    if connection:
        connection.close()

    if cursor:
        cursor.close()


def update_us_data():
    connection = None
    cursor = None

    try:
        us_data = dao.data_fetch()[0]

        connection, cursor = getConnection()

        sql_insert = "insert into us_data (date, positive, death) values( %s, %s, %s)"
        sql_select = "select id from us_data where date=%s"

        for k, v in us_data.items():
            if not cursor.execute(sql_select, k):
                cursor.execute(sql_insert, [k, v.get("positive"), v.get("death")])

        connection.commit()
    except:
        traceback.print_exc()
    finally:
        closeConection(connection, cursor)


def update_state_data():
    connection = None
    cursor = None

    try:
        state_data = dao.data_fetch()[1]
        connection, cursor = getConnection()

        sql_insert = "insert into state_data (date, positive, death, state) values (%s, %s, %s, %s)"
        sql_select = "select id from state_data where date=%s"

        for v in state_data:
            if not cursor.execute(sql_select, v.get("date")):
                cursor.execute(sql_insert, [v.get("date"), v.get("positive"), v.get("death"), v.get("state")])
        connection.commit()

    except:
        traceback.print_exc()

    finally:
        closeConection(connection, cursor)


def import_state_data():
    connection = None
    cursor = None

    try:
        state_data = dao.data_fetch()[1]
        connection, cursor = getConnection()

        sql_insert = "insert into state_data (date, positive, death, state) values (%s, %s, %s, %s)"

        for data in state_data:
            cursor.execute(sql_insert, [data.get("date"), data.get("positive"), data.get("death"), data.get("state")])
        connection.commit()

    except:
        traceback.print_exc()

    finally:
        closeConection(connection, cursor)


def import_us_data():
    connection = None
    cursor = None

    try:
        us_data = dao.data_fetch()[0]

        connection, cursor = getConnection()

        sql_insert = "insert into us_data " \
                     "(date, positive, death, positive_increase, death_increase)" \
                     " values( %s, %s, %s, %s, %s)"

        for k, v in us_data.items():
            cursor.execute(sql_insert, [k, v.get("positive"), v.get("death"),
                                        v.get("positive_increase"), v.get("death_increase")])

        connection.commit()
    except:
        traceback.print_exc()
    finally:
        closeConection(connection, cursor)


if __name__ == "__main__":
    import_us_data();
