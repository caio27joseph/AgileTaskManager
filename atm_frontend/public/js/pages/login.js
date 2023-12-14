// login.js
export function load() {
  $(document).ready(function () {
    $("#loginForm").on("submit", function (event) {
      event.preventDefault();

      console.log("Login form submitted");

      var userData = {
        username: $("#username").val(),
        password: $("#password").val(),
      };

      $.ajax({
        url: "http://127.0.0.1:8000/api/login/",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(userData),
        success: function (response) {
          if (response.token) {
            sessionStorage.setItem("token", response.token);
            window.location.href = "/profile";
          } else {
            alert("Login failed: " + response.message);
          }
        },
        error: function (xhr, status, error) {
          // Handle errors
          console.error("An error occurred: " + error);
        },
      });
    });
  });
}
