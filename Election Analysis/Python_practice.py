import os
from typing import Text

file_to_save=os.path.join("analysis", "election_analysis.txt")

with open(file_to_save, "w") as txt_file:

    txt_file.write("Counties in the Election\n----------------\nArapahoe\nDenver\nJefferson")


