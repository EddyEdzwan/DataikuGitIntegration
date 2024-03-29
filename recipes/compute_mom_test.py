# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
training_data = dataiku.Dataset("training_data")
training_data_df = training_data.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

mom_test_df = training_data_df # For this sample code, simply copy input to output


# Write recipe outputs
mom_test = dataiku.Dataset("mom_test")
mom_test.write_with_schema(mom_test_df)
