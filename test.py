import db_helper as db


def main():
    connection = db.create_connection()
    results_json = db.get_data(connection)
    print(results_json)
    return results_json


if __name__ == "__main__":
    main()
