🖥️ Remote Server Health Dashboard

The Remote Server Health Dashboard is a lightweight Python tool that connects to remote Linux servers using SSH and displays their health status in a simple web interface.
It’s designed to help DevOps engineers and system administrators monitor server performance quickly and easily.

🌟 Key Features

SSH-based remote server monitoring

Real-time collection of:

CPU usage

Memory usage

Disk usage

System uptime

Clean and minimal web dashboard (Flask)

Auto-refreshing metrics

Easy YAML configuration

Works with both SSH keys and passwords

📁 Project Structure
remote-server-health-dashboard/
│
├── app.py               # Dashboard (Flask)
├── collector.py         # SSH-based metrics collector
├── config.yaml          # Servers configuration
├── requirements.txt
└── README.md

⚙️ Installation
1. Clone the repository
git clone https://github.com/your-username/remote-server-health-dashboard.git
cd remote-server-health-dashboard

2. Install dependencies
pip install -r requirements.txt

🛠️ Configuration

Edit config.yaml to define the servers you want to monitor:

servers:
  - name: production-server
    host: 192.168.1.10
    user: ubuntu
    key_path: ~/.ssh/id_rsa

  - name: staging-server
    host: 10.0.0.5
    user: root
    password: "Admin123"


You can add as many servers as you want.

▶️ Running the Dashboard

Start the application:

python app.py


Then open your browser:

http://localhost:5000


You will see a simple dashboard showing live health metrics for each server.

🧩 How It Works

The dashboard loads server list from config.yaml

collector.py connects to each server using SSH

System commands are executed to gather health stats

Data is sent to the Flask dashboard and displayed

Metrics auto-refresh at a set interval

📌 Notes

Requires basic SSH access to each server

Works on any Linux-based machine

Ideal for learning DevOps monitoring concepts

Very lightweight — no database required

🤝 Contributing

Pull requests and feature suggestions are welcome!
Feel free to open an issue if you want to discuss improvements.

⭐ Support

If you like this project, please give it a ⭐ on GitHub — it helps a lot!