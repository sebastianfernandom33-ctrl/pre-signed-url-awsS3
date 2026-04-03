# AWS S3 Pre-Signed URL Lab

This project demonstrates how to securely upload and download files from Amazon S3 using pre-signed URLs generated with AWS Lambda.

## 🧰 Technologies

* AWS Lambda
* Amazon S3
* IAM
* Python (boto3)

## 🏗️ Architecture

Client → Lambda → S3 (Pre-Signed URL)

## 🚀 Features

* Secure file upload using pre-signed URL
* Secure file download using pre-signed URL
* No public access to S3 bucket

## 📡 How It Works

1. Lambda generates a pre-signed URL
2. The client uses the URL to upload/download files
3. Access is temporary and secure

## 🧪 Example (Upload)

```bash
curl -X PUT -T archivo.txt "PRESIGNED_URL"
```

## 🧪 Example (Download)

```bash
curl "PRESIGNED_URL" -o descarga.txt
```

## 🔐 Security

* S3 bucket is private
* Access is controlled via temporary URLs
* IAM policies restrict access

## 🌍 Real-World Use Case

This pattern is commonly used in production systems to allow users to upload files securely without exposing AWS credentials.

## 🧠 Learning Outcomes

* Implemented secure file transfer with pre-signed URLs
* Understood IAM permissions and security
* Worked with AWS Lambda and S3 integration
