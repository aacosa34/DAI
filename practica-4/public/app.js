const root = document.documentElement

const plusSizeButton = document.getElementById('plus-size')
const minusSizeButton = document.getElementById('minus-size')

let actualSize = localStorage.getItem('T_SITE_SIZE') || 'base'

const setSize = (size) => {
  root.classList.remove(`text-${actualSize}`)
  root.classList.add(`text-${size}`)
  actualSize = size
}

setSize(actualSize)

plusSizeButton.addEventListener('click', () => {
  if (actualSize === 'base') {
    setSize('lg')
  } else if (actualSize === 'lg') {
    setSize('xl')
  } else if (actualSize === 'xl') {
    setSize('2xl')
  } else if (actualSize === '2xl') {
    setSize('3xl')
  } else if (actualSize === '3xl') {
    setSize('4xl')
  }
  localStorage.setItem('T_SITE_SIZE', actualSize)
})

minusSizeButton.addEventListener('click', () => {
  if (actualSize === '4xl') {
    setSize('3xl')
  } else if (actualSize === '3xl') {
    setSize('2xl')
  } else if (actualSize === '2xl') {
    setSize('xl')
  } else if (actualSize === 'xl') {
    setSize('lg')
  } else if (actualSize === 'lg') {
    setSize('base')
  }
  localStorage.setItem('T_SITE_SIZE', actualSize)
})

const MOON_SVG = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M12.2256 2.00253C9.59172 1.94346 6.93894 2.9189 4.92893 4.92891C1.02369 8.83415 1.02369 15.1658 4.92893 19.071C8.83418 22.9763 15.1658 22.9763 19.0711 19.071C21.0811 17.061 22.0565 14.4082 21.9975 11.7743C21.9796 10.9772 21.8669 10.1818 21.6595 9.40643C21.0933 9.9488 20.5078 10.4276 19.9163 10.8425C18.5649 11.7906 17.1826 12.4053 15.9301 12.6837C14.0241 13.1072 12.7156 12.7156 12 12C11.2844 11.2844 10.8928 9.97588 11.3163 8.0699C11.5947 6.81738 12.2094 5.43511 13.1575 4.08368C13.5724 3.49221 14.0512 2.90664 14.5935 2.34046C13.8182 2.13305 13.0228 2.02041 12.2256 2.00253ZM17.6569 17.6568C18.9081 16.4056 19.6582 14.8431 19.9072 13.2186C16.3611 15.2643 12.638 15.4664 10.5858 13.4142C8.53361 11.362 8.73568 7.63895 10.7814 4.09281C9.1569 4.34184 7.59434 5.09193 6.34315 6.34313C3.21895 9.46732 3.21895 14.5326 6.34315 17.6568C9.46734 20.781 14.5327 20.781 17.6569 17.6568Z" fill="currentColor" /></svg>'
const SUN_SVG = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 16C14.2091 16 16 14.2091 16 12C16 9.79086 14.2091 8 12 8C9.79086 8 8 9.79086 8 12C8 14.2091 9.79086 16 12 16ZM12 18C15.3137 18 18 15.3137 18 12C18 8.68629 15.3137 6 12 6C8.68629 6 6 8.68629 6 12C6 15.3137 8.68629 18 12 18Z" fill="currentColor" /><path fill-rule="evenodd" clip-rule="evenodd" d="M11 0H13V4.06189C12.6724 4.02104 12.3387 4 12 4C11.6613 4 11.3276 4.02104 11 4.06189V0ZM7.0943 5.68018L4.22173 2.80761L2.80752 4.22183L5.6801 7.09441C6.09071 6.56618 6.56608 6.0908 7.0943 5.68018ZM4.06189 11H0V13H4.06189C4.02104 12.6724 4 12.3387 4 12C4 11.6613 4.02104 11.3276 4.06189 11ZM5.6801 16.9056L2.80751 19.7782L4.22173 21.1924L7.0943 18.3198C6.56608 17.9092 6.09071 17.4338 5.6801 16.9056ZM11 19.9381V24H13V19.9381C12.6724 19.979 12.3387 20 12 20C11.6613 20 11.3276 19.979 11 19.9381ZM16.9056 18.3199L19.7781 21.1924L21.1923 19.7782L18.3198 16.9057C17.9092 17.4339 17.4338 17.9093 16.9056 18.3199ZM19.9381 13H24V11H19.9381C19.979 11.3276 20 11.6613 20 12C20 12.3387 19.979 12.6724 19.9381 13ZM18.3198 7.0943L21.1923 4.22183L19.7781 2.80762L16.9056 5.6801C17.4338 6.09071 17.9092 6.56608 18.3198 7.0943Z" fill="currentColor" /></svg>'

const themeToggleButton = document.getElementById('theme-toggle')

let theme = localStorage.getItem('T_SITE_THEME') || 'light'

const setDarkTheme = () => {
  root.classList.add('dark')
  themeToggleButton.innerHTML = SUN_SVG
  localStorage.setItem('T_SITE_THEME', 'dark')
  theme = 'dark'
}

