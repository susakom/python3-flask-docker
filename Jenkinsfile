// susak Jenkinsfile for python project
pipeline {
    agent any
    environment {
        AZURE_VM_IP = '4.233.87.254' // IP-адрес вашей Azure VM
        SSH_USER = 'susak' // SSH-пользователь для подключения
        SSH_KEY = credentials('susak-linux-vm-key') // ID SSH credentials в Jenkins
    }
    stages {
        stage('Connect to VM') {
            steps {
                script {
                    // Подключение по SSH и выполнение команды на VM
                    sh """
                        ssh -o StrictHostKeyChecking=no -i ${SSH_KEY} ${SSH_USER}@${AZURE_VM_IP} 'echo "Connected to VM"'
                    """
                }
            }
        }
        stage('Sanity Check') {
            steps {
                echo 'Starting on agent azure-vm...'
                sh 'whoami'  // Показывает, от какого пользователя выполняется
                sh 'hostname'  // Показывает имя хоста
            }
        }
        stage('Create Directory') {
            steps {
                // Создаем директорию в /home/susak
                sh '''
                echo "Creating directory /home/susak/test_directory..."
                mkdir -p /home/susak/test_directory
                ls -l /home/susak
                '''
                echo 'Directory created successfully.'
            }
        }
        stage('Check Python and pip versions') {
            steps {
                // Проверка версий Python и pip
                sh '''
                python3 --version
                pip --version
                '''
                echo 'Python and pip versions checked.' 
            }
        }    
        stage('Checkout') {
            steps {
                // Получаем код из репозитория
                git 'https://github.com/susakom/python3-flask-docker.git'
                echo 'Repository cloned successfully.' 
            }
        }
        stage('Install dependencies') {
            steps {
                // Создаём виртуальное окружение и устанавливаем зависимости
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
                echo 'Dependencies installed.' 
            }
        }

        stage('Run Tests') {
            steps {
                // Активация виртуального окружения и запуск тестов из файла test_app.py
                sh '''
                source venv/bin/activate
                python3 -m unittest discover -s . -p "test_app.py"
                '''
                echo 'Tests completed.' 
            }
        }

        stage('Run Flask Application') {
            steps {
                // Запуск Flask приложения
                sh '''
                source venv/bin/activate
                python3 app.py
                '''
                echo 'App run' 
            }
        }
    }
}
