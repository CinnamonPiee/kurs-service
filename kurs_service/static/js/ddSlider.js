(function ($) {
    // Основной метод плагина
    $.fn.ddslick = function (methodOrOptions) {
        if (methods[methodOrOptions]) {
            return methods[methodOrOptions].apply(this, Array.prototype.slice.call(arguments, 1));
        } else if (typeof methodOrOptions === "object" || !methodOrOptions) {
            return methods.init.apply(this, arguments);
        } else {
            $.error("Метод " + methodOrOptions + " не существует.");
        }
    };

    // Методы плагина
    const methods = {
        init: function (options) {
            const settings = $.extend({}, defaults, options);

            // Добавление CSS в <head>, если embedCSS включен
            if ($("#css-ddslick").length === 0 && settings.embedCSS) {
                $("<style>", { id: "css-ddslick", type: "text/css" }).html(css).appendTo("head");
            }

            return this.each(function () {
                const $original = $(this);
                const data = prepareData($original, settings);
                const $container = createDropdown($original, data, settings);

                // Сохранение данных в элементе
                $container.data("ddslick", {
                    settings: settings,
                    original: $original,
                    selectedIndex: -1,
                    selectedData: null,
                });

                // Установка выбранного элемента
                if (settings.defaultSelectedIndex !== null) {
                    selectItem($container, settings.defaultSelectedIndex);
                }

                // Обработчики событий
                $container.find(".dd-select").on("click", function () {
                    toggleDropdown($container);
                });

                $container.find(".dd-option").on("click", function () {
                    const index = $(this).closest("li").index();
                    selectItem($container, index);
                });

                if (settings.clickOffToClose) {
                    $(document).on("click", function (e) {
                        if (!$(e.target).closest($container).length) {
                            closeDropdown($container);
                        }
                    });
                }
            });
        },
        select: function (options) {
            return this.each(function () {
                if (options.index !== undefined) {
                    selectItem($(this), options.index);
                }
            });
        },
        open: function () {
            return this.each(function () {
                toggleDropdown($(this), true);
            });
        },
        close: function () {
            return this.each(function () {
                closeDropdown($(this));
            });
        },
        destroy: function () {
            return this.each(function () {
                const $this = $(this);
                const data = $this.data("ddslick");
                if (data) {
                    $this.removeData("ddslick").unbind().replaceWith(data.original);
                }
            });
        },
    };

    // Настройки по умолчанию
    const defaults = {
        data: [],
        width: 260,
        height: null,
        background: "#eee",
        selectText: "",
        defaultSelectedIndex: null,
        truncateDescription: true,
        imagePosition: "left",
        showSelectedHTML: true,
        clickOffToClose: true,
        embedCSS: true,
        onSelected: function () {},
    };

    // CSS для плагина
    const css = `
        .dd-select { border: 1px solid #ccc; position: relative; cursor: pointer; }
        .dd-options { display: none; position: absolute; z-index: 2000; background: #fff; }
        .dd-option { padding: 10px; cursor: pointer; }
        .dd-option:hover { background: #f3f3f3; }
    `;

    // Подготовка данных для выпадающего списка
    const prepareData = function ($original, settings) {
        const data = settings.data.length ? settings.data : [];
        $original.find("option").each(function () {
            const $option = $(this);
            data.push({
                text: $.trim($option.text()),
                value: $option.val(),
                selected: $option.is(":selected"),
                description: $option.data("description"),
                imageSrc: $option.data("imagesrc"),
            });
        });
        return data;
    };

    // Создание HTML-структуры выпадающего списка
    const createDropdown = function ($original, data, settings) {
        const $container = $("<div>", { class: "dd-container" }).css({ width: settings.width });
        const $select = $("<div>", { class: "dd-select" }).appendTo($container);
        const $options = $("<ul>", { class: "dd-options" }).appendTo($container);

        data.forEach((item, index) => {
            const $option = $("<li>").appendTo($options);
            const $link = $("<a>", { class: "dd-option" }).appendTo($option);

            if (item.imageSrc) {
                $("<img>", { class: "dd-option-image", src: item.imageSrc }).appendTo($link);
            }
            if (item.text) {
                $("<label>", { class: "dd-option-text", text: item.text }).appendTo($link);
            }
            if (item.description) {
                $("<small>", { class: "dd-option-description", text: item.description }).appendTo($link);
            }
        });

        $original.replaceWith($container);
        return $container;
    };

    // Открытие/закрытие выпадающего списка
    const toggleDropdown = function ($container, forceOpen) {
        const $options = $container.find(".dd-options");
        const isVisible = $options.is(":visible");

        if (forceOpen || !isVisible) {
            $options.slideDown("fast");
        } else {
            $options.slideUp("fast");
        }
    };

    // Закрытие выпадающего списка
    const closeDropdown = function ($container) {
        $container.find(".dd-options").slideUp("fast");
    };

    // Выбор элемента
    const selectItem = function ($container, index) {
        const data = $container.data("ddslick");
        const item = data.settings.data[index];
        data.selectedIndex = index;
        data.selectedData = item;

        if (data.settings.showSelectedHTML) {
            const $select = $container.find(".dd-select");
            $select.html(item.text);
        }

        if (typeof data.settings.onSelected === "function") {
            data.settings.onSelected(data);
        }
    };
})(jQuery);