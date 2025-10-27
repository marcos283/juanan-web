/**
 * Menú Hamburguesa Simple
 * Reemplazo funcional para Elementor Pro Off-Canvas
 */

(function() {
    'use strict';

    // Esperar a que el DOM esté listo
    document.addEventListener('DOMContentLoaded', function() {

        // Obtener el contenedor off-canvas
        const offCanvas = document.getElementById('off-canvas-1d5554f');
        if (!offCanvas) return;

        const overlay = offCanvas.querySelector('.e-off-canvas__overlay');
        const main = offCanvas.querySelector('.e-off-canvas__main');

        // Función para abrir el menú
        function openMenu() {
            offCanvas.classList.add('active');
            offCanvas.setAttribute('aria-hidden', 'false');
            offCanvas.removeAttribute('inert');
            document.body.style.overflow = 'hidden'; // Evitar scroll
        }

        // Función para cerrar el menú
        function closeMenu() {
            offCanvas.classList.remove('active');
            offCanvas.setAttribute('aria-hidden', 'true');
            offCanvas.setAttribute('inert', '');
            document.body.style.overflow = ''; // Restaurar scroll
        }

        // Buscar todos los botones de abrir
        const openButtons = document.querySelectorAll('a[href*="off_canvas:open"]');
        openButtons.forEach(function(btn) {
            btn.addEventListener('click', function(e) {
                e.preventDefault();
                openMenu();
            });
        });

        // Buscar todos los botones de cerrar
        const closeButtons = document.querySelectorAll('a[href*="off_canvas:close"]');
        closeButtons.forEach(function(btn) {
            btn.addEventListener('click', function(e) {
                e.preventDefault();
                closeMenu();
            });
        });

        // Cerrar al hacer clic en el overlay
        if (overlay) {
            overlay.addEventListener('click', closeMenu);
        }

        // Cerrar con tecla ESC
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && offCanvas.classList.contains('active')) {
                closeMenu();
            }
        });

        console.log('✓ Menú hamburguesa inicializado correctamente');
    });
})();
