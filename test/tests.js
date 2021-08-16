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
  function clickTest() {
    clicks += 1;
    if (clicks == 10) {
      sendMessage("Click test succeeded");
    }
  }