#!/usr/bin/env python3
challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]
a = challenge[2][1]
b = challenge[2][0]
c = challenge[3]
print(f"My {a}! The {b} do {c}! ")

trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]
d = trial[2]["goggles"]
e = trial[2]["eyes"]
f = trial[-1]
print(f"My {d}! The {e} do {f}!")

nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]
x = nightmare[0]["user"]["name"]
print(f"My {x}! The {y} do {z}!")

