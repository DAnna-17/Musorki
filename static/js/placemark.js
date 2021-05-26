ymaps.ready(init);

function init() {
    var myMap = new ymaps.Map("map", {
            center: [55.76, 37.64],
            zoom: 10
        }, {
            searchControlProvider: 'yandex#search'
        })



    myMap.geoObjects
 .add(new ymaps.Placemark([56.207537, 37.413779 ], {
                balloonContent: 'Организация: ГУП «Экотехпром» , телефон: 8-499-238-49-34 '
            }, {
                iconColor: '#fffff'
            })) .add(new ymaps.Placemark([55.935828, 43.089714 ], {
                balloonContent: 'Организация: МУП «Истринский полигон ТБО» , телефон: 8-495-994-42-92 '
            }, {
                iconColor: '#fffff'
            })) .add(new ymaps.Placemark([1 ], {
                balloonContent: 'Организация: 11 , телефон: 1 '
            }, {
                iconColor: '#fffff'
            })) .add(new ymaps.Placemark([ ], {
                balloonContent: 'Организация:  , телефон:  '
            }, {
                iconColor: '#fffff'
            })) .add(new ymaps.Placemark([ ], {
                balloonContent: 'Организация:  , телефон:  '
            }, {
                iconColor: '#fffff'
            }))}