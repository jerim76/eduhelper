<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EduHelper - AI Homework Assistance</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Poppins', sans-serif;
        }
        
        :root {
            --primary: #4361ee;
            --secondary: #3a0ca3;
            --accent: #f72585;
            --light: #4cc9f0;
            --dark: #1d3557;
            --background: #f8f9fa;
            --card: #ffffff;
        }
        
        body {
            background: linear-gradient(135deg, #f0f4ff 0%, #e6f7ff 100%);
            min-height: 100vh;
            color: var(--dark);
            overflow-x: hidden;
        }
        
        /* Header & Navigation */
        header {
            background: linear-gradient(90deg, var(--primary) 0%, var(--secondary) 100%);
            color: white;
            padding: 15px 5%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            position: sticky;
            top: 0;
            z-index: 1000;
        }
        
        .logo {
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 24px;
            font-weight: 700;
        }
        
        .logo i {
            background: var(--accent);
            width: 45px;
            height: 45px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 10px rgba(247, 37, 133, 0.3);
        }
        
        nav ul {
            display: flex;
            list-style: none;
            gap: 30px;
        }
        
        nav a {
            color: white;
            text-decoration: none;
            font-weight: 500;
            font-size: 18px;
            padding: 8px 15px;
            border-radius: 30px;
            transition: all 0.3s ease;
        }
        
        nav a:hover, nav a.active {
            background: rgba(255, 255, 255, 0.2);
        }
        
        .auth-buttons {
            display: flex;
            gap: 15px;
        }
        
        .btn {
            padding: 12px 28px;
            border-radius: 30px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            border: none;
            font-size: 16px;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }
        
        .btn-primary {
            background: var(--accent);
            color: white;
            box-shadow: 0 4px 15px rgba(247, 37, 133, 0.4);
        }
        
        .btn-primary:hover {
            background: #d81b60;
            transform: translateY(-3px);
        }
        
        .btn-outline {
            background: transparent;
            border: 2px solid white;
            color: white;
        }
        
        .btn-outline:hover {
            background: rgba(255, 255, 255, 0.2);
            transform: translateY(-3px);
        }
        
        /* Page Sections */
        .page {
            display: none;
            padding: 40px 5%;
            min-height: 80vh;
        }
        
        .page.active {
            display: block;
            animation: fadeIn 0.5s ease;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        /* Home Page */
        .hero {
            display: flex;
            align-items: center;
            gap: 50px;
            padding: 60px 0;
        }
        
        .hero-content {
            flex: 1;
        }
        
        .hero h1 {
            font-size: 48px;
            line-height: 1.2;
            margin-bottom: 20px;
            color: var(--secondary);
        }
        
        .hero p {
            font-size: 20px;
            margin-bottom: 30px;
            color: var(--dark);
            opacity: 0.9;
        }
        
        .hero-image {
            flex: 1;
            display: flex;
            justify-content: center;
        }
        
        .hero-image img {
            max-width: 100%;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(67, 97, 238, 0.2);
        }
        
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin: 80px 0;
        }
        
        .feature-card {
            background: var(--card);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease;
            text-align: center;
        }
        
        .feature-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 40px rgba(67, 97, 238, 0.15);
        }
        
        .feature-card i {
            font-size: 48px;
            color: var(--primary);
            margin-bottom: 20px;
            background: rgba(67, 97, 238, 0.1);
            width: 90px;
            height: 90px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .feature-card h3 {
            font-size: 24px;
            margin-bottom: 15px;
            color: var(--secondary);
        }
        
        /* Products & Services Page */
        .products-header {
            text-align: center;
            max-width: 800px;
            margin: 0 auto 60px;
        }
        
        .products-header h2 {
            font-size: 42px;
            color: var(--secondary);
            margin-bottom: 20px;
        }
        
        .pricing-plans {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin: 40px 0;
        }
        
        .pricing-card {
            background: var(--card);
            border-radius: 20px;
            padding: 40px 30px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
            text-align: center;
            position: relative;
            overflow: hidden;
            transition: all 0.3s ease;
        }
        
        .pricing-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 40px rgba(67, 97, 238, 0.15);
        }
        
        .pricing-card.popular {
            border: 3px solid var(--accent);
            transform: scale(1.05);
        }
        
        .popular-badge {
            position: absolute;
            top: 20px;
            right: -40px;
            background: var(--accent);
            color: white;
            padding: 5px 40px;
            transform: rotate(45deg);
            font-weight: 600;
            font-size: 14px;
        }
        
        .price {
            font-size: 48px;
            font-weight: 700;
            color: var(--primary);
            margin: 20px 0;
        }
        
        .price span {
            font-size: 24px;
            color: var(--dark);
            opacity: 0.7;
        }
        
        .pricing-features {
            list-style: none;
            text-align: left;
            margin: 30px 0;
            padding: 0 20px;
        }
        
        .pricing-features li {
            padding: 12px 0;
            border-bottom: 1px solid rgba(0, 0, 0, 0.05);
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .pricing-features li i {
            color: var(--accent);
        }
        
        /* Authentication Page */
        .auth-container {
            display: flex;
            max-width: 1000px;
            margin: 0 auto;
            background: var(--card);
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        }
        
        .auth-image {
            flex: 1;
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 40px;
        }
        
        .auth-image img {
            max-width: 100%;
        }
        
        .auth-form {
            flex: 1;
            padding: 50px;
        }
        
        .auth-tabs {
            display: flex;
            margin-bottom: 30px;
            border-bottom: 2px solid rgba(0, 0, 0, 0.1);
        }
        
        .auth-tab {
            padding: 15px 30px;
            cursor: pointer;
            font-weight: 600;
            font-size: 18px;
            color: var(--dark);
            opacity: 0.7;
            transition: all 0.3s ease;
        }
        
        .auth-tab.active {
            color: var(--primary);
            opacity: 1;
            border-bottom: 3px solid var(--primary);
        }
        
        .form-group {
            margin-bottom: 25px;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 500;
            color: var(--dark);
        }
        
        .form-control {
            width: 100%;
            padding: 15px 20px;
            border: 2px solid #e0e0e0;
            border-radius: 12px;
            font-size: 16px;
            transition: all 0.3s ease;
        }
        
        .form-control:focus {
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(67, 97, 238, 0.2);
        }
        
        .remember-forgot {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 25px;
        }
        
        .remember {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .forgot-link {
            color: var(--primary);
            text-decoration: none;
            font-weight: 500;
        }
        
        /* Chatbot Page */
        .chatbot-container {
            max-width: 1200px;
            margin: 0 auto;
            background: var(--card);
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            display: flex;
            height: 75vh;
        }
        
        .info-panel {
            flex: 0 0 30%;
            background: linear-gradient(160deg, var(--primary) 0%, var(--secondary) 100%);
            color: white;
            padding: 30px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        
        .token-info {
            background: rgba(255, 255, 255, 0.15);
            border-radius: 15px;
            padding: 20px;
            text-align: center;
            margin-top: auto;
        }
        
        .token-count {
            font-size: 32px;
            font-weight: bold;
            color: var(--accent);
            margin: 10px 0;
        }
        
        .chat-panel {
            flex: 0 0 70%;
            display: flex;
            flex-direction: column;
            background: var(--background);
        }
        
        .chat-header {
            background: var(--card);
            padding: 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 3px 10px rgba(0, 0, 0, 0.05);
        }
        
        .curriculum-selector {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .curriculum-selector select {
            padding: 10px 15px;
            border-radius: 20px;
            border: 2px solid var(--primary);
            background: white;
            font-weight: bold;
            color: var(--primary);
        }
        
        .chat-container {
            flex: 1;
            padding: 20px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 15px;
        }
        
        .message {
            max-width: 85%;
            padding: 15px 20px;
            border-radius: 20px;
            position: relative;
            animation: fadeIn 0.3s ease;
        }
        
        .ai-message {
            background: white;
            border: 2px solid #e9ecef;
            border-bottom-left-radius: 5px;
            align-self: flex-start;
            box-shadow: 0 3px 10px rgba(0, 0, 0, 0.03);
        }
        
        .user-message {
            background: linear-gradient(90deg, var(--primary) 0%, var(--secondary) 100%);
            color: white;
            border-bottom-right-radius: 5px;
            align-self: flex-end;
        }
        
        .visual-explanation {
            background: #e3f2fd;
            border-left: 4px solid #2196f3;
            padding: 15px;
            margin-top: 10px;
            border-radius: 0 12px 12px 0;
            font-size: 15px;
        }
        
        .input-area {
            padding: 20px;
            background: var(--card);
            display: flex;
            gap: 15px;
            box-shadow: 0 -3px 10px rgba(0, 0, 0, 0.05);
        }
        
        .input-group {
            flex: 1;
            display: flex;
            gap: 10px;
        }
        
        textarea {
            flex: 1;
            padding: 15px 20px;
            border: 2px solid #e9ecef;
            border-radius: 20px;
            resize: none;
            font-size: 16px;
            transition: border-color 0.3s;
            height: 60px;
        }
        
        textarea:focus {
            outline: none;
            border-color: var(--primary);
        }
        
        .upload-btn {
            background: var(--light);
            color: white;
            border: none;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 20px;
            align-self: flex-end;
        }
        
        .send-btn {
            background: var(--accent);
            color: white;
            border: none;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 20px;
            align-self: flex-end;
            box-shadow: 0 5px 15px rgba(247, 37, 133, 0.4);
        }
        
        .image-preview {
            max-width: 150px;
            border-radius: 15px;
            margin-top: 10px;
            border: 2px dashed var(--primary);
            display: none;
        }
        
        .loader {
            display: flex;
            justify-content: center;
            padding: 15px;
        }
        
        .loader-dot {
            width: 12px;
            height: 12px;
            background: var(--primary);
            border-radius: 50%;
            margin: 0 5px;
            animation: bounce 1s infinite;
        }
        
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
        
        /* Contact Section */
        .contact-section {
            max-width: 1200px;
            margin: 60px auto;
            padding: 40px;
            background: var(--card);
            border-radius: 20px;
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.1);
        }
        
        .contact-header {
            text-align: center;
            margin-bottom: 50px;
        }
        
        .contact-header h2 {
            font-size: 42px;
            color: var(--secondary);
            margin-bottom: 15px;
        }
        
        .contact-header p {
            font-size: 20px;
            color: var(--dark);
            max-width: 700px;
            margin: 0 auto;
        }
        
        .contact-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 40px;
        }
        
        .contact-info {
            padding: 30px;
            background: rgba(67, 97, 238, 0.05);
            border-radius: 15px;
            border-left: 4px solid var(--primary);
        }
        
        .contact-info h3 {
            font-size: 28px;
            margin-bottom: 25px;
            color: var(--secondary);
        }
        
        .contact-item {
            display: flex;
            align-items: flex-start;
            gap: 15px;
            margin-bottom: 25px;
        }
        
        .contact-icon {
            background: var(--primary);
            color: white;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
        }
        
        .contact-details h4 {
            font-size: 20px;
            margin-bottom: 5px;
            color: var(--dark);
        }
        
        .contact-details p, .contact-details a {
            font-size: 18px;
            color: var(--dark);
            text-decoration: none;
            transition: color 0.3s;
        }
        
        .contact-details a:hover {
            color: var(--primary);
        }
        
        .contact-form {
            padding: 30px;
            background: white;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
        }
        
        .contact-form h3 {
            font-size: 28px;
            margin-bottom: 25px;
            color: var(--secondary);
        }
        
        /* Footer */
        footer {
            background: var(--dark);
            color: white;
            padding: 50px 5% 20px;
            margin-top: 80px;
        }
        
        .footer-content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 40px;
            margin-bottom: 40px;
        }
        
        .footer-column h3 {
            font-size: 22px;
            margin-bottom: 25px;
            color: var(--light);
        }
        
        .footer-column ul {
            list-style: none;
        }
        
        .footer-column li {
            margin-bottom: 15px;
        }
        
        .footer-column a {
            color: #c0c0c0;
            text-decoration: none;
            transition: color 0.3s;
        }
        
        .footer-column a:hover {
            color: white;
        }
        
        .social-icons {
            display: flex;
            gap: 15px;
            margin-top: 20px;
        }
        
        .social-icons a {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.1);
            color: white;
            transition: all 0.3s;
        }
        
        .social-icons a:hover {
            background: var(--primary);
            transform: translateY(-3px);
        }
        
        .copyright {
            text-align: center;
            padding-top: 30px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            color: #a0a0a0;
        }
        
        /* Responsive Design */
        @media (max-width: 992px) {
            .hero {
                flex-direction: column;
                text-align: center;
            }
            
            .auth-container {
                flex-direction: column;
            }
            
            .chatbot-container {
                flex-direction: column;
                height: auto;
            }
            
            nav ul {
                gap: 15px;
            }
        }
        
        @media (max-width: 768px) {
            header {
                flex-direction: column;
                gap: 20px;
            }
            
            nav ul {
                flex-wrap: wrap;
                justify-content: center;
            }
            
            .auth-form {
                padding: 30px;
            }
            
            .hero h1 {
                font-size: 36px;
            }
        }
    </style>
