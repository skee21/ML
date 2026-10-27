pip install pandas pgmpy -q
import pandas as pd
import numpy as np
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.inference import VariableElimination
from pgmpy.estimators import MaximumLikelihoodEstimator
heartDisease = pd.read_csv("heart.csv")
heartDisease = heartDisease.replace('?', np.nan)
heartDisease = heartDisease.apply(pd.to_numeric)
heartDisease = heartDisease.dropna()
model = DiscreteBayesianNetwork([
    ('age', 'heartdisease'),
    ('sex', 'heartdisease'),
    ('exang', 'heartdisease'),
    ('cp', 'heartdisease'),
    ('heartdisease', 'restecg'),
    ('heartdisease', 'chol')
])
print('\nLearning CPD using Maximum likelihood estimators')
model.fit(heartDisease, estimator=MaximumLikelihoodEstimator)
print("CPDS learned successfully")
print('\nInferencing with Bayesian Network:')
HeartDiseasetest_infer = VariableElimination(model)
print('\n1. Probability of HeartDisease given evidence=restecg')
q1 = HeartDiseasetest_infer.query(
    variables=['heartdisease'],
    evidence={'restecg': 1}
)
print(q1)
print("\n2. Probability of HeartDisease given evidence=cp")
q2 = HeartDiseasetest_infer.query(
    variables=['heartdisease'],
    evidence={'cp': 1}
)
print(q2)