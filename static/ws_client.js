let socket = new WebSocket("ws://localhost:8888/ws");
let answers = document.getElementById('answers');

socket.onopen = function(e) {
  console.log("connection opened")
};

socket.onclose = function(e) {
  console.log("connection closed")
};

socket.onmessage = function (e) {
  let decodedAnswer = JSON.parse(e.data);
  let answerStub = document.getElementById(Object.keys(decodedAnswer)[0]);
  answerStub.innerHTML = answerStub.innerHTML.replace(/\.\.\./g, Object.values(decodedAnswer)[0]);
};


function createAnswerStub(number) {
  let newAnswer = document.createElement('li');
  newAnswer.innerHTML = "The answer for number " + number + " is ...";
  newAnswer.id = number;
  answers.appendChild(newAnswer);
}

function getFibonacciNumber() {
  let number = document.getElementById("number").value;
  if (document.getElementById(number)) {
    alert("fibonacci for number " + number + " already calculated")
  } else {
    createAnswerStub(number);
    if (socket.readyState === socket.OPEN) {
      console.log("sending request for " + number);
      socket.send(number);
    } else {
      console.error("connection not ready")
    }
  }
}