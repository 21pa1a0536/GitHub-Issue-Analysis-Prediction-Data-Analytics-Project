# 📊 GitHub Issue Analysis & Prediction

This project analyzes and predicts the assignment of issues in open-source GitHub repositories using real-time data fetched through the GitHub API. It combines data analytics and machine learning to offer insights into contributor behavior, issue triaging, and project activity patterns.

---

## 🚀 Overview

- 🔍 **Data Source:** Live GitHub issue data pulled using the GitHub API.
- 🧪 **EDA:** Performed exploratory data analysis on issue titles, labels, and assignment status.
- 🛠️ **Feature Engineering:** Created features such as label count, title length, and time since issue creation.
- 🤖 **Modeling:** Built a logistic regression classifier to predict whether an issue is likely to be assigned.
- 📈 **Performance:** Achieved ~88% model accuracy in real-world classification.

---

## 🧰 Technologies Used

- Python
- GitHub API
- Pandas, NumPy
- scikit-learn
- Matplotlib, Seaborn
- Google Colab / VSCode

---

## 🗂️ Project Structure


github-issue-analysis/
├── README.md
├── extract\_data.py                  # Script to fetch issue data via GitHub API
├── notebooks/
│   └── github\_issue\_analysis.ipynb  # EDA and ML modeling notebook
├── data/
│   └── sample\_issues.csv            # Sample extracted issue data
├── requirements.txt                 # Python dependencies
└── .gitignore

---

## ⚙️ How to Run

1. **Install dependencies**

pip install -r requirements.txt

2. **Set up your GitHub token**

To fetch real-time data, you'll need a GitHub Personal Access Token (PAT).

* Create a token from your GitHub Developer Settings
* Set it as an environment variable:

  import os
  token = os.getenv("GITHUB_TOKEN")
 
* Or store it in a `.env` file and use `python-dotenv` (optional)

3. **Run the data extractor**

python extract_data.py


4. **Explore the notebook**

Open and run the notebook at:

notebooks/github_issue_analysis.ipynb

---

## 🔐 GitHub Token Security

⚠️ **Never upload your GitHub token to GitHub or share it publicly.**
Use environment variables or `.env` files (excluded via `.gitignore`) to store your credentials securely. If your token is accidentally exposed, revoke and regenerate it immediately in your GitHub settings.

---

## 📎 Key Learnings

* Real-time data ingestion using REST APIs
* Cleaning and transforming nested JSON into structured tabular format
* Text-based feature engineering (title length, label count)
* Binary classification using logistic regression
* Applying ML to developer tooling and open-source workflows

---

## 📁 License

This project is open-source and free to use for learning and portfolio purposes.

---

## 🙌 Acknowledgments

* [PyGithub](https://pygithub.readthedocs.io/en/latest/) for API access
* GitHub and the open-source community for real-time data

---

