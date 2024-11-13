$(document).ready(function(){

    //$('[data-toggle="tooltip"], .dataTooltip').tooltip();

    $('.menu .dropdown').hover(function(){
        $(this).addClass('open');
    }, function(){
        $(this).removeClass('open');
    });

    $(function () {
        $('[data-toggle="tooltip"]').tooltip()
    });

    $(function () {
        $('[data-toggle="popover"]').popover()
    })

});