</head>
<body>
    <!-- Header -->
    <header>
        <div class="logo">
            <i class="fas fa-graduation-cap"></i>
            <span>EduHelper</span>
        </div>
        <nav>
            <ul>
                <li><a href="#" class="nav-link active" data-page="home">Home</a></li>
                <li><a href="#" class="nav-link" data-page="products">Products & Services</a></li>
                <li><a href="#" class="nav-link" data-page="chatbot">Homework Helper</a></li>
                <li><a href="#" class="nav-link" data-page="contact">Contact Us</a></li>
                <li><a href="#" class="nav-link" data-page="auth">Sign In</a></li>
            </ul>
        </nav>
        <div class="auth-buttons">
            <button class="btn btn-outline" id="login-btn">Sign In</button>
            <button class="btn btn-primary" id="signup-btn">Sign Up</button>
        </div>
    </header>

    <!-- Home Page -->
    <section id="home" class="page active">
        <div class="hero">
            <div class="hero-content">
                <h1>AI-Powered Homework Help for Busy Parents</h1>
                <p>Get instant explanations for any homework question. Our AI tutor provides step-by-step solutions in simple terms for all subjects and grade levels.</p>
                <div class="hero-buttons">
                    <button class="btn btn-primary" id="try-free-btn">Try Free Now</button>
                    <button class="btn btn-outline" style="border-color: var(--primary); color: var(--primary);">Learn More</button>
                </div>
            </div>
            <div class="hero-image">
                <img src="https://images.unsplash.com/photo-1580582932707-520aed937b7b?auto=format&fit=crop&w=800" alt="Happy student with homework">
            </div>
        </div>
        
        <div class="features">
            <div class="feature-card">
                <i class="fas fa-camera"></i>
                <h3>Snap & Solve</h3>
                <p>Take a picture of any homework problem and get instant step-by-step solutions.</p>
            </div>
            <div class="feature-card">
                <i class="fas fa-robot"></i>
                <h3>AI Tutor</h3>
                <p>Our advanced AI explains concepts in simple terms with real-world examples.</p>
            </div>
            <div class="feature-card">
                <i class="fas fa-book"></i>
                <h3>Curriculum Aligned</h3>
                <p>Content aligned with Kenyan CBC and 8-4-4 curricula for all grade levels.</p>
            </div>
        </div>
    </section>

    <!-- Products & Services Page -->
    <section id="products" class="page">
        <div class="products-header">
            <h2>Our Products & Services</h2>
            <p>Choose the perfect plan to support your child's learning journey</p>
        </div>
        
        <div class="pricing-plans">
            <div class="pricing-card">
                <h3>Basic Plan</h3>
                <div class="price">KES 50<span>/week</span></div>
                <ul class="pricing-features">
                    <li><i class="fas fa-check"></i> 10 questions per week</li>
                    <li><i class="fas fa-check"></i> Math & Science subjects</li>
                    <li><i class="fas fa-check"></i> Text-based questions only</li>
                    <li><i class="fas fa-check"></i> Basic explanations</li>
                    <li><i class="fas fa-times"></i> Image recognition</li>
                    <li><i class="fas fa-times"></i> Swahili support</li>
                </ul>
                <button class="btn btn-outline" style="border-color: var(--primary); color: var(--primary);">Get Started</button>
            </div>
            
            <div class="pricing-card popular">
                <div class="popular-badge">POPULAR</div>
                <h3>Family Plan</h3>
                <div class="price">KES 300<span>/month</span></div>
                <ul class="pricing-features">
                    <li><i class="fas fa-check"></i> Unlimited questions</li>
                    <li><i class="fas fa-check"></i> All subjects included</li>
                    <li><i class="fas fa-check"></i> Image & text questions</li>
                    <li><i class="fas fa-check"></i> Step-by-step solutions</li>
                    <li><i class="fas fa-check"></i> Swahili & English support</li>
                    <li><i class="fas fa-check"></i> Up to 3 children</li>
                </ul>
                <button class="btn btn-primary">Get Started</button>
            </div>
            
            <div class="pricing-card">
                <h3>School Plan</h3>
                <div class="price">KES 15,000<span>/year</span></div>
                <ul class="pricing-features">
                    <li><i class="fas fa-check"></i> Unlimited school access</li>
                    <li><i class="fas fa-check"></i> Teacher dashboard</li>
                    <li><i class="fas fa-check"></i> Progress tracking</li>
                    <li><i class="fas fa-check"></i> Custom curriculum setup</li>
                    <li><i class="fas fa-check"></i> Multi-language support</li>
                    <li><i class="fas fa-check"></i> Priority customer service</li>
                </ul>
                <button class="btn btn-outline" style="border-color: var(--primary); color: var(--primary);">Contact Sales</button>
            </div>
        </div>
    </section>

    <!-- Contact Page -->
    <section id="contact" class="page">
        <div class="contact-section">
            <div class="contact-header">
                <h2>Contact Us</h2>
                <p>Have questions or need support? Reach out to our team anytime - we're here to help!</p>
            </div>
            
            <div class="contact-container">
                <div class="contact-info">
                    <h3>Get In Touch</h3>
                    
                    <div class="contact-item">
                        <div class="contact-icon">
                            <i class="fas fa-phone"></i>
                        </div>
                        <div class="contact-details">
                            <h4>Phone</h4>
                            <p>+254 758 943 430</p>
                        </div>
                    </div>
                    
                    <div class="contact-item">
                        <div class="contact-icon">
                            <i class="fas fa-envelope"></i>
                        </div>
                        <div class="contact-details">
                            <h4>Email</h4>
                            <a href="mailto:owinojerim269@gmail.com">owinojerim269@gmail.com</a>
                        </div>
                    </div>
                    
                    <div class="contact-item">
                        <div class="contact-icon">
                            <i class="fas fa-map-marker-alt"></i>
                        </div>
                        <div class="contact-details">
                            <h4>Location</h4>
                            <p>Nairobi, Kenya</p>
                        </div>
                    </div>
                    
                    <div class="contact-item">
                        <div class="contact-icon">
                            <i class="fas fa-clock"></i>
                        </div>
                        <div class="contact-details">
                            <h4>Working Hours</h4>
                            <p>Monday-Friday: 8AM - 6PM</p>
                            <p>Saturday: 9AM - 1PM</p>
                        </div>
                    </div>
                </div>
                
                <div class="contact-form">
                    <h3>Send Us a Message</h3>
                    <form>
                        <div class="form-group">
                            <label for="contact-name">Your Name</label>
                            <input type="text" id="contact-name" class="form-control" placeholder="Enter your name">
                        </div>
                        
                        <div class="form-group">
                            <label for="contact-email">Email Address</label>
                            <input type="email" id="contact-email" class="form-control" placeholder="Enter your email">
                        </div>
                        
                        <div class="form-group">
                            <label for="contact-subject">Subject</label>
                            <input type="text" id="contact-subject" class="form-control" placeholder="What is this regarding?">
                        </div>
                        
                        <div class="form-group">
                            <label for="contact-message">Message</label>
                            <textarea id="contact-message" class="form-control" placeholder="Type your message here..." rows="5"></textarea>
                        </div>
                        
                        <button type="submit" class="btn btn-primary" style="width: 100%;">Send Message</button>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <!-- Authentication Page -->
    <section id="auth" class="page">
        <div class="auth-container">
            <div class="auth-image">
                <img src="https://images.unsplash.com/photo-1532012197267-da84d127e765?auto=format&fit=crop&w=500" alt="Student studying">
            </div>
            <div class="auth-form">
                <div class="auth-tabs">
                    <div class="auth-tab active" data-tab="login">Sign In</div>
                    <div class="auth-tab" data-tab="signup">Sign Up</div>
                </div>
                
                <div class="tab-content" id="login-tab">
                    <div class="form-group">
                        <label for="login-email">Email Address</label>
                        <input type="email" id="login-email" class="form-control" placeholder="Enter your email">
                    </div>
                    
                    <div class="form-group">
                        <label for="login-password">Password</label>
                        <input type="password" id="login-password" class="form-control" placeholder="Enter your password">
                    </div>
                    
                    <div class="remember-forgot">
                        <div class="remember">
                            <input type="checkbox" id="remember">
                            <label for="remember">Remember me</label>
                        </div>
                        <a href="#" class="forgot-link">Forgot Password?</a>
                    </div>
                    
                    <button class="btn btn-primary" style="width: 100%;">Sign In</button>
                    
                    <div style="text-align: center; margin-top: 20px;">
                        <p>Or sign in with</p>
                        <div class="social-icons" style="justify-content: center;">
                            <a href="#"><i class="fab fa-google"></i></a>
                            <a href="#"><i class="fab fa-facebook-f"></i></a>
                            <a href="#"><i class="fab fa-microsoft"></i></a>
                        </div>
                    </div>
                </div>
                
                <div class="tab-content" id="signup-tab" style="display: none;">
                    <div class="form-group">
                        <label for="signup-name">Full Name</label>
                        <input type="text" id="signup-name" class="form-control" placeholder="Enter your full name">
                    </div>
                    
                    <div class="form-group">
                        <label for="signup-email">Email Address</label>
                        <input type="email" id="signup-email" class="form-control" placeholder="Enter your email">
                    </div>
                    
                    <div class="form-group">
                        <label for="signup-password">Password</label>
                        <input type="password" id="signup-password" class="form-control" placeholder="Create a password">
                    </div>
                    
                    <div class="form-group">
                        <label for="signup-confirm">Confirm Password</label>
                        <input type="password" id="signup-confirm" class="form-control" placeholder="Confirm your password">
                    </div>
                    
                    <div class="form-group">
                        <input type="checkbox" id="terms">
                        <label for="terms">I agree to the <a href="#" style="color: var(--primary);">Terms of Service</a> and <a href="#" style="color: var(--primary);">Privacy Policy</a></label>
                    </div>
                    
                    <button class="btn btn-primary" style="width: 100%;">Create Account</button>
                </div>
            </div>
        </div>
    </section>

    <!-- Chatbot Page -->
    <section id="chatbot" class="page">
        <div class="chatbot-container">
            <div class="info-panel">
                <div class="logo" style="font-size: 20px; margin-bottom: 40px;">
                    <i class="fas fa-graduation-cap"></i>
                    <span>Homework Helper</span>
                </div>
                
                <div>
                    <h3>How it Works</h3>
                    <p style="margin: 20px 0; line-height: 1.6;">1. Upload a photo or type your question</p>
                    <p style="margin: 20px 0; line-height: 1.6;">2. Our AI analyzes the problem</p>
                    <p style="margin: 20px 0; line-height: 1.6;">3. Get step-by-step explanation</p>
                </div>
                
                <div class="token-info">
                    <p>Your available tokens:</p>
                    <div class="token-count">15</div>
                    <p>KES 5 per question</p>
                    <button class="btn btn-primary" style="background: white; color: var(--accent); width: 100%; margin-top: 15px;">Buy More Tokens</button>
                </div>
            </div>
            
            <div class="chat-panel">
                <div class="chat-header">
                    <div class="curriculum-selector">
                        <i class="fas fa-book" style="color: var(--primary);"></i>
                        <select id="curriculum-select">
                            <option value="General">CBC Curriculum</option>
                            <option value="CBC">8-4-4 Curriculum</option>
                            <option value="8-4-4">International</option>
                        </select>
                    </div>
                    <div>
                        <span style="color: var(--primary); font-weight: bold;">KES 5/question</span>
                    </div>
                </div>
                
                <div class="chat-container" id="chat-container">
                    <div class="message ai-message">
                        Hello there! 👋 I'm your Homework Helper. Send me any homework question or snap a photo, and I'll explain it in simple terms. 
                        <div class="visual-explanation">
                            <strong>Try asking:</strong><br>
                            "Explain photosynthesis for a 5th grader"<br>
                            "How do I solve 3/4 ÷ 1/2?"<br>
                            "What's the difference between 'their' and 'there'?"
                        </div>
                    </div>
                    
                    <div class="message user-message">
                        Can you explain fractions to my 4th grader?
                    </div>
                    
                    <div class="message ai-message">
                        Of course! Fractions are like pizza slices 🍕. Imagine a pizza cut into 8 equal slices. If you eat 3 slices, you've eaten 3/8 of the pizza. The top number (numerator) is how many slices you have, the bottom number (denominator) is the total slices in the pizza.
                        <div class="visual-explanation">
                            <strong>🍕 Visual Example:</strong><br>
                            1/2 = Half a pizza<br>
                            3/4 = Three quarters of a pizza<br>
                            1/8 = One slice from an 8-slice pizza
                        </div>
                    </div>
                </div>
                
                <div class="input-area">
                    <div class="input-group">
                        <textarea id="question-input" placeholder="Type your question here..."></textarea>
                        <label class="upload-btn" for="image-upload">
                            <i class="fas fa-camera"></i>
                            <input type="file" id="image-upload" accept="image/*" style="display: none;">
                        </label>
                        <button class="send-btn" id="send-btn">
                            <i class="fas fa-paper-plane"></i>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="footer-content">
            <div class="footer-column">
                <h3>EduHelper</h3>
                <p>AI-powered homework assistance for busy parents and students across Kenya.</p>
                <div class="social-icons">
                    <a href="#"><i class="fab fa-facebook-f"></i></a>
                    <a href="#"><i class="fab fa-twitter"></i></a>
                    <a href="#"><i class="fab fa-instagram"></i></a>
                    <a href="#"><i class="fab fa-linkedin-in"></i></a>
                </div>
            </div>
            
            <div class="footer-column">
                <h3>Quick Links</h3>
                <ul>
                    <li><a href="#" data-page="home">Home</a></li>
                    <li><a href="#" data-page="products">Products & Services</a></li>
                    <li><a href="#" data-page="chatbot">Homework Helper</a></li>
                    <li><a href="#" data-page="contact">Contact Us</a></li>
                    <li><a href="#" data-page="auth">Sign In</a></li>
                </ul>
            </div>
            
            <div class="footer-column">
                <h3>Resources</h3>
                <ul>
                    <li><a href="#">Math Worksheets</a></li>
                    <li><a href="#">Science Guides</a></li>
                    <li><a href="#">CBC Resources</a></li>
                    <li><a href="#">Parent Tips</a></li>
                    <li><a href="#">Learning Blog</a></li>
                </ul>
            </div>
            
            <div class="footer-column">
                <h3>Contact Us</h3>
                <ul>
                    <li><i class="fas fa-map-marker-alt"></i> Nairobi, Kenya</li>
                    <li><i class="fas fa-phone"></i> +254 758 943 430</li>
                    <li><i class="fas fa-envelope"></i> owinojerim269@gmail.com</li>
                </ul>
            </div>
        </div>
        
        <div class="copyright">
            <p>&copy; 2023 EduHelper. All rights reserved.</p>
        </div>
    </footer>

    <script>
        // Page Navigation
        document.querySelectorAll('.nav-link, .footer-column a').forEach(link => {
            link.addEventListener('click', function(e) {
                if(this.getAttribute('data-page')) {
                    e.preventDefault();
                    
                    // Remove active class from all links
                    document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
                    
                    // Add active class to clicked link
                    this.classList.add('active');
                    
                    // Hide all pages
                    document.querySelectorAll('.page').forEach(page => {
                        page.classList.remove('active');
                    });
                    
                    // Show selected page
                    const pageId = this.getAttribute('data-page');
                    document.getElementById(pageId).classList.add('active');
                    
                    // Scroll to top
                    window.scrollTo(0, 0);
                }
            });
        });
        
        // Auth Tabs
        document.querySelectorAll('.auth-tab').forEach(tab => {
            tab.addEventListener('click', function() {
                // Remove active class from all tabs
                document.querySelectorAll('.auth-tab').forEach(t => t.classList.remove('active'));
                
                // Add active class to clicked tab
                this.classList.add('active');
                
                // Hide all tab content
                document.querySelectorAll('.tab-content').forEach(content => {
                    content.style.display = 'none';
                });
                
                // Show selected tab content
                const tabId = this.getAttribute('data-tab');
                document.getElementById(`${tabId}-tab`).style.display = 'block';
            });
        });
        
        // Chatbot functionality
        const chatContainer = document.getElementById('chat-container');
        const questionInput = document.getElementById('question-input');
        const imageUpload = document.getElementById('image-upload');
        const sendBtn = document.getElementById('send-btn');
        
        sendBtn.addEventListener('click', function() {
            const question = questionInput.value.trim();
            
            if (question) {
                // Add user message to chat
                addMessage(question, 'user');
                
                // Clear input
                questionInput.value = '';
                
                // Simulate AI response
                simulateAIResponse(question);
            }
        });
        
        // Enter key handler
        questionInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                sendBtn.click();
            }
        });
        
        // Image upload handler
        imageUpload.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(event) {
                    // Add image message to chat
                    addMessage("Homework Image", 'user', event.target.result);
                    
                    // Simulate AI response for image
                    simulateAIResponse("Can you explain this homework problem?");
                }
                reader.readAsDataURL(file);
            }
        });
        
        // Function to add a new message to the chat
        function addMessage(text, sender, image = null) {
            const messageDiv = document.createElement('div');
            messageDiv.classList.add('message', sender + '-message');
            messageDiv.textContent = text;
            
            if (image) {
                const imgPreview = document.createElement('img');
                imgPreview.src = image;
                imgPreview.classList.add('image-preview');
                imgPreview.style.display = 'block';
                messageDiv.appendChild(imgPreview);
            }
            
            chatContainer.appendChild(messageDiv);
            
            // Scroll to bottom
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }
        
        // Function to simulate AI response
        function simulateAIResponse(userMessage) {
            // Show loading indicator
            const loader = document.createElement('div');
            loader.classList.add('loader');
            loader.innerHTML = `
                <div class="loader-dot"></div>
                <div class="loader-dot"></div>
                <div class="loader-dot"></div>
            `;
            chatContainer.appendChild(loader);
            
            // Scroll to bottom
            chatContainer.scrollTop = chatContainer.scrollHeight;
            
            // Simulate processing delay
            setTimeout(() => {
                // Remove loader
                loader.remove();
                
                let response = '';
                let visual = '';
                
                // Generate appropriate response based on user input
                if (userMessage.toLowerCase().includes('fraction') || 
                    userMessage.toLowerCase().includes('divide')) {
                    response = "Dividing fractions is easier than it looks! Let me explain:";
                    visual = `
                        <div class="visual-explanation">
                            <strong>🍕 Fraction Division Example:</strong><br>
                            Problem: 3/4 ÷ 1/2<br><br>
                            Step 1: Flip the second fraction → 1/2 becomes 2/1<br>
                            Step 2: Multiply: 3/4 × 2/1 = 6/4<br>
                            Step 3: Simplify: 6/4 = 1 1/2<br><br>
                            So 3/4 ÷ 1/2 = 1 1/2. That's one and a half pizzas!
                        </div>
                    `;
                } else if (userMessage.toLowerCase().includes('photo')) {
                    response = "Photosynthesis is how plants make food using sunlight! Here's a simple explanation:";
                    visual = `
                        <div class="visual-explanation">
                            <strong>🌱 Photosynthesis Process:</strong><br>
                            1. 🌞 Sunlight provides energy<br>
                            2. 💧 Water absorbed by roots<br>
                            3. 💨 Carbon dioxide from air<br>
                            4. 🍃 Chlorophyll captures light<br>
                            5. 🍬 Produces sugar (food) and oxygen<br><br>
                            Formula: Sunlight + Water + CO₂ → Sugar + Oxygen
                        </div>
                    `;
                } else if (userMessage.toLowerCase().includes('grammar') || 
                           userMessage.toLowerCase().includes('there')) {
                    response = "Let's clarify the difference between 'their', 'there', and 'they're':";
                    visual = `
                        <div class="visual-explanation">
                            <strong>📚 Grammar Guide:</strong><br>
                            <span style="color:#3a0ca3;font-weight:bold;">Their:</span> Shows ownership (e.g., "Their house is big")<br>
                            <span style="color:#3a0ca3;font-weight:bold;">There:</span> Refers to a place (e.g., "Put it over there")<br>
                            <span style="color:#3a0ca3;font-weight:bold;">They're:</span> Short for "they are" (e.g., "They're coming soon")
                        </div>
                    `;
                } else {
                    response = "Great question! Here's a simple explanation:";
                    visual = `
                        <div class="visual-explanation">
                            <strong>🎓 Key Points:</strong><br>
                            • Remember to break problems into smaller steps<br>
                            • Use real-world examples to understand concepts<br>
                            • Practice makes perfect!<br>
                            • Always check your work<br><br>
                            Would you like me to go into more detail?
                        </div>
                    `;
                }
                
                // Create response element
                const aiMessage = document.createElement('div');
                aiMessage.classList.add('message', 'ai-message');
                aiMessage.innerHTML = response + visual;
                chatContainer.appendChild(aiMessage);
                
                // Scroll to bottom
                chatContainer.scrollTop = chatContainer.scrollHeight;
            }, 2000);
        }
        
        // Auth button functionality
        document.getElementById('login-btn').addEventListener('click', function() {
            document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
            document.querySelector('[data-page="auth"]').classList.add('active');
            
            document.querySelectorAll('.page').forEach(page => {
                page.classList.remove('active');
            });
            
            document.getElementById('auth').classList.add('active');
        });
        
        document.getElementById('signup-btn').addEventListener('click', function() {
            document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
            document.querySelector('[data-page="auth"]').classList.add('active');
            
            document.querySelectorAll('.page').forEach(page => {
                page.classList.remove('active');
            });
            
            document.getElementById('auth').classList.add('active');
            
            // Switch to signup tab
            document.querySelectorAll('.auth-tab').forEach(t => t.classList.remove('active'));
            document.querySelector('[data-tab="signup"]').classList.add('active');
            
            document.querySelectorAll('.tab-content').forEach(content => {
                content.style.display = 'none';
            });
            
            document.getElementById('signup-tab').style.display = 'block';
        });
        
        document.getElementById('try-free-btn').addEventListener('click', function() {
            document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
            document.querySelector('[data-page="chatbot"]').classList.add('active');
            
            document.querySelectorAll('.page').forEach(page => {
                page.classList.remove('active');
            });
            
            document.getElementById('chatbot').classList.add('active');
        });
    </script>
</body>
</html>
