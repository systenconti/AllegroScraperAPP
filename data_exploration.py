import sqlite3
from datetime import datetime


now = datetime.now()
date = now.strftime("%d.%m.%Y")

connection = sqlite3.connect('data.db')

dates = []
offers = [['Karma AS WILD FISH 12kg only bez zbóż rybna sucha', 'https://allegro.pl/oferta/karma-as-wild-fish-12kg-only-bez-zboz-rybna-sucha-10220232459', '235,45 zł'],
          ['Alpha Spirit Wild Fish ryby półwilgotna karma 12kg',
              'https://allegro.pl/oferta/alpha-spirit-wild-fish-ryby-polwilgotna-karma-12kg-9956784790', '236,99 zł'],
          ['Alpha Spirit Wild Fish 12kg RYBY',
              'https://allegro.pl/oferta/alpha-spirit-wild-fish-12kg-ryby-9926782116', '238,60 zł']]

dates.append(date)

offers = [offer + dates for offer in offers]

def store(offerslist):
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO offers VALUES(?,?,?,?)", offerslist)
    connection.commit()

def read(searchdate):
    """Searchdate format = 'dd.mm.yyyy'"""
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM offers WHERE searchdate='{searchdate}'")
    rows = cursor.fetchall()
    print(rows)
    return rows



if __name__ == "__main__":
    store(offers)
    read('06.04.2023')
