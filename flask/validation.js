function validateForm() {
    var x = document.forms["myForm"]["projectFilePath"].value;
    if (x == "") {
      alert("Name must be filled out");
      return false;
    }

    var x = document.forms["myForm"]["projectFilePath2"].value;
    if (x == "") {
      alert("Name must be filled out");
      return false;
    }
}