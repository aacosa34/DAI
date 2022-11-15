  const recetas = []    
  let html_str=''
  let i = 0
  // fetch devuelve una promise
  fetch('/api/recipes')           // GET por defecto, se ejecuta al cargar la página
  .then(res => res.json())        // respuesta en json, otra promise
  .then(filas => {               // arrow function
      filas.recetas.forEach(fila => {     // bucle ES6, arrow function
          i++
          recetas.push(fila)      // se guardan para después sacar cada una             
          // ES6 templates
          html_str += `<tr>
                         <td>${i}</td>
                         <td>
                            <button onclick="detalle('${i-1}')" 
                                  type="button" class="btn btn-outline btn-sm"
                                  data-bs-toggle="modal" data-bs-target="#detailModal">
                            ${fila.name}
                         </button>
                  </td>
                  <td>
                  <button type="button" class="btn btn-warning btn-sm">Edit</button>
                  <button type="button" class="btn btn-danger btn-sm">Delete</button>
                  </td>
                  </tr>`         // ES6 templates
      });
      document.getElementById('tbody').innerHTML=html_str  // se pone el html en su sitio
    })

  function detalle(i) {  // saca un modal con la información de cada coctel
    // saca un modal con receta[i]
  }
     

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

const button_plus = document.querySelector("#size-plus")
const button_minus = document.querySelector("#size-minus")

button_plus.onclick = () => {
  console.log("plus")
  htmlTag.style.fontSize = "40px"
}

button_minus.onclick = () => {
  htmlTag.style.fontSize = "20px"
}