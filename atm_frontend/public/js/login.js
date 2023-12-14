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
        url: "/login",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(userData),
        success: function (response) {
          // Handle successful response
          if (response.success) {
            window.location.href = "/dashboard"; // Redirect on success
          } else {
            alert("Login failed: " + response.message);
          }
        },
        error: function (xhr, status, error) {
          // Handle errors
          alert("An error occurred: " + error);
        },
      });
    });
  });
}
