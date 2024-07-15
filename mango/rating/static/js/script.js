  var animating = false;
  var cardsCounter = 0;
  var numOfCards = document.querySelectorAll('.swipe__card').length / 2;
  var decisionVal = 80;
  var pullDeltaX = 0;
  var deg = 0;
  var card, cardReject, cardLike;

  function pullChange() {
    animating = true;
    deg = pullDeltaX / 10;
    card.style.transform = `translateX(${pullDeltaX}px) rotate(${deg}deg)`;

    var opacity = pullDeltaX / 100;
    var rejectOpacity = (opacity >= 0) ? 0 : Math.abs(opacity);
    var likeOpacity = (opacity <= 0) ? 0 : opacity;
    cardReject.style.opacity = rejectOpacity;
    cardLike.style.opacity = likeOpacity;
  };

  function release() {

    if (pullDeltaX >= decisionVal) {
      card.classList.add("to-right");
    } else if (pullDeltaX <= -decisionVal) {
      card.classList.add("to-left");
    }

    if (Math.abs(pullDeltaX) >= decisionVal) {
      card.classList.add("inactive");

      setTimeout(function() {
        card.classList.add("below");
        card.classList.remove("inactive", "to-left", "to-right");
        cardsCounter++;
        if (cardsCounter === numOfCards) {
          cardsCounter = 0;
          document.querySelectorAll(".swipe__card").forEach(function(card) {
            card.classList.remove("below");
          });
        }
      }, 300);
    }

    if (Math.abs(pullDeltaX) < decisionVal) {
      card.classList.add("reset");
    }

    setTimeout(function() {
      card.style.transform = "";
      card.classList.remove("reset");
      document.querySelectorAll(".swipe__choice", card).forEach(function(choice) {
        choice.style.opacity = "";
      });

      pullDeltaX = 0;
      animating = false;
    }, 300);
  };

  document.addEventListener("mousedown", function(e) {
    if (e.target.closest('.swipe__card:not(.inactive)')) {
      if (animating) return;

      card = e.target.closest('.swipe__card');
      cardReject = card.querySelector(".swipe__choice.m--reject");
      cardLike = card.querySelector(".swipe__choice.m--like");
      var startX = e.pageX;

      function moveHandler(e) {
        var x = e.pageX;
        pullDeltaX = (x - startX);
        if (!pullDeltaX) return;
        pullChange();
      }

      function upHandler() {
        document.removeEventListener("mousemove", moveHandler);
        document.removeEventListener("mouseup", upHandler);
        if (!pullDeltaX) return; // prevents from rapid click events
        release();
      }

      document.addEventListener("mousemove", moveHandler);
      document.addEventListener("mouseup", upHandler);
    }
  });

  document.addEventListener("touchstart", function(e) {
    if (e.target.closest('.swipe__card:not(.inactive)')) {
      if (animating) return;

      card = e.target.closest('.swipe__card');
      cardReject = card.querySelector(".swipe__choice.m--reject");
      cardLike = card.querySelector(".swipe__choice.m--like");
      var startX = e.touches[0].pageX;

      function moveHandler(e) {
        var x = e.touches[0].pageX;
        pullDeltaX = (x - startX);
        if (!pullDeltaX) return;
        pullChange();
      }

      function upHandler() {
        document.removeEventListener("touchmove", moveHandler);
        document.removeEventListener("touchend", upHandler);
        if (!pullDeltaX) return; // prevents from rapid click events
        release();
      }

      document.addEventListener("touchmove", moveHandler);
      document.addEventListener("touchend", upHandler);
    }
  });
