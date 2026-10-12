
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Quick Commerce Monitoring Pipeline'
            }
        }

        stage('Validate Python') {
            steps {
                sh 'python3 -m py_compile delivery_metrics.py'
            }
        }

        stage('Validate Compose') {
            steps {
                sh 'docker compose config -q'
            }
        }

        stage('Validate Monitoring Config') {
            steps {
                sh 'docker run --rm --entrypoint promtool -v "$PWD/prometheus.yml:/etc/prometheus/prometheus.yml:ro" -v "$PWD/alert_rules.yml:/etc/prometheus/alert_rules.yml:ro" prom/prometheus:latest check config /etc/prometheus/prometheus.yml'
                sh 'docker run --rm --entrypoint promtool -v "$PWD/alert_rules.yml:/etc/prometheus/alert_rules.yml:ro" prom/prometheus:latest check rules /etc/prometheus/alert_rules.yml'
            }
        }
    }

    post {
        success {
            echo 'All Quick Commerce monitoring checks passed.'
        }
        failure {
            echo 'A validation stage failed. Check the console output.'
        }
    }
}
