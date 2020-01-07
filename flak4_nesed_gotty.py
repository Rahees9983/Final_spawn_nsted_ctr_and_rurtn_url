import flask
import subprocess
import kubernetes
import os
import deploy_k8s
import spawn_ctr_rtrn_url

app = flask.Flask(__name__)

@app.route('/spawn_gotty_cntr',methods =['GET'])
def spawn_nested_container():
    print("inside the spawn_nested container methiod insise the api")
    # namespace_existance = os.system("kubectl get namespace nested-ctr-namespace")
    # if namespace_existance == 0:
    #     print("namespace nested-ctr-namespace already exists ")
    # else:
    #     print("namespace nested-ctr-namespace does not exists inside your cluster creating it ")
    #     os.system("kubectl create namespace nested-ctr-namespace")
    #     print("Namespace nested-ctr-namespace created successfully ")
    # print("")

    deploy_k8s.main()
    # ur_url = subprocess.getoutput("minikube service ssh-python-service --url")
    ur_url = subprocess.getoutput("minikube service list")


    return ur_url,"Hello Sultan Mirza This is url returned by the nested container flask !!!!!!!!!!!!1"
    # return "Rahees gotty container is up using the runnuing container nested containers .....!!!!!!!!!!!!"

@app.route('/get_url',methods=['GET'])
def return_url():
    print("Return url for the gotty container")

    new_url = spawn_ctr_rtrn_url.main()
    return new_url," this is your URL "


if __name__ == "__main__":
    app.run(debug=True,port=5011,host='0.0.0.0')
    