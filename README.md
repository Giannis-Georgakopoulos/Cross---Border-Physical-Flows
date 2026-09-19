# Cross-Border Physical Flows

A Python desktop application for viewing Greece's cross-border electricity flows from local Excel files. The interface supports daily, monthly and yearly views for 2022–2023.

## Features

- Displays total incoming and outgoing energy and net position (outgoing minus incoming).
- Shows exchanges with Albania, Bulgaria, Italy, North Macedonia and Turkey.
- Includes charts, daily hourly profiles and maximum exchange statistics.
- Compares Greece's total incoming and outgoing energy with Germany, France or Denmark for the selected period.

## Project files

- `main_window .py` — graphical interface.
- `greece algorithms/` — calculations for Greece.
- `compare algorithms/` — calculations for the comparison countries.
- `DATAENERGY.zip` and `DATAENERGY_2.zip` — data archives.
- `logo.png` — application icon.

## Requirements

Uses Python, Tkinter, ttkbootstrap, Pillow, pandas and Matplotlib.

The code expects extracted Excel files under `DATAENERGY/` and `DATAENERGY_2/`, uses Windows-style data paths, and imports the calculation modules directly. Those modules must be available on Python's import path when launching `main_window .py`.
