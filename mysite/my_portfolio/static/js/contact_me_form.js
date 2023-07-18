$(document).ready(function() {
    $('#ContactMeForm').submit(function(event) {
      event.preventDefault(); // Prevent the default form submission

      // Get form data as an object
      const formData = $(this).serializeArray().reduce(function(obj, item) {
        obj[item.name] = item.value;
        return obj;
      }, {});

      // Get a reference to the submit button
      var button = $(this).find('input[type="submit"]');

      // Make the AJAX POST request to your Django REST API
      $.ajax({
        type: 'POST',
        url: '/contact-me/', // Replace with your API endpoint URL
        data: JSON.stringify(formData),
        contentType: 'application/json',
        success: function(response) {
          // Handle the API response if needed
          console.log(response);
          // Do something with the response data
          alert("Message sent successfully!");
          // Disable the button after success
          button.prop('disabled', true);
        },
        error: function(xhr, ajaxOptions, thrownError) {
    // do something with the error, such as showing an error message
    alert(xhr.responseText);
          console.error(error);
        }
      });
    });
  });