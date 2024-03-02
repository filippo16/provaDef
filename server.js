const express = require('express');
const app = express();
const port = 5000;

app.use(express.static('dist'));

app.listen(port, () => {
  console.log(`App listening at http://0.0.0.0:${port}`);
});