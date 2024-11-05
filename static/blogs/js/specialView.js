/**
 * Created by Azamat Mirvosiqov on 29.01.2015.
 */

var min = 16,
    max = 30;

function makeNormal() {
    $('html').removeClass('blackAndWhite blackAndWhiteInvert');
    $.removeCookie('specialView', {path: '/'});
}

function makeBlackAndWhite() {
    makeNormal();
    $('html').addClass('blackAndWhite');
    $.cookie("specialView", 'blackAndWhite', {path: '/'});
}

function makeBlackAndWhiteDark() {
    makeNormal();
    $('html').addClass('blackAndWhiteInvert');
    $.cookie("specialView", 'blackAndWhiteInvert', {path: '/'});
}

function setFontSize(size) {
    if (size < min) {
        size = min;
    }
    if (size > max) {
        size = max;
    }
    $('').css({'font-size': parseInt(size) + 9 + 'px'});
    $('.accordion li a,.head_menu .nav>li>a, .attention ').css({'font-size': parseInt(size) + 2 + 'px'});
    $('.main-news h1,.news_list li a').css({'font-size': parseInt(size) + 4 + 'px'});
    $('.link_list a, .expmenu li a, .main-news p a, p, .anons_link, .text_anons,.slide_text .table_sl_text, .work ul li, .table_link, .list_title, .list_news li a').css({'font-size': parseInt(size) - 2 + 'px'});
    $('.smallText, .caption').css({'font-size': parseInt(size) - 4 + 'px'});
    $('.right_logo').css({'font-size': parseInt(size) + 14 + 'px'});

    $('.classicGridViewListtext, .selectArea, .selectArea li, .footer_name, .footer_text div, .download_list li span').css({'font-size': size + 'px'});

}

function saveFontSize(size) {
    $.cookie("fontSize", size, {path: '/'});
}
function changeSliderText(sliderId, value) {
    var position = Math.round(Math.abs((value - min) * (100 / (max - min))));
    $('#' + sliderId).prev('.sliderText').children('.range').text(position);
}

$(document).ready(function () {
    var appearance = $.cookie("specialView");
    switch (appearance) {
        case 'blackAndWhite':
            makeBlackAndWhite();
            break;
        case 'blackAndWhiteInvert':
            makeBlackAndWhiteDark();
            break;
    }

    $('.no-propagation').click(function (e) {
        e.stopPropagation();
    });

    $('.appearance .spcNormal').click(function () {
        makeNormal();
    });
    $('.appearance .spcWhiteAndBlack').click(function () {
        makeBlackAndWhite();

    });
    $('.appearance .spcDark').click(function () {
        makeBlackAndWhiteDark();
    });


    $('#fontSizer').slider({
        min: min,
        max: max,
        range: "min",
        slide: function (event, ui) {
            setFontSize(ui.value);
            changeSliderText('fontSizer', ui.value);
        },
        change: function (event, ui) {
            saveFontSize(ui.value);
        }
    });

    var fontSize = $.cookie("fontSize");
    if (typeof(fontSize) != 'undefined') {
        $("#fontSizer").slider('value', fontSize);
        setFontSize(fontSize);
        changeSliderText('fontSizer', fontSize);
    }

});