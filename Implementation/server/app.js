import express from "express";
import bodyParser from "body-parser";
const app = express();
const port = 3000;
app.use(bodyParser.json());
import detectionsRoute from "./routes/detections.js";

app.use("/detections", detectionsRoute);
app.get("/", (req, res) => {
  res.send("Welcome to LabMon");
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
