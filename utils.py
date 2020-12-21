import pandas as pd
import csv
import requests
from datetime import datetime
from entries.models import Entry, Director, Actor, Country, Genre


def convert_bytes_to_json_string(bytes):
    data = bytes.decode('utf-8').splitlines()
    df = pd.DataFrame(data)
    return df.to_dict()


def csv_to_json():
    with open("data.csv", encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for rows in csv_reader:
            for _ in rows:
                entry = Entry(
                    show_id=rows['show_id'],
                    title=rows['title'],
                    type=rows['type'],
                    date_added=datetime.strptime(
                        rows['date_added'], "%B %d, %Y"
                    ).date().strftime("%Y-%m-%d"),
                    release_year=rows['release_year'],
                    rating=rows['rating'],
                    duration=rows['duration'],
                    description=rows.get('description', None)
                )
                entry_model = entry.copy(update={
                    'directors': [Director(name=name)
                                  for name in rows['director'].split(",")
                                  if len(rows['director'])],
                    'casts': [Actor(name=name)
                              for name in rows['cast'].split(",")
                              if len(rows['cast'])],
                    'countries': [Country(name=name)
                                  for name in rows['country'].split(",")
                                  if len(rows['country'])],
                    'listed_in': [Genre(name=name)
                                  for name in rows['listed_in'].split(",")
                                  if len(rows['listed_in'])]
                })
            response = requests.post(
                "http://localhost:8000/browse/",
                data=entry_model.json()
            )
            print(response.reason)


if __name__ == "__main__":
    csv_to_json()
