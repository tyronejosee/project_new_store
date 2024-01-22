$(document).ready(function() {
  var containerTimeout, dropdownTimeout;
  var containerTimeoutUser, dropdownTimeoutUser;
  var $dropdownContainer = $('#dropdownContainer');
  var $dropdown = $('#dropdown');
  var $zoomableContainer = $(".zoomable-container");
  var $zoomableWrapper = $(".zoomable-wrapper");

  $dropdownContainer.mouseenter(function() {
      containerTimeout = setTimeout(function() {
          $dropdown.stop(true, true).slideDown(200);
      }, 200);
  });

  $dropdownContainer.add($dropdown).mouseleave(function() {
      clearTimeout(containerTimeout);
  });

  $dropdown.mouseenter(function() {
      clearTimeout(containerTimeout);
  }).mouseleave(function() {
      dropdownTimeout = setTimeout(function() {
          $dropdown.stop(true, true).slideUp(200);
      }, 200);
  });

  $dropdown.mouseenter(function() {
      clearTimeout(dropdownTimeout);
  });

  $('#userWrapper').mouseenter(function() {
    containerTimeoutUser = setTimeout(function() {
        $('#userList').stop(true, true).slideDown(200);
    }, 200);
  });

  $('[data-collapse-toggle="navbar-search"]').on('click', function() {
    $('#navbar-search').toggleClass('hidden');
    });

  $("#sidebarToggle").click(function () {
    $("#sidebar").toggleClass("-translate-x-full sm:translate-x-0");
  });

  $('#userWrapper, #userList').mouseleave(function() {
      clearTimeout(containerTimeoutUser);
  });

  $('#userList').mouseenter(function() {
      clearTimeout(containerTimeoutUser);
  }).mouseleave(function() {
      dropdownTimeoutUser = setTimeout(function() {
          $('#userList').stop(true, true).slideUp(200);
      }, 200);
  });

  $('#userList').mouseenter(function() {
      clearTimeout(dropdownTimeoutUser);
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

  $("#btnScroll").click(function() {
      $("html, body").animate({
          scrollTop: 0
      }, 500);
  });

  var zoomFactor = 3;
  $zoomableContainer.on('mouseenter', function() {
      var container = $(this);
      var wrapper = container.find(".zoomable-wrapper");
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
      $zoomableContainer.off('mousemove');
      $zoomableWrapper.css({
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


// JS
document.addEventListener('DOMContentLoaded', function () {
    const toggleModeButton = document.getElementById('toggleModeButton');
    const htmlElement = document.documentElement;
    const darkModeStyles = document.getElementById('darkModeStyles');
    let isDarkMode = true;

    toggleModeButton.addEventListener('click', () => {
        isDarkMode = !isDarkMode;

        if (isDarkMode) {
            htmlElement.classList.add('dark');
            darkModeStyles.href = "/static/css/dark-mode.css";
        } else {
            htmlElement.classList.remove('dark');
            darkModeStyles.href = "/static/css/light-mode.css";
        }
    });
});