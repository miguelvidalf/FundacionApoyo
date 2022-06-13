console.log('activo')

document.querySelector('#btn1').addEventListener('click', traerdatos());
function traerdatos(){
    console.log('correcto');
    const xhttp = new XMLHttpRequest();

    xhttp.open("get","datosinventario.json",true);
    xhttp.send();
    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status==200){

           // console.log(this.responseText);

            let datos = JSON.parse(this.responseText);
            let res = document.querySelector('#res');
            res.innerHTML='';
            for(let i of datos){
                res.innerHTML += `
                <tr>
                    <td>${i.ID}</td>
                    <td>${i.Categoria}</td>
                    <td>${i.Nombre}</td>
                    <td>${i.Estado}</td>
                    <td>Eliminar</td>
                </tr>
                `
            }
        }
        
    };

    xhttp.open("get","datosbodega.json",true);
    xhttp.send();
    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status==200){

           // console.log(this.responseText);

            let datos = JSON.parse(this.responseText);
            let rep = document.querySelector('#rep');
            rep.innerHTML='';
            for(let i of datos){
                rep.innerHTML += `
                <tr>
                    <td>${i.ID}</td>
                    <td>${i.Categoria}</td>
                    <td>${i.Nombre}</td>
                    <td>${i.Descripcion}</td>
                    <td>${i.Precio}</td>
                    <td>${i.descsub}</td>
                    <td>${i.descof}</td>
                </tr>
                `
            }
        }
        
    };

    xhttp.open("get","datosinventario.json",true);
    xhttp.send();
    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status==200){

           // console.log(this.responseText);

            let datos = JSON.parse(this.responseText);
            let red = document.querySelector('#red');
            red.innerHTML='';
            for(let i of datos){
                rep.innerHTML += `
                <tr>
                    <td>${i.ID}</td>
                    <td>${i.tipou}</td>
                    <td>${i.rut}</td>
                    <td>${i.nombre}</td>
                    <td>${i.apllido}</td>
                    <td>${i.direccion}</td>
                    <td>${i.consubcrpcion}</td>
                </tr>
                `
            }
        }
    }; 
}