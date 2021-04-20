var func = function() {
        var x = document.getElementsByName("operation");
        var num1 = parseInt(document.getElementById("num1").value);
        var num2 = parseInt(document.getElementById("num2").value);

        if (x[0].checked) {
            var sum1 = num1 + num2;
            document.getElementById("name").innerHTML = sum1;

        } else if (x[1].checked) {
            var diff = num1 - num2
            document.getElementById("name").innerHTML = diff;
        }