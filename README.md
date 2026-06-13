# 🛒 ModernStore - Full Stack E-Commerce Website

A modern and responsive full-stack E-Commerce web application built with Django. Users can browse products, search by category, manage their shopping cart, place orders, track order history, cancel orders, and manage their profile.

---

## 🌐 Live Demo

https://prawin-modernstore.onrender.com

---

## 👤 Admin login

https://prawin-modernstore.onrender.com/admin/

### 🏠 Home Page
- Product listing
- Featured products
- Search functionality
- Category navigation

### 🛍 Product Details
- Product image
- Description
- Price
- Stock information
- Add to Cart

### 🛒 Shopping Cart
- Update quantity
- Remove products
- Dynamic total calculation

### 📦 Order Management
- Place orders
- View order history
- Cancel orders
- Delete cancelled orders

### 👤 User Profile
- Update personal information
- Manage address and contact details

---

# ✨ Features

## 🔐 Authentication System

- User Registration
- User Login
- User Logout
- Secure Password Validation
- User Profile Management

---

## 🛍 Product Management

- Product Categories
- Product Images
- Product Descriptions
- Product Pricing
- Stock Management
- Product Detail Pages

---

## 🔍 Search & Filtering

- Search Products by Name
- Search Products by Description
- Category-Based Filtering

---

## 🛒 Shopping Cart

- Add Products to Cart
- Remove Products from Cart
- Update Product Quantity
- Real-Time Cart Total Calculation
- AJAX Cart Updates

---

## 💳 Checkout System

- Shipping Information Form
- Order Creation
- Automatic Cart Clearing After Checkout
- Order Summary

---

## 📦 Order Management

- View Order History
- View Individual Order Details
- Cancel Pending Orders
- Delete Cancelled Orders
- Automatic Stock Restoration on Cancellation

---

## 🎨 UI/UX Features

- Responsive Design
- Mobile Friendly Layout
- Dark Mode Support
- Toast Notifications
- Modern Interface
- Clean Navigation

---

## 📱 Responsive Design

The application is fully responsive and works on:

- Desktop 💻
- Laptop 🖥️
- Tablet 📱
- Mobile 📲

---

# 🏗 Tech Stack

## Backend

- Django 4.2
- Python 3

## Frontend

- HTML5
- CSS3
- JavaScript (Vanilla JS)

## Database

- SQLite3

## Authentication

- Django Authentication System

## Media Handling

- Pillow

---

# 📂 Project Structure

```text
ecommerce/
│
├── ecommerce/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── store/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── signals.py
│   ├── context_processors.py
│
├── templates/
│
├── static/
│   ├── css/
│   ├── js/
│
├── media/
│
├── manage.py
│
└── requirements.txt
```

---

# 🗄 Database Models

## Category

- Name
- Slug
- Created Date

---

## Product

- Category
- Name
- Slug
- Image
- Description
- Price
- Stock
- Created Date

---

## Profile

- User
- Phone
- Address
- City
- Postal Code

---

## Cart

- User
- Created Date
- Updated Date

---

## CartItem

- Cart
- Product
- Quantity

---

## Order

- User
- Full Name
- Address
- City
- Postal Code
- Phone
- Total Amount
- Status
- Created Date

---

## OrderItem

- Order
- Product
- Quantity
- Price

---

# 🚀 Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/modernstore.git
cd modernstore
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 5️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

---

## 6️⃣ Start Development Server

```bash
python manage.py runserver
```

---

## 7️⃣ Open Browser

```text
http://127.0.0.1:8000/
```

---

# 🔑 Admin Panel

Access Django Admin:

```text
http://127.0.0.1:8000/admin/
```

Admin can:

- Add Categories
- Add Products
- Update Stock
- Manage Orders
- Manage Users

---

# 🌙 Dark Mode

The application includes Dark Mode support.

Features:

- Theme Toggle Button
- Theme Persistence
- Smooth Theme Switching

---

# 📦 Order Workflow

```text
Browse Products
      ↓
Add To Cart
      ↓
Update Cart
      ↓
Checkout
      ↓
Order Created
      ↓
Order History
      ↓
Cancel Order (Optional)
      ↓
Delete Cancelled Order (Optional)
```

---

# 🛡 Security Features

- CSRF Protection
- Django Authentication
- Login Required Views
- Secure Password Validation
- Protected Order Access
- User-Specific Data Access

---

# 📈 Future Improvements

- Wishlist System
- Product Reviews
- Product Ratings
- Payment Gateway Integration
- Email Notifications
- Coupon System
- Order Tracking
- Product Recommendations
- User Profile Pictures
- Multiple Product Images

---

# 🎯 Learning Outcomes

This project demonstrates:

- Django Models
- Django Views
- Django Forms
- Authentication System
- CRUD Operations
- AJAX Requests
- Database Relationships
- Responsive Design
- Full Stack Development
- Deployment Ready Architecture

---

# 👨‍💻 Author

**Maadesh**

Full Stack Developer (Learning)

Built as a Full Stack Django E-Commerce Project for internship and portfolio purposes.

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the repository

📢 Share with others

---

# 📄 License

This project is created for educational and portfolio purposes.
