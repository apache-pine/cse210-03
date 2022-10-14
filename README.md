# Jumper

Jumper is a game in which the player seeks to solve a puzzle by guessing the letters
of a secret word one at a time. A secret word is randomly chosen from a bank of words,
each turn the player has a chance to guess one letter. If the letter is in the word
it will be displayed in the blank spot. If not, one of the lines on the jumper's
parachute is cut. If the jumper has no more parachute, the game is over. If every letter in the word is guessed, the player wins.

---

## Getting Started

To launch the game, first ensure that you have Python 3.8.0 or newer installed
and running on your machine. Open a terminal and browse to the root folder. Start
the program by running the following command:

```
python3 jumper
```

Alternatively, you can open the program from an IDE, like VS Code. Start the IDE
and open to the root folder. Select the main module inside the hilo folder and
click "run".

---

## Project Structure

The project files and folders are organized as follows:

```
root                            (project root folder)
+-- jumper                      (source code for game)
  +-- game                      (specific classes)
    +-- director.py             (director class)
    +-- player.py               (player class)
    +-- secret_word.py          (secret word class)
    +-- terminal_service.py     (terminal service class)
  +-- __main__.py               (program entry point)
+-- README.md                   (general info)
```

---

## Required Technologies

- Python 3.8.0

---

## Authors

- Brandon Smith - player
- Garrett Cooper - director
- Kylar Sorensen - director, README
- McKay Thomas - terminal_service, `__main__.py`
- Zak Sattler - secret_word
