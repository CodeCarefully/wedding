$(function() {
    $('.navbutton').click(function() {
        $('.navbutton').removeClass('active');
        $(this).addClass('active');
    });
});

$(document).on('click','.navbar-collapse.in',function(e) {

    if( $(e.target).is('a') && ( $(e.target).attr('class') != 'dropdown-toggle' ) ) {
        $(this).collapse('hide');
    }

});