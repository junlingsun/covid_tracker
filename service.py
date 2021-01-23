import time
import pymysql


def getTime():
    timeString = time.strftime("%m-%d-%Y %X")
    return timeString


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


def query(sql, *args):
    connection, cursor = getConnection()
    cursor.execute(sql, args)
    data = cursor.fetchall()
    closeConection(connection, cursor)
    return data


def get_c1_data():
    sql = "select positive, death, positive_increase, death_increase from us_data order by date desc limit 1"
    data = query(sql)
    return data[0]


def get_c2_data():
    sql = "select state, positive, death from state_data where " \
          "date = (select date from state_data order by date desc limit 1)"
    data = query(sql)
    return data


def get_l1_data():
    sql = "select date, positive, death from us_data order by date desc"
    data = query(sql)
    return data


def get_l2_data():
    sql = "select date, positive_increase, death_increase from us_data order by date desc"
    data = query(sql)
    return data


def get_r1_data():
    sql = "select state, positive from state_data order by date desc, positive desc limit 10"
    data = query(sql)
    return data


if __name__ == "__main__":
    print(get_r1_data())
