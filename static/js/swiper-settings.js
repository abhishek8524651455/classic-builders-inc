const testimonialSwiper = new Swiper(".testimonials-swiper", {
  slidesPerView: 1,
  loop: true,
  navigation: {
    nextEl: ".testimonials-arrow-right",
    prevEl: ".testimonials-arrow-left",
  },
  breakpoints: {
    1321: {
      slidesPerView: 2,
    },
  },
});

const swiper = new Swiper(".mySwiper", {
  slidesPerView: 1,
  grabCursor: true,
  loop: true,
  autoplay: {
    delay: 2000,
    disableOnInteraction: false,
  },
  breakpoints: {
    750: {
      slidesPerView: 2,
    },
  },
});
