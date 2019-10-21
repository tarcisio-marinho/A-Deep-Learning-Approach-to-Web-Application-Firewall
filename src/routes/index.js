var express = require('express');
var router = express.Router();
const { spawn } = require('child_process');

/* GET home page. */
router.get('/', (req, res, next) =>{
  res.render('index', { title: 'Express' });


    const mlPython = spawn('python', ['identify.py']);

    mlPython.stdout.on('data', (data) =>{
        console.log(data.toString());
        res.write(data);
        res.end('end');
    });
});

module.exports = router;
