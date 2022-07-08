const formulario = document.getElementById('formulario');
formulario.addEventListener('submit', function(event){
    event.preventDefault();

    const data = new FormData(formulario);

    console.log([...data])
  
    console.log(document.getElementById('ahorros').value)
    console.log(typeof(document.getElementById('ahorros').value))
    s = {
        "ahorros": parseFloat(document.getElementById('ahorros').value),
        "capitalAportado": parseFloat(document.getElementById("capitalAportado").value),
        "capitalInmueble": parseFloat(document.getElementById('capitalInmueble').value),
        "cuota": 0.0,
        "esPrimeraVivienda": true,
        "fechaNacimiento": "hoy",
        "nomina": parseFloat(document.getElementById('nomina').value),
        "otrosPrestamos": parseFloat(document.getElementById('otrosPrestamos').value),
        "plazo": parseInt(document.getElementById('plazo').value),
        "plazoRestante": 0,
        "prestamo": 0.0,
        "tasaInteres": 0.0,
        "tipoInteres": "fijo",
        "totalIntereses": 0.0
    }

    fetch('http://127.0.0.1:8859/api/calculadora',{
        method: "POST",
        body: JSON.stringify(s),
        headers: {
            "Content-Type": "application/json"
        }
    })

    .then(res => res.json())
    .then(data => {
        console.log(data.porcentaje)
        imprimirTabla(data.hipoteca.amortizaciones);
        imprimirTarjetas(data)
    
    })
    .catch(err => console.log(err))

})

//Método para pintar datos en pantalla
function imprimirTabla(datos){
    var html = ''
    for (let i = 0; i < datos.length; i++) {
        var row = `<tr>
                <td>${datos[i].numeroCuota}</td>
                <td>${datos[i].cuota}</td>
                <td>${datos[i].interes}</td>
                <td>${datos[i].cuotaAmortizacion}</td>
                <td>${datos[i].totalAmortizacion}</td>
                <td>${datos[i].capitalPorAmortizar}</td>
              </tr>`

        html = html + row
    }

    document.querySelector('#table_id > tbody').innerHTML = html;

}


//Método para pintar datos en pantalla
function imprimirTarjetas(datos){

    document.getElementById('precioInmuebleCard').innerHTML = datos.hipoteca.capitalInmueble;
    document.getElementById('importeInicialCard').innerHTML = datos.hipoteca.capitalAportado;
    document.getElementById('prestamoCard').innerHTML = datos.hipoteca.prestamo;
    document.getElementById('cuotaMensualCard').innerHTML = datos.hipoteca.cuota;
    document.getElementById('tipointeresCard').innerHTML = datos.hipoteca.tipoInteres;
    document.getElementById('interesCard').innerHTML = datos.hipoteca.tasaInteres;
    document.getElementById('totalInteresCard').innerHTML = datos.hipoteca.totalIntereses;
    console.log(document.getElementById('porcentajeCard'))
    document.getElementById('porcentajeCard').innerHTML = datos.porcentaje;
    

}