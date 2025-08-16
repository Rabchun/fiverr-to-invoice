const express = require("express");
const app = express();

app.get("/", (req, res) => {
  console.log("New visit from IP:", req.ip, "Headers:", req.headers["x-forwarded-for"]);
  res.send("Hello! Your visit is logged.");
});

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Server running on port ${port}`));
