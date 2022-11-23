const { Schema, model } = require('mongoose')

const recipeSchema = new Schema({
  name: String,
  ingredients: [
    {
      name: String,
      quantity: {
        value: Number,
        unit: String
      }
    }
  ],
  garnish: String,
  instructions: [String],
  slug: String
})

const Recipe = model('Recipe', recipeSchema)

// Cocktel.find({}).then(result => {
//   console.log(result)
//   mongoose.connection.close()
// })

export default Recipe
