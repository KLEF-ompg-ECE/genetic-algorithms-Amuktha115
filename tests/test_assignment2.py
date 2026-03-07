"""
Autograding Tests — Assignment 2: GA Knapsack (2 experiments)
=============================================================
Section A — Code runs correctly         (25 pts)
Section B — Plot files exist            (25 pts)
Section C — README observations filled  (35 pts)
Section D — Code was modified           (15 pts)
                                  TOTAL  100 pts

Run locally:  python -m pytest tests/test_assignment2.py -v
"""

import subprocess, sys, os, re
import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# =============================================================================
# SECTION A — Code runs correctly  (25 pts)
# =============================================================================

class TestCodeRuns:

    @pytest.fixture(autouse=True, scope="class")
    def run_program(self, tmp_path_factory):
        r = subprocess.run(
            [sys.executable, "ga_knapsack.py"],
            cwd=ROOT, capture_output=True, text=True, timeout=120
        )
        TestCodeRuns._result = r

    def test_runs_without_error(self):
        """Program must exit with code 0."""
        assert self._result.returncode == 0, \
            f"Program crashed (exit {self._result.returncode}):\n{self._result.stderr[:400]}"

    def test_output_shows_value(self):
        """Output must print the Value of the best solution."""
        assert "Value" in self._result.stdout, \
            "'Value' not found in output — is print_solution() called?"

    def test_output_shows_weight(self):
        """Output must print the Weight of the best solution."""
        assert "Weight" in self._result.stdout, \
            "'Weight' not found in output — is print_solution() called?"

    def test_output_shows_generations(self):
        """Output must print generation count."""
        assert "eneration" in self._result.stdout, \
            "Generation count not printed"

    def test_multiple_experiment_runs(self):
        """Output must show at least 2 runs (Exp 1 + at least one Exp 2 variant)."""
        count = self._result.stdout.count("Final best value")
        assert count >= 2, \
            f"Expected >=2 runs in output (Exp1 + at least one Exp2), found {count}"


# =============================================================================
# SECTION B — Plot files exist  (25 pts)
# =============================================================================

class TestPlotsExist:

    def _plot(self, fname):
        return os.path.join(ROOT, "plots", fname)

    def test_plots_directory_exists(self):
        assert os.path.isdir(os.path.join(ROOT, "plots")), \
            "plots/ directory not found — create it and save plots there"

    def test_experiment_1_exists(self):
        assert os.path.isfile(self._plot("experiment_1.png")), \
            "plots/experiment_1.png missing"

    def test_experiment_2a_exists(self):
        assert os.path.isfile(self._plot("experiment_2a.png")), \
            "plots/experiment_2a.png missing (mutation_rate=0.01)"

    def test_experiment_2b_exists(self):
        assert os.path.isfile(self._plot("experiment_2b.png")), \
            "plots/experiment_2b.png missing (mutation_rate=0.05)"

    def test_experiment_2c_exists(self):
        assert os.path.isfile(self._plot("experiment_2c.png")), \
            "plots/experiment_2c.png missing (mutation_rate=0.30)"

    def test_all_plots_non_empty(self):
        plots_dir = os.path.join(ROOT, "plots")
        if not os.path.isdir(plots_dir):
            pytest.skip("plots/ directory missing")
        for fname in ["experiment_1.png", "experiment_2a.png",
                      "experiment_2b.png", "experiment_2c.png"]:
            path = os.path.join(plots_dir, fname)
            if os.path.isfile(path):
                assert os.path.getsize(path) > 1000, \
                    f"{fname} appears empty ({os.path.getsize(path)} bytes)"


# =============================================================================
# SECTION C — README observations filled in  (35 pts)
# =============================================================================

class TestREADME:

    @pytest.fixture(autouse=True)
    def load_readme(self):
        path = os.path.join(ROOT, "README.md")
        assert os.path.isfile(path), "README.md not found"
        self.text = open(path).read()

    PLACEHOLDERS = ["YOUR ANSWER", "YOUR OBSERVATION", "YOUR REFLECTION", "PASTE"]

    def _filled(self, marker):
        m = re.search(
            rf"{re.escape(marker)}.*?```\n(.*?)```", self.text, re.DOTALL)
        if not m:
            return False
        content = m.group(1).strip()
        return bool(content) and not any(p in content for p in self.PLACEHOLDERS)

    def test_student_name_filled(self):
        line = self.text.split("Student Name")[1].split("\n")[0]
        assert "___" not in line, "Student name is still blank"

    def test_q1_answered(self):
        assert self._filled("Q1."), \
            "Q1 still placeholder — answer what fitness() returns"

    def test_q2_answered(self):
        assert self._filled("Q2."), \
            "Q2 still placeholder — answer what tournament_select() does"

    def test_q3_answered(self):
        assert self._filled("Q3."), \
            "Q3 still placeholder — explain the elitism line"

    def test_exp1_packing_list_pasted(self):
        assert self._filled("Copy the printed packing list"), \
            "Experiment 1 packing list not pasted"

    def test_exp1_observation_written(self):
        assert self._filled("Look at `plots/experiment_1.png`"), \
            "Experiment 1 plot observation still blank"

    def test_exp2_results_table_filled(self):
        section = self.text[
            self.text.find("Experiment 2"):self.text.find("## Summary")]
        rows = [l for l in section.split("\n") if l.startswith("| 0.")]
        filled = [r for r in rows
                  if r.count("|") >= 4 and
                  any(c.strip() not in ("", "Yes", "No", " ")
                      for c in r.split("|")[2:5])]
        assert len(filled) >= 2, \
            f"Experiment 2 table: only {len(filled)} rows have data (need >= 2)"

    def test_exp2_observation_written(self):
        assert self._filled("Compare the three plots"), \
            "Experiment 2 observation (compare plots) still blank"

    def test_exp2_best_rate_answered(self):
        assert self._filled("Which mutation_rate gave the best result"), \
            "Experiment 2 'Which mutation_rate gave best result?' not answered"

    def test_reflection_written(self):
        assert self._filled("most important thing you learned about Genetic"), \
            "Summary reflection still blank"


# =============================================================================
# SECTION D — Code was modified  (15 pts)
# =============================================================================

class TestCodeModified:

    @pytest.fixture(autouse=True)
    def load_code(self):
        self.code = open(os.path.join(ROOT, "ga_knapsack.py")).read()

    def test_exp2_rate_001_present(self):
        assert "0.01" in self.code, \
            "mutation_rate=0.01 not found — add Experiment 2a block"

    def test_exp2_rate_030_present(self):
        assert "0.30" in self.code or "0.3," in self.code, \
            "mutation_rate=0.30 not found — add Experiment 2c block"

    def test_exp2_three_plot_saves(self):
        count = self.code.count("experiment_2")
        assert count >= 3, \
            f"Expected 3 experiment_2 plot saves in code, found {count}"
