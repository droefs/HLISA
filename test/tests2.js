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