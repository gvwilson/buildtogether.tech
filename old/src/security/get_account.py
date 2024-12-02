def get_account(database_connection):
    username = input('Username:')
    query = 'select * from User where username="{}";'.format(username)
    result = database_connection.run(query)
    return result
