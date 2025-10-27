#!/usr/bin/env python3
"""
Script para actualizar el color del botón hamburguesa en todos los archivos HTML
"""

import re
from pathlib import Path

def update_button_color(file_path):
    """Actualiza el color del botón hamburguesa"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Verificar si tiene el botón
        if '.hamburger-button {' not in content:
            print(f"  [SKIP] {file_path.name} - no tiene el menu hamburguesa")
            return False

        # Verificar si ya tiene el nuevo color
        if 'background: #084E89;' in content and '.hamburger-button {' in content:
            print(f"  - {file_path.name} ya tiene el nuevo color")
            return False

        # Reemplazar el color antiguo
        content = re.sub(
            r'(\.hamburger-button\s*\{[^}]*background:\s*)#2c3e50',
            r'\1#084E89',
            content
        )

        content = re.sub(
            r'(\.hamburger-button:hover\s*\{[^}]*background:\s*)#34495e',
            r'\1#0a5fa6',
            content
        )

        # Actualizar las sombras
        content = re.sub(
            r'box-shadow:\s*0\s+2px\s+10px\s+rgba\(0,\s*0,\s*0,\s*0\.2\);',
            'box-shadow: 0 4px 12px rgba(8, 78, 137, 0.4);',
            content
        )

        content = re.sub(
            r'(\.hamburger-button:hover[^}]*)(transform:[^;]+;)',
            r'\1\2\n    box-shadow: 0 6px 16px rgba(8, 78, 137, 0.6);',
            content
        )

        # Escribir el archivo
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  [OK] {file_path.name}")
        return True

    except Exception as e:
        print(f"  [ERROR] {file_path.name}: {e}")
        return False

def main():
    base_path = Path(__file__).parent
    print("Actualizando color del boton hamburguesa...")
    print()

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
        if update_button_color(html_file):
            updated += 1

    print()
    print(f"[COMPLETADO] {updated} archivos actualizados de {total} total")

if __name__ == '__main__':
    main()
