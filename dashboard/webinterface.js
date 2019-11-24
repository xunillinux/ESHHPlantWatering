//js for webinterface
// Our labels along the x-axis
var days = [1, 2, 3, 4, 5, 6, 7];
// For drawing the lines
var humidity = [50, 56, 52, 40, 60, 70, 77];
var light = [3, 5, 4, 7, 6, 4, 3];
var temperature = [20, 16, 15, 18, 22, 22, 23];


window.onload = function(){
    
    var ctx = document.getElementById("humidityChart");
    var ctx = document.getElementById("lightChart");
    var ctx = document.getElementById("tempChart");
    var humidityChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: days,
        datasets: [
        { 
            data: humidity,
            label: "Humidity"
        }
        ]
    },
    });
/*
    var lightChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: days,
            datasets: [
            { 
                data: light,
                label: "Light"
            }
            ]
        }
        });

    var tempChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: days,
            datasets: [
            { 
                data: temperature,
                label: "Temperature"
            }
            ]
        }
        });*/
}

function getHumidityValues(){

}

function getBrightnessValues(){

}
function getTempValues(){

}
function getImages(){

}
function activatePump(){

}
function getHumidityThreshold(){

}

function setHumidityThreshold(){

}

function getPumpWateramount(){

}

function setPumpWateramount(){

}


