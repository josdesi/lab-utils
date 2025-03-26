
```
#!/bin/bash
yum update -y
yum install -y git python3-pip

git clone https://github.com/josdesi/lab-utils.git
cd lab-utils/apps/001_high_cpu

pip3 install -r requirements.txt

nohup uvicorn main:app --host 0.0.0.0 --port 80 > app.log 2>&1 &
```




```
sudo cat /var/log/cloud-init-output.log
```




```
sudo tail -f /var/log/cloud-init-output.log
```