"""
Case Study Demonstration Script: Rich Codebase Analysis
Course: 23CSE101 - Computational Problem Solving
Team ID: A11
Members: CB.SC.U4CSE26060, CB.SC.U4CSE26065, CB.SC.U4CSE26039, CB.SC.U4CSE26032
Target Project: Rich (https://github.com/Textualize/rich)

This script programmatically demonstrates the key architectural concepts,
algorithms, data structures, and file operations analyzed in the Case Study Report.
"""

import sys
import os
from pathlib import Path

# Force UTF-8 stream handling on Windows console
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Add the local rich repository to sys.path
RICH_REPO_DIR = Path(__file__).parent / "rich"
sys.path.insert(0, str(RICH_REPO_DIR))

try:
    import rich
    from rich.console import Console
    from rich.table import Table
    from rich.tree import Tree
    from rich.panel import Panel
    from rich.text import Text
    from rich.style import Style
    from rich.segment import Segment
    from rich._ratio import ratio_resolve, Edge
    from rich.cells import cell_len, get_character_cell_size
    from rich._wrap import divide_line
    from rich.file_proxy import FileProxy
except ImportError as e:
    print(f"Error loading local rich package: {e}")
    sys.exit(1)


def section_header(title: str, console: Console):
    console.print()
    console.rule(f"[bold cyan]{title}[/bold cyan]", style="cyan")
    console.print()


def demo_modularity(console: Console):
    """Rubric 1 (2 Marks): Demonstrating the Open-Closed Principle via the Console Protocol."""
    section_header("1. Modularity & The Console Render Protocol (__rich_console__)", console)

    class AcademicCourseScorecard:
        """A custom domain object implementing the Rich Console Protocol.
        Notice that Rich does NOT need to be modified to support this new UI component.
        """
        def __init__(self, course_code: str, title: str, rubrics: dict[str, int]):
            self.course_code = course_code
            self.title = title
            self.rubrics = rubrics

        def __rich_console__(self, console: Console, options):
            table = Table(title=f"[bold gold1]{self.course_code}: {self.title}[/bold gold1]", border_style="bright_blue")
            table.add_column("Rubric Criterion", style="white", justify="left")
            table.add_column("Marks", style="green", justify="right")

            for criterion, marks in self.rubrics.items():
                table.add_row(criterion, f"{marks} Marks")
            table.add_section()
            table.add_row("[bold]Total Evaluation Score[/bold]", f"[bold]{sum(self.rubrics.values())} Marks[/bold]")

            yield Panel(table, title="[magenta]Duck-Typed Protocol Component[/magenta]", expand=False)

    scorecard = AcademicCourseScorecard(
        "23CSE101",
        "Case Study Component",
        {
            "Algorithmic Thinking & Cornerstones": 3,
            "Use of Data Structures & Reasoning": 3,
            "Modularity Design": 2,
            "Functions, Packages & File Operations": 4,
            "Code Walkthrough & Viva": 3
        }
    )
    console.print(scorecard)
    console.print("[dim green][OK] Custom component cleanly rendered using __rich_console__ without modifying Rich core.[/dim green]")


def demo_algorithms(console: Console):
    """Rubric 2 (3 Marks): Ratio Constraint Resolution and Unicode Binary Search."""
    section_header("2. Problem Solving & Algorithmic Thinking", console)

    # A. Ratio Resolution Algorithm
    console.print("[bold yellow]A. Ratio Constraint Resolution (_ratio.py):[/bold yellow]")
    class SimpleEdge:
        def __init__(self, size=None, ratio=1, minimum_size=1):
            self.size = size
            self.ratio = ratio
            self.minimum_size = minimum_size

    total_width = 80
    edges = [SimpleEdge(size=20), SimpleEdge(ratio=1, minimum_size=10), SimpleEdge(ratio=2, minimum_size=15)]
    resolved_widths = ratio_resolve(total_width, edges)
    console.print(f"Total Width: [cyan]{total_width} cols[/cyan] | Constraints: Fixed(20), Ratio(1), Ratio(2)")
    console.print(f"Resolved Column Widths: [bold green]{resolved_widths}[/bold green] (Sum: {sum(resolved_widths)})")

    # B. Cell Width Binary Search
    console.print("\n[bold yellow]B. Unicode Cell Width Measurement vs len() (cells.py):[/bold yellow]")
    samples = ["Hello", "Python 🐍", "Amrita (அம்ரிதா)", "TextualはPythonのフレームワーク"]
    table = Table(title="String Length vs Terminal Cell Width", border_style="cyan")
    table.add_column("Sample Text")
    table.add_column("Python len() (Code points)", justify="right")
    table.add_column("Rich cell_len() (Terminal Cells)", justify="right")

    for s in samples:
        table.add_row(s, str(len(s)), str(cell_len(s)))
    console.print(table)


