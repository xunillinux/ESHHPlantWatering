$( document ).ready(function() {

    function createHumidityChart(){
        
        $.get("/app/GetHumidityValues", function(data){

            //convert JSON data to arrays
            var jsonData = $.parseJSON(data);
            var humidityValues = [];
            $.each(jsonData, function(idx, obj){
                humidityValues.push(obj.humidity_value);
            });
            humidityValues = getLastSevenElements(humidityValues);
            var timeStamps = [];
            $.each(jsonData, function(idx, obj){
                timeStamps.push(obj.measure_date);
            });
            timeStamps = getLastSevenElements(timeStamps);

            //create Chart
            var chartElement = $("#humidityChart");
            createChart(chartElement, timeStamps, humidityValues, "Humidity"); 

        }).fail(function(){
            alert("could not get humidity values data");
        });

    }

    function createBrightnessChart(){
        $.get("/app/GetBrightnessValues", function(data){

            //convert JSON data to arrays
            var jsonData = $.parseJSON(data);
            var brightnessValues = [];
            $.each(jsonData, function(idx, obj){
                brightnessValues.push(obj.brightness_value);
            });
            brightnessValues = getLastSevenElements(brightnessValues);
            var timeStamps = [];
            $.each(jsonData, function(idx, obj){
                timeStamps.push(obj.measure_date);
            });
            timeStamps = getLastSevenElements(timeStamps);

            //create Chart
            var chartElement = $("#brightnessChart");
            createChart(chartElement, timeStamps, brightnessValues, "Brightness"); 

        }).fail(function(){
            alert("could not get brightness values data");
        });
    }

    function createTempChart(){
        $.get("/app/GetTemperatureValues", function(data){

            //convert JSON data to arrays
            var jsonData = $.parseJSON(data);
            var temperatureValues = [];
            $.each(jsonData, function(idx, obj){
                temperatureValues.push(obj.temperature_value);
            });
            temperatureValues = getLastSevenElements(temperatureValues);
            var timeStamps = [];
            $.each(jsonData, function(idx, obj){
                timeStamps.push(obj.measure_date);
            });
            timeStamps = getLastSevenElements(timeStamps);

            //create Chart
            var chartElement = $("#tempChart");
            createChart(chartElement, timeStamps, temperatureValues, "Temperature"); 

        }).fail(function(){
            alert("could not get brightness values data");
        });
    }

    function loadImages(){
        $.get("/app/GetPhotos", function(data){

            //convert JSON data to arrays
            var jsonData = $.parseJSON(data);
            var photoPaths = [];
            $.each(jsonData, function(idx, obj){
                photoPaths.push(obj.photo_path);
            });
            photoPaths = getLastSevenElements(photoPaths);
            var timeStamps = [];
            $.each(jsonData, function(idx, obj){
                timeStamps.push(obj.measure_date);
            });
            timeStamps = getLastSevenElements(timeStamps);
            //loadImages
            $('#images .plantphoto').each(function(idx, obj) {
                if(idx < photoPaths.length){
                    d = new Date();
                    $(this).attr('src', photoPaths[idx]);
                }
            });

        }).fail(function(){
            alert("could not get photo path data");
        });
    }

    function loadSettings(){
        $.get("/app/GetSettings", function(data){

            var jsonData = $.parseJSON(data);
            var humidityThreshold = jsonData[0].humidity_threshhold;
            var pumpWaterAmount = jsonData[0].pump_water_amount;
            $("#humidityInput").val(humidityThreshold);
            $("#waterInput").val(pumpWaterAmount);

        }).fail(function(){
            alert("could not get settings data");
        });
    }

    function activatePump(){

    }

    function createChart(chartElement, dataLabels, dataY, label){
        new Chart(chartElement, {
            type: 'line',
            data: {
                labels: dataLabels,
                datasets: [
                { 
                    data: dataY,
                    label: label
                }
                ]
            },
            });
    }

    function getLastSevenElements(array){
        return (array.length >= 7) ? array.slice(array.length-8, array.length-1) : array;
    }

    function getLastThreeElements(array){
        return (array.length >= 7) ? array.slice(array.length-4, array.length-1) : array;
    }

    $("#settingsForm").submit(function(e) {

        e.preventDefault();
        var form = $(this);
        var url = form.attr('action');
    
        $.ajax({
            type: "POST",
            url: url,
            data: form.serialize(),
            success: function(data)
            {
                alert(data);
            }
        });
    
    });
    
    createHumidityChart();
    createBrightnessChart();
    createTempChart();
    loadImages();
    loadSettings();

});
