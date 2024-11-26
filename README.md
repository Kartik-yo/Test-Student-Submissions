# Test Student Submissions CI/CD Pipeline  

This repository contains a fully automated CI/CD pipeline for testing, verifying, and analyzing student code submissions. The pipeline is designed to handle multiple repositories and integrates key features like build automation, code coverage reporting, and Slack notifications for better collaboration and tracking.  

## Key Features  
- **Automated Build & Test**: Uses Maven to build and run test cases automatically.  
- **Code Coverage Reporting**: Generates coverage reports using JaCoCo for better insights into code quality.  
- **Slack Notifications**: Sends real-time notifications to a Slack channel for build success or failure.  
- **Future-Ready**: The pipeline is designed for scalability, allowing for additional integrations like SonarQube.  

## Pipeline Workflow  
The pipeline workflow is defined in the `main.yaml` file and consists of the following steps:  
1. **Checkout Code**: Pulls the repository's code from GitHub.  
2. **Setup Java Environment**: Installs the required Java version (Temurin JDK 17).  
3. **Run Maven Tests**: Executes `mvn clean verify` to ensure all tests pass.  
4. **Generate Code Coverage Report**: Generates JaCoCo reports for test coverage.  
5. **Slack Notifications**: Notifies about the build status (success or failure).  

## Prerequisites  
To run the pipeline successfully, ensure the following:  
- A GitHub repository with a valid `repositories.txt` file listing student repositories.  
- Maven installed in the project.  
- JaCoCo plugin configured in the `pom.xml` file.  
- A Slack workspace and a webhook URL for notifications.  
- Environment variables configured in GitHub Actions secrets:  
  - `REPO_GITHUB_TOKEN`: GitHub personal access token.  
  - `SLACK_WEBHOOK_URL`: Slack webhook for notifications.  

## Usage  
1. Clone the repository:  
   ```bash
   git clone https://github.com/<your-username>/<your-repository>.git
   cd <your-repository>
   ```
2. Configure the repositories.txt file with the list of repositories to process.
3. Push the code to the main branch to trigger the pipeline automatically.

## Notifications
Slack notifications are sent in the following scenarios:
1. Build Success: A success message is posted.
2. Build Failure: The failure details are posted for quick debugging.

## Limitations
SonarQube integration is temporarily disabled due to project key configuration issues. This can be revisited and enabled later.
Technologies Used:

1. Java: Temurin JDK 17
2. Maven: For build and dependency management
3. JaCoCo: For code coverage
4. GitHub Actions: CI/CD pipeline
5. Slack: For notifications
