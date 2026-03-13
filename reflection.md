# 💭 Reflection: Game Glitch Investigator

## 1. What was broken when you started?

When I first ran the game it looked like it worked, but after playing it I noticed things were wrong. The hints were backwards, so when my guess was too high the game told me to go higher instead of lower. I also noticed the secret number sometimes behaved strangely because it was being turned into a string in some cases. Another issue was that the attempt counter started at 1, so I was losing an attempt before I even guessed.

---

## 2. How did you use AI as a teammate?

I used Claude while working on this project to help review the code and explain where the bugs were. One suggestion that was correct was fixing the hint logic in the check_guess() function so that “Too High” tells the player to go lower and “Too Low” tells them to go higher. I verified this by running the game and testing guesses above and below the secret number. One suggestion that was misleading was about decimal input handling, because the game originally converted decimals to integers. After testing it myself, I realized it made more sense to only allow whole numbers for guessing.

---

## 3. Debugging and testing your fixes

I decided a bug was fixed by running the game again and testing the behavior step by step. For example, I manually tested the hint system by guessing numbers above and below the secret number to see if the hints were correct. I also tested invalid inputs like letters or blank guesses to make sure they did not break the game. AI helped by suggesting different cases to test, like checking what happens when guesses are outside the allowed range.

---

## 4. What did you learn about Streamlit and state?

The secret number kept changing in the original app because Streamlit reruns the whole script every time the user interacts with the page. That means if the secret number is not stored properly, it gets regenerated each time the script runs. I would explain Streamlit reruns to a friend as the app restarting the script every time a button is pressed or input changes. The fix was storing the secret number in st.session_state, which keeps the value between reruns.

---

## 5. Looking ahead: your developer habits

One habit I want to reuse is testing features step by step instead of assuming the code works after writing it. Next time I work with AI on a coding task, I will test the suggestions more carefully instead of trusting them immediately. This project showed me that AI-generated code can be helpful, but it still needs careful review and testing by a developer.