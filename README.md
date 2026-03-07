# Assignment 2 — Genetic Algorithm: Knapsack Problem
## Observation Report

**Student Name  :** ___________________________  
**Student ID    :** ___________________________  
**Date Submitted:** ___________________________  

---

## How to Submit

1. Run each experiment following the instructions below
2. Fill in every answer box — do not leave placeholders
3. Make sure the `plots/` folder contains all required images
4. Commit this README and the `plots/` folder to your GitHub repo

---

## Before You Begin — Read the Code

Open `ga_knapsack.py` and read through it. Then answer these questions.

**Q1. What does the `fitness()` function return? Why does an overweight solution score 0?**

```
[ YOUR ANSWER — 2 to 3 sentences ]
```

**Q2. What does `tournament_select()` do? Why are higher-fitness individuals more likely to be chosen?**

```
[ YOUR ANSWER — 2 to 3 sentences ]
```

**Q3. Look at the `run_ga()` loop. Find this line:**
```python
next_gen = [best_chromosome[:]]
```
**What is this doing? Why is it important to always keep the best solution?**

```
[ YOUR ANSWER — 2 to 3 sentences ]
```

---

## Experiment 1 — Baseline Run

**Instructions:** Run the program without changing anything.
```bash
python ga_knapsack.py
```

**Fill in this table:**

| Metric | Your result |
|--------|-------------|
| Number of generations | |
| Best value at generation 1 | |
| Final best value | |
| Total weight of best solution (kg) | |
| Is solution valid (Yes / No) | |

**Copy the printed packing list here:**
```
[ PASTE PACKING LIST OUTPUT HERE ]
```

**Look at `plots/experiment_1.png` and describe what you see (2–3 sentences).**  
*Where does the biggest improvement happen? Does the curve flatten at some point?*
```
[ YOUR OBSERVATION ]
```

---

## Experiment 2 — Effect of Mutation Rate

**Instructions:** In `ga_knapsack.py`, find the `# EXPERIMENT 2` block in `__main__`.  
Copy it three times and run with `mutation_rate` = **0.01**, **0.05**, and **0.30**.  
Save plots as `experiment_2a.png`, `experiment_2b.png`, `experiment_2c.png`.

**Results table:**

| mutation_rate | Final best value | Weight (kg) | Valid? | Shape of curve |
|--------------|-----------------|-------------|--------|----------------|
| 0.01         |                 |             |        |                |
| 0.05         |                 |             |        |                |
| 0.30         |                 |             |        |                |

**Compare the three plots. What happens when mutation is too low? Too high? (3–4 sentences)**  
*Hint: Too low = no diversity, may get stuck. Too high = random search. What is the sweet spot?*
```
[ YOUR OBSERVATION ]
```

**Which mutation_rate gave the best result? Why do you think that is?**
```
[ YOUR ANSWER ]
```

---

## Summary

**Complete this table with your best result from each experiment:**

| Experiment | Key setting | Final value | Main finding in one sentence |
|------------|-------------|-------------|------------------------------|
| 1 — Baseline | mutation_rate = 0.05 | | |
| 2 — Mutation rate | mutation_rate = ___ | | |

**In your own words — what is the most important thing you learned about Genetic Algorithms from these experiments? (3–5 sentences)**
```
[ YOUR REFLECTION ]
```

---

## Submission Checklist

- [ ] Student name and ID filled in
- [ ] Q1, Q2, Q3 answered
- [ ] Experiment 1: table filled, packing list pasted, plot observation written
- [ ] Experiment 2: results table filled (3 rows), observation and answer written
- [ ] Summary table completed and reflection written
- [ ] `plots/` contains: `experiment_1.png`, `experiment_2a.png`, `experiment_2b.png`, `experiment_2c.png`
