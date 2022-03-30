import pymysql

def main():
    try:

        conn = pymysql.connect(
            host='127.0.0.1', 
            user='root', 
            password='root1!', 
            database='doodb', 
            charset='utf8')

        cursor = conn.cursor()

        # query = "insert into users (email, info) values ('py@naver.com', json_object('age','99'))"
        # result = cursor.execute(query)
        query = 'select * from users'

        cursor.execute(query)
        result = cursor.fetchall()

        conn.close()
        
        # conn.commit()
        print(type(result))    

        for i in result:
            print(i)

        r2 = list(result)
        print(r2[0])

    except Error as e:
        print('에러발생 :', e)


if __name__ == '__main__':
    main()