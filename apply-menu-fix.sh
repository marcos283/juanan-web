#!/bin/bash

# Script para aplicar el fix del menú a todos los archivos HTML

cd "$(dirname "$0")"

echo "Aplicando fix del menú hamburguesa a todos los archivos HTML..."

find . -name "*.html" -type f | grep -v backup | while IFS= read -r file; do
  # Calcular profundidad
  depth=$(echo "$file" | tr -cd '/' | wc -c)

  # Construir ruta relativa
  if [ $depth -eq 1 ]; then
    css_path="menu-simple.css"
    js_path="menu-simple.js"
  elif [ $depth -eq 2 ]; then
    css_path="../menu-simple.css"
    js_path="../menu-simple.js"
  else
    css_path="../../menu-simple.css"
    js_path="../../menu-simple.js"
  fi

  # Verificar si ya tiene las referencias
  if ! grep -q "menu-simple.css" "$file"; then
    echo "Procesando: $file"

    # Buscar la última etiqueta <link> y añadir después
    sed -i "/<link.*rel=['\"]stylesheet['\"].*>/!b;:a;n;/<link.*rel=['\"]stylesheet['\"].*>/ba;i\\    <link rel=\"stylesheet\" href=\"$css_path\">" "$file"

    # Buscar la última etiqueta <script> antes de </body> y añadir después
    sed -i "/<\/body>/i\\    <script src=\"$js_path\"></script>" "$file"

    echo "  ✓ Fix aplicado con rutas: $css_path y $js_path"
  else
    echo "  - $file ya tiene el fix"
  fi
done

echo ""
echo "✓ Proceso completado"
