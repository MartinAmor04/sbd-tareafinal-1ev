# SBD-FinalTask-1EV

This repository contains a system based on Docker Compose to manage bike station data in Coruña. The system consists of two main services:

1. **MongoDB**: A database where the data is stored.
2. **Get-from-API**: A Python service that retrieves information from the CitiBike API and stores it in MongoDB.

It also includes a **CheapShark-API** repository where you will find another proposal with a different API. This API compares digital PC game websites and keeps track of the prices across multiple stores such as Steam or Fanatical.

## 🛠️ Requirements

Make sure you have installed:

- **Docker** 

---

## 🚀 Project Usage

### 1. Clone the Repository
```bash
git clone git@github.com:MartinAmor04/sbd-tareafinal-1ev.git
```
### 2. Connect to Openstack via SSH or VPN:
You can connect with the IP while being connected to the VPN or through SSH.

### 3. Copy docker-compose:
Copy the content of docker-compose and paste it into the new file you create with the text editor 'nano' inside the instance
```bash
nano docker-compose.yml
```
### 4. Build and Start the Services
Use Docker Compose to build and bring up the entire environment:
```bash
docker-compose up -d
```
### 4. Verify the Data in MongoDB
Exec mongosh in order to interactuate with the database 
```bash
docker exec -it mongodb mongosh
```
Inside the MongoDB shell, select the database and check the collections:
```bash
use bicisCorunha
db.stations.find()
db.stations.countDocuments()
```
## Run reader-mongodb.py
### 1. Create and Activate the Virtual Environment
We will use Conda to manage the environment. Run the following commands in your terminal:
```bash
conda create --name API python=3.12.8
conda activate API
conda install pip 
```
With the environment activated, install all the required libraries from the `requirements.txt` file:
```bash
pip install -r requirements.txt
```
Run the script:
```bash
python reader-mongodb.py
```
Note that entries have been limited to a maximum of 5 because there is too much data in the instance, which caused the script to malfunction.

# Documents Stored During Holidays
During the holiday period, from **December 21st** to **January 8th**, our system collects data at a frequency of **49 documents every 3 minutes**. This calculation assumes continuous operation 24 hours a day.

## Calculation

### Holiday Duration
- **From December 21st to 31st**: 11 days.  
- **From January 1st to 8th**: 8 days.  
- **Total**: 19 days.

### Total Minutes
19 days × 24 hours/day × 60 minutes/hour = **27,360 minutes**

### Number of Collection Intervals (every 3 minutes)
27,360 minutes ÷ 3 minutes/interval = **9,120 intervals**

### Total Documents Stored
9,120 intervals × 49 documents/interval = **446,880 documents**

## Result
During the holiday period, the system will store a total of **446,880 documents**.


