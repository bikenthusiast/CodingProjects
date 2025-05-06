import re

def clean_price(val):
    # Ensure it's a string
    val = str(val)
    # Remove non-numeric characters except for . , and -
    val = re.sub(r"[^\d,.-]", "", val)
    # Convert comma to dot for decimal
    val = val.replace(",", ".")
    return val