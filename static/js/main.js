$(document).ready(function() {

    var containerTimeout;
    var dropdownTimeout;

    $('#dropdownContainer').mouseenter(function() {
        containerTimeout = setTimeout(function() {
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

    var zoomFactor = 3;
    var panSpeed = 20;

    $(".zoomable-container").on('mouseenter', function() {
      var container = $(this);
      var wrapper = container.find(".zoomable-wrapper");
      var image = wrapper.find(".zoomable");

      container.on('mousemove', function(event) {
        var offsetX = event.pageX - container.offset().left;
        var offsetY = event.pageY - container.offset().top;

        var newX = (offsetX / container.width()) * 100;
        var newY = (offsetY / container.height()) * 100;

        wrapper.css({
          "transform-origin": newX + "% " + newY + "%",
          "transform": "scale(" + zoomFactor + ")",
        });
      });
    }).on('mouseleave', function() {
      $(".zoomable-container").off('mousemove');
      $(".zoomable-wrapper").css({
        "transform-origin": "center center",
        "transform": "scale(1)"
      });
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
