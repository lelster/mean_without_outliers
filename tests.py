"""
Test Cases from Codewars
Make sure to do:
pip install git+https://github.com/codewars/python-test-framework.git#egg=codewars_test
"""
import codewars_test as test 
from main import clean_mean


test.describe('Example test case')

sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]
cutoff = 3
test.assert_equals(clean_mean(sample, cutoff), 5.5)

test.describe('Slightly tougher example test case')

sample = [1.01, 0.99, 1.02, 1.01, 0.99, 0.97, 1.03, 0.99, 1.02, 0.99, 3, 10]
cutoff = 2
test.assert_equals(clean_mean(sample, cutoff), 1.0)

test.describe('Random test cases')

import random

def mean_and_std(sample):
    mean = sum(sample) / len(sample)
    std = (sum((mean - x) ** 2 for x in sample) / len(sample)) ** 0.5
    return mean, std

def validation(sample, cutoff):
    mean, std = mean_and_std(sample)
    while any(True if abs(mean - x) / std > cutoff else False for x in sample):
        sample = [x for x in sample if abs(mean - x) / std <= cutoff]
        mean, std = mean_and_std(sample)
        if std == 0: 
            return mean
    return round(mean, 2)

for i in range(100):
    sample = []
    mu = random.randint(0, 100)
    sigma = random.randint(1, 100)
    cutoff = round(random.uniform(2.5, 5), 2)
    for i in range(random.randint(20, 100)):
        sample.append(round(random.normalvariate(mu, sigma), 2))
        if random.random() > 0.98:
            sample.append(round(random.normalvariate(mu, sigma * 10), 2))
    test.assert_equals(clean_mean(sample, cutoff), validation(sample, cutoff))