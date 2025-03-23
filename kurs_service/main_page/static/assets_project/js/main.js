/* When the user scrolls down, hide the header. When the user scrolls up, show the header */
$(window).on('load', function () {
    var prevScrollpos = window.pageYOffset;
    window.onscroll = function () {
        var currentScrollPos = window.pageYOffset;
        if (prevScrollpos > currentScrollPos) {
            document.getElementById("header").style.top = "0";
            document.getElementById("sub-menu-kurs").style.top = "+111px";
            document.getElementById("sub-menu-kurs").style.display = "block";
            document.getElementById("sub-menu-kurs").style.position = "visible";
            document.getElementById("sub-menu-kurs").style.boxShadow = "none";
        } else {
            document.getElementById("header").style.top = "-111px";
            document.getElementById("sub-menu-kurs").style.top = "0";
            document.getElementById("sub-menu-kurs").style.display = "block";
            document.getElementById("sub-menu-kurs").style.position = "visible";
            document.getElementById("sub-menu-kurs").style.boxShadow = "none";
        }
        prevScrollpos = currentScrollPos;
    }
});

//Category accordion
$(document).ready(function () {
    $('.sub-menu').dcAccordion({
        eventType: "click",
        autoClose: true,
        saveState: true,
        speed: 300,
        disableLink: true,
    });
});

$(document).ready(function () {
    document.addEventListener('click', function (event) {
        let id = event.target.dataset.toggleId;
        if (!id) return;
        let elem = document.getElementById(id);
        elem.hidden = !elem.hidden;
    });
});
//slider
$(document).ready(function () {
    $('#slider-kurs').flipbox({
        autoplay: true,// default: false
        autoplayReverse: true,
        autoplayWaitDuration: 3000,
        autoplayPauseOnHover: true,
        animationDuration: 1200,
        animationEasing: 'ease'
    })

    $('#slider-kurs-mobile').flipbox({
        autoplay: true,// default: false
        autoplayReverse: true,
        autoplayWaitDuration: 3000,
        autoplayPauseOnHover: true,
        animationDuration: 1200,
        animationEasing: 'ease'
    })
});

//wow animation
$(document).ready(function () {
    new WOW().init();
    $(".wow").addClass("pulse");

    wow = new WOW({
        boxClass: 'wow', // default
        animateClass: 'animated', // default
        offset: 0, // default
        mobile: true, // default
        live: true // default
    });
});

$(document).on('click', '.bottom-fix-catalog', function (e) {
    e.preventDefault();
    $('.menu-mobile-price').toggleClass('menu-mobile-price-active');
})

$(document).on('click', '#call-back-change', function () {
    $('#form-call-back').addClass('hidden');
    $('#form-call-back-change').removeClass('hidden');
})

$(document).on('click', '#call-back-change-back', function () {
    $('#form-call-back').removeClass('hidden');
    $('#form-call-back-change').addClass('hidden');
})

$(document).ready(function () {
        var nowTimeForOperator = new Date();
        var nowTimeForOperatorHour = nowTimeForOperator.getHours()
        if (nowTimeForOperatorHour >= 9 && nowTimeForOperatorHour < 20) {
            $('#notificationOperatorElement').addClass('hidden');
        } else {
            $('#notificationOperatorElement').removeClass('hidden');
        }
    }
);
