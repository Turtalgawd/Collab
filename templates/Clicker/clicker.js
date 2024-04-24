var bread = 0
var breadPerSecond = 0
var breadPerClick = 1
var ovens = 0
var ovenCost = 20
var bakers = 0
var bakerCost = 10
var trees = 0
var treeCost = 200
var boats = 0
var boatCost = 1500
var bakerbots = 0
var bakerbotCost = 12000

function update() {
    bread += Math.round(breadPerSecond/50*100)/100;
    document.getElementById("showBread").innerText = Math.ceil(bread);
    document.getElementById("showBreadPerSecond").innerText = breadPerSecond;
    document.getElementById("showBreadPerClick").innerText = breadPerClick;
}

function time() {
    setInterval(update, 20);
}

function increment() {
    bread += breadPerClick;
}

function buyOven() {
    if (bread >= ovenCost) {
        ovens += 1;
        bread -= ovenCost;
        ovenCost *= 1.50;
        breadPerClick += 1;
        document.getElementById("showOvenCost").innerText = Math.round(ovenCost);
    }
}

function buyBaker() {
    if (bread >= bakerCost) {
        bakers += 1;
        bread -= bakerCost;
        bakerCost *= 1.25;
        breadPerSecond += 1;
        document.getElementById("showBakerCost").innerText = Math.round(bakerCost);
    }
}

function buyTree() {
    if (bread >= treeCost) {
        trees += 1;
        bread -= treeCost;
        treeCost *= 1.25;
        breadPerSecond += 10;
        document.getElementById("showTreeCost").innerText = Math.round(treeCost);
    }
}

function buyBoat() {
    if (bread >= boatCost) {
        boats += 1;
        bread -= boatCost;
        boatCost *= 1.25;
        breadPerSecond += 50;
        document.getElementById("showBoatCost").innerText = Math.round(boatCost);
    }
}

function buyBakerbot() {
    if (bread >= bakerbotCost) {
        bakerbots += 1;
        bread -= bakerbotCost;
        bakerbotCost *= 1.25;
        breadPerSecond += 300;
        document.getElementById("showBakerbotCost").innerText = Math.round(bakerbotCost);
    }
}

time()



