💸 Expenses Tracker



A clean, Python-based \*\*CLI expense tracker\*\* that logs daily spending to CSV and provides monthly summaries, category breakdowns, and keyword search. Part of the \*\*IdeaVault\*\* flagship utility lineup by \*\*A. Aravind Reddy\*\*.



---



✨ Features



\* ➕ Add expenses (amount, category, description, auto-date)

\* 📜 View all expenses in a pretty table

\* 📅 Monthly summary: total, average, biggest expense (with details)

\* 🗂️ Category-wise breakdown for the current month

\* 🔎 Keyword search across category/description

\* 💾 CSV persistence (`expenses.csv` auto-created)



&nbsp;🧰 Requirements



\* Python 3.8+

\* Packages: `pandas`, `tabulate`



Install dependencies:



```bash

pip install pandas tabulate

\# If pip is not found:

python -m pip install pandas tabulate

```



---

🚀 Quick Start



1\. \*\*Clone the repo\*\*



&nbsp;  ```bash

&nbsp;  ```



git clone \[https://github.com/IdeaVault2430/expenses-tracker.git](https://github.com/IdeaVault2430/expenses-tracker.git)

cd expenses-tracker



````

2\. \*\*Install dependencies\*\*

&nbsp;  ```bash

pip install pandas tabulate

````



3\. \*\*Run the app\*\*



&nbsp;  ```bash

&nbsp;  ```



python expenses\\\_tracker.py



```



---



\## ▶️ What You’ll See

```



\\===== 💼 Expense Tracker =====

1️⃣ Add Expense

2️⃣ View All Expenses

3️⃣ Monthly Summary

4️⃣ Category-wise Breakdown

5️⃣ Search Expenses

6️⃣ Exit



```



\*\*Data file:\*\* `expenses.csv` (created in the project folder)



Example record (CSV):

```



Date,Amount,Category,Description

2025-08-26,50000.0,Food,North Indian



```



---



\## 📁 Project Structure

```



expenses-tracker/

├─ expenses\\\_tracker.py   # Main CLI application

├─ README.md             # You’re here

└─ expenses.csv          # Auto-created data file (after first run)



````



---



\## ❓ Troubleshooting

\- \*\*ModuleNotFoundError: pandas\*\* → Run `pip install pandas` (or `python -m pip install pandas`).

\- \*\*FutureWarning from pandas (concat)\*\* → It’s harmless for now. To hide warnings, add to the top of `expenses\_tracker.py`:

&nbsp; ```python

&nbsp; import warnings

&nbsp; warnings.simplefilter("ignore")

````



---



\## 🤝 Contributions



PRs welcome! Feel free to fork, enhance, and open a pull request.



---



\## 📜 License



MIT License — free to use, modify, and distribute.



---



\## 👤 Author



\*\*A. Aravind Reddy\*\* — IdeaVault



\* GitHub: \[https://github.com/IdeaVault2430](https://github.com/IdeaVault2430)



