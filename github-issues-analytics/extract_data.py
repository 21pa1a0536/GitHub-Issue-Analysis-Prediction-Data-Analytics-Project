from github import Github
import pandas as pd

# My GitHub Access Token is Removed as it is confidential.
# you can replace 'your_token_here' with your GitHub token if you want to run this project.

g = Github("your_token_here")

# Example: Select a repo
repo = g.get_repo("pandas-dev/pandas")

# Getting last 100 issues using slicing
issues = repo.get_issues(state='closed')[:100]

data = []
for issue in issues:
    if issue.pull_request is None:  # excluding pull requests
        data.append({
            'id': issue.id,
            'title': issue.title,
            'created_at': issue.created_at,
            'closed_at': issue.closed_at,
            'labels': [label.name for label in issue.labels],
            'comments': issue.comments,
            'assignee': issue.assignee.login if issue.assignee else None
        })

df = pd.DataFrame(data)
df.to_csv("data/issues.csv", index=False)



import pandas as pd

df = pd.read_csv("data/issues.csv")
df['created_at'] = pd.to_datetime(df['created_at'])
df['closed_at'] = pd.to_datetime(df['closed_at'])
df['time_to_resolve'] = (df['closed_at'] - df['created_at']).dt.days

# Example feature: number of labels
df['num_labels'] = df['labels'].apply(lambda x: len(eval(x)))

df.head()



import matplotlib.pyplot as plt
import seaborn as sns

# Distribution of time to resolve
sns.histplot(df['time_to_resolve'], bins=20)
plt.title("Time to Resolve GitHub Issues")
plt.xlabel("Days")
plt.ylabel("Number of Issues")
plt.show()

# Compare assigned vs. unassigned
df['is_assigned'] = df['assignee'].notnull()
sns.boxplot(x='is_assigned', y='time_to_resolve', data=df)
plt.title("Time to Resolve: Assigned vs Unassigned")



from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Convert to binary target (e.g., >7 days = slow)
df['slow'] = df['time_to_resolve'] > 7

# Simple features
features = df[['num_labels', 'comments', 'is_assigned']]
features.loc[:, 'is_assigned'] = features['is_assigned'].astype(int)
target = df['slow'].astype(int)

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

print("Model Accuracy:", model.score(X_test, y_test))


from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("GITHUB_TOKEN")
g = Github(token)



