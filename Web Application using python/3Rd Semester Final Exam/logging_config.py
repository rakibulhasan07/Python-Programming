### Logging-এর Output Formatting ও Configuration ব্যবহার করে প্রোগ্রাম


import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)

logging.info("Program started")
logging.warning("This is a warning")
logging.error("An error occurred")


# ### Output

# ```text
# INFO: Program started
# WARNING: This is a warning
# ERROR: An error occurred
# ```

# ### সংক্ষেপে

# * `logging.basicConfig()` → Logging **configuration** করার জন্য।
# * `level=logging.INFO` → INFO এবং তার উপরের message দেখাবে।
# * `format='%(levelname)s: %(message)s'` → Output-এর **formatting** নির্ধারণ করে।
# * `logging.info()` → সাধারণ তথ্য।
# * `logging.warning()` → সতর্কতা।
# * `logging.error()` → ত্রুটি নির্দেশ করে।
