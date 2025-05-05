// Скрытие/показ заголовка при прокрутке
$(window).on('load', function () {
    let prevScrollPos = window.pageYOffset;

    window.addEventListener('scroll', function () {
        const currentScrollPos = window.pageYOffset;
        const header = document.getElementById("header");
        const subMenu = document.getElementById("sub-menu-kurs");

        if (header && subMenu) {
            if (prevScrollPos > currentScrollPos) {
                header.style.top = "0";
                subMenu.style.top = "111px";
                subMenu.style.display = "block";
                subMenu.style.position = "visible";
                subMenu.style.boxShadow = "none";
            } else {
                header.style.top = "-111px";
                subMenu.style.top = "0";
                subMenu.style.display = "block";
                subMenu.style.position = "visible";
                subMenu.style.boxShadow = "none";
            }
        }

        prevScrollPos = currentScrollPos;
    });
});

// Инициализация аккордеона для категорий
$(document).ready(function () {
    $('.sub-menu').dcAccordion({
        eventType: "click",
        autoClose: true,
        saveState: true,
        speed: 300,
        disableLink: true,
    });
});

// Обработчик для скрытия/показа элементов по атрибуту data-toggle-id
$(document).ready(function () {
    document.addEventListener('click', function (event) {
        const id = event.target.dataset.toggleId;
        if (!id) return;

        const elem = document.getElementById(id);
        if (elem) {
            elem.hidden = !elem.hidden;
        }
    });
});

// Инициализация слайдеров с Flipbox
$(document).ready(function () {
    $('#slider-kurs').flipbox({
        autoplay: true,
        autoplayReverse: true,
        autoplayWaitDuration: 3000,
        autoplayPauseOnHover: true,
        animationDuration: 1200,
        animationEasing: 'ease',
    });

    $('#slider-kurs-mobile').flipbox({
        autoplay: true,
        autoplayReverse: true,
        autoplayWaitDuration: 3000,
        autoplayPauseOnHover: true,
        animationDuration: 1200,
        animationEasing: 'ease',
    });
});

// Инициализация WOW.js для анимаций
$(document).ready(function () {
    new WOW().init();

    // Добавление класса "pulse" для всех элементов с классом "wow"
    $(".wow").addClass("pulse");

    // Дополнительная настройка WOW.js
    const wow = new WOW({
        boxClass: 'wow',
        animateClass: 'animated',
        offset: 0,
        mobile: true,
        live: true,
    });
    wow.init();
});

// Обработчик для мобильного меню
$(document).on('click', '.bottom-fix-catalog', function (e) {
    e.preventDefault();
    $('.menu-mobile-price').toggleClass('menu-mobile-price-active');
});

// Обработчики для переключения форм обратного звонка
$(document).on('click', '#call-back-change', function () {
    $('#form-call-back').addClass('hidden');
    $('#form-call-back-change').removeClass('hidden');
});

$(document).on('click', '#call-back-change-back', function () {
    $('#form-call-back').removeClass('hidden');
    $('#form-call-back-change').addClass('hidden');
});

// Уведомление о времени работы операторов
$(document).ready(function () {
    const now = new Date();
    const currentHour = now.getHours();

    if (currentHour >= 9 && currentHour < 20) {
        $('#notificationOperatorElement').addClass('hidden');
    } else {
        $('#notificationOperatorElement').removeClass('hidden');
    }
});
