var express = require('express');
var router = express.Router();
const { spawn } = require('child_process');
const process = require('process');

router.get('/', (req, res, next) =>{

  // res.send({ title: 'Express'});
  console.log(process.cwd());
  const mlPython = spawn('.', ['knowledge/main.py']);

  mlPython.stdout.on('data', (data) =>{
      console.log(data.toString());
      res.send({data:data.toString()})
  });
});


router.post('/', (req, res, next) =>{
  res.send({data:{teste:'teste'}})
});

module.exports = router;
