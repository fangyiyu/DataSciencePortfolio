

$(document).ready(function () {

    // Preloader Gif
    $("#predict").click(function () {
        $('#preloader').removeClass("invisible");
        $('#preloader').delay(4500).fadeOut('slow');
    });


    // Tooltip and modal
    $('[data-tooltip="tooltip"]').tooltip();

    $('#myModal').on('shown.bs.modal', function () {
        $('#myInput').trigger('focus')
      });

    $( "#datepicker-1" ).datepicker({minDate:'0', maxDate: '7'});

    
    
})  




