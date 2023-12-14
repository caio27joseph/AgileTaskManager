export function load() {
  $(document).ready(function () {
    $("#registerForm").on("submit", function (event) {
      event.preventDefault();

      var userData = {
        username: $("#username").val(),
        email: $("#email").val(),
        password: $("#password").val(),
        confirmPassword: $("#confirmPassword").val(),
      };

      // Basic validation for password match
      if (userData.password !== userData.confirmPassword) {
        success;
        alert("Passwords do not match.");
        return;
      }

      $.ajax({
        url: "http://127.0.0.1:8000/api/register/",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(userData),
        success: function (response) {
          // Handle successful response
          if (response.username) {
            window.location.href = "/login"; // Redirect to login on successful registration
          } else {
            console.error("Registration failed: " + response.message);
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
