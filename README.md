# Diplo Jargon Jumble

A command-line word scramble game themed around diplomacy and international relations terminology. Unscramble the word, use hints if you're stuck, and see how well you know your diplomatic jargon.

## How to Play

1. Run the game:
   ```
   python app.py
   ```
2. Each round shows a scrambled word related to diplomacy.
3. Type your guess, or use one of these commands instead:
   - `hint` — reveals a clue about the word, then asks you to guess again
   - `skip` — skips the round and reveals the answer
   - `quit` — ends the game immediately
4. After 10 rounds, you'll get a final score and a title based on your performance — from "Study up" all the way to "practically an ambassador."
5. When the game ends, you'll be asked if you want to play again.

## Requirements

- Python 3
- A `diplomacy_words.py` file in the same directory, containing a `DIPLOMACY_WORDS` list of `(word, hint)` tuples

## Project Structure

- `app.py` — main game logic
- `diplomacy_words.py` — word bank (word/hint pairs) used by the game

## Notes

- The screen-clear function uses `cls` on Windows and `clear` on macOS/Linux, so replaying the game starts with a fresh terminal.
- Scoring bands and messages can be tweaked directly in the `play_game()` function if you want to adjust difficulty or add new rank titles.
- This is based on a project from Scrimba's "Learn Python" course at https://scrimba.com. Check it out!
