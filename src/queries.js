import axios from "axios";

const SERVER_URL = "localhost:3000";

export function getEmployes(req, res) {
  axios
    .get(`http://${SERVER_URL}/employees`)
    .then((response) => {
      console.log(response.data);
      res.json(response.data);
    })
    .catch((err) => {
      console.log(err);
      res.status(500).send(err);
    });
}

export function getEmployesByID(req, res) {
  axios
    .get(`http://${SERVER_URL}/employees/${req.params.id}`)
    .then((response) => {
      console.log(`ID: ${req.params.id} successfuly found`);
      res.status(200).json(response.data);
    })
    .catch((err) => {
      console.log(`ID: ${req.params.id} not found`);
      res.status(500).send(err);
    });
}

export function patchEmployees(req, res) {
  const body = req.body;
  axios
    .patch(`http://${SERVER_URL}/employees/${req.params.id}`, body)
    .then((response) => {
      console.log(response.data);
      res.status(201).json(response.data);
    })
    .catch((err) => {
      console.log(err);
      res.status(500).send(err);
    });
}

export function deleteEmployees(req, res) {
  axios
    .delete(`http://${SERVER_URL}/employees/${req.params.id}`)
    .then((response) => {
      console.log(`Deleted ID: ${req.params.id}`);
      res.status(200).json(response.data);
    })
    .catch((err) => {
      console.log(`Error deleting ID: ${req.params.id}`);
      res.status(404).send(err);
    });
}

export function postEmployees(req, res) {
  const body = req.body;
  axios
    .post(`http://${SERVER_URL}/employees`, body)
    .then((response) => {
      console.log(`ID: ${response.data.name} successfuly created`);
      res.status(201).json(response.data);
    })
    .catch((err) => {
      res.status(404).send(err);
    });
}
