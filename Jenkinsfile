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
                sh 'python3 --version'
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
                  . venv/bin/activate
                  pip install -r requirements.txt
                '''
                echo 'Dependencies installed.' 
            }
        }

        stage('Run Tests') {
            steps {
                // Активация виртуального окружения и запуск тестов из файла test_app.py
                sh '''
                . venv/bin/activate
                python3 -m unittest discover -s . -p "test_app.py"
                '''
                echo 'Tests completed.' 
            }
        }

        stage('Run Flask Application') {
            steps {
                // Запуск Flask приложения
                sh '''
                . venv/bin/activate
                nohup python3 app.py > flask.log 2>&1 &
                '''
                echo 'App run' 
            }
        }
    }
}
