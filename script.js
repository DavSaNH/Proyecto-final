function agregarFacultad() {
  // Obtener los datos del formulario
  var nombreFacultad = document.getElementById('nombre_facultad').value;

  // Enviar los datos al servidor utilizando AJAX
  var xhr = new XMLHttpRequest();
  xhr.open('POST', '/agregar_facultad', true);
  xhr.setRequestHeader('Content-Type', 'application/json');

  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      // Actualizar la página después de agregar la facultad
      window.location.href = '/';
    }
  };

  var data = JSON.stringify({ nombreFacultad: nombreFacultad });
  xhr.send(data);
}
