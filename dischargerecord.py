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

DISCHARGE_MONTH = 0
HEALTH_SERVICE_AREA = 1
HOSPITAL_COUNTY = 2
OPERATING_CERTIFICATE_NUMBER = 3
FACILITY_ID = 4
FACILITY_NAME = 5
AGE_GROUP = 6
ZIP_CODE = 7
GENDER = 8
RACE = 9
ETHNICITY = 10
LENGTH_STAY = 11
TYPE_ADMISSION = 12
PATIENT_DISPOSITION = 13
DISCHARGE_YEAR = 14
CCS_DIAGNOSIS_CODE = 15
CCS_DIAGNOSIS_DESC = 16
CCS_PROCEDURE_CODE = 17
CCS_PROCEDURE_DESC = 18
APR_DRG_CODE = 19
APR_DRG_DESC = 20
APR_MDC_CODE = 21
APR_MDC_DESC = 22
APR_SEVERITY_ILLNESS_CODE = 23
APR_SEVERITY_ILLNESS_DESC = 24
APR_RISK_MORTALITY = 25
APR_MEDICAL_SURGICAL_DESC = 26
PRIMARY_PAY = 27
SECONDARY_PAY = 28
TERTIARY_PAY = 29
ATTEN_PROV_LIC = 30
OPERA_PROV_LIC = 31
OTHER_PROV_LIC = 32
BIRTH_WEIGHT = 33
ABORTION_IND = 34
EMERGENCY_IND = 35
TOTAL_CHARG = 36
TOTAL_COSTS = 37



class DischargeRecord():

    def __init__(self, row=None):
        self.row = row
        self.COLUMN_INDECES = []
        self.COLUMN_NAMES = []
        self.COLUMN_TYPES = {}
        self.COLUMN_CONV = {}

    def conv_indToInt(self, charInd):
        intInd = 0
        if charInd == 'Y' or charInd == 'y':
            intInd = 1
        return intInd

    def conv_zipcode(self, zipcode):
        if type(zipcode) is str and zipcode == 'OOS':
            return 0
        else:
            return int(zipcode)

    def conv_money(self, amount):
        amountStr = str(amount)
        amountStr = amountStr.replace('$', '')
        amountStr = amountStr.replace(',', '')
        amountStr = amountStr.replace(' ', '')
        return float(amountStr)

    def conv_month(self, month):
        MONTHS = {
            'JAN': 1,
            'FEB': 2,
            'MAR': 3,
            'APR': 4,
            'MAY': 5,
            'JUN': 6,
            'JUL': 7,
            'AUG': 8,
            'SEP': 9,
            'OCT': 10,
            'NOV': 11,
            'DEC': 12
        }
        return MONTHS[month]

    def get_column_indeces(self):
        return self.COLUMN_INDECES

    def get_column_names(self):
        return self.COLUMN_NAMES

    def get_column_types(self):
        return self.COLUMN_TYPES

    def get_column_converters(self):
        return self.COLUMN_CONV

class DimDateRecord(DischargeRecord):

    def __init__(self, row=None):
        self.row = row
        self.COLUMN_INDECES = [DISCHARGE_YEAR, DISCHARGE_MONTH]
        self.COLUMN_NAMES = [
            'DischargeMonth',
            'DischargeYear'
        ]
        self.COLUMN_TYPES = {
            'DischargeYear': 'int64'
        }
        self.COLUMN_CONV = {
            'DischargeMonth': self.conv_month
        }

    def get_row(self):
        return [self.row[DISCHARGE_YEAR, DISCHARGE_MONTH]]

class DimProviderRecord(DischargeRecord):

    def __init__(self, row=None):
        self.row = row
        self.COLUMN_INDECES = [
            ATTEN_PROV_LIC,
            OPERA_PROV_LIC,
            OTHER_PROV_LIC
        ]
        self.COLUMN_NAMES = [
            'AttendingLicenseNo',
            'OperatingLicenseNo',
            'OtherLicenseNo'
        ]
        self.COLUMN_TYPES = {
            'AttendingLicenseNo': 'str',
            'OperatingLicenseNo': 'str',
            'OtherLicenseNo': 'str'
        }

    def get_row(self):
        return [self.row[ATTEN_PROV_LIC], self.row[OPERA_PROV_LIC], self.row[OTHER_PROV_LIC]]

