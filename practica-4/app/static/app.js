window.onload = () => {

  const elemento_busqueda = document.getElementById('buscar')

  // evento para cuando cambia el valor introducido en un <input id="buscar">
  elemento_busqueda.onchange = () =>{
    const texto_busqueda = elemento_busqueda.value
    console.log(texto_busqueda)
  }
}

fetch("/api/recipes")
  .then((res) => res.json())
  .then((datos) => {
    let htmlString = "<table>"
    for (const dato of datos.recetas) {
      htmlString += `<tr><td>${dato.name}</td> ...</tr>`
    }
    htmlString += "</table>"

    // y poner htmlString en su lugar de la página
    const ele = document.getElementById("elemento_encima_de_la_tabla")
    ele.innnerHTML = htmlString
  })
