$(document).ready(function() {

    $('#dropdownCategories').click(function() {
      $('#dropdown').slideToggle(250);
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
  });
