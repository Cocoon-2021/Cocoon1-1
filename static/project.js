function functions() {   
    var p = document.getElementById("psw").value;
    var m=document.getElementById("pswre").value;
    if (p != m) {
        alert("Passwords do not match.");
        return false;
    }
    return true;

}
 
