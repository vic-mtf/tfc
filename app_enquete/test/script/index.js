
const button = document.getElementById('ask');


const onAskGeoCoords = event => {
    if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition(function(position) {
          alert("Latitude : " + position.coords.latitude + "\nLongitude : " + position.coords.longitude);
        }, function(error) {
          if (error.code == error.PERMISSION_DENIED)
          alert("Vous avez désactivé la géolocalisation. Pour l'activer, veuillez aller dans les paramètres de votre navigateur.");
        });
      } else {
        alert("La géolocalisation n'est pas disponible sur ce navigateur.");
      }
      
  
};

button.addEventListener("click", onAskGeoCoords)
