################################################################################
# DSCRGDIM100
#
# DESCRIPTION: This job loads the dimensional data for the first time into
#              the DataWarehouse dimensions
#
# AUTHOR      DATE     CHANGE
# ----------- -------- ------------------------------------------------------
# Ricardo R   20180620 Initial creation
#
################################################################################

################################################################################
#
# Job Step 00: Initialize python environment
#
################################################################################

# Import required packages: pandas, sqlalchemy
import pandas as pd

from sqlalchemy import create_engine

# Import created libraries that contain record properties
from dischargerecord import DimProviderRecord
from dischargerecord import DimDateRecord
from dischargerecord import DimAdmissionRecord
from dischargerecord import DimAPRClassificationRecord
from dischargerecord import DimClinicClassRecord
from dischargerecord import DimPaymentRecord
from dischargerecord import DimDemographicsRecord
from dischargerecord import DimLocationRecord

# Import extra libraries
import jobutils

jobutils.printJobStart("DSCRGDIM100")

################################################################################
#
# Job Step 05: Enviroment preparation
#
################################################################################
jobutils.printStepStart("05")

# Connect to database
print("Connecting to the database...")
engine = create_engine('mssql://LAPTOP-TH3PDN0I/Group_8_DB?driver=ODBC+Driver+17+for+SQL+Server')
print("Connected.")

csvfile = './sample.csv'
print("File name to load: " + csvfile)

################################################################################
#
# Job Step 10: Load Provider Dimension
#
################################################################################
jobutils.printStepStart("10")

print("Loading provider dimension from file " + csvfile + "...")

# Read Original CSV file
prov_df = pd.read_csv(csvfile,
                 header=1,
                 #nrows=10,
                 usecols=DimProviderRecord().get_column_indeces(),
                 names=DimProviderRecord().get_column_names(),
                 dtype=DimProviderRecord().get_column_types())

# Drop duplicate rows
prov_df.drop_duplicates(inplace=True)

# Load rows to database
prov_df.to_csv('DimProvider.csv', index=False)
prov_df.to_sql('DimProvider', con=engine, if_exists='append', index=False)

rowcount = len(prov_df.index)
print("Load complete. Loaded " + str(rowcount) + " rows.")

################################################################################
#
# Job Step 20: Load Date Dimension
#
################################################################################
jobutils.printStepStart("20")

print("Loading Date dimension from file " + csvfile + "...")

# Read Original CSV file
date_df = pd.read_csv(csvfile,
                 header=1,
                 usecols=DimDateRecord().get_column_indeces(),
                 names=DimDateRecord().get_column_names(),
                 dtype=DimDateRecord().get_column_types(),
                 converters=DimDateRecord().get_column_converters())

# Drop duplicate rows
date_df.drop_duplicates(inplace=True)

# Load rows to database
date_df.to_csv('DimDate.csv', index=False)
date_df.to_sql('DimDate', con=engine, if_exists='append', index=False)

rowcount = len(date_df.index)
print("Load complete. Loaded " + str(rowcount) + " rows.")

################################################################################
#
# Job Step 30: Load Admission Dimension
#
################################################################################
jobutils.printStepStart("30")

print("Loading Admission dimension from file " + csvfile + "...")

# Read Original CSV file
admission_df = pd.read_csv(csvfile,
                 header=1,
                 #nrows=10,
                 usecols=DimAdmissionRecord().get_column_indeces(),
                 names=DimAdmissionRecord().get_column_names(),
                 dtype=DimAdmissionRecord().get_column_types(),
                 converters=DimAdmissionRecord().get_column_converters()
                          )

# Drop duplicate rows
admission_df.drop_duplicates(inplace=True)

# Load rows to database
admission_df.to_csv('DimAdmission.csv', index=False)
admission_df.to_sql('DimAdmission', con=engine, if_exists='append', index=False)

rowcount = len(admission_df.index)
print("Load complete. Loaded " + str(rowcount) + " rows.")

################################################################################
#
# Job Step 40: Load APR Classification Dimension
#
################################################################################
jobutils.printStepStart("40")

print("Loading APR Classification dimension from file " + csvfile + "...")

