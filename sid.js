  var app = require('express')();

  app.get('/user/:id', function(req, res) {
    if (!isValidUserId(req.params.id))
      res.send("Unknown user: " + req.params.id);
    else
      ;
  });
