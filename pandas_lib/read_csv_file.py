#  reading csv file with numpy

import pandas as pd
import os




class DataFromCSV:

    def __init__(self, location, pd) -> None:
        self.location = location
        self.pd = pd

    def read_csv_file(self):
        pd = self.pd
        df = pd.read_csv(self.location)
        return df

filelocation = file_location
dfcsv = DataFromCSV(filelocation, pd)
print(dfcsv.read_csv_file())