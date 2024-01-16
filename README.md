 AirBnB_clone_v2

![AirBnB_clone_v2 Logo](https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step2.png)

## Overview

AirBnB_clone_v2 is an extended version of the AirBnB_clone project, offering enhanced features and functionalities. This collaborative effort builds upon the existing AirBnB_clone codebase, implementing tasks related to database storage, model updates, and relationships between different classes.

## Table of Contents

1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [Setup](#setup)
  - [Bug Free](#bug-free)
  - [Console Improvements](#console-improvements)
  - [MySQL Setup Development](#mysql-setup-development)
  - [MySQL Setup Test](#mysql-setup-test)
  - [Delete Object](#delete-object)
4. [Usage](#usage)
5. [Tasks](#tasks)
    1. [Console](#1-console)
    2. [FileStorage](#2-filestorage)
    3. [DBStorage - User](#3-dbstorage---user)
    4. [DBStorage - Place](#4-dbstorage---place)
    5. [DBStorage - City](#5-dbstorage---city)
    6. [DBStorage - State](#6-dbstorage---state)
    7. [DBStorage - Amenity](#7-dbstorage---amenity)
    8. [DBStorage - Place (continued)](#8-dbstorage---place-continued)
    9. [DBStorage - Review](#9-dbstorage---review)
    10. [DBStorage - Amenity... and BOOM!](#10-dbstorage---amenity-and-boom)

## Introduction

The Airbnb Clone v2 project is a Python application that replicates some of the functionalities of the Airbnb website. It includes an interactive console, storage management, and database integration.

## Project Structure

The project is organized into the following directories:

- `models`: Contains the Python classes representing the data model.
- `tests`: Includes unit tests for various components of the application.
- `console.py`: The interactive console for managing the application.
- `main_place_amenities.py`: A script to test the Many-To-Many relationship between `Place` and `Amenity`.

## Setup

To set up the Airbnb Clone v2 project, follow these steps:

1. Clone the GitHub repository:

```bash
git clone https://github.com/your-username/AirBnB_clone_v2.git
```

2. Change into the project directory:

```bash
cd AirBnB_clone_v2
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```
#### Bug Free

To ensure bug-free functionality, all unit tests must pass without any errors at any time in this project, with each storage engine. Use the following commands to run the tests:

```bash
python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1
```

For MySQL testing:

```bash
HBNB_ENV=test HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1
```

#### Console Improvements

Update the `do_create(self, arg)` function in your command interpreter (`console.py`) to allow for object creation with given parameters. The command syntax is as follows:

```bash
create <Class name> <param 1> <param 2> <param 3>...
```

Param syntax:

- String: `<key name>="<value>"` (escape double quotes with a backslash `\` and replace underscores `_` with spaces)
- Float: `<unit>.<decimal>`
- Integer: `<number>`

Example:

```bash
create State name="California"
create State name="Arizona"
all State

create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297
all Place
```

#### MySQL Setup Development

Write a script (`setup_mysql_dev.sql`) that prepares a MySQL server for the project with:

- Database: hbnb_dev_db
- User: hbnb_dev (password: hbnb_dev_pwd)
- All privileges on hbnb_dev_db for hbnb_dev
- SELECT privilege on performance_schema for hbnb_dev

Run the script using:

```bash
cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p
```

#### MySQL Setup Test

Write a script (`setup_mysql_test.sql`) that prepares a MySQL server for testing with:

- Database: hbnb_test_db
- User: hbnb_test (password: hbnb_test_pwd)
- All privileges on hbnb_test_db for hbnb_test
- SELECT privilege on performance_schema for hbnb_test

Run the script using:

```bash
cat setup_mysql_test.sql | mysql -hlocalhost -uroot -p
```

#### Delete Object

Update `FileStorage` (`models/engine/file_storage.py`) to include a new public instance method `delete(self, obj=None)`:

- Delete `obj` from `__objects` if it's inside. If `obj` is `None`, the method should do nothing.
- Update the prototype of `all(self)` to `all(self, cls=None)` to return a list of objects of one type of class if `cls` is provided.

## Usage

To use the Airbnb Clone v2 project, follow these steps:

1. Run the interactive console:

```bash
./console.py
```

2. Execute commands within the console to manage users, places, amenities, and more.

## Tasks

### 1. Console

The console provides an interactive command-line interface for managing the Airbnb Clone v2 application. It supports commands for creating, updating, and querying various entities.

### 2. FileStorage

The `FileStorage` module provides functionality for serializing and deserializing objects to and from JSON format. It enables the persistent storage of application data.

### 3. DBStorage - User

The `DBStorage` module introduces database storage using SQLAlchemy for the `User` class. It includes the necessary updates to create, update, and query user data.

### 4. DBStorage - Place

The `DBStorage` module extends database storage to the `Place` class. It includes table definitions, relationships, and foreign key constraints.

### 5. DBStorage - City

The `DBStorage` module updates the `City` class to establish relationships with the `Place` class. It ensures that linked place objects are automatically deleted when a city is deleted.

### 6. DBStorage - State

The `DBStorage` module updates the `State` class to establish relationships with the `City` class. It ensures that linked city objects are automatically deleted when a state is deleted.

### 7. DBStorage - Amenity

The `DBStorage` module introduces the `Amenity` class and establishes basic table structure for database storage.

### 8. DBStorage - Place (continued)

Continuation of task 4, including additional attributes and relationships for the `Place` class. This task introduces latitude and longitude columns and updates relationships with the `User` and `City` classes.

### 9. DBStorage - Review

The `DBStorage` module extends database storage to the `Review` class. It includes table definitions, relationships, and foreign key constraints.

### 10. DBStorage - Amenity... and BOOM!

The `DBStorage` module introduces the `Amenity` class and establishes a Many-To-Many relationship with the `Place` class using the `place_amenity` table. The script `main_place_amenities.py` demonstrates this relationship with sample data.

**Note**: For detailed instructions on each task, please refer to the specific sections in the README corresponding to each task.

You are now ready to use the Airbnb Clone v2 project! If you encounter any issues or have questions, refer to the documentation or contact the project maintainers. Happy coding!

## Contributing

We welcome contributions from the community! If you'd like to contribute to AirBnB_clone_v2

, please follow our [contribution guidelines](CONTRIBUTING.md).
