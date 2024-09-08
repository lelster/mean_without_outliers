
# Clean Mean Algorithm

## Problem Statement
This repository contains a solution to the Codewars challenge: [Mean without outliers](https://www.codewars.com/kata/5962d557be3f8bb0ca000010/python).

The task is to remove outliers from a list of numbers iteratively, using a cutoff based on the standard deviation. The goal is to calculate a "clean mean" that excludes any values too far from the mean.

## Installation

To run the tests, you need to install the `codewars_test` framework. Use the following command:

```bash
pip install git+https://github.com/codewars/python-test-framework.git#egg=codewars_test
```

## Usage

To test the solution with the provided test cases, run the following:

```bash
python tests.py
```

Where `tests.py` contains the test cases for validation.

### Example:

```python
sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]
cutoff = 3
print(clean_mean(sample, cutoff))  # Output: 5.5
```

### Running Tests:

```python
import codewars_test as test
from main import clean_mean

test.assert_equals(clean_mean([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100], 3), 5.5)
test.assert_equals(clean_mean([1.01, 0.99, 1.02, 1.01, 0.99, 0.97, 1.03, 0.99, 1.02, 0.99, 3, 10], 2), 1.0)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
