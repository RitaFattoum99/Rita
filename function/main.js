//Start Count Function
    let counter = 0;
    function count() {
        counter++;
        document.querySelector("#count").innerHTML = counter;
    }
    document.querySelector("#btnCount").onclick = count;
    //End Count Function

    //Start Change h1 innerHTML Function
    document.querySelector("#btnChange").onclick = function () {
        let change = document.querySelector("#h1Hello");
        if (change.innerHTML === "Hello") {
            change.innerHTML = "GoodBye"
        } else {
            change.innerHTML = "Hello"
        }
    }
    //End Change h1 innerHTML Function

    //Start Change Color h1 By Select Function
    document.querySelector("#selectColor").onchange = function () {
        document.querySelector("#h1Select").style.color = this.value;
    }
    //End Change Color h1 By Select Function

    //  Start Change Color h1 By Button Function
    document.querySelectorAll("button").forEach(function (b) {
        b.onclick = function () {
            document.querySelector("#h1Button").style.color = b.dataset.color;
        }
    })
    //  End Change Color h1 By Button Function

   