const setLightTheme = () => {
  root.classList.remove('dark')
  themeToggleButton.innerHTML = MOON_SVG
  localStorage.setItem('T_SITE_THEME', 'light')
  theme = 'light'
}

theme === 'light' ? setLightTheme() : setDarkTheme()

themeToggleButton.addEventListener('click', () => {
  if (theme === 'light') {
    setDarkTheme()
  } else {
    setLightTheme()
  }
})

let recetas = []
let i = 0
const filasTabla = document.querySelector('[datos-cuerpo-tabla]')
const dataContainer = document.querySelector('[data-container]')
const inputBusqueda = document.querySelector('[data-search]')

inputBusqueda.addEventListener('input', (e) => {
  const value = e.target.value.toLowerCase()
  recetas.forEach((receta) => {
    const esVisible = receta.name.toLowerCase().includes(value)
    receta.element.classList.toggle('hidden', !esVisible)
  })
})

// fetch devuelve una promise
fetch('/api/recipes') // GET por defecto, se ejecuta al cargar la página
  .then(res => res.json()) // respuesta en json, otra promise
  .then(filas => { // arrow function
    recetas = filas.map(fila => { // bucle ES6, arrow function
      i++
      // A traves de los atributos que les he dado a los elementos del template
      // los pueso recoger aqui y cambiarle los valores a cada campo
      const row = filasTabla.content.cloneNode(true).children[0]
      const id = row.querySelector('[data-id]')
      const name = row.querySelector('[data-name]')

      id.textContent = i
      name.textContent = fila.name
      name.setAttribute('onclick', `detalle('${i - 1}')`)

      dataContainer.append(row)

      return {
        id: i,
        name: fila.name,
        ingredients: fila.ingredients,
        instructions: fila.instructions,
        element: row
      }
    })
  })
// set the modal menu element
const targetEl = document.getElementById('modalEl')

// options with default values
const options = {
  placement: 'center-center',
  backdrop: 'dynamic',
  backdropClasses: 'bg-gray-900 bg-opacity-50 dark:bg-opacity-80 fixed inset-0 z-40',
  onHide: () => {
    console.log('modal is hidden')
  },
  onShow: () => {
    console.log('modal is shown')
  },
  onToggle: () => {
    console.log('modal has been toggled')
  }
}

const modal = new Modal(targetEl, options)

const closeModal = () => {
  modal.hide()
}

const detalle = (i) => {
  const { name, ingredients, instructions } = recetas[i]

  document.getElementById('titulo').innerHTML = name
  let ingrString = ''
  ingredients.forEach(ingrediente => {
    ingrString += `<li>${ingrediente.name}</li>`
  })
  document.getElementById('ingredientes').innerHTML = `<ul>${ingrString}</ul>`
  let instrString = ''
  instructions.forEach(instruccion => {
    instrString += `<li>${instruccion}</li>`
  })

  document.getElementById('instrucciones').innerHTML = `<ul>${instrString}</ul>`

  modal.show()
  const cerrar = document.getElementById('close-modal')
  cerrar.addEventListener('click', () => {
    modal.hide()
  })
}

const addRecetaButton = document.getElementById('add-recipe')

addRecetaButton.addEventListener('click', () => {
  const title = document.getElementById('titulo')
  title.innerHTML = 'New recipe'

  const body = document.getElementById('modal-body')
  const footer = document.getElementById('modal-footer')
  const previousFooter = footer.innerHTML
  const previousBody = body.innerHTML

  body.innerHTML = `
    <div class="flex flex-col justify-center items-center">
      <div class="mb-6">
        <label for="new-recipe-name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Name</label>
        <input type="text" id="new-recipe-name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Name of the recipe...">
      </div>
      
      <label for="new-recipe-ingredients" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Ingredients</label>
      <textarea id="new-recipe-ingredients" rows="4" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 mb-4" placeholder="Write the ingredients of the recipe..."></textarea>

      <label for="new-recipe-instructions" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Instructions</label>
      <textarea id="new-recipe-instructions" rows="4" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Write the instructions of the recipe..."></textarea>

    </div>
  `

  footer.innerHTML = `
    <div class="flex justify-end">
      <button id="save-recipe" type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800" data-dismiss="modal">Save recipe</button>
      <button id="close-modal" type="button" class="focus:outline-none text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-900">Dismiss</button>
    </div>
  `
  modal.show()

  const saveRecipe = document.getElementById('save-recipe')

  saveRecipe.addEventListener('click', () => {
    const name = document.getElementById('new-recipe-name').value
    const ingredients = document.getElementById('new-recipe-ingredients').value
    ingredients.split('\n').forEach((ingrediente) => {
      console.log(ingrediente)
    })
  })

  // Añade evento para cerrar el modal y regenerar el contenido anterior para cada
  // elemento que tenga el id close-modal
  const cerrar = document.querySelectorAll('#close-modal')
  cerrar.forEach((elemento) => {
    elemento.addEventListener('click', () => {
      // Cuando cerramos el modal, devolvemos su estado anterior
      body.innerHTML = previousBody
      footer.innerHTML = previousFooter
      modal.hide()
    })
  })
})
