from setuptools import setup, find_packages

setup(
    author = "Shaun Sandbloom",
    description = "A wrapper for pulling data from the Department of Education's College Scorecard API.",
    name = "college_scorecard",
    packages = find_packages(include = [
        'college_scorecard',
        'college_scorecard.*'
    ]
),
    # include_package_data = True,
    # package_data = {'': ['*.json']},
    version = "0.1.0"
)
