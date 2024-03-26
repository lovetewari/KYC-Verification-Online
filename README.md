# e-KYC Verification Process:
e-KYC verification electronically confirms user identities using trusted government IDs for compliance and trust.


https://github.com/lovetewari/KYC-Verification-Online/assets/92184403/39bff6c1-b208-436f-9c37-ad17bc19e42d


## Problem Statement 🛠️

Currently, Know Your Customer (KYC) processes are predominantly offline or non-interactive online processes. These methods are often manual, cumbersome, and lack user engagement. They can be particularly challenging for users with limited financial resources or education levels. Additionally, existing processes may not be inclusive across languages and generations.

We aim to address these challenges by creating an online interactive Video KYC process. This process should be intuitive, self-sufficient, and highly inclusive. It should capture the user's live photograph and basic details such as name, date of birth (DOB), address, PAN card/Aadhaar, signature, income range, and type of employment in a conversational manner. Our goal is to bridge the gap across languages and generations, ensuring accessibility for all users regardless of their financial status or educational background.


## Solution 💪🏽

Our platform aims to streamline and automate the Video KYC process, making it faster, more user-friendly, and compliant. We propose the following features:

**Implementation Steps:**
1. **User Registration:**
   - Users provide basic details like name, email, and phone number for registration.
2. **Document Collection:**
   - Users submit valid government-issued identification documents, following clear instructions on acceptable types and image quality.
3. **Document Verification:**
   - OCR technology extracts information from documents and validates authenticity, expiry date, and other details.
4. **Liveness Detection:**
   - Incorporate liveness detection to ensure physical presence during the verification process.
5. **Data Encryption:**
   - Implement strong encryption mechanisms for data protection during transmission and storage.
6. **Compliance Check:**
   - Ensure compliance with local and international regulations for identity verification.
7. **Biometric Verification (Optional):**
   - Implement biometric verification methods like fingerprint or facial recognition for enhanced security.
8. **Integration:**
   - Integrate e-KYC process seamlessly into the platform's user onboarding.
9. **User Consent:**
   - Clearly communicate the e-KYC process and obtain explicit consent from users.


## Tech Stack:🧠
- **Frontend Development:**
  - HTML, CSS, JavaScript (JS): Frontend development for user interface.
- **Backend Development:**
  - Express.js: Backend framework for server-side logic and API development.
- **Machine Learning:**
  - Transformers: Utilized for advanced natural language processing tasks.
  - OpenCV: Employed for image processing and computer vision functionalities.
- **Infrastructure Management/Cloud Computing/DevOps:**
  - Docker: Containerization technology for efficient deployment and scalability.
  - Kubernetes: Orchestration tool for managing containerized applications.
  - AWS (Amazon Web Services) or Google Cloud Platform (GCP): Cloud computing services for hosting and scaling the application.
  - CI/CD Pipelines: Automated deployment pipelines for continuous integration and delivery.
  
**Future Architecture Working Flow:**
- The application utilizes containerization with Docker to encapsulate the application and its dependencies into isolated containers, ensuring consistency across different environments.
- These containers are then managed and orchestrated using Kubernetes, providing scalability, resilience, and automated deployment capabilities.
- Cloud computing services such as AWS or GCP are utilized to host the containerized application, leveraging their infrastructure for reliability and scalability.
- CI/CD pipelines are implemented for automated testing, building, and deployment of the application, ensuring rapid and reliable delivery of updates.

                         +-------------------+       +-------------------------+
                         |    Frontend       | <---> |         Backend         |
                         | (HTML/CSS/JS)     |       |     (Express.js)        |
                         +-------------------+       +-------------------------+
                                  |                           |
                                  |                           |
                                  |                           |
                                  |                           |
                         +-------------------+                |
                         |  Containerized    |                |
                         |    Application    |<---------------+
                         |  (Docker/K8s)     |
                         +-------------------+
                                  |
                                  |
                         +-------------------+
                         |  Cloud Platform   |
                         |  (AWS/GCP)        |
                         +-------------------+


# Workflow
1) Language Selection
2) Phone number Authentication
3) Information Input
4) Aadhar Card Verification
5) Liveness Detection 
6) Face Recognition
7) Signature Validation
8) Biometrics Validaton (Fingerprint or FaceID(Apple))


**Future Scope:**
- Implementation of serverless computing using AWS Lambda or Google Cloud Functions for cost optimization and scalability.
- Integration of monitoring and logging tools such as Prometheus and ELK stack for real-time performance monitoring and debugging.
- Adoption of Infrastructure as Code (IaC) principles using tools like Terraform or AWS CloudFormation for managing infrastructure configurations.
- Implementation of auto-scaling policies based on resource utilization metrics for efficient resource allocation and cost management.
- Incorporation of security measures such as encryption at rest and in transit, role-based access control (RBAC), and intrusion detection systems (IDS) for enhanced data protection and compliance.



## Acknowledgements

This project was developed as part of the Standard Chartered Hackathon.

## Contributors

- Love Tewari
- Akash Thakur
- Aryan Singh
- Aditya Mishra
- Anshuman Mishra
- Vyshnavi Prabha
