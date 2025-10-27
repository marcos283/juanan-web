/**
 * MENÚ HAMBURGUESA NUEVO - JavaScript
 * Menú completamente funcional desde cero
 */

(function() {
    'use strict';

    // Esperar a que el DOM esté listo
    document.addEventListener('DOMContentLoaded', function() {
        console.log('[MENU] Inicializando menú hamburguesa...');

        // Elementos
        const hamburgerBtn = document.getElementById('hamburger-btn');
        const mobileMenu = document.getElementById('mobile-menu');
        const closeBtn = document.getElementById('close-menu-btn');
        const overlay = document.querySelector('.mobile-menu-overlay');
        const body = document.body;

        // Verificar que existen los elementos
        if (!hamburgerBtn || !mobileMenu) {
            console.error('[MENU] No se encontraron los elementos del menú');
            return;
        }

        console.log('[MENU] Elementos encontrados:', {
            hamburgerBtn: !!hamburgerBtn,
            mobileMenu: !!mobileMenu,
            closeBtn: !!closeBtn,
            overlay: !!overlay
        });

        // Función para abrir el menú
        function openMenu() {
            console.log('[MENU] Abriendo menú...');
            mobileMenu.classList.add('active');
            hamburgerBtn.classList.add('active');
            body.classList.add('menu-open');
            mobileMenu.setAttribute('aria-hidden', 'false');
        }

        // Función para cerrar el menú
        function closeMenu() {
            console.log('[MENU] Cerrando menú...');
            mobileMenu.classList.remove('active');
            hamburgerBtn.classList.remove('active');
            body.classList.remove('menu-open');
            mobileMenu.setAttribute('aria-hidden', 'true');
        }

        // Evento: Click en botón hamburguesa
        hamburgerBtn.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            console.log('[MENU] Click en botón hamburguesa');

            if (mobileMenu.classList.contains('active')) {
                closeMenu();
            } else {
                openMenu();
            }
        });

        // Evento: Click en botón cerrar
        if (closeBtn) {
            closeBtn.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                console.log('[MENU] Click en botón cerrar');
                closeMenu();
            });
        }

        // Evento: Click en overlay
        if (overlay) {
            overlay.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                console.log('[MENU] Click en overlay');
                closeMenu();
            });
        }

        // Evento: Tecla ESC
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && mobileMenu.classList.contains('active')) {
                console.log('[MENU] Tecla ESC presionada');
                closeMenu();
            }
        });

        // Cerrar menú al hacer click en un enlace
        const menuLinks = mobileMenu.querySelectorAll('.mobile-menu-list a');
        menuLinks.forEach(function(link) {
            link.addEventListener('click', function() {
                console.log('[MENU] Click en enlace del menú');
                closeMenu();
            });
        });

        console.log('[MENU] ✓ Menú hamburguesa inicializado correctamente');
    });
})();
