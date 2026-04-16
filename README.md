# 🟩🟨 Wordle Solver using Information Theory 🟨⬛

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Concept](https://img.shields.io/badge/Concept-Information_Theory-success.svg)
![Algorithm](https://img.shields.io/badge/Algorithm-Entropy_Maximization-orange.svg)

## 📌 About the Project
This project is an intelligent algorithm designed to solve the popular word-guessing game **[Wordle](https://www.nytimes.com/games/wordle/index.html)** in the absolute minimum number of attempts. 

Instead of relying on random guessing or simple heuristics, this solver employs **Information Theory** and **Shannon Entropy** to mathematically calculate the optimal next guess. By maximizing the Expected Information Gain, the algorithm aggressively eliminates the maximum possible number of remaining words with every single move.

---

## 👥 Contributors
This project was developed by Computer and Systems Engineering (CSED28++) students at **Alexandria University - Faculty of Engineering**:

* **Anas Alaa Abdo** (ID: `24010004`) - [GitHub Profile](https://github.com/AnasAlaa11)
* **Adham Hamdy Mohamed Mohamed** (ID: `24010094`) - [GitHub Profile](https://github.com/AdhamHamdy14)

---

## 🧠 How it Works (The Math behind the Magic)
The core engine of this solver relies on computing the **Entropy (H)**. 
For every possible word in the dictionary, the solver simulates all possible feedback patterns (Green, Yellow, Gray/Red). It calculates how the remaining pool of target words will be split for each pattern.

Using the formula for Expected Entropy:
`H = - Σ (p_x * log2(p_x))`

The solver ranks the dictionary words and suggests the word with the **highest entropy** (Information Gain). This guarantees that regardless of the feedback the game gives, the remaining possible answers will be drastically reduced.

---

## 📁 Repository Structure
* `main.py`: The core python script containing the algorithm and interactive CLI.
* `dictionary_5_letter.json`: A comprehensive list of valid 5-letter English words (Allowed guesses).
* `targets_5_letter.json`: The specific list of words that can actually be the final answer (Target pool).

---

## 🚀 How to Run & Play

### 1. Prerequisites
Ensure you have Python 3 installed on your machine. No external libraries are required (only built-in modules like `math`, `heapq`, and `json`).

### 2. Execution
Clone the repository, navigate to the directory, and run the script:
```bash
python main.py
