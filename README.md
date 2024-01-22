# Dodgers XIX - Python Game

Welcome to Dodgers XIX! This is a simple game implemented in Python using the Pygame library. The game involves controlling a player to dodge falling stars for as long as possible.

## Instructions

1. Make sure you have Python installed on your system.
2. Install the Pygame library by running the following command:

   ```
   pip install pygame
   ```

3. Download the `bg.jpeg` image file and place it in the same directory as the Python script.

4. Run the script using the following command:

   ```
   python game.py
   ```

5. Use the left and right arrow keys to move the player and dodge the falling stars.

6. Try to survive as long as possible and see how high you can score!

## Code Overview

The Python script `your_script_name.py` implements the Dodgers XIX game. Here is an overview of the key components:

- **Dependencies**: The script uses the Pygame library for game development. Make sure to install it before running the script.

- **Window Setup**: The game window is initialized with a width and height of 1000x800 pixels. The background image (`bg.jpeg`) is loaded and scaled to fit the window.

- **Player and Stars**: The player is represented as a red rectangle, and stars are represented as aqua rectangles. The player can be moved using the left and right arrow keys.

- **Game Loop**: The main game loop continuously updates the game state, handles user input, and redraws the screen. Stars fall from the top, and the player must avoid colliding with them.

- **Time and Score**: The elapsed time is displayed on the screen, indicating how long the player has survived. The game becomes progressively faster, increasing the difficulty.

- **Game Over**: If the player collides with a star, the game displays a "You Lost!" message, waits for a few seconds, and then exits.

Feel free to explore the code, experiment with adjustments, and enhance the game further!

Enjoy playing Dodgers XIX!
