# susak Jenkinsfile for python project
pipeline {
    agent { 
        label 'azure-vm' // Метка узла, на котором будет запускаться билд
    }
    stages {
        stage('Checkout') {
            steps {
                // Получаем код из репозитория
                git branch: 'main', url: 'https://github.com/susakom/python3-flask-docker.git'
            }
        }
           stage('Check Python and pip versions') {
            steps {
                // Проверка версий Python и pip
                sh '''
                python3 --version
                pip --version
                '''
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
            }
        }
        stage('Run Tests') {
            steps {
                // Активация виртуального окружения и запуск тестов из файла test_app.py
                sh '''
                source venv/bin/activate
                python3 -m unittest discover -s . -p "test_app.py"
                '''
            }
        }
        stage('Run Flask Application') {
            steps {
                // Запуск Flask приложения
                sh '''
                source venv/bin/activate
                python3 app.py
                '''
            }
        }
    }
}
