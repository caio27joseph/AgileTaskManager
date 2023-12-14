function loadContent(url, push = true) {
  const xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
      if (xhr.status === 200) {
        document.getElementById("content").innerHTML = xhr.responseText;
        if (push) {
          const pageName = url.split("/").pop().replace(".html", "");
          const newUrl =
            window.location.origin +
            (pageName === "home" ? "/" : "/" + pageName);
          window.history.pushState({ path: newUrl }, "", newUrl);
        }
        // Dynamically import and execute the JavaScript module for the page
        const moduleName = url.split("/").pop().replace(".html", "");
        import(`/js/pages/${moduleName}.js`)
          .then((module) => (module.load ? module.load() : null))
          .catch((err) =>
            console.error(`Failed to load script for ${moduleName}:`, err)
          );
      } else {
        document.getElementById("content").innerHTML = "Page not found";
      }
    }
  };
  xhr.open("GET", url, true);
  xhr.send();
}
document.addEventListener("click", function (event) {
  const element = event.target;
  if (element.tagName === "A" && element.hasAttribute("data-link")) {
    event.preventDefault();
    const page = element.getAttribute("href");
    loadContent(page);
  }
});

window.onpopstate = function (event) {
  if (event.state && event.state.path) {
    loadContent(event.state.path, false);
  }
};

document.addEventListener("DOMContentLoaded", function () {
  // Normalize the path to default to 'home' if it's empty (root path) or '/home'
  let path = window.location.pathname.replace(/^\//, "");
  path = path === "home" || path === "" ? "home" : path;
  loadContent(`pages/${path}.html`, false);
});
