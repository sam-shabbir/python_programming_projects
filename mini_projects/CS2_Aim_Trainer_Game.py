# CS2 Aim Trainer Game
#
# A 3D reaction trainer in the browser (Three.js). Python's job here is to hold the game's
# HTML in a string, save it as a .html file, and open it in your default web browser.
#
# FIX: the original was `game_code = <!DOCTYPE html>...` with no quotes, so Python tried to
# read the HTML as Python code (SyntaxError). A multi-line string needs triple quotes.
# The r in r""" makes it a "raw" string: backslashes in the JavaScript are kept exactly as written.

import os
import webbrowser # built-in module that opens files or URLs in your default browser

game_code = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CS2 Dust2 Adaptive Reaction Trainer</title>
    <style>
        body { margin: 0; overflow: hidden; background-color: #000; font-family: sans-serif; user-select: none; }
        #gameUi { position: absolute; top: 10px; left: 10px; color: #fff; text-shadow: 2px 2px #000; font-size: 18px; pointer-events: none; z-index: 10; }
        #crosshair { position: absolute; top: 50%; left: 50%; width: 10px; height: 10px; transform: translate(-50%, -50%); pointer-events: none; z-index: 10; }
        #crosshair::before, #crosshair::after { content: ''; position: absolute; background: #0f0; }
        #crosshair::before { top: 4px; left: -5px; width: 20px; height: 2px; }
        #crosshair::after { top: -5px; left: 4px; width: 2px; height: 20px; }
        #menu { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.85); display: flex; flex-direction: column; justify-content: center; align-items: center; color: #fff; z-index: 100; }
        button { padding: 12px 24px; font-size: 18px; font-weight: bold; background: #de9b35; border: none; cursor: pointer; border-radius: 4px; color: #000; }
        button:hover { background: #ffb443; }
        .stat-val { font-weight: bold; color: #de9b35; }
    </style>
    <!-- Three.js Library for 3D graphics -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
</head>
<body>

    <div id="crosshair"></div>
    <div id="gameUi">
        <div>Kills: <span id="kills" class="stat-val">0</span></div>
        <div>Bot Speed (Difficulty): <span id="difficulty" class="stat-val">Medium (1.0x)</span></div>
        <div>Streak: <span id="streak" class="stat-val">0</span></div>
    </div>

    <div id="menu">
        <h1 style="color: #de9b35; margin-bottom: 5px;">DUST2 ADAPTIVE AIM TRAINER</h1>
        <p style="margin-bottom: 30px; color: #aaa;">Click Start, move mouse to aim, Left-Click to shoot. WASD to move.</p>
        <button id="startBtn">START TRAINING</button>
    </div>

    <script>
        // --- Game Variables ---
        let scene, camera, renderer;
        let moveForward = false, moveBackward = false, moveLeft = false, moveRight = false;
        let moveSpeed = 0.15;
        let yaw = 0, pitch = 0;
        const mouseSensitivity = 0.002;
        
        let targets = [];
        let score = 0;
        let consecutiveKills = 0;
        let baseBotSpeed = 0.06; 
        let adaptiveMultiplier = 1.0;

        // --- Init Scene ---
        function init() {
            scene = new THREE.Scene();
            scene.background = new THREE.Color(0xace6ff); // Sky blue
            scene.fog = new THREE.FogExp2(0xace6ff, 0.015);

            camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.set(0, 1.6, 5); // Position player slightly back

            renderer = new THREE.WebGLRenderer({ antialias: true });
            renderer.setSize(window.innerWidth, window.innerHeight);
            document.body.appendChild(renderer.domElement);

            // Lighting
            const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
            scene.add(ambientLight);
            const dirLight = new THREE.DirectionalLight(0xfff3e0, 0.8);
            dirLight.position.set(20, 40, 20);
            scene.add(dirLight);

            buildDust2Map();
            spawnBot();

            // Event Listeners
            window.addEventListener('resize', onWindowResize);
            document.addEventListener('keydown', (e) => handleKey(e.code, true));
            document.addEventListener('keyup', (e) => handleKey(e.code, false));
            document.addEventListener('mousemove', handleMouseMove);
            document.addEventListener('mousedown', handleShoot);
            
            document.getElementById('startBtn').addEventListener('click', () => {
                document.body.requestPointerLock();
            });

            document.addEventListener('pointerlockchange', () => {
                if (document.pointerLockElement === document.body) {
                    document.getElementById('menu').style.display = 'none';
                } else {
                    document.getElementById('menu').style.display = 'flex';
                }
            });

            animate();
        }

        // --- Build CS2 Dust2 Geometry ---
        function buildDust2Map() {
            // Ground (Dusty Sand Color)
            const groundGeo = new THREE.PlaneGeometry(80, 80);
            const groundMat = new THREE.MeshLambertMaterial({ color: 0xd2b48c });
            const ground = new THREE.Mesh(groundGeo, groundMat);
            ground.rotation.x = -Math.PI / 2;
            scene.add(ground);

            const wallMat = new THREE.MeshLambertMaterial({ color: 0xe0cda9 });
            const crateMat = new THREE.MeshLambertMaterial({ color: 0xb58a4c });

            // Boundary Walls
            createWall(0, 4, -40, 80, 8, 2, wallMat);
            createWall(0, 4, 40, 80, 8, 2, wallMat);
            createWall(-40, 4, 0, 2, 8, 80, wallMat);
            createWall(40, 4, 0, 2, 8, 80, wallMat);

            // Cover Obstacles
            createWall(-5, 1, -15, 2, 2, 2, crateMat);
            createWall(-5, 3, -14, 1.8, 1.8, 1.8, crateMat); 
            createWall(10, 1.5, 5, 3, 3, 3, crateMat);
            createWall(-12, 1, 10, 2.5, 2.5, 2.5, crateMat);
        }

        function createWall(x, y, z, w, h, d, mat) {
            const geo = new THREE.BoxGeometry(w, h, d);
            const mesh = new THREE.Mesh(geo, mat);
            mesh.position.set(x, y, z);
            scene.add(mesh);
        }

        // --- Enemy Bot Spawn Logic ---
        function spawnBot() {
            // Clear prior bots
            targets.forEach(t => scene.remove(t));
            targets = [];

            const botGroup = new THREE.Group();

            // Bot Body
            const bodyGeo = new THREE.CylinderGeometry(0.4, 0.4, 1.8, 8);
            const bodyMat = new THREE.MeshLambertMaterial({ color: 0x3b3529 }); 
            const body = new THREE.Mesh(bodyGeo, bodyMat);
            body.position.y = 0.9;
            botGroup.add(body);

            // Bot Head
            const headGeo = new THREE.SphereGeometry(0.25, 8, 8);
            const headMat = new THREE.MeshLambertMaterial({ color: 0xdcac64 }); 
            const head = new THREE.Mesh(headGeo, headMat);
            head.position.y = 1.9;
            botGroup.add(head);

            // Fixed spawn directly within sight line
            const randomX = (Math.random() - 0.5) * 15; 
            const randomZ = -10 - Math.random() * 10; 
            botGroup.position.set(randomX, 0, randomZ);

            // Set array boundary markers explicitly
            botGroup.userData = {
                dir: Math.random() > 0.5 ? 1 : -1,
                minX: randomX - 6,
                maxX: randomX + 6
            };

            scene.add(botGroup);
            targets.push(botGroup);
        }

        // --- Inputs ---
        function handleKey(code, isDown) {
            if (code === 'KeyW') moveForward = isDown;
            if (code === 'KeyS') moveBackward = isDown;
            if (code === 'KeyA') moveLeft = isDown;
            if (code === 'KeyD') moveRight = isDown;
        }

        function handleMouseMove(e) {
            if (document.pointerLockElement !== document.body) return;

            yaw -= e.movementX * mouseSensitivity;
            pitch -= e.movementY * mouseSensitivity;
            pitch = Math.max(-Math.PI / 2.2, Math.min(Math.PI / 2.2, pitch));

            camera.rotation.order = "YXZ";
            camera.rotation.set(pitch, yaw, 0);
        }

        // --- Raycast Target Checking ---
        function handleShoot(e) {
            if (document.pointerLockElement !== document.body) return;

            const raycaster = new THREE.Raycaster();
            const center = new THREE.Vector2(0, 0); 
            raycaster.setFromCamera(center, camera);

            let objectsToCheck = [];
            targets.forEach(b => objectsToCheck.push(...b.children));

            const intersects = raycaster.intersectObjects(objectsToCheck);

            if (intersects.length > 0) {
                score++;
                consecutiveKills++;
                adaptiveMultiplier = 1.0 + (consecutiveKills * 0.2); // Elevates difficulty speed 20% per kill
                document.getElementById('difficulty').innerText = `Adaptive (${adaptiveMultiplier.toFixed(1)}x Speed)`;
                updateUi();
                spawnBot();
            } else {
                consecutiveKills = Math.max(0, consecutiveKills - 1); // Drop difficulty step back on miss
                adaptiveMultiplier = Math.max(1.0, 1.0 + (consecutiveKills * 0.2));
                document.getElementById('difficulty').innerText = adaptiveMultiplier === 1.0 ? "Medium (1.0x)" : `Adaptive (${adaptiveMultiplier.toFixed(1)}x Speed)`;
                updateUi();
            }
        }

        function updateUi() {
            document.getElementById('kills').innerText = score;
            document.getElementById('streak').innerText = consecutiveKills;
        }

        function onWindowResize() {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        }

        // --- Game Engine Loop ---
        function animate() {
            requestAnimationFrame(animate);

            if (document.pointerLockElement === document.body) {
                const forward = new THREE.Vector3(0, 0, -1).applyQuaternion(camera.quaternion);
                forward.y = 0; forward.normalize();
                const right = new THREE.Vector3(1, 0, 0).applyQuaternion(camera.quaternion);
                right.y = 0; right.normalize();

                if (moveForward) camera.position.addScaledVector(forward, moveSpeed);
                if (moveBackward) camera.position.addScaledVector(forward, -moveSpeed);
                if (moveRight) camera.position.addScaledVector(right, moveSpeed);
                if (moveLeft) camera.position.addScaledVector(right, -moveSpeed);

                camera.position.x = Math.max(-38, Math.min(38, camera.position.x));
                camera.position.z = Math.max(-38, Math.min(38, camera.position.z));

                // Strafe tracking indices
                targets.forEach(bot => {
                    const data = bot.userData;
                    const speed = baseBotSpeed * adaptiveMultiplier;
                    bot.position.x += speed * data.dir;

                    if (bot.position.x > data.maxX) {
                        bot.position.x = data.maxX;
                        data.dir = -1;
                    }
                    if (bot.position.x < data.minX) {
                        bot.position.x = data.minX;
                        data.dir = 1;
                    }
                });
            }

            renderer.render(scene, camera);
        }

        // --- Crucial: Run initialization engine ---
        init();
    </script>
</body>
</html>"""

print(f"Total characters verified: {len(game_code)}")

# Save next to this script (not wherever the terminal happens to be)
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cs2_aim_trainer.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(game_code)

print(f"Game saved to: {output_path}")
webbrowser.open("file://" + output_path) # open it like double-clicking the file
