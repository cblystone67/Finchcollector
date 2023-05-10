const express = require('express');
const path = require('path');
const favicon = require('serve-favicon');
const morgan = require('morgan');


//intialize the express app
const app = express();


//configure settings
require('dotenv').config();
require("./config/database");//This ensures that the database.js module runs.

//mount middleware
//this does the same as our old URLencoded.
app.use(express.json());//Also will create req.body
app.use(morgan('dev'));
//Use middleware to help express to discover the favicon file.
app.use(favicon(path.join(__dirname, 'build', 'favicon.ico')));
//use middleware to help express to discover the index.html file.
app.use(express.static(path.join(__dirname, 'build')));
//use middleware to help express discover static assets


//mount routes
//API routes go here.

//Catch all route-basically used to always serve index.html so that file gets sent to the router and any additonal routes can be used by AJAX.
app.get('/*', (req, res) => {
  res.sendFile(path.join(__dirname, 'build', 'index.html'));
});

//Tell the app to listen
const port = process.env.PORT || 3001;
app.listen(port, function(){
  console.log(`Express app running on port ${port}`);
});