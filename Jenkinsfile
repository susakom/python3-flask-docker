// susak Jenkinsfile for python project
pipeline {
    agent { label 'azure-vm' }
     
    
    stages {
        stage('Sanity Check') {
            steps {
                echo 'Starting on agent azure-vm...'
                sh 'whoami'  // Показывает, от какого пользователя выполняется
                sh 'hostname'  // Показывает имя хоста
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
                echo 'Test compited.' 
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
