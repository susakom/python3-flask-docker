pipeline {
    agent { label 'azure-vm' }

    
    environment {
        AZURE_VM_IP = '4.233.87.254'
        SSH_USER = 'susak'
        SSH_KEY = credentials('susak-linux-vm-key') // Укажите ID SSH ключа в Jenkins
    }

    stages {
        stage('SSH to VM') {
            steps {
                script {
                    // Подключение к Azure VM по SSH
                    sh """
                        ssh -o StrictHostKeyChecking=no -i ${SSH_KEY} ${SSH_USER}@${AZURE_VM_IP} 'echo "Connected to VM"'
                    """
                }
            }
        }
    }
}
