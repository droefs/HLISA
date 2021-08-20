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
  
  $('#button1').on("click", function() {clickTest()});
  
  let clicks = 0;
  clickTime = performance.now();
  let button1Clicks = []

  function clickTest() {
    let previousClickTime = clickTime;
    clickTime = performance.now();

    // Log clicks
    button1Clicks.push({
      "x": event.pageX,
      "y": event.pageY,
      "dwellTime": clickTime - previousClickTime
    });

    clicks += 1;
    if (clicks == 10) {
      if (clicksLookBotlike(button1Clicks))
        sendMessage("Click test failed");
      else
        sendMessage("Click test succeeded");
    }
  }

  function clicksLookBotlike(button1Clicks) {
    let buttonCoordinates = document.getElementById("button1").getBoundingClientRect();
    let botlikeClicks = 0;
			for (let i = 0; i < button1Clicks.length; i++) {
				if (button1Clicks[i]["dwellTime"] < 5) {
					botlikeClicks++;
				}
				else if (Math.abs(button1Clicks[i]["x"] - (buttonCoordinates.left + buttonCoordinates.width / 2)) < 2 &&
				Math.abs(button1Clicks[i]["y"] - (buttonCoordinates.top + buttonCoordinates.height / 2)) < 2) {
					botlikeClicks++;
				}
      }
    return botlikeClicks > button1Clicks.length / 2;
  }