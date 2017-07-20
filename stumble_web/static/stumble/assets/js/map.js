/**
 * Created by zacharydipasquale on 7/17/17.
 */




function initMap() {

    var map = L.map('map', {
        minZoom: 5
    }).setView([42.35, -71.08], 13);

    var street = L.tileLayer('https://api.mapbox.com/styles/v1/zdepo/cj5aby3930f942rqw45hrltlg/tiles/256/{z}/{x}/{y}?access_token=' +
        'sk.eyJ1IjoiemRlcG8iLCJhIjoiY2o1YWQxdHRwMGpzeTMzcDFibGcza3N0bSJ9.z78hGqHKlqX5Vtgus_N4vA').addTo(map);
    var sat = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v10/tiles/256/{z}/{x}/{y}?access_token=' +
        'sk.eyJ1IjoiemRlcG8iLCJhIjoiY2o1YWQxdHRwMGpzeTMzcDFibGcza3N0bSJ9.z78hGqHKlqX5Vtgus_N4vA');
    var dark = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/dark-v9/tiles/256/{z}/{x}/{y}?access_token=' +
        'sk.eyJ1IjoiemRlcG8iLCJhIjoiY2o1YWQxdHRwMGpzeTMzcDFibGcza3N0bSJ9.z78hGqHKlqX5Vtgus_N4vA');
    var baseMaps = {
        "Street": street,
        "Satellite": sat,
        "Dark": dark
    };
    L.control.layers(baseMaps).addTo(map);
    L.GeoIP.centerMapOnPosition(map, 15);

}

initMap();




