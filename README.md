# 🟩🟨 Wordle Solver using Information Theory 🟨⬛

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Concept](https://img.shields.io/badge/Concept-Information_Theory-success.svg)
![Algorithm](https://img.shields.io/badge/Algorithm-Entropy_Maximization-orange.svg)

## 📌 Description
🧠 An optimal Wordle solver using Information Theory. This Python algorithm calculates Shannon Entropy to find the mathematically best guess, eliminating the most words per turn! 🟩🟨⬛

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
```

### 3. Usage Instructions

1. **Select Mode:** The program will ask if you want to see just the absolute *Top 1 guess* or a ranked list of the *Top 15 guesses*.

2. **Make a Guess:** The solver will suggest the best mathematical starting word (e.g., `tares` or `roate`). Enter your chosen word into the actual Wordle game, then type it into the script.

3. **Input Feedback:** Input the color feedback provided by the Wordle game using the following format:

   * `g` = **Green** (Correct letter, correct position)
   * `y` = **Yellow** (Correct letter, wrong position)
   * `r` = **Red/Gray** (Letter not in the word)
   
   *Example:* If the game gives you Green, Gray, Yellow, Gray, Green, you type: `gryrg`

4. **Repeat:** The script will instantly filter the remaining words, recalculate the entropy, and give you the best next guess. Repeat until you win!

---

## 💻 Example Output
```text
Welcome to Wordle Solver!
Show top (1) guess or (15) guesses? Enter 1 or 15: 1

====== Round 1 ======
Remaining possible answers: 2315

Information Gain Reporting for best guess (tares):
prior entropy H(W) = 11.176798 bits
best-guess expected feedback entropy H(Y) = 6.193952
expected posterior entropy H(W|Y) = 4.982845
information gain I(W;Y) = 6.193952

Best guess: tares   entropy = 6.193952

Enter your guess: tares
Enter feedback (g/y/r): rrrgr
```