def demo_data_structures(console: Console):
    """Rubric 3 (3 Marks): Bitmask Style Attributes, NamedTuple Segments, and Tree Hierarchy."""
    section_header("3. Data Structures: Bitmasks, NamedTuples & Explicit Stacks", console)

    # A. Bitmask inspection
    s = Style(bold=True, italic=True, underline=False, color="red")
    console.print(f"Style Representation: [magenta]{s}[/magenta]")
    console.print(f"Internal Bitmask _attributes: [bold cyan]{bin(s._attributes)}[/bold cyan]")
    console.print(f"Configured Attributes Mask _set_attributes: [bold cyan]{bin(s._set_attributes)}[/bold cyan]")
    console.print(f"Descriptor Access (s.bold): [bold green]{s.bold}[/bold green], (s.italic): [bold green]{s.italic}[/bold green]")

    # B. Tree Data Structure
    console.print("\n[bold yellow]N-ary Tree Data Structure with Iterative DFS Traversal:[/bold yellow]")
    tree = Tree("[bold cyan]Textualize/rich Codebase Architecture[/bold cyan]")
    c1 = tree.add("Layer 1: User Facing Components (Table, Tree, Markdown)")
    c2 = tree.add("Layer 2: Lexical Parsers (markup.py, ansi.py)")
    c3 = tree.add("Layer 3: Solvers (_ratio.py, cells.py, _wrap.py)")
    c4 = tree.add("Layer 4: Primitives (Segment NamedTuple, Style Bitmask)")
    c5 = tree.add("Layer 5: Drivers (Console, FileProxy, Win32 API)")
    console.print(tree)


def demo_file_operations(console: Console):
    """Rubric 4 (2 Marks): File Operations & Stream Handling."""
    section_header("4. File Operations for Data Handling & Multi-Format Export", console)

    export_path = Path(__file__).parent / "demo_export.html"
    recording_console = Console(record=True, width=70)
    recording_console.print(Panel("[bold green]Rich Case Study - File I/O Export Verification[/bold green]\nSuccessfully generated by Team A11.", title="Export Demonstration"))
    recording_console.save_html(str(export_path))

    console.print(f"[green][OK] Live HTML Export written to disk:[/green] [cyan]{export_path.name}[/cyan] ({export_path.stat().st_size} bytes)")
    console.print("[green][OK] Context manager [bold]with open(..., 'w', encoding='utf-8')[/bold] securely handled stream write.[/green]")


def main():
    console = Console()
    console.print(Panel(
        "[bold cyan]Case Study Live Verification & Code Walkthrough[/bold cyan]\n"
        "[white]Course: 23CSE101 · Computational Problem Solving[/white]\n"
        "[white]Team A11: CB.SC.U4CSE26060, CB.SC.U4CSE26065, CB.SC.U4CSE26039, CB.SC.U4CSE26032[/white]\n"
        "[white]Subject Codebase: Textualize/rich (49,000+ GitHub Stars)[/white]",
        border_style="bright_magenta"
    ))

    demo_modularity(console)
    demo_algorithms(console)
    demo_data_structures(console)
    demo_file_operations(console)

    console.print()
    console.rule("[bold green]Case Study Verification Complete[/bold green]", style="green")


if __name__ == "__main__":
    main()
