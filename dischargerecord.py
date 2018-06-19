"""
     1  Health Service Area
     2  Hospital County
     3  Operating Certificate Number
     4  Facility Id
     5  Facility Name
     6  Age Group
     7  Zip Code - 3 digits
     8  Gender
     9  Race
    10  Ethnicity
    11  Length of Stay
    12  Type of Admission
    13  Patient Disposition
    14  Discharge Year
    15  CCS Diagnosis Code
    16  CCS Diagnosis Description
    17  CCS Procedure Code
    18  CCS Procedure Description
    19  APR DRG Code
    20  APR DRG Description
    21  APR MDC Code
    22  APR MDC Description
    23  APR Severity of Illness Code
    24  APR Severity of Illness Description
    25  APR Risk of Mortality
    26  APR Medical Surgical Description
    27  Payment Typology 1
    28  Payment Typology 2
    29  Payment Typology 3
    30  Attending Provider License Number
    31  Operating Provider License Number
    32  Other Provider License Number
    33  Birth Weight
    34  Abortion Edit Indicator
    35  Emergency Department Indicator
    36  Total Charges
    37  Total Costs
"""

HEALTH_SERVICE_AREA = 0
HOSPITAL_COUNTY = 1
OPERATING_CERTIFICATE_NUMBER = 2
FACILITY_ID = 3
FACILITY_NAME = 4
AGE_GROUP = 5
ZIP_CODE = 6
GENDER = 7
RACE = 8
ETHNICITY = 9
LENGTH_STAY = 10
TYPE_ADMISSION = 11
PATIENT_DISPOSITION = 12
DISCHARGE_YEAR = 13
CCS_DIAGNOSIS_CODE = 14
CCS_DIAGNOSIS_DESC = 15
CCS_PROCEDURE_CODE = 16
CCS_PROCEDURE_DESC = 17
APR_DRG_CODE = 18
APR_DRG_DESC = 19
APR_MDC_CODE = 20
APR_MDC_DESC = 21
APR_SEVERITY_ILLNESS_CODE = 22
APR_SEVERITY_ILLNESS_DESC = 23
APR_RISK_MORTALITY = 24
APR_MEDICAL_SURGICAL_DESC = 25
PAYMENT_TYPO_1 = 26
PAYMENT_TYPO_2 = 27
PAYMENT_TYPO_3 = 28
ATTEN_PROV_LIC = 29
OPERA_PROV_LIC = 30
OTHER_PROV_LIC = 31
BIRTH_WEIGHT = 32
ABORTION_IND = 33
EMERGENCY_IND = 34
TOTAL_CHARG = 35
TOTAL_COSTS = 36



class DischargeRecord():

    def __init__(self, row):
        self.row = row

class DimDateRecord(DischargeRecord):

    def get_row(self):
        return [self.row[DISCHARGE_YEAR]]

class DimProviderRecord(DischargeRecord):

    def get_row(self):
        return [self.row[ATTEN_PROV_LIC], self.row[OPERA_PROV_LIC], self.row[OTHER_PROV_LIC]]
