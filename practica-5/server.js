import './mongo.js'
import { express } from 'express'
import { Recipe } from './models/Recipe.js'

const app = express()
const port = 3000

app.use(express.json())

app.get('/api/recipes', (req, res) => {
  Recipe.find({}).then(recipes => {
    res.json(recipes)
  })
})

app.post('/api/recipes', (req, res) => {
  const { name, instructions, ingredients, slug, garnish } = req.body

  if (!name || !instructions || !ingredients || !slug) {
    res.status(400).json({ error: 'Missing required fields' })
  }

  const newRecipe = new Recipe({
    name,
    instructions,
    ingredients,
    slug,
    garnish
  })

  newRecipe.save().then(savedRecipe => {
    res.status(200).send(savedRecipe)
  })
})

app.put('/api/recipes/:id', (req, res) => {
  const { id } = req.params
  const { name, instructions, ingredients, slug, garnish } = req.body

  if (!name || !instructions || !ingredients || !slug) {
    res.status(400).json({ error: 'Missing required fields' })
  }

  Recipe.findByIdAndUpdate(id, { name, instructions, ingredients, slug, garnish }, { new: true }).then(updatedRecipe => {
    res.status(200).send(updatedRecipe)
  })
})

app.delete('/api/recipes/:id', (req, res) => {
  const { id } = req.params

  Recipe.findByIdAndDelete(id).then(() => {
    res.status(200).send()
  }).catch(err => res.json({ 'Recipe not found': err }))
})

app.listen(port, () => {
  console.log(`App listening on port ${port}`)
})
