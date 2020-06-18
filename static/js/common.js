$('.reviews__slider').slick({
    dots: true,
    infinite: true,
    speed: 300,
    slidesToShow: 1,
    adaptiveHeight: true,
    lazyLoad: 'ondemand',
    autoPlay: true,
    autoplaySpeed: 2000
});
$('.lessons__list_block').slick({
    dots: true,
    infinite: true,
    speed: 300,
    slidesToShow: 3,
    adaptiveHeight: true,
    lazyLoad: 'ondemand',
    autoPlay: true,
    autoplaySpeed: 2000
});
$('.test__elem').on('click', function () {
    var attr = $(this).attr('data-correct');

    if (String(attr) == "false") {
        alert('bad')
    } else {
        alert('good')
    }
});