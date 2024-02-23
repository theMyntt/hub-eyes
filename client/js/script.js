const title = $("title").text();

if (title.toLowerCase() === "login") {
  console.log("Route /");
} else {
  const localName = localStorage.getItem("userName");
  const localEmail = localStorage.getItem("userEmail");

  if (!localName && !localEmail) window.location.href = "/";
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
