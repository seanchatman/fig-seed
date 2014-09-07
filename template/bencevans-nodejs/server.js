var express = require('express');
var http    = require('http');
var app     = express();

app.get('/', function(req, res, next) {
    res.send('hello world');
});

http.createServer(app).listen(process.env.PORT || 3000, function() {
    console.log('Listening on port ' + (process.env.PORT || 3000));
});