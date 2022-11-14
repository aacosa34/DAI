window.onload = () => {

  const elemento_busqueda = document.getElementById('buscar')

  // evento para cuando cambia el valor introducido en un <input id="buscar">
  elemento_busqueda.onchange(() =>{
    const texto_busqueda = elemento_busqueda.value
    console.log(texto_busqueda)
  })
}