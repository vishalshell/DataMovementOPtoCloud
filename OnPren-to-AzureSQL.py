import pyodbc
import time
import logging

def connect_to_on_premise_sql_database():
    """Connects to the on-premise SQL database."""

    server = "your_on_premise_sql_server_name"
    database = "your_on_premise_sql_database_name"
    username = "your_on_premise_sql_username"
    password = "your_on_premise_sql_password"

    connection_string = f"Driver={pyodbc.SQLServer};Server={server};Database={database};Uid={username};Pwd={password}"
    conn = pyodbc.connect(connection_string)

    logging.info("Connected to on-premise SQL database.")

    return conn

def connect_to_azure_sql_database():
    """Connects to the Azure SQL Database."""

    server = "your_azure_sql_server_name.database.windows.net"
    database = "your_azure_sql_database_name"
    username = "your_azure_sql_username"
    password = "your_azure_sql_password"

    connection_string = f"Driver={pyodbc.SQLServer};Server={server};Database={database};Uid={username};Pwd={password}"
    conn = pyodbc.connect(connection_string)

    logging.info("Connected to Azure SQL Database.")

    return conn

def transfer_data(conn_on_premise, conn_azure):
    """Transfers data from the on-premise SQL database to the Azure SQL Database."""

    cursor_on_premise = conn_on_premise.cursor()
    cursor_azure = conn_azure.cursor()

    query = "SELECT * FROM your_table_name"
    cursor_on_premise.execute(query)

    records = cursor_on_premise.fetchmany(10000)
    transferred_records = []
    duplicate_records = []
    error_records = []
    while records:
        for record in records:
            try:
                cursor_azure.execute("INSERT INTO your_table_name (column1, column2, ...) VALUES (?, ?, ...)", record)
                transferred_records.append(record)
            except Exception as e:
                if "duplicate key value violates unique constraint" in str(e):
                    duplicate_records.append(record)
                else:
                    error_records.append(record)
            conn_azure.commit()
            time.sleep(1)
            records = cursor_on_premise.fetchmany(10000)

    cursor_on_premise.close()
    cursor_azure.close()

    # Generate a report

    report = {
        "transferred_records": transferred_records,
        "duplicate_records": duplicate_records,
        "error_records": error_records,
    }

    logging.info("Report: %s", report)

    return report

def main():
    """The main function."""

    conn_on_premise = connect_to_on_premise_sql_database()
    conn_azure = connect_to_azure_sql_database()

    report = transfer_data(conn_on_premise, conn_azure)

    print("Report:")
    print(report)

    conn_on_premise.close()
    conn_azure.close()

if __name__ == "__main__":
    main()
