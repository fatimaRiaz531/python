import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

# Page config
st.set_page_config(
    page_title="Fatima's Portfolio",
    page_icon="��",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom Theme
st.markdown("""
<style>
    /* Custom Theme */
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at 50% 50%, #1a1a2e, #16213e, #0f172a);
    }
</style>
""", unsafe_allow_html=True)

# Animated Background
st.markdown("""
<div class="background">
    <span></span><span></span><span></span>
    <span></span><span></span><span></span>
    <span></span><span></span><span></span>
    <span></span><span></span><span></span>
    <span></span><span></span><span></span>
</div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-container">
    <div class="hero-content">
        <div class="hero-text">
            <h1 class="glitch-text" data-text="Fatima">Fatima</h1>
            <div class="animated-text">
                <span class="text first-text">I'm a</span>
                <span class="text sec-text">Frontend Developer</span>
            </div>
            <p class="hero-description">
                Crafting modern web experiences with cutting-edge technologies
            </p>
        </div>
        <div class="skills-container">
            <div class="skill-pill">⚡ HTML & CSS</div>
            <div class="skill-pill">🎨 Figma Design</div>
            <div class="skill-pill">📱 TypeScript</div>
            <div class="skill-pill">⚛️ Next.js</div>
            <div class="skill-pill">🐍 Python</div>
            <div class="skill-pill">🤖 AI Development</div>
        </div>
        <div class="cta-container">
            <a href="#contact" class="cta-button primary">Get In Touch</a>
            <a href="#projects" class="cta-button secondary">View Projects</a>
        </div>
    </div>
    <div class="hero-visual">
        <div class="cube-container">
            <div class="cube">
                <div class="face front">Frontend</div>
                <div class="face back">Backend</div>
                <div class="face right">Design</div>
                <div class="face left">AI</div>
                <div class="face top">Python</div>
                <div class="face bottom">Next.js</div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# About Section
st.markdown("""
<div class="about-section">
    <h2 class="section-title">About Me</h2>
    <div class="about-content">
        <p>
            I'm a passionate Frontend Developer with a keen eye for design and user experience. 
            My expertise includes building responsive websites and web applications using modern 
            technologies like Next.js and TypeScript. I also create intuitive UI designs using Figma.
        </p>
        <p>
            Currently, I'm expanding my skills into Python development and exploring the exciting 
            world of AI, particularly focusing on Agentic AI and machine learning applications.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# Projects Section
st.markdown("""
<div class="projects-section">
    <h2 class="section-title">Featured Projects</h2>
    <div class="projects-grid">
        <div class="project-card">
            <div class="project-content">
                <h3>Social Media Platform</h3>
                <p>A full-stack social media application with real-time features</p>
                <div class="tech-stack">
                    <span>Next.js</span>
                    <span>TypeScript</span>
                    <span>Tailwind</span>
                </div>
                <div class="project-links">
                    <a href="https://social-media-app-next-js-orcin.vercel.app/" target="_blank">Live Demo</a>
                    <a href="https://github.com/fatimaRiaz531/Social-Media-App-NextJS.git" target="_blank">Source Code</a>
                </div>
            </div>
        </div>
       <div class="project-card">
            <div class="project-content">
                <h3>Ecommerce Website</h3>
                <p>A full-stack Ecommerce Website</p>
                <div class="tech-stack">
                    <span>Next.js</span>
                    <span>TypeScript</span>
                    <span>Tailwind</span>
                </div>
                <div class="project-links">
                    <a href="https://hackathon2-figma-website-nfmd.vercel.app/" target="_blank">Live Demo</a>
                    <a href="https://github.com/fatimaRiaz531/hackathon2-figma-website.git" target="_blank">Source Code</a>
                </div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Skills Section
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<div class="skills-section">
    <h2 class="section-title">My Skills</h2>
    <div class="skills-grid">
        <div class="skill-card">
            <div class="skill-icon">
                <i class="fab fa-html5"></i>
            </div>
            <h3>HTML/CSS</h3>
            <div class="skill-level">95%</div>
        </div>
        
        <div class="skill-card">
            <div class="skill-icon">
                <i class="fab fa-figma"></i>
            </div>
            <h3>Figma</h3>
            <div class="skill-level">90%</div>
        </div>
        
        <div class="skill-card">
            <div class="skill-icon">
                <i class="fab fa-react"></i>
            </div>
            <h3>Next.js</h3>
            <div class="skill-level">85%</div>
        </div>
        
        <div class="skill-card">
            <div class="skill-icon">
                <i class="fab fa-js"></i>
            </div>
            <h3>TypeScript</h3>
            <div class="skill-level">80%</div>
        </div>
        
        <div class="skill-card">
            <div class="skill-icon">
                <i class="fab fa-python"></i>
            </div>
            <h3>Python</h3>
            <div class="skill-level">Learning</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Contact Section
st.markdown("""
<div class="contact-section">
    <h2 class="section-title">Get In Touch</h2>
    <div class="contact-container">
        <form class="contact-form">
            <input type="text" placeholder="Your Name" required>
            <input type="email" placeholder="Your Email" required>
            <textarea placeholder="Your Message" required></textarea>
            <button type="submit">Send Message</button>
        </form>
        <div class="social-links">
            <a href="https://github.com/fatimaRiaz531" target="_blank">
                <i class="fab fa-github"></i>
            </a>
            <a href="mailto:your.email@example.com">
                <i class="fas fa-envelope"></i>
            </a>
            <a href="https://linkedin.com/in/yourprofile" target="_blank">
                <i class="fab fa-linkedin"></i>
            </a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Custom CSS
st.markdown(
    """
    <style>
    .gradient-text {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 4rem !important;
        font-weight: 800 !important;
        margin-bottom: 2rem;
    }
    
    .intro-text {
        font-size: 1.2rem;
        line-height: 1.6;
        color: #E0E0E0;
    }
    
    .cta-buttons {
        display: flex;
        gap: 1rem;
        margin-top: 2rem;
    }
    
    .cta-primary, .cta-secondary {
        padding: 0.8rem 1.5rem;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .cta-primary {
        background: linear-gradient(45deg, #FF6B6B, #FF8E53);
        color: white;
    }
    
    .cta-secondary {
        background: rgba(255, 255, 255, 0.1);
        color: white;
        border: 2px solid rgba(255, 255, 255, 0.2);
    }
    
    .cta-primary:hover, .cta-secondary:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
    }

    .project-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 2rem;
        border-radius: 15px;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
        margin-bottom: 1rem;
    }

    .project-card:hover {
        transform: translateY(-5px);
        background: rgba(255, 255, 255, 0.1);
    }

    .project-card h3 {
        color: #4ECDC4;
        margin-bottom: 1rem;
    }

    .project-links {
        margin-top: 1rem;
        display: flex;
        gap: 1rem;
    }

    .project-links a {
        color: #FF6B6B;
        text-decoration: none;
        font-weight: bold;
    }

    .project-links a:hover {
        text-decoration: underline;
    }

    .section-title {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2rem;
        font-weight: 800;
        margin-bottom: 2rem;
    }

    .skill-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 2rem;
        border-radius: 15px;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
        margin-bottom: 1rem;
    }

    .skill-card:hover {
        transform: translateY(-5px);
        background: rgba(255, 255, 255, 0.1);
    }

    .skill-icon {
        font-size: 2rem;
        margin-bottom: 1rem;
    }

    .skill-bar {
        background: rgba(255, 255, 255, 0.2);
        height: 20px;
        border-radius: 10px;
        overflow: hidden;
    }

    .skill-progress {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        height: 100%;
        transition: width 0.3s ease;
    }

    .skill-list {
        list-style: none;
        padding-left: 0;
    }

    .skill-list li {
        margin-bottom: 0.5rem;
    }

    .contact-container {
        display: flex;
        gap: 2rem;
    }

    .contact-form {
        flex: 1;
    }

    .form-group {
        position: relative;
        margin-bottom: 2rem;
    }

    .focus-border {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 2px;
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        transform: scaleX(0);
        transform-origin: left;
        transition: transform 0.3s ease;
    }

    .form-group input:focus ~ .focus-border,
    .form-group textarea:focus ~ .focus-border {
        transform: scaleX(1);
    }

    .submit-btn {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        color: white;
        padding: 0.8rem 1.5rem;
        border-radius: 8px;
        border: none;
        font-weight: bold;
        transition: all 0.3s ease;
    }

    .submit-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
    }

    .social-links {
        display: flex;
        gap: 1rem;
    }

    .social-icon {
        color: #4ECDC4;
        font-size: 1.5rem;
        transition: color 0.3s ease;
    }

    .social-icon:hover {
        color: #FF6B6B;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load custom CSS
with open('assets/styles/style.css', 'r') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True) 