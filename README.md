🚀 TYSONCLOUD-prototype
TYSONCLOUD-prototype is a localized version of TYSONCLOUD that helps dynamically deploy web applications with your own hardware. TYSONCLOUD-prototype focuses on being minimal which is why it usses Docker and integrates with Git for easy way to manage your applications.
🌟 Features

Docker-Based Deployments: Deploy websites using Docker images for consistent and scalable hosting. 📦
GitHub Repository Integration: Pull and deploy code directly from GitHub repositories, streamlining the development-to-deployment pipeline. 🔗
Simplified Workflow: Designed with ease of use in mind, allowing developers to focus on building rather than managing infrastructure. 🛠️
Frontend-Driven Deployment: Manage deployments through an intuitive web interface, eliminating the need for command-line interactions. 🌐
Extensible Framework: Built to support future enhancements for authentication, scaling, and advanced cloud features. 🚀

🛠️ Installation
Prerequisites

Docker: Ensure Docker is installed and running on your system. Install Docker 🐳
Git: Required for cloning the repository. Install Git 📂
Python 3.8+: Needed for running the backend scripts. Install Python 🐍
pip: Python package manager for installing dependencies. 📦

Steps

Clone the Repository
git clone https://github.com/timmyjinks/TYSONCLOUD-prototype.git
cd TYSONCLOUD-prototype


Set Up Environment VariablesCreate a .env file in the project root and add the following:
 CLOUDFLARE_API_TOKEN=<your-cloudflared-api-token>
 TUNNEL_ID=<your-cloudflared-tunnel-id>
 ACCOUNT_ID=<your-cloudflared-account-id>
 ZONE_ID=<your-cloudflared-zone-id>


Build and Run Docker Containers
docker-compose up --build

This command builds and starts the necessary containers for the prototype. Watch the magic happen! ✨


🎮 Usage

Access the Frontend Interface

After running docker-compose up, open your browser and navigate to http://localhost:8080 (or the configured port).
The frontend provides an intuitive interface to manage deployments. Get ready to deploy with a few clicks! 🖱️


Deploy a Website via Docker Image

In the frontend, select the "Deploy Docker Image" option.
Enter the Docker image name and tag (e.g., your_image_name:tag) from your configured registry.
Click "Deploy" to initiate the deployment process. Boom—your app is live! 🚀


Deploy from a GitHub Repository

In the frontend, select the "Deploy from GitHub" option.
Provide the repository URL (e.g., https://github.com/username/repository.git) and branch (e.g., main).
Click "Deploy" to pull and deploy the repository code. From repo to reality in seconds! 🌟


Verify Deployment

Once deployed, the website is accessible at the provided URL (e.g., http://localhost:8080).

Check the deployment status in the frontend dashboard or verify running containers using:
docker ps



[Insert Image Placeholder: Screenshot of deployed website in browser]


🤝 Contributing
Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request with your changes. Ensure your code follows the project’s style guidelines and includes appropriate tests. Join us in shaping the future of TYSONCLOUD! 🌍
📜 License
This project is licensed under the MIT License. See the LICENSE file for details.
📬 Contact
For questions or feedback, reach out via the GitHub Issues page or contact Tyson Jenkins at tysonjenkins.dev. Let’s build the cloud together! 💻
