setTimeout(function(){
    $('#preloader').fadeOut();
    $('.sk-spinner-wordpress').delay(150).fadeOut('slow');
}, 1000);

function initParallax() {
    $('#home').parallax("50%", 0.3);
}
initParallax();

$(window).scroll(function() {
    if ($(this).scrollTop() > 200) {
        $('.go-top').fadeIn(200);
    } else {
        $('.go-top').fadeOut(200);
    }
});

// Animate the scroll to top
$('.go-top').click(function(event) {
    event.preventDefault();
    $('html, body').animate({scrollTop: 0}, 300);
});
