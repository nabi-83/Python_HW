from sqlalchemy import create_engine, text

db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_string)


def test_insert():
    connection = db.connect()
    transaction = connection.begin()

    sql = text('INSERT INTO subject(\"subject_id\", \"subject_title\") '
               'VALUES (:new_id, :new_title)')
    result = connection.execute(sql, {"new_id": 20, "new_title": "Testing"})

    assert result.rowcount == 1

    check_sql = text('SELECT * FROM subject WHERE subject_id = :id')
    check_result = connection.execute(check_sql, {"id": 20})
    inserted_data = check_result.fetchone()

    assert inserted_data is not None
    assert inserted_data.subject_id == 20
    assert inserted_data.subject_title == "Testing"

    transaction.commit()
    connection.close()


def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql = text('UPDATE subject SET subject_title = :title '
               'WHERE subject_id = :id')
    result = connection.execute(sql, {"title": 'Freedom', "id": 20})

    assert result.rowcount == 1

    check_sql = text('SELECT subject_title '
                     'FROM subject WHERE subject_id = :id')
    check_result = connection.execute(check_sql, {"id": 20})
    updated_data = check_result.fetchone()

    assert updated_data is not None
    assert updated_data.subject_title == "Freedom"

    transaction.commit()
    connection.close()


def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM subject WHERE subject_id = :id")
    result = connection.execute(sql, {"id": 20})

    assert result.rowcount == 1, "Должна быть удалена одна строка"

    check_sql = text('SELECT * FROM subject WHERE subject_id = :id')
    check_result = connection.execute(check_sql, {"id": 20})
    deleted_data = check_result.fetchone()

    assert deleted_data is None

    transaction.commit()
    connection.close()