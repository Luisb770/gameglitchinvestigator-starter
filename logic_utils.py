def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""

    # I noticed this function was not actually built yet. It only raised
    # NotImplementedError, so the game would crash if I called it. I fixed it
    # by adding the real difficulty ranges and a default case.
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 200
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """

    # I saw this function also only had NotImplementedError, so it would fail
    # instead of checking the user's input. I fixed it by making it validate
    # blank input and convert the guess into a whole number.
    if raw is None:
        return False, None, "Enter a guess."

    if raw.strip() == "":
        return False, None, "Enter a guess."

    try:
        value = int(raw)
    except ValueError:
        return False, None, "That is not a whole number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """

    # I noticed this function was missing too, which means the game could not
    # tell whether my guess was right, high, or low. I fixed it by adding the
    # real comparison logic and matching hint messages.
    if guess == secret:
        return "Win", "🎉 Correct!"
    elif guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""

    # I saw this last function was also unfinished and would crash during score
    # updates. I fixed it by adding simple score rules so wins give points and
    # wrong guesses lower the score.
    if outcome == "Win":
        points = 100 - 10 * (attempt_number - 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score