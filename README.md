# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience


**Game’s Purpose**
The purpose of the game is for the player to guess a secret number within a range based on the selected difficulty level. The game gives hints after each guess to tell the player if the guess is too high or too low. The player must guess the correct number before running out of attempts while trying to earn the highest score possible.

**Bugs I Found**
When I tested the game, I noticed the hint logic was backwards, so a guess that was too high told the player to go higher instead of lower. The attempt counter also started at one instead of zero, which meant the player lost an attempt before making a guess. I also saw that the game allowed guesses outside the allowed range and that invalid inputs could count as attempts.

**Fixes I Applied**
I fixed the hint logic so the directions correctly match whether the guess is too high or too low. I changed the attempt counter so it starts at zero and only increases when a valid guess is entered. I also added input validation so only whole numbers inside the allowed range are accepted and invalid inputs do not count as attempts.



## 📸 Demo



## 🚀 Stretch Features


