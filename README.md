# SnowEx Database

This is an exercise in replicating database creation for the
 NASA SnowEx datasets, following https://github.com/SnowEx/snowexsql and 
https://github.com/SnowEx/snowex_db. The goal is to learn new tools such as
[SQLModel](https://sqlmodel.tiangolo.com/) 
and [FastAPI](https://fastapi.tiangolo.com/), 
as well as alternative database design patterns.

## Command-Line Interface

Currently there is a single app and function for database testing and 
development: 

`snowexdb populate_database add-density`

## Acknowledgements

* [sqlmodel-repository-pattern](https://github.com/manukanne/sqlmodel-repository-pattern/tree/main)
* [NSF Resilience App Project](https://github.com/UW-THINKlab/resilience/tree/main)
* [Scientific Software Engineering Center](https://escience.washington.edu/software-engineering/ssec/), especially [Don Setiawan](https://github.com/lsetiawan) and [Cordero Core](https://github.com/uwcdc).