#!/usr/bin/python3
"""Printing dictionary data stored as lists to the screen"""

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
for x in farms:
    print(x.get("name", "unknown farm"), end=":\n")

    for y in x.get("agriculture"):
        print(" -", y)
