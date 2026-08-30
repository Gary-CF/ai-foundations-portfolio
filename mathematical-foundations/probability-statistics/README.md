# Probability & Mathematical Statistics

A structured set of notes on probability theory and mathematical statistics, organized as a compact and reusable foundation for later study in machine learning, optimization, online learning, bandits, and reinforcement learning.

## Contents

The current version covers:

- Knowledge map
- Random events and probability
- Conditional probability and independence
- Discrete random variables
- Continuous random variables
- Multivariate random vectors
- Numerical characteristics
- Concentration inequalities and limit theorems
- Mathematical statistics basics
- Parameter estimation

Two appendices extend the main notes toward sequential decision-making:

- Martingales and adaptive concentration
- Markov chains

## PDF

[Read the compiled notes](./probability-statistics-notes.pdf)

## Source Structure

    .
    ├── index.qmd
    ├── chapters/
    ├── appendices/
    ├── images/
    └── _quarto.yml

The notes are maintained as a Quarto Book.

To build the project locally, run:

    quarto render

The generated `_book/` and `.quarto/` directories are excluded from version control.