# Read Original CSV file
apr_classification_df = pd.read_csv(csvfile,
                 header=1,
                 #nrows=10,
                 usecols=DimAPRClassificationRecord().get_column_indeces(),
                 names=DimAPRClassificationRecord().get_column_names(),
                 dtype=DimAPRClassificationRecord().get_column_types())

# Drop duplicate rows
apr_classification_df.drop_duplicates(inplace=True)

# Load rows to database
apr_classification_df.to_csv('DimAPRClassification.csv', index=False)
apr_classification_df.to_sql('DimAPRClassification',
                             con=engine,
                             if_exists='append',
                             index=False)

rowcount = len(apr_classification_df.index)
print("Load complete. Loaded " + str(rowcount) + " rows.")

################################################################################
#
# Job Step 50: Load Clinic Class Dimension
#
################################################################################
jobutils.printStepStart("50")

print("Loading Clinic Class dimension from file " + csvfile + "...")

# Read Original CSV file
clinic_class_df = pd.read_csv(csvfile,
                 header=1,
                 usecols=DimClinicClassRecord().get_column_indeces(),
                 names=DimClinicClassRecord().get_column_names(),
                 dtype=DimClinicClassRecord().get_column_types())

# Drop duplicate rows
clinic_class_df.drop_duplicates(inplace=True)

# Load rows to database
clinic_class_df.to_csv('DimClinicClass.csv', index=False)
clinic_class_df.to_sql('DimClinicClass', con=engine, if_exists='append', index=False)

rowcount = len(clinic_class_df.index)
print("Load complete. Loaded " + str(rowcount) + " rows.")

################################################################################
#
# Job Step 60: Load Payment Dimension
#
################################################################################
jobutils.printStepStart("60")

print("Loading Payment dimension from file " + csvfile + "...")

# Read Original CSV file
payment_df = pd.read_csv(csvfile,
                 header=1,
                 usecols=DimPaymentRecord().get_column_indeces(),
                 names=DimPaymentRecord().get_column_names(),
                 dtype=DimPaymentRecord().get_column_types())

# Drop duplicate rows
payment_df.drop_duplicates(inplace=True)

# Load rows to database
payment_df.to_csv('DimPayment.csv', index=False)
payment_df.to_sql('DimPayment', con=engine, if_exists='append', index=False)

rowcount = len(payment_df.index)
print("Load complete. Loaded " + str(rowcount) + " rows.")

################################################################################
#
# Job Step 70: Load Demographics Dimension
#
################################################################################
jobutils.printStepStart("70")

print("Loading Demographics dimension from file " + csvfile + "...")

# Read Original CSV file
demographics_df = pd.read_csv(csvfile,
                 header=1,
                 usecols=DimDemographicsRecord().get_column_indeces(),
                 names=DimDemographicsRecord().get_column_names(),
                 dtype=DimDemographicsRecord().get_column_types())

# Drop duplicate rows
demographics_df.drop_duplicates(inplace=True)

# Load rows to database
demographics_df.to_csv('DimDemographics.csv', index=False)
demographics_df.to_sql('DimDemographics', con=engine, if_exists='append', index=False)

rowcount = len(demographics_df.index)
print("Load complete. Loaded " + str(rowcount) + " rows.")

################################################################################
#
# Job Step 80: Load Location Dimension
#
################################################################################
jobutils.printStepStart("80")

# Read Original CSV file
location_df = pd.read_csv(csvfile,
                 header=1,
                 usecols=DimLocationRecord().get_column_indeces(),
                 names=DimLocationRecord().get_column_names(),
                 dtype=DimLocationRecord().get_column_types(),
                 converters=DimLocationRecord().get_column_converters()
                         )

# Drop duplicate rows
location_df.drop_duplicates(inplace=True)

# Load rows to database
location_df.to_csv('DimLocation.csv', index=False)
location_df.to_sql('DimLocation', con=engine, if_exists='append', index=False)

rowcount = len(location_df.index)
print("Load complete. Loaded " + str(rowcount) + " rows.")

################################################################################
#
# EoJ: End of Job
#
################################################################################
jobutils.printJobEnd("DSCRGDIM100")
