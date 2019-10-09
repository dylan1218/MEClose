from openpyxl import Workbook, load_workbook

def Get_Reconciled_Balance(month, year, entity, accountNumber, pathname):
    endingBalanceIdentifier = "/EB"  + str(month) + str(year) + str(entity) + str(accountNumber)

    wb = load_workbook(filename = path, read_only=False, data_only=True)
    sheet_ranges = wb['Summary']

    for row in sheet_ranges.iter_rows():
        for entry in row:
            try:
                if endingBalanceIdentifier == entry.value:
                    endingBalanceIdentifier_Cell = entry
                    
            except(AttributeError, TypeError):
                continue
    print(endingBalanceIdentifier_Cell.offset(row=0, column=-1).value)
