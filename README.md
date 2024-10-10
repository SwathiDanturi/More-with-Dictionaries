[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/4-6plzpo)
> **COMP-801 Integrated Computing Practicum**
# Homework 2

> h2start

Due before Wednesday midnight, before Week 8 class

- Upload to Canvas the PDF of the DESIGN.md
- Push to the remote all the changes made to the local repo

##  Requirements

Use test-driven incremental development to:
- Document the Python modules and the design file DESIGN.md with your name as developer
- Create testing modules and write testing functions for the methods in `ScrableLetters` class
- Design the `ScrabbleLetters` methods in DESIGN.md, including the class constructor. 
- Apply version control to demonstrate the development steps: document, test, and design.

**NOTE**: Do NOT proceed with implementing the methods for this assignment. 

## Getting Started
1. Open `git-bash` (in Windows OS) or `terminal` utility (in MacOS or Linux)
2. Clone remote repo into your **comp801/homework** directory 
- Do NOT create **h2** directory. Cloning will do that. 
- Use the `clone` command with TWO arguments as shown below:
```
git clone <URL of your remote repo> h2
```
3. Open h2 folder in VS Code.
4. Run `client.py` in two ways:
  - In the VS Code integrated terminal, run `python client.py`
  - Use the Run Python File button in the upper right corner. 
5. Create 4 testing modules, `test_xxx.py`, where `xxx` is the name of the `ScrableLetters` methodsthat the module is testing. 
6. Check the erors reported in the **Problems** tab of the VS Code
  - Format each file with the code analysis tools and manually, if needed.


## Evaluation
### Documentation (14 pts)

This is **all or nothing requirement**.  

The project has 6 Python modules:

- `client.py`, `scrabble_letters.py`
- 4 testing modules for the methods in the `ScrableLetters` class, including the constructor 
- Write complete docstrings for each module
- Fill in the developer name.

The project must also have a DESIGN.md. Fill in the developer name. 

### Testing functions implementation (16 pts)
8 testing functions, at 2 pts each
- 2 testing functions in each testing module.
- Be sure to include a testing module for the constructor. 
    
### DESIGN.md (16 pts)
4 designs, at 4 pts each

### Incremental development (9 pts)

- 1 commit for proper documentation
- 1-2 commits for implementing each testing module
- 1 commit for each design
- Minimum of 9 commits, with meaningful commit messages and in the correct order

### Code analysis and styling (5 pts)

## Guidelines
1. **Document** properly ALL the files in the repository (EXCEPT for the TXT and CSV files)
  - Version control this step
2. **Understand** what each method is supposed to do, based on the docstring 
   description, BEFORE writing the test cases.
3. Write **testing functions** to demonstrate your understanding of each method.
  - Version control this step
4. **Design** each method
  - Version control this step
5. Repeat steps 2 to 4 for each method (4 times total) to complete this phase of the homework. 
6. Complete **code analysis** by resolving the **Problems** reported in VS Code. 

## Collaboration

With the CAs or course instructors ONLY
- No collaboration with peers or other people is allowed, EXCEPT for the CAs and course instructors
- No other sources of content (internet, GPT tools, etc.) are allowed.
- You are NOT allowed to give your work on this assignment to somebody else, or to do it for someone else 

## Submission
- The commit history of the development process for **h2start** is pushed to GitHub
- The PDF of DESIGN.md is uploaded to the submission link in Canvas. 

---

> h2final

Due **Monday** midnight, after Week 8 class
- Push to the remote all the changes made to the local repo. 

## Requirements
- Continue the work on **h2** repository by implementing, testing, and debugging the `ScrambleLetters` methods. 
- Apply version control
- Resolve all the **Problems** reported in VS Code by running the code analysis tools. 

## Getting started
You already have the local repo for this assignment from **H2 Start** assignment. 

## Evaluation

### Implementation (24 pts)
- 4 methods, at 6 points each


### Incremental development (8 pts)
Version control must show correct order and meaningful commit messages.

- 4 commits, 1 commit for each method
- 1 commit for code analysis, if needed

This is **all or nothing** requirement.

### Code analysis and styling (8 pts)

This is **all or nothing** requirement.

## Guidelines

- Implement the methods according to the design you submitted for H2 Start
- Test your implementation based on the testing functions you developed in H2 Start.
- If there are errors, debug and fix the errors. This might require changes to:
  - Method design in DESIGN.md
  - Method implementation in the Python module
- Apply version control to demonstrate the changes you have made to
- When implementation is complete, do a thorough code analysis with the tools installed in VS Code
  - Fix all the Problems reported by running these tools.  

## Collaboration with the CAs or course instructors ONLY
- No collaboration with peers or other people is allowed, EXCEPT for the CAs and course instructors
- No other sources of content (internet, GPT tools, etc.) are allowed.
- You are NOT allowed to give your work on this assignment to somebody else, or to do it for someone else 

## Submission
- The commit history of the development process for **h2final** is pushed to GitHub
- The PDF of DESIGN.md is uploaded to the submission link in Canvas. 


