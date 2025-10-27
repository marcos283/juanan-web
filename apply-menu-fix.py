#!/usr/bin/env python3
"""
Script para aplicar el fix del menú hamburguesa a todos los archivos HTML
"""

import os
import re
from pathlib import Path

def get_relative_path(file_path, base_path):
    """Calcula la ruta relativa correcta según la profundidad del archivo"""
    rel_path = os.path.relpath(file_path, base_path)
    depth = rel_path.count(os.sep)

    if depth == 0:
        return "", ""
    elif depth == 1:
        return "../", "../"
    else:
        prefix = "../" * depth
        return prefix, prefix

def apply_fix_to_file(file_path, base_path):
    """Aplica el fix del menú a un archivo HTML específico"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Verificar si ya tiene el fix
        if 'menu-simple.css' in content:
            print(f"  - {file_path} ya tiene el fix")
            return False

        # Calcular rutas relativas
        css_prefix, js_prefix = get_relative_path(file_path, base_path)
        css_path = f"{css_prefix}menu-simple.css"
        js_path = f"{js_prefix}menu-simple.js"

        # Añadir CSS después de la última etiqueta <link rel="stylesheet">
        # Buscar la última ocurrencia de <link rel="stylesheet"
        last_link_pos = -1
        for match in re.finditer(r'<link[^>]+rel=["\']stylesheet["\'][^>]*>', content):
            last_link_pos = match.end()

        if last_link_pos > -1:
            # Insertar después del último link
            css_tag = f'\n    <link rel="stylesheet" href="{css_path}">'
            content = content[:last_link_pos] + css_tag + content[last_link_pos:]

        # Añadir JS antes de </body>
        body_close_match = re.search(r'</body>', content)
        if body_close_match:
            js_tag = f'    <script src="{js_path}"></script>\n'
            pos = body_close_match.start()
            content = content[:pos] + js_tag + content[pos:]

        # Escribir el archivo modificado
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  [OK] {file_path} -> {css_path}, {js_path}")
        return True

    except Exception as e:
        print(f"  [ERROR] Error procesando {file_path}: {e}")
        return False

def main():
    base_path = Path(__file__).parent
    print("Aplicando fix del menú hamburguesa a todos los archivos HTML...")
    print()

    # Encontrar todos los archivos HTML
    html_files = []
    for pattern in ['*.html', '*/*.html', '*/*/*.html']:
        html_files.extend(base_path.glob(pattern))

    # Filtrar backups
    html_files = [f for f in html_files if 'backup' not in str(f)]

    total = 0
    updated = 0

    for html_file in sorted(html_files):
        total += 1
        if apply_fix_to_file(html_file, base_path):
            updated += 1

    print()
    print(f"[COMPLETADO] {updated} archivos actualizados de {total} total")

if __name__ == '__main__':
    main()
