#!/usr/bin/env python3
"""
Script para añadir CSS que oculta los elementos de Elementor
"""

import os
import re
from pathlib import Path

def apply_hide_css(file_path, css_content):
    """Aplica el CSS para ocultar Elementor a un archivo HTML"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Verificar si ya tiene el CSS
        if 'Ocultar botones y menú original de Elementor' in content:
            print(f"  - {file_path.name} ya tiene el CSS")
            return False

        # Buscar el bloque de CSS del menú hamburguesa
        # y añadir el CSS justo antes del </style>
        pattern = r'(body\.menu-open\s*\{[^}]+\})\s*(</style>)'
        match = re.search(pattern, content, re.DOTALL)

        if match:
            # Insertar después del bloque body.menu-open y antes de </style>
            css_to_add = '\n\n/* Ocultar botones y menú original de Elementor */\n' + css_content + '\n'
            content = content[:match.end(1)] + css_to_add + '\n' + match.group(2) + content[match.end(2):]

            # Escribir el archivo modificado
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f"  [OK] {file_path.name}")
            return True
        else:
            print(f"  [SKIP] {file_path.name} - no se encontro <style>")
            return False

    except Exception as e:
        print(f"  [ERROR] {file_path.name}: {e}")
        return False

def main():
    base_path = Path(__file__).parent
    print("Aplicando CSS para ocultar elementos de Elementor...")
    print()

    # Leer el CSS
    with open(base_path / 'hide-elementor.css', 'r', encoding='utf-8') as f:
        css_content = f.read()

    # Encontrar todos los archivos HTML
    html_files = []
    for pattern in ['*.html', '*/*.html', '*/*/*.html']:
        html_files.extend(base_path.glob(pattern))

    # Filtrar backups
    html_files = [f for f in html_files if 'backup' not in str(f).lower()
                  and 'hamburger-menu' not in str(f).lower()]

    total = 0
    updated = 0

    for html_file in sorted(html_files):
        total += 1
        if apply_hide_css(html_file, css_content):
            updated += 1

    print()
    print(f"[COMPLETADO] {updated} archivos actualizados de {total} total")

if __name__ == '__main__':
    main()
