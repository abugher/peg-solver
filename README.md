# Program Usage:

    ./pegSolver

Find and display one solution to the puzzle.

    ./pegSolver -a

Find and display every solution to the puzzle.  Slower.


# Library Usage

    import PegPuzzle

    puzzle = PegPuzzle.Puzzle()
    solutions = puzzle.solve()

Optional arguments may be specified for `solve()`.  Setting `all` to `True`
causes `solve()` to find every solution, while a value of `False` causes it to
find only the first solution.  Setting `output` to `True` will cause `solve()`
to  output solutions as it finds them, including a visual representation of
each state of the puzzle, while a value of `False` will cause it to omit any
output.

`solve()` returns a list of solutions.  Each solution is a list of steps.  Each
step is a list containing three elements assumed to be *x* and *y* coordinates
of a peg (integers) followed by direction of travel (string).
