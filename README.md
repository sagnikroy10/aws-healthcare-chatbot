# 🩺 Doctor Appointment Chatbot

## 🧠 Overview
This project is a **virtual health assistant chatbot** built using **Amazon Lex V2** that helps users **book, cancel, or reschedule doctor appointments**. The chatbot is deployed on an **Amazon S3 static website** and communicates with **AWS Lambda, DynamoDB, SQS, and SNS** for backend operations. It provides a smooth and interactive experience for users looking to manage their healthcare appointments online.

## ⚙️ How It Works
- The chatbot is powered by **Amazon Lex V2**, which understands user messages and identifies intents such as booking, canceling, or rescheduling appointments.  
- **AWS Lambda (LF1)** handles the logic for processing user requests and sends data to **SQS** for message queuing.  
- Another **Lambda (LF2)** reads messages from **SQS**, queries data from **DynamoDB**, and sends notifications through **SNS**.  
- The **frontend** (HTML, CSS, JavaScript) is hosted on **Amazon S3**, allowing users to interact with the bot via a clean and responsive chat interface.

## ✨ Features
- Book, cancel, and reschedule doctor appointments  
- Automatic email or SMS confirmation through SNS  
- Clean, responsive chatbot UI hosted on S3  
- End-to-end integration of AWS services (Lex, Lambda, DynamoDB, SQS, SNS)

## 🚀 Tech Stack
**Frontend:** HTML, CSS, JavaScript  
**Backend:** AWS Lambda, DynamoDB, SQS, SNS  
**Chatbot Engine:** Amazon Lex V2  
**Hosting:** Amazon S3  

## 🧩 Architecture
1. **Amazon Lex V2** — handles natural language understanding  
2. **Lambda LF1** — processes intents and sends messages to SQS  
3. **SQS Queue** — stores user requests temporarily  
4. **Lambda LF2** — reads from SQS and interacts with DynamoDB and SNS  
5. **DynamoDB** — stores appointment and doctor data  
6. **SNS** — sends notifications (email/SMS)  
7. **S3 Website** — serves as the chatbot frontend  

## 🧱 Challenges Faced
Since this was my first time using AWS, it took time to understand how services like Lex, Lambda, and S3 connect and work together. Deploying on S3 and managing IAM permissions for Lambda and API Gateway were also challenging at first.

## 🔧 Future Improvements
- Make the chatbot more interactive with a modern UI  
- Integrate real-time doctor availability using APIs  
- Add voice support and live appointment confirmations  

## 💡 Learning Outcome
This project helped me understand **serverless architecture**, **cloud integration**, and how different **AWS services** interact in a real-world use case.


<img width="641" height="674" alt="image" src="https://github.com/user-attachments/assets/4700efe3-64fe-41b0-adb6-dd24b6e7de7d" />

