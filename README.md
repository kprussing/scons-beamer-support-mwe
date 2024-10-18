# Exploring Beamer Support in SCons

This is a minimal working example to explore the dependency tree for
beamer in SCons.  To see the tree, use

    scons --tree=all,prune beamer-support.pdf

The initial state before any changes is:

    +-beamer-support.pdf
      +-beamer-support.tex
      +-mwe.png
        +-mwe.py

The desired tree would be something along the lines of:

    +-beamer-support.pdf
      +-beamer-support.tex
      +-mwe.png
        +-mwe.py
      + tex/beamerthememse.sty
        + tex/beamercolorthememse.sty
        + tex/beamerfontthememse.sty
        + tex/beamerinnerthememse.sty
        + tex/beamerouterthememse.sty
