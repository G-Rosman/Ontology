import sqlite3
from typing import List, Dict
import subprocess
from link_class import process_links
def generate_graph(db_path: str) -> str:
    """
    Генерирует граф в формате DOT на основе данных из базы данных.
    
    :param db_path: Путь к SQLite базы данных
    :return: Текст графического представления в формате DOT
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM links ORDER BY name_start, name_end")
    rows = cursor.fetchall()

    # Генерируем граф
    graph = "digraph G {\n"
    graph += "node[color = black, fontsize = 12];\n"
    graph += "edge[color = black, fontsize = 12];\n"

    for row in rows:
        id, start, direction, rool, quantor, end, ring = row
        graph += f'"{start}" -> "{end}" [dir=both,color = '
        if (rool == "5"):  
            graph += "blue,"
        elif (rool == "13"):
            graph += "black,"
        elif (rool == "7"):
            graph += "red,"

        if ring:
            graph += "style = dotted, "

        if quantor == "aa":
            graph += "arrowhead=normal, arrowtail=box"
        elif quantor == "ae":
            graph += "arrowhead=normal, arrowtail=obox"
        elif quantor == "ea":
            graph += "arrowhead=onormal, arrowtail=box"
        elif quantor == "ee":
            graph += "arrowhead=onormal, arrowtail=obox"

        graph += "];\n"
    graph += "}\n"

    conn.close()
    return graph


def draw():
    while (process_links()):
        pass


    db_path = "example.db"
    dot_file_path = "graph.dot"
    picture = "output.png"

    graph_text = generate_graph(db_path)

    with open(dot_file_path, "w") as f:
        f.write(graph_text)

    cmd = ['dot', '-Tpng', dot_file_path, '-o', picture]
    subprocess.run(cmd, capture_output=True, text=True, check=True)
