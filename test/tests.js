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


  // Clicking test:
  
  $('#button1').on("mousedown", function() {clickTest()});
  $('#button1').on("mouseup", function() {
    button1Timings.push({
      "dwellTime": performance.now() - pressTime
    });
  });
  
  let clicks = 0;
  let pressTime = performance.now();
  let button1Clicks = []
  let button1Timings = []

  function clickTest() {
    pressTime = performance.now();

    button1Clicks.push({
      "x": event.pageX,
      "y": event.pageY
    });

    clicks += 1;
    if (clicks == 10) {
      if (clicksLookBotlike(button1Clicks, button1Timings))
        sendMessage("Test 1: failed (click test)");
      else
        sendMessage("Test 1: succeeded (click test)");
    }
  }

  function clicksLookBotlike(button1Clicks, button1Timings) {
    let buttonCoordinates = document.getElementById("button1").getBoundingClientRect();
    let botlikeClicks = 0;
			for (let i = 0; i < button1Timings.length; i++) {
        if (button1Timings[i]["dwellTime"] < 5) {
					botlikeClicks++;
				}
				else if (Math.abs(button1Clicks[i]["x"] - (buttonCoordinates.left + buttonCoordinates.width / 2)) < 2 &&
				Math.abs(button1Clicks[i]["y"] - (buttonCoordinates.top + buttonCoordinates.height / 2)) < 2) {
					botlikeClicks++;
				}
      }
    return botlikeClicks > button1Clicks.length / 2;
  }

  // Context clicking test:

  $('#button2').on("mousedown", function() {contextClickTest(event)});

  function contextClickTest(event) {
    
    if (event.which === 3)
      sendMessage("Test 2: succeeded (Context click test)");
    else
      sendMessage("Test 2: failed: (Context click test)");
  }

  // Test whether cursor location is correct after scroll:

  $('#button3').on("mousedown", function() {cursorLocationAfterScroll(event)});

  function cursorLocationAfterScroll(event) {
    sendMessage("Test 3: succeeded (Cursor location after scroll test)");
  }

  $('#button4').on("mousedown", function() {cursorLocationAfterScroll2(event)});

  function cursorLocationAfterScroll2(event) {
    sendMessage("Test 3: failed (Cursor location after scroll test)");
  }