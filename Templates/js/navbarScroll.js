window.onscroll = function () {
    scrollFunction();
  };

  function scrollFunction() {
    if (
      document.body.scrollTop > 80 ||
      document.documentElement.scrollTop > 80
    ) {
      document.getElementById("navbar").style.padding = "10px 0px";
      document.getElementById("navbar").style.transitionDuration = "0.6s";
    } else {
        document.getElementById("navbar").style.padding = "30px 0px";
    }
  }