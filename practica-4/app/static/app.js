// para que se ejecute al cargar la página
window.onload = () => {

  const elemento_busqueda = document.getElementById('buscar')

  // evento para cuando cambia el valor introducido en un <input id="buscar">
  elemento_busqueda.onchange = () => {
    const texto_busqueda = elemento_busqueda.value
    console.log(texto_busqueda)
  }
}
const ele = document.querySelector("#app")

fetch("/api/recipes")
  .then((res) => res.json())
  .then((recetas) => {
    const htmlString = recetas.recetas.map(
      (receta) => { 
        return `
          <tr>
            <td>${receta.name}</td>
            <td>${receta.ingredients.length}</td>
            <td>${receta.instructions.join(', ')}</td>
            <td>${receta.slug}</td>
          </tr>
        `
      }
    )

    ele.innerHTML = `
      <h1>Lista de ${recetas.len} recetas</h1>
      <table>
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Num. ingredientes</th>
            <th>Instrucciones</th>
            <th>Slug</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          ${htmlString.join('')}
        </tbody>
      </table>`
  })

const dark_toggle = document.querySelector("#dark-toggle")
htmlTag = document.documentElement
htmlTag.setAttribute("data-theme", "light")

dark_toggle.onclick = () => {  
  if(htmlTag.getAttribute('data-theme') == 'dark') {
    htmlTag.setAttribute("data-theme", "light")
    dark_toggle.innerHTML = `Cambiar a modo oscuro`
  } else {
    htmlTag.setAttribute("data-theme", "dark")
    dark_toggle.innerHTML = `Cambiar a modo claro`
  }
}
