import random
import streamlit as st


def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        # I noticed Hard was using 1 to 50, which actually made it easier than Normal.
        # I fixed it by making Hard use a bigger range so the difficulty makes more sense.
        return 1, 200
    return 1, 100


def parse_guess(raw: str):
    if raw is None:
        return False, None, "Enter a guess."

    if raw.strip() == "":
        return False, None, "Enter a guess."

    try:
        # I saw the old code turned decimals like 7.9 into 7, which could confuse the player.
        # I fixed it by only allowing whole numbers, since this is a number guessing game.
        value = int(raw)
    except ValueError:
        return False, None, "That is not a whole number."

    return True, value, None


def check_guess(guess, secret):
    if guess == secret:
        return "Win", "🎉 Correct!"
    elif guess > secret:
        # I noticed this hint was backwards before. If my guess is too high,
        # I should be told to go lower, not higher. I fixed the message to match the result.
        return "Too High", "📉 Go LOWER!"
    else:
        # I also fixed the low hint because it was reversed before.
        # If my guess is too low, the game should tell me to go higher.
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        # I noticed the old formula gave a weird score drop because it used attempt_number + 1.
        # I fixed it so earlier wins give better scores in a more normal way.
        points = 100 - 10 * (attempt_number - 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        # I saw the old code sometimes gave me points for a wrong answer.
        # I fixed it so wrong guesses always reduce the score instead of randomly helping me.
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score


st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

# I noticed the secret number only got created once, so changing difficulty did not always update it.
# I fixed this by also storing the last difficulty and resetting the game when the difficulty changes.
if "last_difficulty" not in st.session_state:
    st.session_state.last_difficulty = difficulty

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

if "attempts" not in st.session_state:
    # I saw attempts started at 1, which made the player lose one turn right away.
    # I fixed it by starting attempts at 0 so the count begins correctly.
    st.session_state.attempts = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

if st.session_state.last_difficulty != difficulty:
    # I noticed that switching difficulty did not reset the game state.
    # I fixed it by resetting everything when the player picks a new difficulty.
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.last_difficulty = difficulty

st.subheader("Make a guess")

# I noticed the old message always said 1 to 100, even when the difficulty changed the range.
# I fixed it so the message uses the real low and high values from the selected difficulty.
st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)

with st.expander("Developer Debug Info"):
    # I saw the debug box was revealing the secret number, which breaks the game.
    # I fixed it by removing the secret from the visible debug output.
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{difficulty}"
)

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

if new_game:
    # I noticed the old New Game button only reset some parts of the game.
    # I fixed it by resetting the attempts, score, status, history, and secret number.
    st.session_state.attempts = 0
    st.session_state.secret = random.randint(low, high)
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        # I noticed invalid input used to count as an attempt, which felt unfair.
        # I fixed it so only real guesses count against the player.
        st.error(err)
    else:
        # I added a range check because the old code let me enter numbers outside the game range.
        # I fixed it by blocking guesses that are below the minimum or above the maximum.
        if guess_int < low or guess_int > high:
            st.error(f"Enter a number between {low} and {high}.")
        else:
            st.session_state.attempts += 1
            st.session_state.history.append(guess_int)

            # I noticed the old code sometimes changed the secret number into a string.
            # I fixed it by always keeping the secret as an integer so comparisons stay correct.
            secret = st.session_state.secret

            outcome, message = check_guess(guess_int, secret)

            if show_hint and outcome != "Win":
                st.warning(message)

            st.session_state.score = update_score(
                current_score=st.session_state.score,
                outcome=outcome,
                attempt_number=st.session_state.attempts,
            )

            if outcome == "Win":
                st.balloons()
                st.session_state.status = "won"
                st.success(
                    f"You won! The secret was {st.session_state.secret}. "
                    f"Final score: {st.session_state.score}"
                )
            else:
                if st.session_state.attempts >= attempt_limit:
                    st.session_state.status = "lost"
                    st.error(
                        f"Out of attempts! "
                        f"The secret was {st.session_state.secret}. "
                        f"Score: {st.session_state.score}"
                    )

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")