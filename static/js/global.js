//NavBar Animation
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
  
  AOS.init({
    offset: 120
  });


  //ChatBot
  (function(){var js,fs,d=document,id="tars-widget-script",b="https://tars-file-upload.s3.amazonaws.com/bulb/";if(!d.getElementById(id)){js=d.createElement("script");js.id=id;js.type="text/javascript";js.src=b+"js/widget.js";fs=d.getElementsByTagName("script")[0];fs.parentNode.insertBefore(js,fs)}})();window.tarsSettings = {"convid":"DY0m2X"};