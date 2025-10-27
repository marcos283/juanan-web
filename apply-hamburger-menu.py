#!/usr/bin/env python3
"""
Script para aplicar el nuevo menú hamburguesa a todos los archivos HTML
"""

import os
import re
from pathlib import Path

def get_base_path(file_path, base_path):
    """Calcula la ruta base según la profundidad del archivo"""
    rel_path = os.path.relpath(file_path, base_path)
    depth = rel_path.count(os.sep)

    if depth == 0:
        return ""
    elif depth == 1:
        return "../"
    else:
        return "../" * depth

def apply_menu_to_file(file_path, base_path, menu_html, css_content, js_content):
    """Aplica el menú hamburguesa a un archivo HTML específico"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Verificar si ya tiene el nuevo menú
        if 'hamburger-button' in content:
            print(f"  - {file_path.name} ya tiene el nuevo menu")
            return False

        # Calcular ruta base
        base = get_base_path(file_path, base_path)

        # Reemplazar __BASE__ en el HTML del menú
        menu_html_with_base = menu_html.replace('__BASE__', base)

        # 1. Insertar CSS inline en el <head> antes de </head>
        css_tag = f'\n<style>\n{css_content}\n</style>\n'
        content = re.sub(r'</head>', css_tag + '</head>', content, count=1)

        # 2. Insertar HTML del menú después de <body>
        content = re.sub(r'(<body[^>]*>)', r'\1\n' + menu_html_with_base + '\n', content, count=1)

        # 3. Insertar JavaScript inline antes de </body>
        js_tag = f'\n<script>\n{js_content}\n</script>\n'
        content = re.sub(r'</body>', js_tag + '</body>', content, count=1)

        # Escribir el archivo modificado
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  [OK] {file_path.name}")
        return True

    except Exception as e:
        print(f"  [ERROR] {file_path.name}: {e}")
        return False

def main():
    base_path = Path(__file__).parent
    print("Aplicando nuevo menu hamburguesa a todos los archivos HTML...")
    print()

    # Leer archivos del menú
    with open(base_path / 'hamburger-menu.html', 'r', encoding='utf-8') as f:
        menu_html = f.read()

    with open(base_path / 'hamburger-menu.css', 'r', encoding='utf-8') as f:
        css_content = f.read()

    with open(base_path / 'hamburger-menu.js', 'r', encoding='utf-8') as f:
        js_content = f.read()

    # Encontrar todos los archivos HTML
    html_files = []
    for pattern in ['*.html', '*/*.html', '*/*/*.html']:
        html_files.extend(base_path.glob(pattern))

    # Filtrar backups y archivos del menú
    html_files = [f for f in html_files if 'backup' not in str(f).lower()
                  and 'hamburger-menu' not in str(f).lower()]

    total = 0
    updated = 0

    for html_file in sorted(html_files):
        total += 1
        if apply_menu_to_file(html_file, base_path, menu_html, css_content, js_content):
            updated += 1

    print()
    print(f"[COMPLETADO] {updated} archivos actualizados de {total} total")

if __name__ == '__main__':
    main()
