const formulario = document.getElementById('formulario');
const options = { style: 'currency', currency: 'EUR' };
const numberFormat = new Intl.NumberFormat('es-ES', options);

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
            "Content-Type": "application/json",
            "Authorization" : "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Ik1hcmNvcyIsInBhc3N3b3JkIjoxMjMsImV4cCI6MTY1Nzc5NjIyNH0.tEATWj83zVpwUduR4o96CEortX-jgkCAxIZ65KLZOg8"
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
                <td>${numberFormat.format(datos[i].cuota)}</td>
                <td>${numberFormat.format(datos[i].interes)}</td>
                <td>${numberFormat.format(datos[i].cuotaAmortizacion)}</td>
                <td>${numberFormat.format(datos[i].totalAmortizacion)}</td>
                <td>${numberFormat.format(Math.abs(datos[i].capitalPorAmortizar))}</td>
              </tr>`

        html = html + row
    }

    document.querySelector('#table_id > tbody').innerHTML = html;

}


//Método para pintar datos en pantalla
function imprimirTarjetas(datos){

    document.getElementById('precioInmuebleCard').innerHTML = numberFormat.format(datos.hipoteca.capitalInmueble);
    document.getElementById('importeInicialCard').innerHTML = numberFormat.format(datos.hipoteca.capitalAportado);
    document.getElementById('prestamoCard').innerHTML = numberFormat.format(datos.hipoteca.prestamo);
    document.getElementById('cuotaMensualCard').innerHTML = numberFormat.format(datos.hipoteca.cuota);
    document.getElementById('tipointeresCard').innerHTML = datos.hipoteca.tipoInteres;
    document.getElementById('interesCard').innerHTML = Number.parseFloat(datos.hipoteca.tasaInteres).toFixed(2) + '%';
    document.getElementById('totalInteresCard').innerHTML = numberFormat.format(datos.hipoteca.totalIntereses);
    document.getElementById('porcentajeCard').innerHTML = Number.parseFloat(datos.porcentaje).toFixed(2) + '%';
    

}