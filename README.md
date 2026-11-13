# DNA Sequence Group Classifier

This is a simple machine-learning project that classifies DNA sequences into Group A or Group B.

The website extracts six features from each DNA sequence:

- A count
- T count
- G count
- C count
- Sequence length
- GC content (%)

It then uses a Decision Tree model to predict the group of an unknown DNA sequence.

## Dataset

| Sequence ID | DNA sequence | Group |
|---|---|---|
| S1 | ATGCGATC | A |
| S2 | ATGCGTAC | A |
| S3 | GCGCGTAT | B |
| S4 | GCGCGCGC | B |

## Unknown sequence

The unknown sequence is:

`ATGCGCGATC`

The model predicts **Group B**.

The unknown sequence has 3 G bases and 60% GC content. These values are closer to the patterns found in the Group B training sequences.

## Model accuracy

The training accuracy is **100%**.

This means the model correctly classified all four training sequences. However, this does not prove that the model will correctly classify new sequences because the dataset is very small.

## How the model works

The Decision Tree mainly uses the G count:

- 2 G bases: Group A
- 3 or more G bases: Group B

The unknown sequence has 3 G bases, so it is predicted as Group B.

## Genomics application

AI and machine learning can be used in genomics for disease-risk prediction from genetic variants. Models can identify patterns in DNA variants and support early screening and personalised medicine.

## Limitation

The model was trained using only four sequences. It may not generalise well to new or very different DNA sequences. A larger and more diverse dataset, with separate training and testing data, would be needed for reliable genomic classification.
