// Three.js setup
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
  75,
  window.innerWidth / window.innerHeight,
  0.1,
  1000
);
const renderer = new THREE.WebGLRenderer({
  canvas: document.querySelector('#bg'),
  alpha: true,
});

renderer.setPixelRatio(window.devicePixelRatio);
renderer.setSize(window.innerWidth, window.innerHeight);
camera.position.setZ(30);

// Create animated background
function addStar() {
  const geometry = new THREE.SphereGeometry(0.25, 24, 24);
  const material = new THREE.MeshStandardMaterial({ color: 0xffffff });
  const star = new THREE.Mesh(geometry, material);

  const [x, y, z] = Array(3)
    .fill()
    .map(() => THREE.MathUtils.randFloatSpread(100));
  star.position.set(x, y, z);
  scene.add(star);
}

// Add multiple stars
Array(200).fill().forEach(addStar);

// Add lights
const pointLight = new THREE.PointLight(0xffffff);
pointLight.position.set(5, 5, 5);
const ambientLight = new THREE.AmbientLight(0xffffff);
scene.add(pointLight, ambientLight);

// Create torus
const geometry = new THREE.TorusGeometry(10, 3, 16, 100);
const material = new THREE.MeshStandardMaterial({ color: 0xff6347 });
const torus = new THREE.Mesh(geometry, material);
scene.add(torus);

// Create floating animation for stars
function moveStars() {
  const stars = scene.children.filter(
    (child) => child.geometry && child.geometry.type === 'SphereGeometry'
  );
  stars.forEach((star) => {
    star.position.y += Math.sin(Date.now() * 0.001 + star.position.x) * 0.01;
  });
}

// Animation loop
function animate() {
  requestAnimationFrame(animate);

  torus.rotation.x += 0.01;
  torus.rotation.y += 0.005;
  torus.rotation.z += 0.01;

  moveStars();

  // Rotate camera slightly based on mouse position
  const mouseX = (event.clientX - window.innerWidth / 2) * 0.0002;
  const mouseY = (event.clientY - window.innerHeight / 2) * 0.0002;

  camera.position.x += (mouseX - camera.position.x) * 0.05;
  camera.position.y += (-mouseY - camera.position.y) * 0.05;

  renderer.render(scene, camera);
}

// Add mouse move event listener
document.addEventListener('mousemove', onMouseMove);

function onMouseMove(event) {
  mouseX = event.clientX - window.innerWidth / 2;
  mouseY = event.clientY - window.innerHeight / 2;
}

animate();

// Make it responsive
window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});

// Smooth scrolling for navigation
function scrollToSection(sectionId) {
  const section = document.getElementById(sectionId);
  section.scrollIntoView({ behavior: 'smooth' });
}

// Form submission
document.querySelector('form').addEventListener('submit', function (e) {
  e.preventDefault();
  const name = this.querySelector('input[type="text"]').value;
  const email = this.querySelector('input[type="email"]').value;
  const message = this.querySelector('textarea').value;

  // Here you can add your form submission logic
  console.log('Form submitted:', { name, email, message });

  // Clear form
  this.reset();
  alert('Message sent successfully!');
});

// Project card hover effects
document.querySelectorAll('.project-card').forEach((card) => {
  card.addEventListener('mouseenter', function () {
    this.style.transform = 'translateY(-10px)';
  });

  card.addEventListener('mouseleave', function () {
    this.style.transform = 'translateY(0)';
  });
});

// Add active class to current navigation item
const navLinks = document.querySelectorAll('nav ul li a');
window.addEventListener('scroll', () => {
  let current = '';

  document.querySelectorAll('section').forEach((section) => {
    const sectionTop = section.offsetTop;
    if (pageYOffset >= sectionTop - 60) {
      current = section.getAttribute('id');
    }
  });

  navLinks.forEach((link) => {
    link.classList.remove('active');
    if (link.getAttribute('href').substring(1) === current) {
      link.classList.add('active');
    }
  });
});
