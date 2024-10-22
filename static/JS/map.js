let map;
function initAutocomplete() {
    // Initialize Google Maps Autocomplete for address input
    const addressInput = document.getElementById('address');
    const autocomplete = new google.maps.places.Autocomplete(addressInput);
    autocomplete.addListener('place_changed', function () {
        const place = autocomplete.getPlace();
        if (place.geometry) {
            document.getElementById('latitude').value = place.geometry.location.lat();
            document.getElementById('longitude').value = place.geometry.location.lng();
        }
    });
}

function initMap() {
    // Initialize a new Google Map for property detail view
    const propertyLat = parseFloat('{{ property.latitude }}');
    const propertyLng = parseFloat('{{ property.longitude }}');
    const propertyLocation = { lat: propertyLat, lng: propertyLng };

    map = new google.maps.Map(document.getElementById('map'), {
        center: propertyLocation,
        zoom: 15,
    });

    const marker = new google.maps.Marker({
        position: propertyLocation,
        map: map,
        title: '{{ property.name }}',
    });
}

