################################################################################
# DSCRGFCT100
#
# DESCRIPTION: This job loads the fact data for the first time into
#              the DataWarehouse fact table
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
from dischargerecord import FactDischarge

# Import extra libraries
import jobutils

jobutils.printJobStart("DSCRGFCT100")

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

csvfile = '../SPARC_10k_part-ce.csv'
print("File name to load: " + csvfile)

################################################################################
#
# Job Step 10: Load Dimensions
#
################################################################################
jobutils.printStepStart("10")

print("Loading dimensions to memory...")

dim_date_df = pd.read_sql_table('DimDate', con=engine).fillna('')
dim_location_df = pd.read_sql_table('DimLocation', con=engine).fillna('')
dim_demographics_df = pd.read_sql_table('DimDemographics', con=engine).fillna('')
dim_payment_df = pd.read_sql_table('DimPayment', con=engine).fillna('')
dim_clinic_class_df = pd.read_sql_table('DimClinicClass', con=engine).fillna('')
dim_apr_class_df = pd.read_sql_table('DimAPRClassification', con=engine).fillna('')
dim_admission_df = pd.read_sql_table('DimAdmission', con=engine).fillna('')
dim_provider_df = pd.read_sql_table('DimProvider', con=engine).fillna('')

print("Done. Dimensions loaded.")

################################################################################
#
# Job Step 20: Extract Facts from CSV
#
################################################################################
jobutils.printStepStart("20")

print("Loading fact from csv file: " + csvfile)

# Load facts from csv
fact_discharge_df = pd.read_csv(csvfile,
                                header=0,
                                names=FactDischarge().get_column_names(),
                                dtype=FactDischarge().get_column_types(),
                                converters=FactDischarge().get_column_converters()
                               )
fact_discharge_df = fact_discharge_df.fillna('')

print("Done.")

################################################################################
#
# Job Step 30: Load Facts to DB
#
################################################################################
jobutils.printStepStart("30")

print("Loading fact table...")

df_array = []
rowcount = 0

# Iterate fact dataframe
for fact in fact_discharge_df.itertuples():

    fact_record = {}

    # fact_date_key = dim_date_df.loc[dim_date_df['DischargeYear'] == fact[14]].iloc[0]['DateKey']

    # fact_date_key = dim_date_df.query("DischargeYear == " + str(fact[14])).iloc[0]['DateKey']

    fact_date_key = dim_date_df[
        (dim_date_df['DischargeYear'] == fact[15]) &
        (dim_date_df['DischargeMonth'] == fact[1])
    ].iloc[0]['DateKey']

    fact_provider_key = dim_provider_df[
        (dim_provider_df['AttendingLicenseNo'] == fact[31]) &
        (dim_provider_df['OperatingLicenseNo'] == fact[32]) &
        (dim_provider_df['OtherLicenseNo'] == fact [33])
    ].iloc[0]['ProviderKey']

    fact_admission_key = dim_admission_df[
        (dim_admission_df['TypeAdmission'] == fact[13]) &
        (dim_admission_df['PatientDisposition'] == fact[14]) &
        (dim_admission_df['AbortionIndicator'] == fact[35]) &
        (dim_admission_df['EmergencyIndicator'] == fact[36])
    ].iloc[0]['AdmissionKey']

    fact_apr_key = dim_apr_class_df[
        (dim_apr_class_df['DrgCode'] == fact[20]) &
        (dim_apr_class_df['MdcCode'] == fact[22]) &
        (dim_apr_class_df['SeverityIllnessCode'] == fact[24]) &
        (dim_apr_class_df['RiskOfMortality'] == fact[26])
    ].iloc[0]['AprKey']

    fact_clinic_class_key = dim_clinic_class_df[
        (dim_clinic_class_df['DiagnosisCode'] == fact[16]) &
        (dim_clinic_class_df['ProcedureCode'] == fact[18])
    ].iloc[0]['ClinicClassKey']

    fact_payment_key = dim_payment_df[
        (dim_payment_df['PrimaryPayMethod'] == fact[28]) &
        (dim_payment_df['SecondaryPayMethod'] == fact[29]) &
        (dim_payment_df['TertiaryPayMethod'] == fact[30])
    ].iloc[0]['PaymentKey']

    fact_demographics_key = dim_demographics_df[
        (dim_demographics_df['AgeGroup'] == fact[7]) &
        (dim_demographics_df['Gender'] == fact[9]) &
        (dim_demographics_df['Race'] == fact[10]) &
        (dim_demographics_df['Ethnicity'] == fact[11])
    ].iloc[0]['DemographicsKey']

    fact_location_key = dim_location_df[
        (dim_location_df['HealthServiceArea'] == fact[2]) &
        (dim_location_df['HospitalCounty'] == fact[3]) &
        (dim_location_df['FacilityID'] == fact[5]) &
        (dim_location_df['ZipCode'] == fact[8])
    ].iloc[0]['LocationKey']

    fact_record = {
        'ProviderKey': fact_provider_key,
        'DateKey': fact_date_key,
        'AdmissionKey': fact_admission_key,
        'AprKey': fact_apr_key,
        'ClinicClassKey': fact_clinic_class_key,
        'PaymentKey': fact_payment_key,
        'DemographicsKey': fact_demographics_key,
        'LocationKey': fact_location_key,
        'BirthWeight': fact[34],
        'LengthStay': fact[12],
        'TotalCharges': fact[37],
        'TotalCosts': fact[38]
    }

    df_array.append(fact_record)
    rowcount += 1

    if (rowcount % 500) == 0:
        fact_record_df = pd.DataFrame(df_array)
        df_array = []
        fact_record_df.to_sql('FactDischarge', if_exists='append', con=engine, index=False)
        print("Loaded " + str(rowcount) + " rows...")


print("Done. Loaded " + str(rowcount) + " rows.")

################################################################################
#
# EoJ: End of Job
#
################################################################################
jobutils.printJobEnd("DSCRGFCT100")
