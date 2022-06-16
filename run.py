"""
This is a choose your own adventure game, based loosely on the theme's of
the book The Heart of Darkness by Joseph Conrad.
You must navigate your way up the Congo river at the height of the
Belgian colonial conquest.
"""

import functions
import narrative

functions.pass_args_in(
    narrative.TITLE_TEXT, functions.begin_game)
