$(document).ready(function () {

    ymaps.ready(init);

    function init() {
        var myMap = new ymaps.Map('map', {
            center: [55.751446, 37.618779],
            zoom: 11,
            controls: ['smallMapDefaultSet']
        }, {
            searchControlProvider: 'yandex#search'
        });

        var trafficControl = new ymaps.control.TrafficControl({ state: {
                // Now traffic jams are displayed.
                providerKey: 'traffic#actual',
                // We start immediately showing traffic jams on the map.
                trafficShown: false
            }});
        // Let's add a control to the map.
        myMap.controls.add(trafficControl);
        // Get a link to the "Now" traffic jam provider and turn on the display of info points.
        trafficControl.getProvider('traffic#actual').state.set('infoLayerShown', true);

        var placemark = new ymaps.Placemark([55.799178, 37.644773], {
            iconContent: 'OOO "КУРС"',
            // Let's set the content of the balloon header.
            balloonContentHeader: '<a href = "/" class="map-link">OOO "КУРС"</a><br>' +
                '<span class="map-link-description">Прозрачный автосервис<br/>у нас один курс.</span>',
            // Let's set the content of the main part of the balloon.
            balloonContentBody: '<img src="static/assets_project/img/imgLogo/sports-car-auto.png" height="100" width="150"> <br/> ' +
                '<a href="tel:8(800)444-13-18" class="map-link-phone">8 (910) 448-45-06</a><br/>' +
                '<b>Время работы</b> <br/> С 9:00 до 20:00',
            // Let's set the content of the bottom part of the balloon.
            balloonContentFooter: 'Информация предоставлена:<br/>OOO "КУРС"',
            // Let's set the content of the tooltip.
            hintContent: 'OOO "КУРС"'
        }, {
            preset: "islands#redStretchyIcon",
            balloonPanelMaxMapArea: 0
        });
        // Let's add a label to the map.
        myMap.geoObjects.add(placemark);
        // Let's open the balloon on the label.
        placemark.balloon.open();
    }

});