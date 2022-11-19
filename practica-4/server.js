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

app.post('/api/recipes', (req, res) => {
  const recipe = req.body

  if (!recipe.slug) {
    return res.status(400).json({
      error: 'content missing'
    })
  }

  const newRecipe = new Recipe({
    name: recipe.name,
    ingredients: recipe.ingredients,
    garnish: recipe.garnish,
    instructions: recipe.instructions,
    slug: recipe.slug
  })

  newRecipe.save().then(savedRecipe => {
    res.json(savedRecipe)
  })
})

app.put('/api/recipes/:id', (req, res) => {
})

app.delete('/api/recipes/:id', (req, res) => {
})

app.listen(port, () => {
  console.log(`App listening on port ${port}`)
})
