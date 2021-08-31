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
        sendMessage("Test 1: Click test failed");
      else
        sendMessage("Test 1: Click test succeeded");
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
      sendMessage("Test 2 succeeded (Context click test)");
    else
      sendMessage("Test 2 failed: (Context click test)");
  }