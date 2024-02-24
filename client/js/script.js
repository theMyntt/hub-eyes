const title = $("title").text();
const localName = localStorage.getItem("userName");
const localEmail = localStorage.getItem("userEmail");

if (title.toLowerCase() === "login" || title.toLowerCase() === "signup") {
  console.log("Route /");
} else {
  if (!localName && !localEmail) {
    window.location.href = "/";
  } 
}

function loginOnSubmit() {
  const email = $("#EM_USER").val().toLowerCase();
  const password = $("#PW_USER").val();

  const postData = {
    EM_USER: email.toString(),
    PW_USER: password.toString(),
  };

  $.ajax({
    url: "http://localhost:5000/api/account/login",
    type: "POST",
    data: JSON.stringify(postData),
    contentType: "application/json",
    success: (res) => {
      if (res != "Usuário não encontrado") {
        localStorage.setItem("userName", res[0][0]);
        localStorage.setItem("userEmail", res[0][1]);
        window.location.replace("p/home");
      } else {
        alert("Usuário ou senha inválidos!");
      }
    },
    error: function (err) {
      alert(err);
    },
  });
}

$("#menu-icon").on("click", () => {
  $("#navbar").toggleClass("active");
});


$("#welcome-again-local").text(`Welcome, ${localName}`);

function logOut() {
  localStorage.clear();
  window.location.replace("/");
  return "Saiu"
}

function createOnSubmit() {
  const pw1 = $("#PW_USER").val().toString();
  const pw2 = $("#PW_USER_CONF").val().toString();

  if (pw2 === pw1) {
    const name = $("#NM_USER").val();
    const email = $("#EM_USER").val().toLowerCase();
    const password = $("#PW_USER").val();
    const cellphone = $("#TF_USER").val();
  
    const postData = {
      NM_USER: name.toString(),
      EM_USER: email.toString(),
      PW_USER: password.toString(),
      TF_USER: cellphone.toString(),
    };

    try {
      $.ajax({
        url: "http://localhost:5000/api/account/create",
        type: "POST",
        data: JSON.stringify(postData),
        contentType: "application/json",
        success: function (res) {
          if (res !== "Erro ao inserir") {
            alert("Cadastrado");

            window.location.href = "/"
          } else {
            alert("Erro interno");
          }
        },
        error: function (err) {
          alert(err);
        },
      });
    } catch (err) {
      console.error(err);
    }
  } else {
    alert("Passwords does not match.");
  }

  // window.open("/");
}
