# Run this in Google Colab to produce the required report output.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = pd.DataFrame({
    "Sequence_ID": ["S1", "S2", "S3", "S4"],
    "DNA_Sequence": ["ATGCGATC", "ATGCGTAC", "GCGCGTAT", "GCGCGCGC"],
    "Group": ["A", "A", "B", "B"]
})


def extract_features(sequence):
    sequence = sequence.upper()
    length = len(sequence)
    a = sequence.count("A")
    t = sequence.count("T")
    g = sequence.count("G")
    c = sequence.count("C")
    gc_content = ((g + c) / length) * 100
    return [a, t, g, c, length, gc_content]


feature_names = ["A", "T", "G", "C", "Length", "GC_percent"]

X = pd.DataFrame(
    [extract_features(sequence) for sequence in data["DNA_Sequence"]],
    columns=feature_names
)
y = data["Group"]

model = DecisionTreeClassifier(random_state=1)
model.fit(X, y)

training_predictions = model.predict(X)
training_accuracy = accuracy_score(y, training_predictions)

unknown_sequence = "ATGCGCGATC"
unknown_features = pd.DataFrame(
    [extract_features(unknown_sequence)],
    columns=feature_names
)
prediction = model.predict(unknown_features)[0]

print("Feature table:")
print(pd.concat([data, X], axis=1))

print("\nTraining accuracy:", training_accuracy)
print("Unknown sequence:", unknown_sequence)
print("Predicted group:", prediction)

print("\nFeature importance:")
for feature, importance in zip(feature_names, model.feature_importances_):
    print(f"{feature}: {importance:.3f}")
Publish the website
Go to GitHub and create a public repository called dna-group-classifier.

Upload index.html, README.md, and colab_notebook.py.

In the repository, open Settings.

In the left menu, click Pages.

Under Build and deployment, set:

Source: Deploy from a branch

Branch: main

Folder: / (root)

Click Save.

Wait 1–3 minutes, then refresh the Pages page.

GitHub will show a link like:

text
https://YOUR-USERNAME.github.io/dna-group-classifier/
Send that link to your teacher. GitHub Pages serves the static HTML/JavaScript site directly from the repository, so it remains accessible without you starting a server each time.

What to tell your teacher
Say:

I built a DNA sequence group classifier website using HTML, CSS, and JavaScript. The machine-learning model was trained in Python using scikit-learn, and the website shows the feature table, model accuracy, feature importance, and prediction for the unknown sequence. The website is hosted on GitHub Pages so it can be opened directly through a link.

The Python/Colab file demonstrates the actual model training, while the GitHub Pages website presents the results in an always-available interface.

Show me how to turn on GitHub Pages
Can you explain how the HTML form works
What should I write in the README file
How do I show this to my teacher
Let's review the rubric checklist

⠸



