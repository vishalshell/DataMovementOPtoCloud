# Data Transfer Script README

This script is designed to transfer data from an on-premise SQL database to an Azure SQL Database. It employs the use of pyodbc for database connectivity, time for controlled iterations, and logging for informative messages.

## Components

### Importing Libraries

The script begins by importing the required libraries: `pyodbc`, `time`, and `logging`.

### Connection Functions

1. `connect_to_on_premise_sql_database()`: This function establishes a connection to the on-premise SQL database using provided credentials.

2. `connect_to_azure_sql_database()`: This function connects to the Azure SQL Database using the provided credentials.

### Data Transfer Function

The `transfer_data()` function is responsible for transferring data from the on-premise database to the Azure SQL Database.

- Data is fetched in chunks of 10,000 records and processed iteratively.
- Each record is inserted into the Azure SQL Database.
- Records are categorized as follows:
  - If insertion is successful, the record is added to the transferred_records list.
  - If a duplicate key violation error occurs, the record is added to the duplicate_records list.
  - For any other exceptions, the record is added to the error_records list.
- The script pauses for 1 second after each iteration.
- The transfer process continues until all records are transferred.

### Main Function

The `main()` function acts as the entry point of the script:

1. It calls the connection functions to establish database connections.
2. It invokes the `transfer_data()` function to initiate the data transfer.
3. Once the transfer is completed, it displays a report including transferred records, duplicate records, and error records.
4. It closes the database connections.

### Script Execution

The script checks if it's being executed as the main module using the `if __name__ == "__main__":` condition. This prevents the main function from executing when the script is imported as a module in another script.

### Error Handling

- The script employs exception handling to manage errors during data transfer.
- If a duplicate key violation error occurs, it identifies the error message and adds the record to the duplicate_records list.
- For other exceptions, the script adds the record to the error_records list.

### Logging

- The script utilizes the `logging` module to log messages, including successful database connections and the final report.

### Comments

The script includes comments to describe the purpose and functionality of each function and section of code.

## Note

This script assumes that correct database credentials and connection details have been provided. It also offers basic handling for duplicate key violations and exceptions. Adaptations may be necessary for your specific database schemas, table structures, and use case requirements.
