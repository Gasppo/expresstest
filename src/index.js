//import { getEmployes } from './queries';
import express from "express";
import {
  deleteEmployees,
  getEmployes,
  getEmployesByID,
  patchEmployees,
  postEmployees,
} from "./queries.js";
const app = express();
const port = 5000;

app.use(express.json());

//GET ALL
app.get("/employees", getEmployes);

//GET ID
app.get("/employees/:id", getEmployesByID);

//DELETE
app.delete("/employees/:id", deleteEmployees);

//POST
app.post("/employees", postEmployees);

//PATCH
app.patch("/employees/:id", patchEmployees);

app.get("/", (req, res) => {});

app.listen(port, () => {
  console.log(`App listening at http://localhost:${port}`);
});
