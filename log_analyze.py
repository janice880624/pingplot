import os
import numpy as np

file="./pingplot_v1.1.0_172.101.1.16_2022-07-27.log"

for line in open(file, "r", encoding="utf-8"):
    # if "time" in line:
    #     print(line)
    print(line)