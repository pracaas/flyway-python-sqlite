# Flyway Migration using SQLite database

This guide explains how to set up Flyway for new and an existing database.
## Usage of Flyway Migration

### 1. **Flyway Migration for startup**
a. Install Flyway.
> brew install flyway

b. Setup Config file
> Example flyway.conf file from new database project

c. Place your migration Files:
>  place your SQL files in sql/migration as mentioned in project

d. Naming convention for SQL DDLs.
> V1__create_table.sql

e. Run Migration.
> flyway migrate

f. Result:
![img.png](img.png)

g. From new_database project run migration script
> flyway_migration.py.py

### 2. **Flyway Migration for existing database**
a. Repeat steps 1a - 1d   

b. Create a baseline
> flyway baseline

c. Run Migration.
> flyway migrate

d. Result:
![img_1.png](img_1.png)

e. From existing_database project run migration script
> existing_flyway_migration.py