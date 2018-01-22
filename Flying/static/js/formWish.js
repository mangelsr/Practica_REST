$(document).ready(function(){

    let error_function = function (jqXHR, exception) {
        var msg = '';
        if (jqXHR.status === 0) {
            msg = 'Not connect.\n Verify Network.';
        } else if (jqXHR.status == 404) {
            msg = 'Requested page not found. [404]';
        } else if (jqXHR.status == 500) {
            msg = 'Internal Server Error [500].';
        } else if (exception === 'parsererror') {
            msg = 'Requested JSON parse failed.';
        } else if (exception === 'timeout') {
            msg = 'Time out error.';
        } else if (exception === 'abort') {
            msg = 'Ajax request aborted.';
        } else {
            msg = 'Uncaught Error.\n' + jqXHR.responseText;
        }
        alert(msg);
    };


    $('formREST').submit(function (event){
        event.preventDefault();
        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            contentType: "application/json; charset=utf-8",
            success: function(data){
                console.log(data);
            },
            error: error_function,
        });
        window.location.replace("/deseo");
    });


    $.ajax({
        url: $('#formREST').attr('action'),
        type: 'GET',
        success: function(data){
            console.log(data);
            let tabla = $('#tablaWish');
            for (element in data.results){
                let fila = $('<tr>');
                
                let nombre = $('<td>');
                let celular = $('<td>');
                let fecha_partida = $('<td>');
                let fecha_retorno = $('<td>');
                let ciudad_partida = $('<td>');
                let ciudad_retorno = $('<td>');
                let escalas = $('<td>');

                nombre.append(data.results[element].name);
                celular.append(data.results[element].phone);
                fecha_partida.append(data.results[element].dateI);
                fecha_retorno.append(data.results[element].dateF);
                ciudad_partida.append(data.results[element].cityI);
                ciudad_retorno.append(data.results[element].cityF);
                escalas.append(data.results[element].stops);

                fila.append(nombre).append(celular).append(fecha_partida)
                    .append(fecha_retorno).append(ciudad_partida)
                    .append(ciudad_retorno).append(escalas);
                
                tabla.append(fila);
            }
            $('#resultWish').hide().fadeIn('slow');
        },
        error: error_function,
    });
});