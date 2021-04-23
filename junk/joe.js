function joe() {
    var addcheck = document.getElementById("add").checked;
    var subcheck = document.getElementById("sub").checked;
    var num1 = parseInt(document.getElementById("num1").value);
    var num2 = parseInt(document.getElementById("num2").value);


    if (addcheck) {
        var sum = num1 + num2
        document.getElementById("p1").innerHTML = sum;
    }
    if (subcheck) {
        var diff = num1 - num2
        document.getElementById("p1").innerHTML = diff;
    }


}