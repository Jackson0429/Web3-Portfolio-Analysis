"""
This scrip runs the analysis for the phantom wallet
"""


def run(data):
    # basic data cleaning
    data = data.dropna(axis=0, how='all')
    data = data.reset_index(drop=True)