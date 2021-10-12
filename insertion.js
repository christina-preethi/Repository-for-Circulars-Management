const fetch = require("node-fetch");

let circularDocument = {
    "key": "gen/21-03-2021",
    "to": "all depts",
    "from": "event coridinator",
    "title": "event details",
    "body": "There is a tech talk in chem dept seminar hall @ 12:00pm tomorrow",
    "time": "2021-03-17 17:01:00"
}

async function insertCircular(circular) {
    const response = await fetch("http://127.0.0.1:5000/api/insert", {
        method: "PUT", 
        body: JSON.stringify(circular),
        // headers: {'Content-Type': 'application/json'}
    });
    
    if (response.status == 200) {
        let json = await response.json(); // (3)
        return json;
    }
}

// insertCircular(circularDocument)
//   .then(data => {
//     console.log("respone =", data); // JSON data parsed by `data.json()` call
//   }).catch(exp => {
//       console.log(exp);
//   });


let circularBody = {
    "body":"holiday"
}

async function searchCirculars(body) {
    const response = await fetch("http://127.0.0.1:5000/api/search", {
        method: "POST", 
        body: JSON.stringify(body),
        headers: {'Content-Type': 'application/json'}
    });
    
    if (response.status == 200) {
        let json = await response.json(); // (3)
        return json;
    }
// return response;
}

searchCirculars(circularBody)
  .then(data => {
    console.log("response =", data); // JSON data parsed by `data.json()` call
  }).catch(exp => {
      console.log(exp);
  });




let circularKey = {
    "key":"gen/21-03-2021"
}

async function deleteCirculars(key) {
    const response = await fetch("http://127.0.0.1:5000/api/delete", {
        method: "DELETE", 
        body: JSON.stringify(key),
        headers: {'Content-Type': 'application/json'}
    });
    
    if (response.status == 200) {
        let json = await response.json(); // (3)
        return json;
    }
// return response;
}

// deleteCirculars(circularKey)
//   .then(data => {
//     console.log("response =", data); // JSON data parsed by `data.json()` call
//   }).catch(exp => {
//       console.log(exp);
//   });