"""Welcome to Reflex!."""

from webPython import styles

# Import all the pages.
from webPython.pages import *

import reflex as rx

# Create the app and compile it.
app = rx.App(style=styles.base_style)
app.compile()
