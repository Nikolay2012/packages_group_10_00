def delete_table(cursor: object, name_table: str):

    cursor.execute(f"DROP TABLE {name_table}")  