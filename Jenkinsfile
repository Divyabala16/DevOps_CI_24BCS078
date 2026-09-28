pipeline{
    agent any

    stages{
        stage('Checkout'){
           steps{
             checkout scm
       } 
    }  
    stage('Build'){
       steps{
         bat 'python src\\app.py'
      }
    }
    stage('Test'){
       steps{
         bat 'python -m unittest discover -s tests -v' 
      }
    }
  }

  post{
     success{
        echo 'Build and tests completed successfully!'
    }
     failure{
        echo 'Build or tests failed.'
        }
    }
}
