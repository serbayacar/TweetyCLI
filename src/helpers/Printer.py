from rich.console import Console
from rich.table import Table
from rich import box


class Printer():

    @staticmethod
    def asTable(title):
        table = Table(title = title, show_header=True, box = box.SIMPLE_HEAVY)
        return table

    @staticmethod
    def addRow(table, text):
        table.add_row('@'+text.user.name + '\n', text.text + '\n')
        return table

    @staticmethod
    def addColumn(table, text):
        for t in text:
            table.add_column(t)

        return table

    @staticmethod
    def print(table):
        console = Console()
        console.print(table)
        return True

   