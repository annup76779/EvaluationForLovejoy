# Lovejoy Antique Evaluation Web Application Documentation

## Table of Contents

1. [Introduction](#introduction)
2. [Project Overview](#project-overview)
3. [Technologies Used](#technologies-used)
4. [Features and Implementation Details](#features-and-implementation-details)
   - [User Registration](#user-registration)
   - [Password Policy Enforcement](#password-policy-enforcement)
   - [Email Verification](#email-verification)
   - [User Login](#user-login)
   - [Password Recovery](#password-recovery)
   - [Evaluation Request Page](#evaluation-request-page)
   - [Admin Request Listing Page](#admin-request-listing-page)
   - [File Upload Security](#file-upload-security)
   - [Brute Force Protection](#brute-force-protection)
   - [Logging and Monitoring](#logging-and-monitoring)
   - [Session Security](#session-security)
   - [Security Measures Implemented](#security-measures-implemented)
5. [Skipped Features](#skipped-features)
6. [Conclusion](#conclusion)

---

## Introduction

The Lovejoy Antique Evaluation Web Application is designed to provide users with a secure platform to request antique evaluations. It emphasizes robust security measures, responsive design, and user-friendly interfaces to ensure both functionality and protection against common web vulnerabilities.

---

## Project Overview

- **Purpose**: Allow users to submit antique evaluation requests, including uploading photos and providing comments.
- **Audience**: Users interested in antique evaluations and administrators managing the requests.
- **Goals**:
  - Implement secure user authentication and authorization.
  - Provide a responsive and intuitive user interface.
  - Ensure data integrity and protection against security threats.

---

## Technologies Used

- **Python 3.x**: Backend programming language.
- **Django**: Web framework for rapid development and clean design.
- **SQLite**: Default database for development (easily switchable for production).
- **Bootstrap**: Frontend framework for responsive design.
- **JavaScript**: Enhances frontend interactivity and validation.
- **HTML5 & CSS3**: Markup and styling languages for web pages.
- **Django-Axes**: Protects against brute force attacks.
- **Python-Magic**: Validates file uploads to ensure correct file types.

---

## Features and Implementation Details

### User Registration

#### Description

- **Functionality**: Allows users to create an account by providing a username, email, phone number, and password.
- **Implementation**:
  - **Custom User Model**: Extended Django's `AbstractUser` to include a `phone_number` field.
  - **Forms**: Utilized Django forms with Bootstrap for styling.
  - **Validation**:
    - Backend: Ensured unique usernames and emails, validated phone number format.
    - Frontend: Used HTML5 attributes (`required`, `pattern`) for immediate feedback.

#### Tools and Technologies

- Django Models and Forms
- Bootstrap for styling
- JavaScript for additional validation

#### Needs Addressed

- **User Authentication**: Establishes a secure method for users to access the application.
- **Data Integrity**: Validates and stores accurate user information.
- **User Experience**: Provides a straightforward registration process.

#### Impact on Application

- **Foundation for User Interactions**: Enables personalized experiences and access control.
- **Security**: Validated inputs prevent malicious data from entering the system.
- **Scalability**: Custom user model allows for future expansion of user-related features.

---

### Password Policy Enforcement

#### Description

- **Functionality**: Enforces strong password requirements and provides real-time feedback on password strength.
- **Implementation**:
  - **Custom Password Validator**: Enforced minimum length, uppercase, lowercase, digit, and special character requirements.
  - **Frontend Feedback**: Implemented a JavaScript-based password strength meter.

#### Tools and Technologies

- Django's `AUTH_PASSWORD_VALIDATORS`
- Custom Python validators
- JavaScript for the strength meter

#### Needs Addressed

- **Security**: Strong passwords reduce the risk of unauthorized access.
- **Compliance**: Meets industry standards for password policies.
- **User Guidance**: Helps users create secure passwords through immediate feedback.

#### Impact on Application

- **Enhanced Account Security**: Protects user data and accounts.
- **User Trust**: Users feel confident in the application's commitment to security.
- **Reduced Support**: Fewer account recovery issues due to compromised passwords.

---

### Email Verification

#### Description

- **Functionality**: Requires users to verify their email address before activating their account.
- **Implementation**:
  - Sent verification emails with unique tokens.
  - Accounts remain inactive until verification is completed.
  - Used Django's `urlsafe_base64_encode` and token generators for secure links.

#### Tools and Technologies

- Django's email utilities
- Token generation and validation
- Custom email templates

#### Needs Addressed

- **Account Security**: Ensures users own the email addresses they register with.
- **Spam Prevention**: Reduces fake or malicious account creation.
- **Communication Reliability**: Validated emails improve notification delivery.

#### Impact on Application

- **Improved Data Quality**: Maintains a database of verified, active users.
- **Security Enhancement**: Adds an extra layer of account protection.
- **Professionalism**: Users perceive the application as trustworthy and secure.

---

### User Login

#### Description

- **Functionality**: Allows registered users to log in securely.
- **Implementation**:
  - Utilized Django's authentication system.
  - Customized login view to provide informative error messages.
  - Integrated Bootstrap for responsive design.

#### Tools and Technologies

- Django Authentication
- Bootstrap for form styling
- Custom views for enhanced control

#### Needs Addressed

- **User Access**: Provides a secure entry point for users.
- **Feedback Mechanism**: Informs users of login success or failure.
- **Session Management**: Maintains user sessions securely.

#### Impact on Application

- **User Engagement**: Facilitates ongoing interaction with the application.
- **Security**: Protects against unauthorized access.
- **User Satisfaction**: Streamlined login process improves user experience.

---

### Password Recovery

#### Description

- **Functionality**: Enables users to reset their passwords via email.
- **Implementation**:
  - Used Django's built-in password reset views.
  - Customized email templates and forms.
  - Logged password reset requests for monitoring.

#### Tools and Technologies

- Django's password reset framework
- Email sending configurations
- Logging mechanisms

#### Needs Addressed

- **User Convenience**: Allows self-service password recovery.
- **Security**: Securely handles password changes.
- **Account Management**: Reduces support burden for password issues.

#### Impact on Application

- **User Retention**: Users can easily regain access, reducing abandonment.
- **Security Monitoring**: Logs provide insights into potential abuse.
- **Professional Image**: Offers features users expect from modern applications.

---

### Evaluation Request Page

#### Description

- **Functionality**: Authenticated users can submit evaluation requests with comments and photo uploads.
- **Implementation**:
  - Created `EvaluationRequest` model to store requests.
  - Form with validation for required fields.
  - File uploads handled securely with size and type checks.

#### Tools and Technologies

- Django Models and Forms
- Custom upload handlers
- Bootstrap for responsive design

#### Needs Addressed

- **Core Service Delivery**: Enables the primary function of antique evaluations.
- **User Interaction**: Engages users by allowing submissions.
- **Data Collection**: Gathers necessary information for evaluations.

#### Impact on Application

- **Value Proposition**: Delivers on the application's main promise.
- **User Satisfaction**: Provides an easy and secure way to request services.
- **Operational Efficiency**: Organizes data for administrators to process requests.

---

### Admin Request Listing Page

#### Description

- **Functionality**: Displays a list of all evaluation requests for administrators.
- **Implementation**:
  - Used Django's `ListView` for efficient data handling.
  - Added pagination and filtering by date, user, and keywords.
  - Styled with Bootstrap for clarity and responsiveness.

#### Tools and Technologies

- Django Class-Based Views
- Pagination and filtering mechanisms
- Bootstrap for table styling

#### Needs Addressed

- **Data Management**: Allows admins to review and manage requests efficiently.
- **Scalability**: Handles large numbers of requests without performance degradation.
- **Usability**: Provides tools to find and process specific requests quickly.

#### Impact on Application

- **Administrative Efficiency**: Streamlines the evaluation process.
- **Enhanced Control**: Gives administrators oversight of user submissions.
- **Professional Operation**: Supports organized and effective business processes.

---

### File Upload Security

#### Description

- **Functionality**: Securely handles file uploads by renaming files and validating content.
- **Implementation**:
  - Renamed uploaded files with timestamps to prevent overwriting.
  - Validated file size and type (images only).
  - Stored files in a dedicated directory with restricted access.

#### Tools and Technologies

- Custom file upload functions
- `python-magic` for file type validation
- Django's storage backends

#### Needs Addressed

- **Security**: Prevents malicious files from being uploaded.
- **Data Integrity**: Ensures correct association of files with requests.
- **User Experience**: Simplifies the process of adding images to requests.

#### Impact on Application

- **Reduced Risk**: Minimizes potential security threats from file uploads.
- **Data Organization**: Maintains a clean and orderly file system.
- **User Confidence**: Users trust the application with their personal files.

---

### Brute Force Protection

#### Description

- **Functionality**: Protects against brute force login attempts by limiting failed logins.
- **Implementation**:
  - Integrated `django-axes` to monitor and lock out repeated failed attempts.
  - Configured custom lockout templates and cool-off periods.
  - Removed deprecated settings to comply with the latest `django-axes` version.

#### Tools and Technologies

- `django-axes` library
- Logging for tracking attempts
- Custom templates for user feedback

#### Needs Addressed

- **Security**: Shields user accounts from automated hacking attempts.
- **Compliance**: Aligns with security best practices.
- **User Protection**: Ensures legitimate users aren't compromised.

#### Impact on Application

- **Enhanced Security Posture**: Strengthens defense against common attack vectors.
- **User Awareness**: Notifies users of suspicious activities.
- **Operational Assurance**: Reduces risk of unauthorized access.

---

### Logging and Monitoring

#### Description

- **Functionality**: Implements comprehensive logging for key events and potential security issues.
- **Implementation**:
  - Configured Django's logging framework with custom handlers.
  - Logged failed login attempts, password reset requests, and file uploads.
  - Ensured logs are stored securely and access is restricted.

#### Tools and Technologies

- Django's logging system
- Custom loggers and formatters
- Secure file permissions

#### Needs Addressed

- **Security Monitoring**: Tracks and analyzes potential threats.
- **Debugging**: Facilitates troubleshooting and error resolution.
- **Compliance**: Provides an audit trail for security audits.

#### Impact on Application

- **Proactive Security**: Early detection of anomalies prevents escalation.
- **Operational Transparency**: Clear record of application activities.
- **Maintenance Efficiency**: Simplifies identification of issues.

---

### Session Security

#### Description

- **Functionality**: Secures user sessions against hijacking and cross-site attacks.
- **Implementation**:
  - Enabled secure and HTTP-only cookies.
  - Configured CSRF settings to ensure tokens are transmitted securely.
  - Set session expiration policies.

#### Tools and Technologies

- Django session and CSRF settings
- HTTPS enforcement
- Cookie configuration

#### Needs Addressed

- **Data Protection**: Safeguards session data from interception.
- **Regulatory Compliance**: Meets standards for secure session management.
- **User Trust**: Assures users of the application's commitment to security.

#### Impact on Application

- **Risk Reduction**: Lowers the chance of session-based attacks.
- **User Assurance**: Builds confidence in secure interactions.
- **Security Baseline**: Establishes a foundation for secure development.

---

### Security Measures Implemented

#### Description

- **Functionality**: Addressed common web vulnerabilities through best practices.
- **Implementation**:
  - **SQL Injection Prevention**: Used Django ORM to prevent injection attacks.
  - **Cross-Site Scripting (XSS)**: Ensured proper escaping in templates.
  - **Cross-Site Request Forgery (CSRF)**: Enabled CSRF protection on all forms.

#### Tools and Technologies

- Django's built-in protections
- Input validation and sanitization
- Secure coding practices

#### Needs Addressed

- **Application Integrity**: Prevents malicious manipulation of the application.
- **Data Security**: Protects sensitive information from unauthorized access.
- **User Safety**: Ensures users interact with a secure platform.

#### Impact on Application

- **Robust Security**: Comprehensive defenses against common threats.
- **Compliance**: Aligns with OWASP Top Ten security recommendations.
- **User Confidence**: Encourages continued use by ensuring safety.

---

## Skipped Features

### CAPTCHA Implementation

- **Decision**: Chose to skip the implementation of CAPTCHA for simplicity.
- **Reasoning**:
  - Considered non-critical for the MVP.
  - Other security measures in place mitigate automated attacks.
- **Impact**:
  - Slightly increased risk of automated bot interactions.
  - Future iterations can include CAPTCHA if necessary.

### Role-Based Access Control (RBAC)

- **Decision**: Opted not to implement detailed RBAC at this stage.
- **Reasoning**:
  - Application currently doesn't require complex role distinctions.
  - Administrators are identified by `is_staff` status.
- **Impact**:
  - All staff users have equal access to admin features.
  - Simplifies the current access model, but may need revisiting as the application grows.

---

## Conclusion

The Lovejoy Antique Evaluation Web Application successfully integrates essential features with a strong emphasis on security and user experience. By utilizing robust frameworks and adhering to best practices, the application provides a solid foundation for both users seeking antique evaluations and administrators managing those requests. The careful implementation of security measures ensures that user data is protected, and the application is resilient against common web vulnerabilities.

---

**Note**: This documentation outlines the key features and their implementations, providing insight into the application's capabilities and the rationale behind design decisions. Future enhancements can build upon this foundation to introduce additional functionalities and improvements.
# Here’s a **table of URLs and pages** for the application:

| **URL**                             | **Page Name**                    | **Description**                                                                                   | **Access Level**         | **Features**                                                                                     |
|-------------------------------------|-----------------------------------|---------------------------------------------------------------------------------------------------|--------------------------|--------------------------------------------------------------------------------------------------|
| `/`                                 | Home Page                        | Landing page of the application. Provides an introduction and navigation links.                  | Public                   | Navigation to key pages.                                                                        |
| `/users/register/`                  | Registration Page                | Allows users to create an account.                                                               | Public                   | Form validation, password strength feedback, and email verification.                           |
| `/users/login/`                     | Login Page                       | Allows registered users to log in.                                                               | Public                   | Secure login, informative error messages, brute force protection.                              |
| `/users/logout/`                    | Logout Page                      | Logs out the current user and redirects to the home page.                                         | Logged-In Users          | Ends user session securely.                                                                    |
| `/users/reset-password/`            | Password Reset Page              | Allows users to reset their password via email.                                                  | Public                   | Sends password reset link via email.                                                           |
| `/users/reset-password-confirm/<uidb64>/<token>/` | Password Reset Confirm Page      | Allows users to set a new password after verification.                                            | Public                   | Verifies token validity before password reset.                                                 |
| `/users/verification-sent/`         | Email Verification Sent Page     | Informs users that an email verification link has been sent.                                      | Public                   | Displays feedback to users.                                                                    |
| `/users/verify-email/<uid>/<token>/`| Email Verification Page          | Verifies a user’s email address using a secure token.                                             | Public                   | Activates user account upon verification.                                                      |
| `/evaluations/request/`             | Evaluation Request Page          | Allows users to submit evaluation requests with comments and optional file uploads.              | Logged-In Users          | Form validation, secure file uploads, and contact preference selection.                        |
| `/evaluations/success/`             | Evaluation Submission Success    | Confirms successful submission of an evaluation request.                                          | Logged-In Users          | Provides feedback after a successful submission.                                               |
| `/evaluations/admin-requests/`      | Admin Request Listing Page       | Displays a paginated list of all evaluation requests.                                             | Admin Users (`is_staff`) | Pagination, filtering by date, user, and keywords.                                             |
| `/permission-denied/`               | Permission Denied Page           | Displays an error message for unauthorized access attempts.                                       | Unauthorized Users       | Provides appropriate feedback to unauthorized users.                                           |
| `/media/uploads/<filename>/`        | Uploaded Files                   | URL to access uploaded files (handled by Django’s media storage settings).                       | Restricted (Django)      | Uploaded files stored securely with timestamp-based naming to prevent overwriting.             |

---

### **Additional Notes**
- **Public Pages**:
  - Accessible to all users, such as the home, login, and registration pages.
  - Ensures proper feedback and navigation for first-time users.

- **Logged-In User Pages**:
  - Accessible only after successful login, such as the evaluation request page.
  - Requires user authentication.

- **Admin-Only Pages**:
  - Restricted to staff users (`is_staff=True`), such as the admin request listing page.
  - Ensures sensitive data is visible only to authorized personnel.

- **Media Files**:
  - Uploaded files are served via Django’s `MEDIA_URL` and stored securely under `MEDIA_ROOT`.

Let me know if you need more details or adjustments!