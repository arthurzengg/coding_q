class Table:
    def __init__(self, name, columns):
        self.name = name
        self.no_columns = columns
        self.row = {}
        self.row_inserted = 1


class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.db = dict()
        for i in range(len(names)):
            self.db[names[i]] = Table(names, columns)

    def insertRow(self, name: str, row: List[str]) -> None:
        self.db[name].row[self.db[name].row_inserted] = row
        self.db[name].row_inserted += 1

    def deleteRow(self, name: str, rowId: int) -> None:
        self.db[name].row.pop(rowId)

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.db[name].row[rowId][columnId - 1]