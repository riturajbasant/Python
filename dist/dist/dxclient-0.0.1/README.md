# README #

### DxOpenClient Implementation using PyXB ###

This branch is for DxOpenClient Implementation using PyXB. 

This is done as an attempt to make DxOpen Python implementation operational for version 2.x
General thought is 2.7+ (since 2.7 is currently most stable, at the time of writing this text.)
This is being done using PyXB package which converts entities in .xsd to python objects.

generateDS also does the same but post conversion, had to move to Python 3.7 necessarily.

Hence this branch has been cut to attempt backward compatibility for end users currently operating on
Python 2.x

Some other notes:
    1.
    generateDS conversion footprint is considreably less than PyXB's.
    genDS Dxopen schema FP: somewhat 4 MB.
    PyXB  Dxopen schema FP: somewhat 13-14 MB.

    2.
    genDS conversion is somewhat cleaner and easy to read as compare to PyXB's.

### What is this repository for? ###

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact