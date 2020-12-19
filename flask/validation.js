function validateForm() {
    var x = document.forms["myForm"]["revenues-twelve-months"].value;
    if (x == "") {
      alert("O campo de faturamento 12 meses deve ser preenchido");
      return false;
    }

    var x = document.forms["myForm"]["revenue-month"].value;
    if (x == "") {
      alert("O campo de faturamento deve ser preenchido");
      return false;
    }
}