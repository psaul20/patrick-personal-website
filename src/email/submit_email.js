;(function () {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  var forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission
  Array.prototype.slice.call(forms).forEach(function (form) {
    form.addEventListener(
      'submit',
      function (event) {
        event.preventDefault()
        event.stopPropagation()
        if (form.checkValidity()) {
          var data = JSON.stringify($(form).serializeJSON())
          $.ajax({
            url: 'http://127.0.0.1:8080',
            contentType: 'application/json; charset=utf-8',
            // dataType: 'json',
            type: 'POST',
            enctype: 'gzip, deflate, br',
            data: data,
            success: function (response) {
              console.log('Success Response')
              $('#email-success').show()
            },
            error: function (response) {
              console.log('Error Response')
              $('#email-fail').show()
            }
          })
        }
        form.classList.add('was-validated')
      },
      false
    )
  })
})()

// // Example starter JavaScript for disabling form submissions if there are invalid fields
// ;(function () {
//   'use strict'

//   // Fetch all the forms we want to apply custom Bootstrap validation styles to
//   var forms = document.querySelectorAll('.needs-validation')

//   // Loop over them and prevent submission
//   Array.prototype.slice.call(forms).forEach(function (form) {
//     form.addEventListener(
//       'submit',
//       function (event) {
//         if (!form.checkValidity()) {
//           event.preventDefault()
//           event.stopPropagation()
//         }

//         form.classList.add('was-validated')
//       },
//       false
//     )
//   })
// })()
