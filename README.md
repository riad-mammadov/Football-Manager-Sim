# ⚽ Football Manager Simulator (Python)

A Python based Football Manager simulation that models football teams, players, and matches with probabilistic outcomes. This is a personal side project aimed at exploring OOP design, simulations, and will later include a GUI interface (+ possible deployment).

## 🚀 Features

- Teams with real individual players, positions, and dynamic skill ratings
- Simulate matches between two teams using probabilistic outcomes based on team strength
- Includes randomness to ensure realistic results (better teams don’t always win)
- Track player performance (e.g. goals scored, assists)
- Save / Load game

## 🧠 How It Works

- Each player has attributes: name, position, rating, and goals (will add more as i work on this)
- A team consists of a full squad of players (18) and an overall rating (calculated from player ratings)
- Match simulation uses a weighted random probability model:
  - Takes into account average team rating
  - Adds a draw chance
  - Simulates outcomes: win, lose, or draw

## 🛠 Technologies (so far)

- Python
- Object-Oriented Programming (OOP)
