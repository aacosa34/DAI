const connect = require('mongoose')
const connectionString = 'mongodb://mongo_db:27017/cockteles'

// conexion a MongoDB
connect(connectionString, {
  useNewUrlParser: true,
  useUnifiedTopology: true

})
  .then(() => {
    console.log('Database connected')
  })
  .catch((err) => {
    console.error(err)
  })
