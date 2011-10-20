/*
 * User: bteam
 * Date: 20.10.11
 * Time: 10:48
 */
dojo.addOnLoad(function() {
    var element = document.getElementById("map");
    var zavod = new google.maps.LatLng(59.34506, 56.91378)
    var mapTypeIds = [];
    for (var type in google.maps.MapTypeId) {
        mapTypeIds.push(google.maps.MapTypeId[type]);
    }
    mapTypeIds.push("OSM");

    var map = new google.maps.Map(element, {
        center: zavod,
        zoom: 14,
        mapTypeId: "OSM",
        mapTypeControlOptions: {
            mapTypeIds: mapTypeIds
        }
    });

    map.mapTypes.set("OSM", new google.maps.ImageMapType({
        getTileUrl: function(coord, zoom) {
            return "http://tile.openstreetmap.org/" + zoom + "/" + coord.x + "/" + coord.y + ".png";
        },
        tileSize: new google.maps.Size(256, 256),
        name: "OpenStreetMap",
        maxZoom: 18
    }));
    
    var marker = new google.maps.Marker({
        position: zavod,
        title:"Березниковский кирпичный завод"
    });
    marker.setMap(map);

});