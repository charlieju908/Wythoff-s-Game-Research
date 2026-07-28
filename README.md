# Wythoff-s-Game-Research

1. Overview
   
Wythoff's game is a two-player impartial combinatorial game involving two separate numbers. Players take turns subtracting any one given amount from one or both piles, given by (a-k,b) or (a-k,b-k). The objective is to    be the player who is the last to subtract from the piles.

2. Files
   
"Wythoffs_Game_Solver.py" -- Main playable algorithm for solving game positions.
"Wythoffs_Game_Simulator.py" -- Testing framework used to simulate losing positions in order to find underlying patterns.

3. Goal
   
The main goal of this project was to find an independent solution to Wythoff's game that did not involve directly computing the golden ratio in any way.

4. Conclusion
   
This project represents an exploration of Wythoff's Game through computational methods. The solver was independently developed to identify game positions and investigate patterns among losing positions. Ultimately,     "Wythoffs_Game_Solver.py" was able to correctly identify the solution to the game through an iterative construction algorithm that generates Wythoff pairs by selecting the next unused integer and deriving its corresponding pair. Earlier versions of the solver appeared to produce incorrect results; however, further investigation revealed that these inconsistencies were caused by assumptions made over an insufficient range rather than a flaw in the logic itself. Expanding the testing range allowed the solver to be properly validated and highlighted the importance of rigorous computational testing when analyzing irrational mathematical patterns. The "Wythoffs_Game_Simulator.py" file utilizes the established golden ratio-based solution to Wythoff's Game, using Beatty sequences to generate known Wythoff pairs. This simulator was used as a reference tool throughout development, allowing the independently developed construction algorithm in "Wythoffs_Game_Solver.py" to be tested, compared, and refined against the known mathematical solution.
   
