require('./mongo')
const express = require('express')
const path = require('path')
const Recipe = require('./models/Recipe')

const app = express()
const port = 3000

app.use(express.static(path.join(__dirname, 'public')))
app.use(express.static(path.join(__dirname, 'node_modules')))

app.get('/', (req, res) => {
  res.sendFile('index.html')
})

app.get('/api/recipes', (req, res) => {
  Recipe.find({}).then(recipes => {
    res.json(recipes)
  })
})

app.listen(port, () => {
  console.log(`App listening on port ${port}`)
})
