const mongoose = require('mongoose')
const connectionString = 'mongodb://localhost:27017/cockteles'

// conexion a MongoDB
mongoose.connect(connectionString,
  {
    useNewUrlParser: true,
    useUnifiedTopology: true
  })
  .then(() => {
    console.log('Database connected')
  })
  .catch((err) => {
    console.error(err)
  })
