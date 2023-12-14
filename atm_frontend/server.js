const express = require("express");
const path = require("path");
const app = express();

const PORT = process.env.PORT || 3000;

app.use(express.static(path.join(__dirname, "public")));

app.get("*", (req, res) => {
  // If the request is for a file, serve it as is
  if (req.url.match(/\.(html|css|js|png|jpg)$/)) {
    res.sendFile(path.resolve(__dirname, "public", req.url));
  } else {
    // For everything else, serve index.html and let the client-side handle the routing
    res.sendFile(path.resolve(__dirname, "public", "index.html"));
  }
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});