import express from "express";
const router = express.Router();

router.get("/", (req, res) => {
  res.send("Detections");
});
router.post("/", (req, res) => {
  console.log(req.body);
  res.send(req.body);
});

export default router;
