$.ajax({
    type: "POST",
    url: window.location + "api/plugin/complicationpro",
    data: JSON.stringify({command:"getURL",url:window.location}),
 	contentType: "application/json"
});