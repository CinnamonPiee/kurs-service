(function ($) {
    $.fn.dcAccordion = function (options) {
        // Настройки по умолчанию
        const defaults = {
            classParent: 'dcjq-parent', // Класс для родительских элементов
            classActive: 'active', // Класс для активных ссылок
            eventType: 'click', // Тип события (click или hover)
            autoClose: true, // Автоматически закрывать другие пункты меню
            speed: 'slow', // Скорость анимации
            disableLink: true, // Отключать ссылки для родительских элементов
        };

        // Объединяем пользовательские настройки с настройками по умолчанию
        const settings = $.extend({}, defaults, options);

        // Инициализация аккордеона
        return this.each(function () {
            const $menu = $(this); // Текущий элемент меню

            // Установка начального состояния аккордеона
            setUpAccordion($menu);

            // Обработчик событий для пунктов меню
            $menu.find('li > a').on(settings.eventType, function (e) {
                const $link = $(this); // Текущая ссылка
                const $parentLi = $link.parent('li'); // Родительский элемент <li>
                const $submenu = $link.siblings('ul'); // Вложенный список <ul>

                // Отключение ссылки, если она имеет вложенное меню
                if (settings.disableLink && $submenu.length > 0) {
                    e.preventDefault();
                }

                // Если вложенное меню уже открыто, закрываем его
                if ($submenu.is(':visible')) {
                    closeMenu($submenu, $link);
                } else {
                    // Закрываем другие пункты меню, если включен autoClose
                    if (settings.autoClose) {
                        closeAllMenus($menu, $parentLi);
                    }
                    // Открываем текущее меню
                    openMenu($submenu, $link);
                }
            });
        });

        // Установка начального состояния аккордеона
        function setUpAccordion($menu) {
            $menu.find('ul').hide(); // Скрываем все вложенные списки
            $menu.find('li > a').each(function () {
                const $link = $(this);
                if ($link.siblings('ul').length > 0) {
                    $link.addClass(settings.classParent); // Добавляем класс родительским ссылкам
                }
            });
        }

        // Открытие меню
        function openMenu($submenu, $link) {
            $submenu.slideDown(settings.speed); // Анимация открытия
            $link.addClass(settings.classActive); // Добавляем класс активной ссылке
        }

        // Закрытие меню
        function closeMenu($submenu, $link) {
            $submenu.slideUp(settings.speed); // Анимация закрытия
            $link.removeClass(settings.classActive); // Убираем класс активной ссылки
        }

        // Закрытие всех меню, кроме текущего
        function closeAllMenus($menu, $currentLi) {
            $menu.find('ul').not($currentLi.find('ul')).slideUp(settings.speed); // Закрываем все вложенные списки
            $menu.find('a').not($currentLi.find('a')).removeClass(settings.classActive); // Убираем класс активных ссылок
        }
    };
})(jQuery);