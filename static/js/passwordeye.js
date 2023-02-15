function pushHideButton() {
    const txtPass = document.getElementById("textPassword");
    const btnEye = document.getElementById("buttonEye");
    if (txtPass.type === "text") {
      txtPass.type = "password";
      btnEye.className = "fa fa-eye";
    } else {
      txtPass.type = "text";
      btnEye.className = "fa fa-eye-slash";
    }
  }