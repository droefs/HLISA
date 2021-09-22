function sendMessage(message) {
    const f = new Request("http://localhost:8000/", {
          method: 'POST',
          body: JSON.stringify({
            message: message
          }),
          headers: {
              'Content-Type': 'application/json'
          }
      });
      fetch(f);
  }

function trackCursor(e) {
  // console.log("A mousemove ended at: (" + e.clientX + ", " + e.clientY + ")");
  $('#cursor').css({'left': (e.pageX-10) + "px"});
  $('#cursor').css({'top': (e.pageY-10) + "px"});
}

document.addEventListener("mousemove", function(e) {trackCursor(e)});

// New page cursor location test

$('#button1').on("mousedown", function() {newPageCursorlocationTest(event)});

function newPageCursorlocationTest(event) {
    sendMessage("Test 4: succeeded (New page cursor location test)");
}

$('#button2').on("mousedown", function() {newPageCursorlocationTestFail(event)});

function newPageCursorlocationTestFail(event) {
    sendMessage("Test 4: failed (New page cursor location test)");
}

// Drag and drop test

$('#draggable_element').on("dragstart", function() {event.dataTransfer.setData("data", event.target.id);});

$('#drag_endpoint').on("dragover", function() {event.preventDefault();});
$('#drag_endpoint').on("drop", function() {event.preventDefault(); event.target.appendChild(document.getElementById(event.dataTransfer.getData("data"))); sendMessage("Test 5: succeeded (Drag and drop test)");});

// Move to element with offset test

function elementWithOffsetTest(event) {
  let rect = document.getElementById("element_with_offset").getBoundingClientRect();
  let left_relative = rect['left'] - window.pageXOffset + 12;
  let top_relative = rect['top'] - window.pageYOffset + 34;
  if (event.clientX == left_relative && event.clientY == top_relative) {
    sendMessage("Test 6: succeeded (Element with offset test)");
  }
  else {
    sendMessage("Test 6: failed (Element with offset test)");
    console.log("Target: (" + left_relative + ", " + top_relative + ", clicked on: (" + event.clientX + ", " + event.clientY + ")");
  }
}

$('#element_with_offset').on("click", function() {elementWithOffsetTest(event)});

// Double click test

let suspiciousDoubleclick = false;
let mouseDoubleclickMousedown = 0;
let mouseDoubleclickMouseup = 0;
let previousMouseDoubleclickMousedown = 0;

function checkDwellTime() {
  console.log(performance.now() + " mouseup");
  previousMouseDoubleclickMouseup = mouseDoubleclickMouseup;
  mouseDoubleclickMouseup = performance.now();
  if (mouseDoubleclickMouseup - mouseDoubleclickMousedown < 20) {
    suspiciousDoubleclick = true;
    }
  if (mouseDoubleclickMousedown - previousMouseDoubleclickMouseup < 10) {
    suspiciousDoubleclick = true
  }

}

function storeMouseDown() {
  console.log(performance.now() + " mousedown");
  mouseDoubleclickMousedown = performance.now();
}

function doubleClickTest() {
  if (suspiciousDoubleclick) {
    sendMessage("Test 7: failed (Double click test) (This happens by chance once in approximately every 25 double clicks due to the random distribution)");
    suspiciousDoubleclick = false;
  } else {
    sendMessage("Test 7: succeeded (Double click test)");
  }
}

$('#double_click').on("dblclick", function() {doubleClickTest();});

$('#double_click').on("mousedown", function() {storeMouseDown();});
$('#double_click').on("mouseup", function() {checkDwellTime();});

// Drag and drop with offset test

$('#draggable_element_offset').on("dragstart", function() {event.dataTransfer.setData("data2", event.target.id);});

$('#drag_endpoint_offset').on("dragover", function() {event.preventDefault();});
$('#drag_endpoint_offset').on("drop", function() {event.preventDefault(); event.target.appendChild(document.getElementById(event.dataTransfer.getData("data2"))); sendMessage("Test 8: succeeded (Drag and drop with offset test)");});

// Send keys to element test

let keydownTime = performance.now();
let keyupTime = performance.now();
let keySendToElementFailure = false;
let keySendToElementCount = 0;

function flightTimeTest() {
  keydownTime = performance.now();
  if (keydownTime - keyupTime < 5) {
    keySendToElementFailure = false;
    sendMessage("Test 9: failed (Send keys to element test) (This happens by chance once in approximately every 25 keys send due to the random distribution)");
  }
}

function dwellTimeTest() {
  keyupTime = performance.now();
  if (keyupTime - keydownTime < 5) {
    keySendToElementFailure = false;
    sendMessage("Test 10: failed (Send keys to element test) (This happens by chance once in approximately every 25 keys send due to the random distribution)");
  }
  keySendToElementCount++;
  if (keySendToElementCount > 8 && !keySendToElementFailure) {
    sendMessage("Test 9, 10: succeeded (Send keys to element test)");
  }
}

$('#send_keys_to_element_test').on("keydown", function() {flightTimeTest()});
$('#send_keys_to_element_test').on("keyup", function() {dwellTimeTest()});