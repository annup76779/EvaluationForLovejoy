### **Steps to Run the Application**

#### **1. Setup and Installation**
1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   - Apply migrations to initialize the database:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

5. **Collect Static Files**:
   - Gather static files for production (if needed):
     ```bash
     python manage.py collectstatic
     ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**:
   - Open a browser and navigate to:
     ```
     http://127.0.0.1:8000/
     ```

---

### **User Flow**

#### **1. Guest User (Unregistered User)**

1. **Home Page**:
   - The guest user lands on the home page and can see an introduction to the application with navigation links (e.g., Register, Login).
   
2. **Register**:
   - Click on "Register" and fill in the registration form:
     - Provide a valid email, username, phone number, and strong password.
   - After submission:
     - A verification email is sent to the provided email address.
     - The user is redirected to the **verification sent page**.

3. **Email Verification**:
   - Check the email inbox for the verification email.
   - Click on the verification link to activate the account.
   - The link redirects the user to the login page.

4. **Login**:
   - Log in using the registered username and password.
   - If login is successful, the user is redirected to the evaluation request page.

---

#### **2. Normal User (Logged-In User)**

1. **Submit Evaluation Request**:
   - After logging in, the user can navigate to the **evaluation request page**.
   - Fill in the evaluation form:
     - Enter a comment.
     - Select a preferred contact method (email or phone).
     - Optionally, upload a photo of the antique item.
   - Submit the form:
     - The request is saved in the database.
     - A confirmation page is displayed indicating successful submission.

2. **Logout**:
   - Users can log out from the application via the logout link in the navigation bar.
   - This ends the session and redirects the user to the home page.

---

#### **3. Admin User**

1. **Login**:
   - Admin users (users with `is_staff=True`) log in like normal users.

2. **Admin Request Listing Page**:
   - After login, admin users can access the **admin request listing page** (`/evaluations/admin-requests/`).
   - Features available:
     - View a paginated list of all evaluation requests.
     - Filter requests by:
       - Date range.
       - Username.
       - Keywords in comments.
     - Click on uploaded photos to view them.

3. **Review and Process Requests**:
   - Admins can use the provided filtering options to narrow down results and review specific evaluation requests.

4. **Logout**:
   - Admins can log out like normal users.

---

### **Complete Flow Summary**

| **User Type** | **Actions**                                                                                                                 | **Outcome**                                                                                      |
|---------------|-----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| **Guest User** | - Registers an account.                                                                                                    | - Receives verification email.                                                                  |
|               | - Verifies email.                                                                                                          | - Account is activated, and the user can log in.                                                |
| **Normal User**| - Logs in.                                                                                                                 | - Gains access to the evaluation request page.                                                  |
|               | - Submits evaluation requests (comment, contact preference, optional file upload).                                          | - Requests are saved in the database and processed by admins.                                   |
| **Admin User** | - Logs in.                                                                                                                 | - Gains access to the admin request listing page.                                               |
|               | - Views paginated, filterable list of evaluation requests.                                                                 | - Can review submissions and view uploaded photos.                                              |

---

### **Next Steps After Running**
If the application is working as expected:
1. **Deploy** to a production server (e.g., Heroku, AWS).
2. **Monitor** logs and user feedback to address any issues.
3. **Enhance** skipped features (e.g., CAPTCHA or role-based access control) if needed.

Let me know if you need help with any specific part of the flow or deployment!