class DimAdmissionRecord(DischargeRecord):

    def __init__(self, row=None):
        self.row = row
        self.COLUMN_INDECES = [
            TYPE_ADMISSION,
            PATIENT_DISPOSITION,
            ABORTION_IND,
            EMERGENCY_IND
        ]
        self.COLUMN_NAMES = [
            'TypeAdmission',
            'PatientDisposition',
            'AbortionIndicator',
            'EmergencyIndicator'
        ]
        self.COLUMN_TYPES = {
            'TypeAdmission': 'str',
            'PatientDisposition': 'str'
        }
        self.COLUMN_CONV = {
            'AbortionIndicator': self.conv_indToInt,
            'EmergencyIndicator': self.conv_indToInt
        }

class DimAPRClassificationRecord(DischargeRecord):

    def __init__(self, row=None):
        self.row = row
        self.COLUMN_INDECES = [
            APR_DRG_CODE,
            APR_DRG_DESC,
            APR_MDC_CODE,
            APR_MDC_DESC,
            APR_SEVERITY_ILLNESS_CODE,
            APR_SEVERITY_ILLNESS_DESC,
            APR_RISK_MORTALITY,
            APR_MEDICAL_SURGICAL_DESC
            ]
        self.COLUMN_NAMES = [
            'DrgCode',
            'DrgDescription',
            'MdcCode',
            'MdcDescription',
            'SeverityIllnessCode',
            'SeverityIllnessDescription',
            'RiskOfMortality',
            'MedicalSurgicalDescription'
        ]
        self.COLUMN_TYPES = {
            'DrgCode': 'int64',
            'DrgDescription': 'str',
            'MdcCode': 'int64',
            'MdcDescription': 'str',
            'SeverityIllnessCode': 'int64',
            'SeverityIllnessDescription': 'str',
            'RiskOfMortality': 'str',
            'MedicalSurgicalDescription': 'str'
        }

class DimClinicClassRecord(DischargeRecord):

    def __init__(self, row=None):
        self.row = row
        self.COLUMN_INDECES = [
            CCS_DIAGNOSIS_CODE,
            CCS_DIAGNOSIS_DESC,
            CCS_PROCEDURE_CODE,
            CCS_PROCEDURE_DESC
        ]
        self.COLUMN_NAMES = [
            'DiagnosisCode',
            'DiagnosisDescription',
            'ProcedureCode',
            'ProcedureDescription'
        ]
        self.COLUMN_TYPES = {
            'DiagnosisCode': 'int64',
            'DiagnosisDescription': 'str',
            'ProcedureCode': 'int64',
            'ProcedureDescription': 'str'
        }

class DimPaymentRecord(DischargeRecord):

    def __init__(self, row=None):
        self.row = row
        self.COLUMN_INDECES = [
            PRIMARY_PAY,
            SECONDARY_PAY,
            TERTIARY_PAY
        ]
        self.COLUMN_NAMES = [
            'PrimaryPayMethod',
            'SecondaryPayMethod',
            'TertiaryPayMethod'
        ]
        self.COLUMN_TYPES = {
            'PrimaryPayMethod': 'str',
            'SecondaryPayMethod': 'str',
            'TertiaryPayMethod': 'str'
        }

class DimDemographicsRecord(DischargeRecord):

    def __init__(self, row=None):
        self.row = row
        self.COLUMN_INDECES = [
            AGE_GROUP,
            GENDER,
            RACE,
            ETHNICITY
        ]
        self.COLUMN_NAMES = [
            'AgeGroup',
            'Gender',
            'Race',
            'Ethnicity'
        ]
        self.COLUMN_TYPES = {
            'AgeGroup': 'str',
            'Gender': 'str',
            'Race': 'str',
            'Ethnicity': 'str'
        }

class DimLocationRecord(DischargeRecord):

    def __init__(self, row=None):
        self.row = row
        self.COLUMN_INDECES = [
            HEALTH_SERVICE_AREA,
            HOSPITAL_COUNTY,
            FACILITY_ID,
            FACILITY_NAME,
            ZIP_CODE
        ]
        self.COLUMN_NAMES = [
            'HealthServiceArea',
            'HospitalCounty',
            'FacilityID',
            'FacilityName',
            'ZipCode'
        ]
        self.COLUMN_TYPES = {
            'HealthServiceArea': 'str',
            'HospitalCounty': 'str',
            'FacilityID': 'int64',
            'FacilityName': 'str'
        }
        self.COLUMN_CONV = {
            'ZipCode': self.conv_zipcode
        }

