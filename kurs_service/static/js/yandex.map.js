document.addEventListener('DOMContentLoaded', function () {
    if (document.getElementById('map')) {
        ymaps.ready(init);
    }

    function init() {
        var myMap = new ymaps.Map('map', {
            center: [55.751446, 37.618779],
            zoom: 11,
            controls: ['smallMapDefaultSet']
        }, {
            searchControlProvider: 'yandex#search'
        });

        // Добавление управления пробками
        var trafficControl = new ymaps.control.TrafficControl({
            state: {
                providerKey: 'traffic#actual',
                trafficShown: false
            }
        });
        myMap.controls.add(trafficControl);
        trafficControl.getProvider('traffic#actual').state.set('infoLayerShown', true);

        // Добавление метки
        var placemark = new ymaps.Placemark([55.799178, 37.644773], {
            iconContent: 'OOO "КУРС"',
            balloonContentHeader: '<a href="/" class="map-link">OOO "КУРС"</a><br>' +
                '<span class="map-link-description">Прозрачный автосервис<br/>у нас один курс.</span>',
            balloonContentBody: '<img src="/media/img-logo/sports-car-auto.png" height="100" width="150"> <br/> ' +
                '<a href="tel:8(800)444-13-18" class="map-link-phone">8 (910) 448-45-06</a><br/>' +
                '<b>Время работы</b> <br/> С 9:00 до 20:00',
            balloonContentFooter: 'Информация предоставлена:<br/>OOO "КУРС"',
            hintContent: 'OOO "КУРС"'
        }, {
            preset: "islands#redStretchyIcon",
            balloonPanelMaxMapArea: 0
        });

        myMap.geoObjects.add(placemark);
        placemark.balloon.open();
    }

});