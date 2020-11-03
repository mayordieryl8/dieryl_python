import pymysql

def CreateNewAccount(email_address, password):
    connection = pymysql.connect(
        "xxxxx", "xxxx", "xxxx", "xxxxx", 3306)
    with connection.cursor() as cursor:
        sql = "INSERT INTO `tblusers` (`user_email`, `user_pwd`) VALUES (%s, %s)"
        cursor.execute(sql, (email_address, password))
    connection.commit()

    success_message = "Account successfully created!"
    return success_message
