const http = require('http');
var fs = require('fs');

var server = http.createServer(function(request, response) {
    if (request.method == 'GET') {
        if (request.url == "/index.html" || request.url == "/") {
			response.writeHead(200, {'content-type': 'text/html'});
            fs.createReadStream('index.html').pipe(response);
		}
		else if (request.url == "/jquery.js"){
			response.writeHead(200, {'content-type': 'text/html'});
            fs.createReadStream('jquery.js').pipe(response);
        }
        else if (request.url == "/tests.js"){
			response.writeHead(200, {'content-type': 'text/html'});
            fs.createReadStream('tests.js').pipe(response);
		}
    }
    else if (request.method == 'POST') {
        request.on("data", function (data) {
            let message = JSON.parse(data);
            console.log(message.message);
            response.writeHead(200, {"Content-Type": "text/plain"});
            response.end();
        });
    }
});
server.listen(8000);