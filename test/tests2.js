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

$('#draggable_element').on("dragstart", function() {event.dataTransfer.setData("data", event.target.id);});

$('#drag_endpoint').on("dragover", function() {event.preventDefault();});
$('#drag_endpoint').on("drop", function() {event.preventDefault(); event.target.appendChild(document.getElementById(event.dataTransfer.getData("data"))); sendMessage("Test 5: succeeded (Drag and drop test)");});

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