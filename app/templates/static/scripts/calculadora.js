const formulario = document.getElementById("formulario")

formulario.addEventListener("submit", async function(event)
    {
        event.preventDefault
        const url = "http://127.0.0.1:8859/api/calculadora";
        const data = new FormData(formulario);
        console.log("asdasd" + data.getAll)
        console.table(Object.fromEntries(data)) // Works if all fields are uniq
        alert("ada")

        let response = await fetch(url, {
            "method": "POST",
            "headers" : {
                "Content-Type": "application/json"
            },
            "body" : JSON.stringify(data)
        })


        

    });
