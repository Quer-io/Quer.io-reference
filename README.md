# Quer.io-reference
This repository is an example of how [Quer.io](https://github.com/Quer-io/Quer.io) could be used.

This repository contains example Python scripts that use Quer.io, a SQLite database and a docker environment
that sets up a Postgresql database and a MariaDB database. 

This project is intended to be used as a way to get to know how to use Quer.io. 
This predefined, built in environment can be used to play around or just as an reference on how to make basic queries
.

  
## Database

This example repositorys Postgres has a schema like this. 

![db_schema](https://github.com/Quer-io/Quer.io/blob/db/normalized/documentation/database/diagrams/querio_multitable.JPG)
  

SQLite and MariaDB do not have the querio_view created by default 
and only have the following tables:
- person (No FK to Profession)
- github
- person_github

## Usage

Things you need:

 - Python 3.6
 - pip3
 - Docker and Docker compose (For Postgresql and MariaDB)

**Note: Library mysqlclient requires an installation of
 MySQL or MariaDB in your system. If you have no intention of 
 installing them you can just remove mysqlclient from requirements.txt**
 
 Install requirements from project root with:
 
 `pip3 install -r requirements.txt`
 
 Scripts can be run with basic python like this:
 
 `python3 querio_sqlite_example.py`
 
 ### Using sqlite
 This repository contains a SQLite-database that has already been populated with 10000 
 rows of data. The script **querio_sqlite_example.py** uses this database to create a 
 Quer.io-model and makes some queries to it. Feel free to clone the repository and
 modify the queries as much as you like locally.
 
 If you want to test it on a larger SQLite database, you just need to run:
 
 `python3 sqlite/init_sqlite.py [row count]`
 
 from project root.
 
 ### Setting up Postgres and MariaDB with Docker compose
 After installing everything defined above first thing to do is open a command prompt
 and navigate to the project root folder. Then start the environment by following these steps:
 
 - `cd docker-enviornment`
 - `docker-compose up`
 
 *If you run into permission problems add `sudo` in front of the commands*
 
 Databases are now being deployed and populated. This will set up and populate both mariadb and postgres databases.
 However if you want to start only some containers you can do it like this:
 
 **Postgres + Postgres populator**
 
 `docker-compose up postgres normalized-postgres-populator`
 
 Sets up a postgres-database and populates it
 
 **MariaDB + MariaDB-populator**
   
 `docker-compose up mariadb normalized-mariadb-populator`
 
 Sets up a MariaDB-database and populates it
 
  **MariaDB + Postgres**
   
 `docker-compose up mariadb postgres`
 
 Only sets up the databases. If the database has been populated before, population is not needed
 anymore.
 
 
 Our Docker-Compose set up uses [wait-for-it](https://github.com/vishnubob/wait-for-it)
 
 