class FactDischarge(DischargeRecord):

    def __init__(self, row=None):
        self.row = row
        self.COLUMN_INDECES = [
            DISCHARGE_MONTH,
            HEALTH_SERVICE_AREA,
            HOSPITAL_COUNTY,
            OPERATING_CERTIFICATE_NUMBER,
            FACILITY_ID,
            FACILITY_NAME,
            AGE_GROUP,
            ZIP_CODE,
            GENDER,
            RACE,
            ETHNICITY,
            LENGTH_STAY,
            TYPE_ADMISSION,
            PATIENT_DISPOSITION,
            DISCHARGE_YEAR,
            CCS_DIAGNOSIS_CODE,
            CCS_DIAGNOSIS_DESC,
            CCS_PROCEDURE_CODE,
            CCS_PROCEDURE_DESC,
            APR_DRG_CODE,
            APR_DRG_DESC,
            APR_MDC_CODE,
            APR_MDC_DESC,
            APR_SEVERITY_ILLNESS_CODE,
            APR_SEVERITY_ILLNESS_DESC,
            APR_RISK_MORTALITY,
            APR_MEDICAL_SURGICAL_DESC,
            PRIMARY_PAY,
            SECONDARY_PAY,
            TERTIARY_PAY,
            ATTEN_PROV_LIC,
            OPERA_PROV_LIC,
            OTHER_PROV_LIC,
            BIRTH_WEIGHT,
            ABORTION_IND,
            EMERGENCY_IND,
            TOTAL_CHARG,
            TOTAL_COSTS
        ]
        self.COLUMN_NAMES = [
            'DischargeMonth',
            'HealthServiceArea',
            'HospitalCounty',
            'OperatingCertNo',
            'FacilityID',
            'FacilityName',
            'AgeGroup',
            'ZipCode',
            'Gender',
            'Race',
            'Ethnicity',
            'LengthStay',
            'TypeAdmission',
            'PatientDisposition',
            'DischargeYear',
            'DiagnosisCode',
            'DiagnosisDescription',
            'ProcedureCode',
            'ProcedureDescription',
            'DrgCode',
            'DrgDescription',
            'MdcCode',
            'MdcDescription',
            'SeverityIllnessCode',
            'SeverityIllnessDescription',
            'RiskOfMortality',
            'MedicalSurgicalDescription',
            'PrimaryPayMethod',
            'SecondaryPayMethod',
            'TertiaryPayMethod',
            'AttendingLicenseNo',
            'OperatingLicenseNo',
            'OtherLicenseNo',
            'BirthWeight',
            'AbortionIndicator',
            'EmergencyIndicator',
            'TotalCharges',
            'TotalCosts'
        ]
        self.COLUMN_TYPES = {
            'DischargeYear': 'int64',
            'AttendingLicenseNo': 'str',
            'OperatingLicenseNo': 'str',
            'OtherLicenseNo': 'str',
            'TypeAdmission': 'str',
            'PatientDisposition': 'str',
            'DrgCode': 'int64',
            'DrgDescription': 'str',
            'MdcCode': 'int64',
            'MdcDescription': 'str',
            'SeverityIllnessCode': 'int64',
            'SeverityIllnessDescription': 'str',
            'RiskOfMortality': 'str',
            'MedicalSurgicalDescription': 'str',
            'DiagnosisCode': 'int64',
            'DiagnosisDescription': 'str',
            'ProcedureCode': 'int64',
            'ProcedureDescription': 'str',
            'PrimaryPayMethod': 'str',
            'SecondaryPayMethod': 'str',
            'TertiaryPayMethod': 'str',
            'AgeGroup': 'str',
            'Gender': 'str',
            'Race': 'str',
            'Ethnicity': 'str',
            'HealthServiceArea': 'str',
            'HospitalCounty': 'str',
            'FacilityID': 'int64',
            'FacilityName': 'str',
            'BirthWeight': 'float64',
            'LengthStay': 'float64'
        }
        self.COLUMN_CONV = {
            'DischargeMonth': self.conv_month,
            'AbortionIndicator': self.conv_indToInt,
            'EmergencyIndicator': self.conv_indToInt,
            'TotalCharges': self.conv_money,
            'TotalCosts': self.conv_money,
            'ZipCode': self.conv_zipcode
        }
