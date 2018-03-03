import csv

MEMO_STRING = 0
VENDOR = 1

# lists
memos_list = []
vendors_list = []

# dictionary
memo_to_vendor_dict = {}

with open("Sample memos - memos.csv", 'r') as memofile:
    memo = csv.reader(memofile)
    next(memo)  # skip the first line
    for row in memo:
        memos_list.append(row[MEMO_STRING])
        vendors_list.append(row[VENDOR].lstrip('[\'').rstrip('\']'))
        memo_to_vendor_dict[row[MEMO_STRING]] = row[VENDOR].lstrip('[\'').rstrip('\']')


# functions to analyze the pattern

def analyze_pattern1(memos_list, vendors_list, memo_to_vdendor_dict):
    pass

analyze_pattern1(memos_list, vendors_list, memo_to_vendor_dict)