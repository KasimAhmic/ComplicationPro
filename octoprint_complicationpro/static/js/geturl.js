$.ajax({
    type: "POST",
    url: "http://0.0.0.0:5000/api/plugin/complicationpro",
    data: JSON.stringify({command:"getURL",url:window.location}),
 	contentType: "application/json"
});