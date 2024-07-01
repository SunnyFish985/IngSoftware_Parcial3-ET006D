$().ready(function(){
    $('#formTransfer').validate({
        rules:{
            idVehiculo: {
                required: true,
                maxlength: 8
            },
            patente: {
                required: true,
                maxlength: 6
            },
            cantAsientos: {
                required: true,
                digits: true,
                min: 3
            },
            imagen: {
                required: true,
                accept: "image/*"
            },
            categoria: {
                required: true
            }
        },
        messages: {
            idVehiculo: {
                required: "Por favor, ingrese el ID del vehículo",
                maxlength: "El ID del vehículo no puede tener más de 8 caracteres"
            },
            patente: {
                required: "Por favor, ingrese la patente",
                maxlength: "La patente no puede tener más de 6 caracteres"
            },
            cantAsientos: {
                required: "Por favor, ingrese la cantidad de asientos",
                digits: "Por favor, ingrese solo números",
                min: "La cantidad de asientos debe ser al menos 3"
            },
            imagen: {
                required: "Por favor, suba una imagen del vehículo",
                accept: "Por favor, suba un archivo de imagen válido"
            },
            categoria: {
                required: "Por favor, seleccione una categoría"
            }
        },
        errorElement: 'div',
        errorPlacement: function(error, element) {
            error.addClass('invalid-feedback');
            if (element.prop('type') === 'checkbox') {
                error.insertAfter(element.parent('label'));
            } else {
                error.insertAfter(element);
            }
        },
        highlight: function(element, errorClass, validClass) {
            $(element).addClass('is-invalid').removeClass('is-valid');
        },
        unhighlight: function(element, errorClass, validClass) {
            $(element).addClass('is-valid').removeClass('is-invalid');
        }
    });
});

$().ready(function(){
    $('#formChofer').validate({
        rules: {
            idChofer: {
                required: true,
                digits: true
            },
            rut: {
                required: true,
                digits: true,
                max: 99999999
            },
            dv: {
                required: true,
                maxlength: 1,
                pattern: /^[0-9K]$/
            },
            pNom: {
                required: true,
                maxlength: 30,
                lettersonly: true
            },
            sNom: {
                maxlength: 30,
                lettersonly: true
            },
            pApe: {
                required: true,
                maxlength: 30,
                lettersonly: true
            },
            sApe: {
                required: true,
                maxlength: 30,
                lettersonly: true
            }
        },
        messages: {
            idChofer: {
                required: "Por favor, ingrese el ID del chofer",
                digits: "El ID del chofer debe ser un número"
            },
            rut: {
                required: "Por favor, ingrese el RUT",
                digits: "El RUT debe ser un número",
                max:"El rut no debe superar los 8 dígitos"
            },
            dv: {
                required: "Por favor, ingrese el dígito verificador",
                maxlength: "El dígito verificador debe ser un solo carácter",
                pattern: "El dígito verificador debe ser un número entre 0 y 9 o la letra K"
            },
            pNom: {
                required: "Por favor, ingrese el primer nombre",
                maxlength: "El primer nombre no debe exceder los 30 caracteres",
                lettersonly: "Solo puede ocupar letras en este campo"
            },
            sNom: {
                maxlength: "El segundo nombre no debe exceder los 30 caracteres",
                lettersonly: "Solo puede ocupar letras en este campo"
            },
            pApe: {
                required: "Por favor, ingrese el primer apellido",
                maxlength: "El primer apellido no debe exceder los 30 caracteres",
                lettersonly: "Solo puede ocupar letras en este campo"
            },
            sApe: {
                required: "Por favor, ingrese el segundo apellido",
                maxlength: "El segundo apellido no debe exceder los 30 caracteres",
                lettersonly: "Solo puede ocupar letras en este campo"
            }
        },
        errorElement: 'div',
        errorClass: 'invalid-feedback',
        highlight: function(element) {
            $(element).closest('.form-control').addClass('is-invalid');
        },
        unhighlight: function(element) {
            $(element).closest('.form-control').removeClass('is-invalid');
        },
        errorPlacement: function(error, element) {
            error.insertAfter(element);
        }
    });
});