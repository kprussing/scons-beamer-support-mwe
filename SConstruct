#!/usr/bin/env python

import os

env = Environment(PDFLATEX="lualatex", # Personal preference only
                  TEXINPUTS="tex", # Tell SCons where to find extra files
                  ENV={"PATH": os.environ["PATH"], # For my LaTeX install
                       "TEXINPUTS": "tex" + os.sep, # Have LaTeX search here to
                       },
                  IMPLICIT_COMMAND_DEPENDENCIES=False, # Implicit dependencies are boring
                  )

# Make an image to see a more complex tree
env.Command("mwe.png", "mwe.py", action="python $SOURCE")

# Define the main target
pdf = env.PDF("beamer-support.tex")
