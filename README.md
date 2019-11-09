# sample webapp test assignment

## App Requirements

* python3 >= 3.6.8
* flask >= 1.1.1
* mysql-connector >= 2.2.9
* Flask-SQLAlchemy >= 2.4.1
* SQLAlchemy >= 1.3.10
* gunicorn >= 19.9.0
* ansible >= 2.9
* aws account 

## How-to

### Deploy to aws:

1. clone the repo
2. set aws related vars in ormuco/ansible/vars/instance.yaml ( or provide them via ansible-playbook -e .. ):

```yaml
   num_instance: 1 # ammount of instances to create
   ami: ami-0039c41a10b230acb # ami used - official ubuntu 18.04
   vpc_subnet: vpc subnet
   region: region
   zone: availiability zone
   key_name: your key name
   group_id: some group id in your vpc
   private_key: "path to private key"
```
3. export AWS_ACCESS_KEY and AWS_SECRET_KEY

4. run playbook:
```bash
    cd ormuco/ansible
    ansible-playbook pb.yaml    
```

* please note: each run will create new instance.

### Run app locally

1. install pip3 
2. install requirements:
```bash
    cd ormuco/app
    pip3 install -r pip_req.txt
```
3. start local app:
```bash
./startserver.sh
```
it will run on 127.0.0.1:8000



