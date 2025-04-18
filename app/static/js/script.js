// function headerImage (){
//     let img = document.createElement('img');
//     img.src = "https://picsum.photos/200/300";
//     document.getElementById('header').appendChild(img);
//     res.innerHTML = "Image Element added.";

// } 
    //mainhtml code
    const animation_elements = document.querySelectorAll('.animate-on-scroll');

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('animate');
        } else {
          entry.target.classList.toggle('animate');
        }
      })
    }, {
      threshold: 0.5
    });

    for (let i=0; i < animation_elements.length; i++) {
      const el = animation_elements[i];

      observer.observe(el);
    };


    let slideIndex = 1;
      showSlides(slideIndex);

    // Next/previous controls
    function plusSlides(n) {
      showSlides(slideIndex += n);
    }

    // Thumbnail image controls
    function currentSlide(n) {
      showSlides(slideIndex = n);
    }

    function showSlides(n) {
      let i;
      let slides = document.getElementsByClassName("mySlides");
      let dots = document.getElementsByClassName("demo");
      let captionText = document.getElementById("caption");
      if (n > slides.length) {slideIndex = 1}
      if (n < 1) {slideIndex = slides.length}
      for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
      }
      for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
      }
      slides[slideIndex-1].style.display = "block";
      dots[slideIndex-1].className += " active"; 
      captionText.innerHTML = dots[slideIndex-1].alt;
    } 

    document.addEventListener("keydown", (event) => {
      if (event.key === "ArrowRight") {
        plusSlides(1);
      } else if (event.key === "ArrowLeft") {
        plusSlides(-1);
      }
    });

//contact form submission event listener
document.getElementById('contactForm').addEventListener('submit', function (event) {
    event.preventDefault();
    
    // Clear previous errors
    const errorElements = document.querySelectorAll('.error-message');
    errorElements.forEach(el => el.style.display = 'none');
    
    // Get form values
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const phone = document.getElementById('phone').value.trim();
    const message = document.getElementById('message').value.trim();
    
    // Validation flags
    let isValid = true;
    
    // Name validation
    if (name === '') {
        document.getElementById('nameError').textContent = 'Name is required';
        document.getElementById('nameError').style.display = 'block';
        isValid = false;
    }
    
    // Email validation
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (email === '' || !emailPattern.test(email)) {
        document.getElementById('emailError').textContent = 'Valid email is required';
        document.getElementById('emailError').style.display = 'block';
        isValid = false;
    }
    
    // Phone validation
    const phonePattern = /^[0-9]{10}$/;
    if (phone === '' || !phonePattern.test(phone)) {
        document.getElementById('phoneError').textContent = 'Valid phone number is required';
        document.getElementById('phoneError').style.display = 'block';
        isValid = false;
    }
    
    // Message validation
    if (message === '') {
        document.getElementById('messageError').textContent = 'Message is required';
        document.getElementById('messageError').style.display = 'block';
        isValid = false;
    }
    
    // If form is valid, you can submit it or perform any other action
    if (isValid) {
        alert('Form submitted successfully!');
    }
    });

    document.getElementById('orderForm').addEventListener('submit', function (event) {
      event.preventDefault();
      
      // Clear previous errors
      const errorElements = document.querySelectorAll('.error-message');
      errorElements.forEach(el => el.style.display = 'none');
      
      // Get form values
      const name = document.getElementById('name').value.trim();
      const email = document.getElementById('email').value.trim();
      const phone = document.getElementById('phone').value.trim();

      // Validation flags
      let isValid = true;
      
      // Name validation
      if (name === '') {
          document.getElementById('nameError').textContent = 'Name is required';
          document.getElementById('nameError').style.display = 'block';
          isValid = false;
      }
      
      // Email validation
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (email === '' || !emailPattern.test(email)) {
          document.getElementById('emailError').textContent = 'Valid email is required';
          document.getElementById('emailError').style.display = 'block';
          isValid = false;
      }
      
      // Phone validation
      const phonePattern = /^[0-9]{10}$/;
      if (phone === '' || !phonePattern.test(phone)) {
          document.getElementById('phoneError').textContent = 'Valid phone number is required';
          document.getElementById('phoneError').style.display = 'block';
          isValid = false;
      }

      
      // If form is valid, you can submit it or perform any other action
      if (isValid) {
          alert('orderForm submitted successfully!');
      }
      });
  
  