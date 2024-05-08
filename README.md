# Chicago Lobbyist Database Application

# Overview
This project is a Python-based console application that manages data related to registered lobbyists in Chicago. Utilizing an N-tier architecture, the application connects to a database that holds information about lobbyists, their employers, clients, and compensation. The project is structured in three parts, each corresponding to a specific software layer:

Data Access Tier (Part 1): Responsible for directly interacting with the database through SQL queries.
Object Mapping Tier (Part 2): Provides Python classes that model the data retrieved from the data access tier.
Presentation Tier (Part 3): Handles user interactions and displays the processed data via the command-line interface.
Database Structure
The Chicago Lobbyist database comprises eight tables: LobbyistInfo, LobbyistYears, EmployerInfo, EmployerYears, ClientInfo, ClientYears, LobbyistAndEmployer, and Compensation. Each table provides a comprehensive view of the lobbyist ecosystem in Chicago, allowing the application to perform various analyses and operations.

# Key Features
The application features five main commands, accessed via a user-friendly menu:

Search Lobbyists: Find lobbyists by their first or last name using SQL wildcards.
View Lobbyist Details: Retrieve comprehensive details of a specific lobbyist, including years of registration, employers, and total compensation.
Top N Lobbyists: Identify the top N lobbyists based on total compensation for a specific year.
Add Registration Year: Register an existing lobbyist for a new year.
Set Salutation: Update the salutation for a given lobbyist.

# Requirements
Python 3: The application uses Python for data manipulation and user interaction.
SQLite3: SQL queries are executed via the sqlite3 package for efficient data access.
Project Development
Part 1 (Data Access Tier): Implement functions to execute SQL queries directly against the database.
Part 2 (Object Mapping Tier): Create Python classes to represent data objects, interfacing with the data access layer.
Part 3 (Presentation Tier): Develop the main user interface to accept commands and coordinate data retrieval from the object mapping layer.
