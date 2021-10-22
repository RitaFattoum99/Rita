    //  Start Calculate BMI 
    function calc() {
        let height = document.querySelector("#height").value;
        let weight = document.querySelector("#weight").value;
        let result = document.querySelector("#result");
        let img = document.createElement("img");
        result.value = ((weight * 10000) / (height * height)).toFixed(2);
        document.querySelector("#result").innerHTML = Math.round(result.value);

        // Underweight
        if (result.value <= 18.5) {
            document.querySelector("#Presult").innerHTML = "Underweight";
            img.setAttribute("src", "/photo/under.png");
            document.querySelector("#imageBMI").appendChild(img);
        }
        //  Normal
        else if (result.value >= 18.5 && result.value <= 24.9) {
            document.querySelector("#Presult").innerHTML = "Normal";
            img.setAttribute("src", "/photo/normal.png");
            document.querySelector("#imageBMI").appendChild(img);
        }
        // Overweight
        else if (result.value >= 25 && result.value <= 29.9) {
            document.querySelector("#Presult").innerHTML = "Overweight";
            img.setAttribute("src", "/photo/obes1.png");
            document.querySelector("#imageBMI").appendChild(img);
        }
        // Obese
        else {
            document.querySelector("#Presult").innerHTML = "Obese";
            img.setAttribute("src", "/photo/obes2.png");
            document.querySelector("#imageBMI").appendChild(img);
        }
    };
    document.querySelector("#click").onclick = calc;
    //  End Calculate BMI 
