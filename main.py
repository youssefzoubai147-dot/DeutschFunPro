import json
from rich.console import Console
from rich.table import Table

console = Console()

def check_app():
    with open('dictionary.json', 'r', encoding='utf-8') as f:
        dict_data = json.load(f)
    with open('all_lessons.json', 'r', encoding='utf-8') as f:
        lessons_data = json.load(f)

    table = Table(title="DeutschFun Pro - جاهزية البيانات")
    table.add_column("المكون", style="cyan")
    table.add_column("الإجمالي", style="green")

    table.add_row("قاموس الكلمات", str(len(dict_data)))
    table.add_row("إجمالي الدروس (A1-B1)", str(len(lessons_data)))

    console.print(table)

if __name__ == "__main__":
    check_app()
