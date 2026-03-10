from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Black Nebula - Ultimate Gaming Dashboard By Shakir</title>
    <style>
        :root {
            --black-1: #0a0a0a;
            --black-2: #0f0f0f;
            --black-3: #151515;
            --black-4: #1a1a1a;
            --black-5: #202020;
            --black-glass: rgba(20, 20, 20, 0.7);
            --neon-red: #ff1744;
            --neon-blue: #00b0ff;
            --neon-purple: #7c4dff;
            --neon-green: #00e676;
            --glow-red: rgba(255, 23, 68, 0.6);
            --glow-blue: rgba(0, 176, 255, 0.6);
            --glow-purple: rgba(124, 77, 255, 0.6);
            --text-primary: #e8e8e8;
            --text-secondary: #a0a0a0;
            --text-muted: #707070;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
            background: linear-gradient(135deg, var(--black-1) 0%, var(--black-2) 25%, var(--black-3) 50%, var(--black-4) 75%, var(--black-5) 100%);
            background-attachment: fixed;
            color: var(--text-primary);
            min-height: 100vh;
            overflow-x: hidden;
            position: relative;
        }

        /* Particle Background */
        .particles {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 1;
        }

        .particle {
            position: absolute;
            border-radius: 50%;
            background: linear-gradient(45deg, var(--neon-red), var(--neon-blue));
            animation: float 20s infinite linear;
        }

        @keyframes float {
            0% { transform: translateY(100vh) rotate(0deg); opacity: 0; }
            10% { opacity: 1; }
            90% { opacity: 1; }
            100% { transform: translateY(-100px) rotate(360deg); opacity: 0; }
        }

        /* Navigation */
        .navbar {
            position: fixed;
            top: 0;
            width: 100%;
            background: rgba(15, 15, 15, 0.95);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            z-index: 1000;
            padding: 1rem 2rem;
        }

        .nav-container {
            max-width: 1400px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.8rem;
            font-weight: 800;
            background: linear-gradient(45deg, var(--neon-red), var(--neon-purple));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-shadow: 0 0 30px var(--glow-red);
        }

        .nav-links {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        .nav-links a {
            color: var(--text-secondary);
            text-decoration: none;
            font-weight: 500;
            padding: 0.5rem 1rem;
            border-radius: 25px;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .nav-links a:hover {
            color: var(--text-primary);
            background: rgba(255, 255, 255, 0.1);
            box-shadow: 0 5px 20px var(--glow-purple);
        }

        /* Main Container */
        .main-container {
            margin-top: 80px;
            min-height: calc(100vh - 80px);
            padding: 2rem;
            max-width: 1400px;
            margin-left: auto;
            margin-right: auto;
        }

        /* Hero Section */
        .hero {
            text-align: center;
            padding: 4rem 2rem;
            background: linear-gradient(135deg, rgba(255, 23, 68, 0.1), rgba(124, 77, 255, 0.1));
            border-radius: 30px;
            margin-bottom: 4rem;
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(20px);
        }

        .hero h1 {
            font-size: clamp(3rem, 8vw, 6rem);
            font-weight: 900;
            letter-spacing: -0.02em;
            background: linear-gradient(45deg, var(--neon-red), var(--neon-blue), var(--neon-purple), var(--neon-green));
            background-size: 300% 300%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: gradientShift 4s ease infinite;
            margin-bottom: 1.5rem;
        }

        @keyframes gradientShift {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }

        .hero p {
            font-size: 1.4rem;
            color: var(--text-secondary);
            max-width: 600px;
            margin: 0 auto 3rem;
            line-height: 1.6;
        }

        .cta-button {
            display: inline-block;
            padding: 1.2rem 3rem;
            background: linear-gradient(45deg, var(--neon-red), var(--neon-purple));
            color: white;
            text-decoration: none;
            border-radius: 50px;
            font-weight: 700;
            font-size: 1.1rem;
            box-shadow: 0 10px 30px var(--glow-red);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .cta-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 20px 40px var(--glow-purple);
        }

        .cta-button::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
            transition: left 0.5s;
        }

        .cta-button:hover::before {
            left: 100%;
        }

        /* Stats Grid */
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-bottom: 4rem;
        }

        .stat-card {
            background: var(--black-glass);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 25px;
            padding: 2.5rem 2rem;
            text-align: center;
            transition: all 0.4s ease;
            position: relative;
            overflow: hidden;
        }

        .stat-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, var(--neon-red), var(--neon-blue), var(--neon-purple));
            background-size: 200% 100%;
            animation: gradientMove 3s ease infinite;
        }

        @keyframes gradientMove {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }

        .stat-card:hover {
            transform: translateY(-10px) scale(1.02);
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.5);
        }

        .stat-number {
            font-size: 3rem;
            font-weight: 800;
            color: var(--neon-blue);
            margin-bottom: 0.5rem;
            text-shadow: 0 0 20px var(--glow-blue);
        }

        .stat-label {
            font-size: 1rem;
            color: var(--text-secondary);
            text-transform: uppercase;
            letter-spacing: 0.1em;
        }

        /* Gaming Dashboard */
        .dashboard-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 2rem;
            margin-bottom: 4rem;
        }

        @media (max-width: 1024px) {
            .dashboard-grid {
                grid-template-columns: 1fr;
            }
        }

        .system-monitor {
            background: var(--black-glass);
            backdrop-filter: blur(25px);
            border-radius: 25px;
            padding: 2rem;
            border: 1px solid rgba(255, 255, 255, 0.1);
            height: 400px;
            position: relative;
            overflow: hidden;
        }

        .system-title {
            display: flex;
            align-items: center;
            gap: 0.8rem;
            margin-bottom: 2rem;
            font-size: 1.3rem;
            font-weight: 700;
            color: var(--neon-purple);
        }

        .cpu-grid, .gpu-grid, .ram-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1rem;
            margin-bottom: 1.5rem;
        }

        .metric {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            padding: 1rem;
            text-align: center;
            transition: all 0.3s ease;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }

        .metric:hover {
            background: rgba(255, 255, 255, 0.1);
            transform: translateY(-2px);
        }

        .metric-value {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--neon-green);
        }

        .metric-label {
            font-size: 0.85rem;
            color: var(--text-muted);
            margin-top: 0.3rem;
        }

        /* Recent Activity */
        .activity-feed {
            background: var(--black-glass);
            backdrop-filter: blur(25px);
            border-radius: 25px;
            padding: 2rem;
            border: 1px solid rgba(255, 255, 255, 0.1);
            height: 400px;
        }

        .activity-item {
            display: flex;
            align-items: center;
            gap: 1rem;
            padding: 1.2rem 0;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            transition: all 0.3s ease;
        }

        .activity-item:hover {
            background: rgba(255, 255, 255, 0.05);
            padding-left: 1rem;
        }

        .activity-icon {
            width: 40px;
            height: 40px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
            flex-shrink: 0;
        }

        .activity-content h4 {
            color: var(--text-primary);
            margin-bottom: 0.3rem;
            font-size: 0.95rem;
        }

        .activity-content p {
            color: var(--text-secondary);
            font-size: 0.85rem;
        }

        /* Game Library */
        .game-library {
            margin-top: 4rem;
        }

        .library-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 2rem;
        }

        .section-title {
            font-size: 2rem;
            font-weight: 800;
            background: linear-gradient(45deg, var(--neon-blue), var(--neon-purple));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .games-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 1.5rem;
        }

        .game-card {
            background: var(--black-glass);
            backdrop-filter: blur(20px);
            border-radius: 20px;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: all 0.4s ease;
            position: relative;
        }

        .game-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, var(--neon-red), var(--neon-green));
        }

        .game-card:hover {
            transform: translateY(-15px);
            box-shadow: 0 30px 60px rgba(0, 0, 0, 0.6);
        }

        .game-image {
            height: 160px;
            background: linear-gradient(45deg, var(--neon-purple), var(--neon-blue));
            position: relative;
            overflow: hidden;
        }

        .game-image::after {
            content: 'Featured';
            position: absolute;
            top: 1rem;
            right: 1rem;
            background: var(--neon-red);
            color: white;
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 700;
        }

        .game-info {
            padding: 1.5rem;
        }

        .game-title {
            font-size: 1.3rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            color: var(--text-primary);
        }

        .game-meta {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
        }

        .game-platforms {
            display: flex;
            gap: 0.5rem;
        }

        .platform-tag {
            background: rgba(255, 255, 255, 0.1);
            color: var(--text-secondary);
            padding: 0.2rem 0.6rem;
            border-radius: 12px;
            font-size: 0.75rem;
        }

        .game-footer {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .play-button {
            background: linear-gradient(45deg, var(--neon-green), var(--neon-blue));
            color: white;
            border: none;
            padding: 0.6rem 1.5rem;
            border-radius: 25px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .play-button:hover {
            transform: scale(1.05);
            box-shadow: 0 5px 20px var(--glow-green);
        }

        /* Footer */
        .footer {
            background: var(--black-3);
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            padding: 3rem 2rem 2rem;
            margin-top: 6rem;
        }

        .footer-content {
            max-width: 1400px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
        }

        .footer-section h3 {
            color: var(--neon-purple);
            margin-bottom: 1.5rem;
            font-size: 1.2rem;
        }

        .footer-section a {
            color: var(--text-secondary);
            text-decoration: none;
            display: block;
            margin-bottom: 0.8rem;
            transition: color 0.3s ease;
        }

        .footer-section a:hover {
            color: var(--neon-blue);
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .main-container {
                padding: 1rem;
            }
            
            .hero {
                padding: 2rem 1rem;
            }
            
            .nav-links {
                display: none;
            }
            
            .stats-grid {
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            }
        }

        /* Scrollbar Styling */
        ::-webkit-scrollbar {
            width: 12px;
        }

        ::-webkit-scrollbar-track {
            background: var(--black-3);
        }

        ::-webkit-scrollbar-thumb {
            background: linear-gradient(var(--neon-purple), var(--neon-blue));
            border-radius: 6px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(var(--neon-red), var(--neon-purple));
        }
    </style>
</head>
<body>
    <!-- Particle Background -->
    <div class="particles" id="particles"></div>

    <!-- Navigation -->
    <nav class="navbar">
        <div class="nav-container">
            <div class="logo">BLACK NEBULA</div>
            <ul class="nav-links">
                <li><a href="#dashboard">Dashboard</a></li>
                <li><a href="#library">Library</a></li>
                <li><a href="#stats">Stats</a></li>
                <li><a href="#settings">Settings</a></li>
                <li><a href="#store">Store</a></li>
            </ul>
        </div>
    </nav>

    <!-- Main Content -->
    <div class="main-container">
        <!-- Hero Section -->
        <section class="hero">
            <h1>Black Nebula</h1>
            <p>Experience the ultimate gaming dashboard with deep black aesthetics, real-time system monitoring, and thousands of hours of premium gaming content. Built with pure elegance and performance.</p>
            <a href="#dashboard" class="cta-button">Enter Gaming Universe</a>
        </section>

        <!-- Stats Grid -->
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-number" data-target="248">0</div>
                <div class="stat-label">Games Installed</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" data-target="1274">0</div>
                <div class="stat-label">Hours Played</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" data-target="452">0</div>
                <div class="stat-label">Achievements</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" data-target="98">0</div>
                <div class="stat-label">Framerate (FPS)</div>
            </div>
        </div>

        <!-- Gaming Dashboard -->
        <div class="dashboard-grid" id="dashboard">
            <!-- System Monitor -->
            <div class="system-monitor">
                <div class="system-title">
                    <span style="font-size: 1.5rem;">🖥️</span>
                    System Monitor
                </div>
                <div class="cpu-grid">
                    <div class="metric">
                        <div class="metric-value" data-cpu="47">47%</div>
                        <div class="metric-label">CPU</div>
                    </div>
                    <div class="metric">
                        <div class="metric-value" data-gpu="72">72%</div>
                        <div class="metric-label">GPU</div>
                    </div>
                    <div class="metric">
                        <div class="metric-value" data-ram="68">68%</div>
                        <div class="metric-label">RAM</div>
                    </div>
                </div>
                <div class="ram-grid">
                    <div class="metric">
                        <div class="metric-value" data-temp="67">67°</div>
                        <div class="metric-label">Temp</div>
                    </div>
                    <div class="metric">
                        <div class="metric-value" data-fps="142">142</div>
                        <div class="metric-label">FPS</div>
                    </div>
                    <div class="metric">
                        <div class="metric-value" data-ping="23">23ms</div>
                        <div class="metric-label">Ping</div>
                    </div>
                </div>
            </div>

            <!-- Recent Activity -->
            <div class="activity-feed">
                <div class="system-title">Recent Activity</div>
                <div class="activity-item">
                    <div class="activity-icon" style="background: rgba(0, 230, 118, 0.2); color: var(--neon-green);">✓</div>
                    <div class="activity-content">
                        <h4>Game Update Complete</h4>
                        <p>Cyberpunk 2077 updated to v2.1.3</p>
                    </div>
                </div>
                <div class="activity-item">
                    <div class="activity-icon" style="background: rgba(255, 23, 68, 0.2); color: var(--neon-red);">⚠</div>
                    <div class="activity-content">
                        <h4>Driver Update Available</h4>
                        <p>NVIDIA RTX 4090 - New drivers available</p>
                    </div>
                </div>
                <div class="activity-item">
                    <div class="activity-icon" style="background: rgba(124, 77, 255, 0.2); color: var(--neon-purple);">🎮</div>
                    <div class="activity-content">
                        <h4>New Achievement Unlocked</h4>
                        <p>Master Hacker in Deus Ex</p>
                    </div>
                </div>
                <div class="activity-item">
                    <div class="activity-icon" style="background: rgba(0, 176, 255, 0.2); color: var(--neon-blue);">📊</div>
                    <div class="activity-content">
                        <h4>Personal Best</h4>
                        <p>DOOM Eternal - 142 FPS average</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Game Library -->
        <section class="game-library" id="library">
            <div class="library-header">
                <h2 class="section-title">Game Library</h2>
                <select style="background: var(--black-glass); border: 1px solid rgba(255,255,255,0.1); color: var(--text-primary); padding: 0.5rem 1rem; border-radius: 20px;">
                    <option>All Games</option>
                    <option>Recently Played</option>
                    <option>Favorites</option>
                </select>
            </div>
            <div class="games-grid">
                <div class="game-card">
                    <div class="game-image"></div>
                    <div class="game-info">
                        <div class="game-title">Cyberpunk 2077</div>
                        <div class="game-meta">
                            <div class="game-platforms">
                                <span class="platform-tag">PC</span>
                                <span class="platform-tag">RTX</span>
                            </div>
                            <div style="color: var(--neon-green);">● Live</div>
                        </div>
                        <div class="game-footer">
                            <span style="color: var(--text-secondary);">2h 45m</span>
                            <button class="play-button">Play Now</button>
                        </div>
                    </div>
                </div>
                <div class="game-card">
                    <div class="game-image" style="background: linear-gradient(45deg, var(--neon-red), var(--neon-purple));"></div>
                    <div class="game-info">
                        <div class="game-title">DOOM Eternal</div>
                        <div class="game-meta">
                            <div class="game-platforms">
                                <span class="platform-tag">PC</span>
                            </div>
                            <div style="color: var(--neon-green);">● Live</div>
                        </div>
                        <div class="game-footer">
                            <span style="color: var(--text-secondary);">127h 30m</span>
                            <button class="play-button">Launch</button>
                        </div>
                    </div>
                </div>
                <div class="game-card">
                    <div class="game-image" style="background: linear-gradient(45deg, var(--neon-blue), var(--neon-green));"></div>
                    <div class="game-info">
                        <div class="game-title">Half-Life: Alyx</div>
                        <div class="game-meta">
                            <div class="game-platforms">
                                <span class="platform-tag">VR</span>
                                <span class="platform-tag">PC</span>
                            </div>
                            <div style="color: var(--neon-purple);">● Installed</div>
                        </div>
                        <div class="game-footer">
                            <span style="color: var(--text-secondary);">89h 12m</span>
                            <button class="play-button">VR Launch</button>
                        </div>
                    </div>
                </div>
                <div class="game-card">
                    <div class="game-image" style="background: linear-gradient(45deg, var(--neon-orange), var(--neon-red));"></div>
                    <div class="game-info">
                        <div class="game-title">Elden Ring</div>
                        <div class="game-meta">
                            <div class="game-platforms">
                                <span class="platform-tag">PC</span>
                            </div>
                            <div style="color: var(--neon-red);">● DLC Ready</div>
                        </div>
                        <div class="game-footer">
                            <span style="color: var(--text-secondary);">342h 18m</span>
                            <button class="play-button">Continue</button>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>

    <!-- Footer -->
    <footer class="footer">
        <div class="footer-content">
            <div class="footer-section">
                <h3>Black Nebula</h3>
                <p style="color: var(--text-secondary); margin-bottom: 1rem;">The ultimate gaming experience with unmatched black aesthetics and performance monitoring.</p>
                <div style="display: flex; gap: 1rem;">
                    <div style="width: 40px; height: 40px; background: var(--neon-blue); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.2rem;">D</div>
                    <div style="width: 40px; height: 40px; background: var(--neon-purple); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.2rem;">T</div>
                </div>
            </div>
            <div class="footer-section">
                <h3>Quick Links</h3>
                <a href="#">Dashboard</a>
                <a href="#">Library</a>
                <a href="#">Store</a>
                <a href="#">Settings</a>
                <a href="#">Support</a>
            </div>
            <div class="footer-section">
                <h3>Company</h3>
                <a href="#">About Us</a>
                <a href="#">Careers</a>
                <a href="#">Privacy</a>
                <a href="#">Terms</a>
            </div>
            <div class="footer-section">
                <h3>Support</h3>
                <a href="#">Help Center</a>
                <a href="#">Contact</a>
                <a href="#">System Requirements</a>
                <a href="#">Bug Reports</a>
            </div>
        </div>
        <div style="text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid rgba(255,255,255,0.1); color: var(--text-muted);">
            © 2026 Black Nebula. Built with Flask. Pure Black Aesthetics.
        </div>
    </footer>

    <script>
        // Particle System
        function createParticles() {
            const particles = document.getElementById('particles');
            for (let i = 0; i < 100; i++) {
                const particle = document.createElement('div');
                particle.className = 'particle';
                particle.style.width = Math.random() * 4 + 1 + 'px';
                particle.style.height = particle.style.width;
                particle.style.left = Math.random() * 100 + '%';
                particle.style.animationDelay = Math.random() * 20 + 's';
                particle.style.animationDuration = (Math.random() * 10 + 15) + 's';
                particles.appendChild(particle);
            }
        }

        // Animated Counters
        function animateCounters() {
            const counters = document.querySelectorAll('[data-target]');
            counters.forEach(counter => {
                const target = parseInt(counter.dataset.target);
                const increment = target / 100;
                let current = 0;
                const timer = setInterval(() => {
                    current += increment;
                    if (current >= target) {
                        counter.textContent = target;
                        clearInterval(timer);
                    } else {
                        counter.textContent = Math.floor(current);
                    }
                }, 20);
            });
        }

        // Smooth Scrolling
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            });
        });

        // Game Card Interactions
        document.querySelectorAll('.play-button').forEach(button => {
            button.addEventListener('click', function() {
                this.style.transform = 'scale(0.95)';
                setTimeout(() => {
                    this.style.transform = '';
                    // Simulate game launch
                    alert('🚀 Launching game...');
                }, 150);
            });
        });

        // Navbar Scroll Effect
        window.addEventListener('scroll', () => {
            const navbar = document.querySelector('.navbar');
            if (window.scrollY > 50) {
                navbar.style.background = 'rgba(10, 10, 10, 0.98)';
                navbar.style.boxShadow = '0 5px 30px rgba(0, 0, 0, 0.5)';
            } else {
                navbar.style.background = 'rgba(15, 15, 15, 0.95)';
                navbar.style.boxShadow = 'none';
            }
        });

        // Initialize
        document.addEventListener('DOMContentLoaded', () => {
            createParticles();
            setTimeout(animateCounters, 500);
            
            // Dynamic metric updates
            setInterval(() => {
                const metrics = ['data-cpu', 'data-gpu', 'data-ram', 'data-temp', 'data-fps', 'data-ping'];
                metrics.forEach(attr => {
                    const elements = document.querySelectorAll(`[${attr}]`);
                    elements.forEach(el => {
                        let value = parseFloat(el.textContent);
                        const change = (Math.random() - 0.5) * 5;
                        value = Math.max(0, Math.min(100, value + change));
                        if (attr === 'data-temp') value = Math.max(45, Math.min(95, value));
                        if (attr === 'data-fps') value = Math.max(60, Math.min(200, value));
                        if (attr === 'data-ping') value = Math.max(10, Math.min(100, value));
                        el.textContent = attr.includes('temp') ? value.toFixed(0) + '°' : 
                                        attr.includes('ping') ? value.toFixed(0) + 'ms' : value.toFixed(0) + '%';
                    });
                });
            }, 2000);
        });
    </script>
</body>
</html>
    """

@app.route("/api/system")
def system_stats():
    import random
    return {
        "cpu": random.randint(30, 85),
        "gpu": random.randint(40, 95),
        "ram": random.randint(50, 90),
        "temp": random.randint(55, 80),
        "fps": random.randint(100, 180),
        "ping": random.randint(15, 45)
    }

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

