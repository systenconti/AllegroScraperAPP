# AllegroScraperAPP
> This app allows user to scrape auctions list of desired products.

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Contact](#contact)


## General Information
Allegro scraping app allows user to automatically search for desired product. In my case it
was dog food for my dogs. App sends user 10 cheapest auctions and a screenshot of
these auctions via e-mail. It all happens with only one click.
<!-- You don't have to answer all the questions - just the ones relevant to your project. -->


## Technologies Used
- Python 3.11
- Selenium
- SQLite


## Features
- Scrape auctions with one click
- Send auctions automatically via email
- Store results in SQLite database
- "read" function allows querying database by date. This could be useful when comparing prices in the future.


## Project Status
Project is: _complete_


## Room for Improvement
I believe that usage of database in this project could have a greater potential than just querying by date and printing it out in the console.

Improvement ideas:
- Creating a functionality that sends an e-mail with old and new auctions. This would allow user to compare prices in the same e-mail.

## Contact
Created by [@systenconti](https://github.com/systenconti) - feel free to contact me!
