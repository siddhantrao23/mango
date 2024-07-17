$(document).ready(function() {

  var animating = false;
  var cardsCounter = 0;
  var numOfCards = document.querySelectorAll('.swipe__card').length;
  var decisionVal = 80;
  var pullDeltaX = 0;
  var deg = 0;
  var $card, $cardReject, $cardLike;

  function pullChange() {
    animating = true;
    deg = pullDeltaX / 10;
    $card.css("transform", "translateX("+ pullDeltaX +"px) rotate("+ deg +"deg)");

    var opacity = pullDeltaX / 100;
    var rejectOpacity = (opacity >= 0) ? 0 : Math.abs(opacity);
    var likeOpacity = (opacity <= 0) ? 0 : opacity;
    $cardReject.css("opacity", rejectOpacity);
    $cardLike.css("opacity", likeOpacity);
  };

  function release() {
  
    if (pullDeltaX >= decisionVal) {
      $card.addClass("to-right liked");
      var curr = $(".user__rating").text();
      $(".user__rating").text(Number(curr) + 1);
    } else if (pullDeltaX <= -decisionVal) {
      $card.addClass("to-left disliked");
    }

    if (Math.abs(pullDeltaX) >= decisionVal) {
      $card.addClass("inactive");

      setTimeout(function() {
        $card.addClass("below").removeClass("inactive to-left to-right");
        cardsCounter++;
        if (cardsCounter === numOfCards) {
          showSubmitButton();
        }
      }, 300);
    }

    if (Math.abs(pullDeltaX) < decisionVal) {
      $card.addClass("reset");
    }

    function showSubmitButton() {
      $(document).off("mousedown touchstart");
      $("#rating-form").show();
    }

    setTimeout(function() {
      $card.attr("style", "").removeClass("reset")
        .find(".swipe__choice").attr("style", "");

      pullDeltaX = 0;
      animating = false;
    }, 300);
  };

  $(document).on("mousedown touchstart", ".swipe__card:not(.inactive)", function(e) {
    if (animating) return;

    $card = $(this);
    $cardReject = $(".swipe__choice.m__reject", $card);
    $cardLike = $(".swipe__choice.m__like", $card);
    var startX =  e.pageX || e.originalEvent.touches[0].pageX;

    $(document).on("mousemove touchmove", function(e) {
      var x = e.pageX || e.originalEvent.touches[0].pageX;
      pullDeltaX = (x - startX);
      if (!pullDeltaX) return;
      pullChange();
    });

    $(document).on("mouseup touchend", function() {
      $(document).off("mousemove touchmove mouseup touchend");
      if (!pullDeltaX) return; // prevents from rapid click events
      release();
    });
  });

  $("#submit-rating-button").on("click", function() {
    var curr = $(".user__rating").text();
    $("#rating-input").val(curr);
  });

});