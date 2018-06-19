import csv

import pprint

from dischargerecord import DimDateRecord
from dischargerecord import DimProviderRecord


# with open('./sample.csv', newline='') as csvfile:
#     rowreader = csv.reader(csvfile)
#     for row in rowreader:
#         newrow = dischargerecord.DimDateRecord(row)
#         print(str(newrow.get_row()))
#         print(row[dischargerecord.DISCHARGE_YEAR])
#         exit()

unique_date_rows = []
skip_first_row = True

with open('./sample.csv', newline='') as csvfile:
    rowreader = csv.reader(csvfile)
    for row in rowreader:
        daterow = DimDateRecord(row)

        if skip_first_row:
            skip_first_row = False
        else:
            if daterow.get_row() in unique_date_rows:
                pass
            else:
                unique_date_rows.append(daterow.get_row())

    pprint.pprint(unique_date_rows)

unique_prov_rows = []
skip_first_row = True

with open('./sample.csv', newline='') as csvfile:
    rowreader = csv.reader(csvfile)
    for row in rowreader:
        provrow = DimProviderRecord(row)

        if skip_first_row:
            skip_first_row = False
        else:
            if provrow.get_row() in unique_prov_rows:
                pass
            else:
                unique_prov_rows.append(provrow.get_row())

    pprint.pprint(unique_prov_rows)


exit()
