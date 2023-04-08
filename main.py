import os
import requests
import time
baseurl = "https://austry-html.vercel.app/"
paths = ["assets/vendors/jquery/jquery-3.6.0.min.js","assets/vendors/bootstrap/js/bootstrap.bundle.min.js","assets/vendors/jarallax/jarallax.min.js","assets/vendors/jquery-ajaxchimp/jquery.ajaxchimp.min.js","assets/vendors/odometer/odometer.min.js","assets/vendors/swiper/swiper.min.js","assets/vendors/tiny-slider/tiny-slider.min.js","assets/vendors/wnumb/wNumb.min.js","assets/vendors/wow/wow.js","assets/vendors/isotope/isotope.js","assets/vendors/jquery-appear/jquery.appear.min.js","assets/vendors/jquery-circle-progress/jquery.circle-progress.min.js","assets/vendors/jquery-magnific-popup/jquery.magnific-popup.min.js","assets/vendors/jquery-validate/jquery.validate.min.js","assets/vendors/nouislider/nouislider.min.js","assets/vendors/countdown/countdown.min.js","assets/vendors/owl-carousel/owl.carousel.min.js","assets/vendors/bxslider/jquery.bxslider.min.js","assets/vendors/bootstrap-select/js/bootstrap-select.min.js","assets/vendors/vegas/vegas.min.js","assets/vendors/jquery-ui/jquery-ui.js","assets/vendors/timepicker/timePicker.js","assets/vendors/circleType/jquery.circleType.js","assets/vendors/circleType/jquery.lettering.min.js","assets/vendors/sidebar-content/jquery-sidebar-content.js","assets/js/austry.js","assets/vendors/bootstrap/css/bootstrap.min.css","assets/vendors/animate/animate.min.css","assets/vendors/animate/custom-animate.css","assets/vendors/fontawesome/css/all.min.css","assets/vendors/jarallax/jarallax.css","assets/vendors/jquery-magnific-popup/jquery.magnific-popup.css","assets/vendors/nouislider/nouislider.min.css","assets/vendors/nouislider/nouislider.pips.css","assets/vendors/odometer/odometer.min.css","assets/vendors/swiper/swiper.min.css","assets/vendors/austry-icons/style.css","assets/vendors/tiny-slider/tiny-slider.min.css","assets/vendors/reey-font/stylesheet.css","assets/vendors/owl-carousel/owl.carousel.min.css","assets/vendors/owl-carousel/owl.theme.default.min.css","assets/vendors/bxslider/jquery.bxslider.css","assets/vendors/bootstrap-select/css/bootstrap-select.min.css","assets/vendors/vegas/vegas.min.css","assets/vendors/jquery-ui/jquery-ui.css","assets/vendors/timepicker/timePicker.css","assets/css/austry.css","assets/css/austry-responsive.css"]
print(f"Total tasks: {len(paths)}")
start_time = time.time()
counter = 0
for path in paths:
    os.makedirs(os.path.dirname(path),exist_ok=True)
    url = baseurl + path
    response = requests.get(url)
    with open(path, "w") as f:
        f.write(response.text)
        f.close()
    counter += 1
    print(f"done {counter}")
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Total time for completion: {elapsed_time}")
    
    
    
    
    