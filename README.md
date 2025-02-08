# Program Usage:

    ./pegSolver

Find and display one solution to the puzzle.

    ./pegSolver -a

Find and display every solution to the puzzle.  Slower.


# Library Usage

    import PegSolver

    puzzle = PegSolver.Puzzle()

    solutions = puzzle.solve()

See the code for arguments to `solve()`.  If output is requested, the `solve()`
method will output solutions as it finds them, includin a visual representation
of each state of the puzzle.

`solve()` returns a list of solutions.  Each solution is a list of steps.  Each
step is a list containing three elements:  `x`, `y`, and `direction`,
specifying the coordinates of a peg and the direction it should be moved.  

