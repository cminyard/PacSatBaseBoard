# PacSatBaseBoard

This is a base board design to start with for a PacSat design, or
really any Pumpkin Space CSKB board.

To use this, pull this project up in KiCad, then do "Save As" under
the file menu and save it in a new directory to use as the starting
point for your board.  You might have to deal with the .git directory
being copied.

All local footprints go into the "footprints" directory, create symbol
libraries in the "symbols" directory as necessary.  There are already
connectors added to those.

NOTE: The CSKB standard has ESQ-126-39-G-D PC104 connectors, which
have 12.19mm pins.  This leaves around 3mm of pin exposed between the
boards.  This design has ESQ-126-38-G-D PC104 connectors, which has
7.36mm pins.  This leaves the 11.05mm as the board height, and 11.11mm
(.438") spacers are pretty common.
