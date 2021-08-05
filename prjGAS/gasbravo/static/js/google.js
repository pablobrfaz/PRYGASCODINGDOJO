let map;
let marker;
function initMap() 
{
    map = new google.maps.Map(document.getElementById("mapa"), {
    center: { lat: -34.397, lng: 150.644 },
    zoom: 15,
    });
    
    infoWindow = new google.maps.InfoWindow();
    const locationButton = document.createElement("button");
    locationButton.textContent = "Ir a mi dirección actual";
    locationButton.classList.add("custom-map-control-button");
    map.controls[google.maps.ControlPosition.TOP_CENTER].push(locationButton);
    marker = new google.maps.Marker();
    locationButton.addEventListener("click", () => {
    // Try HTML5 geolocation.
    if (navigator.geolocation) 
    {
        navigator.geolocation.getCurrentPosition((position) => 
        {
            const pos = 
            {
                lat: position.coords.latitude,
                lng: position.coords.longitude,
            };
            map.setCenter(pos);
            marker.setPosition(pos);
            marker.setMap(map);
            marker.setDraggable(true);
            google.maps.event.addListener(marker, 'position_changed', function(){
                getMarkerCoords(marker);
                });
        }
            ,() => { 
                handleLocationError(true, infoWindow, map.getCenter());}
        
        );
        

        function getMarkerCoords(marker)
        {   
            var markerCoords = marker.getPosition();
            console.log(markerCoords.lat()+ ' ' +markerCoords.lng());
            $('#id_lat').val( markerCoords.lat());
            $('#id_lng').val( markerCoords.lng());

        }
    } 
    else 
    {
      // Browser doesn't support Geolocation
    handleLocationError(false, infoWindow, map.getCenter());
    }
});
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(pos);
  infoWindow.setContent(
    browserHasGeolocation
      ? "Error: The Geolocation service failed."
      : "Error: Your browser doesn't support geolocation."
  );
  infoWindow.open(map);
}