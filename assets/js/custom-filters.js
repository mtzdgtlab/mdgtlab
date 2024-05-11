$(document).ready(function(){
    // Inicializar Isotope en el contenedor correcto
    var $grid = $('.row').isotope({
        itemSelector: '.item',
        layoutMode: 'fitRows'
    });

    // Enlace de filtros
    $('.project-filter').on('click', 'li', function() {
        var filterValue = $(this).attr('data-filter');
        $grid.isotope({ filter: filterValue });
    });

    // Asegurar que las páginas de productos se manejan correctamente
    $('.product-page').hide();
    $('#page-1').show();

    // Para manejar la paginación correctamente
    $('.page-numbers').on('click', function(e) {
        e.preventDefault();
        var pageNumber = $(this).text();
        $('.product-page').hide();
        $('#page-' + pageNumber).show();
    });
});
