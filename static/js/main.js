$(document).ready(function() {

    var containerTimeout;
    var dropdownTimeout;

    $('#dropdownContainer').mouseenter(function() {
        // Establecer un temporizador para el contenedor (por ejemplo, 500 ms)
        containerTimeout = setTimeout(function() {
            // La animación del contenedor se activa solo después de que el mouse ha estado en el área durante 500 ms
            $('#dropdown').stop(true, true).slideDown(250);
        }, 250);
    });

    $('#dropdownContainer, #dropdown').mouseleave(function() {
        clearTimeout(containerTimeout);
    });

    $('#dropdown').mouseenter(function() {
        clearTimeout(containerTimeout);
    });

    $('#dropdown').mouseleave(function() {
        dropdownTimeout = setTimeout(function() {
            $('#dropdown').stop(true, true).slideUp(250);
        }, 250);
    });

    $('#dropdown').mouseenter(function() {
        clearTimeout(dropdownTimeout);
    });

    $('.show-image-popup').on('click', function(e) {
      e.preventDefault();
      var imageUrl = $(this).data('src');
      var modalImg = $('#expandedImage');
      modalImg.attr('src', imageUrl);
      $('#imagePopup').removeClass('hidden');
    });
  
    $('#closeImagePopup, .modal-overlay').on('click', function() {
      $('#imagePopup').addClass('hidden');
    });
  
    $("#scrollToTop").click(function() {
      $("html, body").animate(
        {
          scrollTop: 0
        },
        500
      );
    });

    $("#user-menu-button").on("click", function () {
      var $userDropdown = $("#user-dropdown");
      if ($userDropdown.is(":hidden")) {
        $userDropdown.slideDown("fast");
      } else {
        $userDropdown.slideUp("fast");
      }
    });

    $("#product-tabs a").click(function (e) {
      e.preventDefault();
      $(".tab-content").addClass("hidden");
      $($(this).attr("href")).removeClass("hidden");
    });

    $("#debug").text("pass");
  });
