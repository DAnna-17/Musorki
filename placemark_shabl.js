ymaps.ready(init);

function init() {
    var myMap = new ymaps.Map("map", {
            center: [55.76, 37.64],
            zoom: 10
        }, {
            searchControlProvider: 'yandex#search'
        }),



    myMap.geoObjects
 .add(new ymaps.Placemark([1, 2 ], {
            balloonContent: 'Организация:2 , телефон: 3 '
        }, {
            iconColor: '#fffff'
        }))}