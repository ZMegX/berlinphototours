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

//contact form submission event listener

function validateForm(formId, fields) {
  let isValid = true;

  // Clear previous errors
  fields.forEach(field => {
    const errorEl = document.getElementById(`${formId}${field}Error`);
    if (errorEl) errorEl.style.display = 'none';
  });

  // Loop through fields and validate
  fields.forEach(field => {
    const input = document.getElementById(`${formId}${field}`);
    const value = input.value.trim();
    const errorEl = document.getElementById(`${formId}${field}Error`);

    if (value === '') {
      errorEl.textContent = `${field.charAt(0).toUpperCase() + field.slice(1)} is required`;
      errorEl.style.display = 'block';
      isValid = false;
      return;
    }

    if (field === 'Email') {
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailPattern.test(value)) {
        errorEl.textContent = 'Valid email is required';
        errorEl.style.display = 'block';
        isValid = false;
      }
    }

    if (field === 'Phone') {
      const phonePattern = /^[0-9]{10}$/;
      if (!phonePattern.test(value)) {
        errorEl.textContent = 'Valid phone number is required';
        errorEl.style.display = 'block';
        isValid = false;
      }
    }
  });

  return isValid;
}
// as the form are on two different webpages I use a if statement
const contactForm = document.getElementById('contactForm');
if (contactForm) {
  contactForm.addEventListener('submit', function (event) {
    event.preventDefault();
    const isValid = validateForm('contact', ['Name', 'Email', 'Phone', 'Message']);
    if (isValid) {
      alert('Contact form submitted!');
    }
  });
}

const orderForm = document.getElementById('orderForm');
if (orderForm) {
  orderForm.addEventListener('submit', function (event) {
    event.preventDefault();
    const isValid = validateForm('order', ['Name', 'Email', 'Phone']);
    if (isValid) {
      alert('Order form submitted!');
    }
  });
}

