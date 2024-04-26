query = 'select * from User where username=?;'
result = database_connection.run(query, username)
