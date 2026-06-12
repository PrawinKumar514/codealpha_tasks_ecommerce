# ModernStore - Complete E-Commerce Website

A fully functional, production-ready e-commerce platform built with Django. Features user authentication, product catalog, shopping cart, order processing, dark mode, and responsive design.

## ✨ Features

### User System
- User registration with validation
- Secure login/logout
- Password validation (Django defaults)
- User profile page with editable details
- Order history for each user

### Product Management
- Product listings with pagination
- Product detail pages with images
- Category-based filtering
- Search by product name or description
- Stock quantity tracking

### Shopping Cart
- Add/remove items without page refresh (AJAX)
- Update quantities dynamically
- Real-time cart counter update
- Toast notifications for actions
- Cart total calculation

### Order Processing
- Secure checkout with shipping form
- Order summary before placement
- Order status tracking (Pending, Processing, Shipped, Delivered, Cancelled)
- Order history with detailed views
- Automatic stock deduction after order

### User Experience
- **Dark Mode Toggle** with localStorage persistence
- Fully responsive design (Mobile, Tablet, Desktop)
- Modern product cards with hover effects
- Smooth animations
- Empty cart illustration
- Professional color scheme

### Admin Panel
- Full CRUD for Products, Categories, Orders
- Image preview in product list
- Search and filters
- Order status management

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Django 4.2 |
| Database | SQLite (development) / PostgreSQL (production) |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Icons | Font Awesome 6 |
| Images | Pillow (Django ImageField) |

## 📁 Project Structure
ecommerce/
├── manage.py
├── requirements.txt
├── README.md
├── ecommerce/ # Project settings
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── store/ # Main app
│ ├── models.py # Category, Product, Cart, Order
│ ├── views.py # Class-based & function-based views
│ ├── admin.py # Admin customizations
│ ├── forms.py # Registration, Profile, Checkout forms
│ ├── urls.py # App routes
│ ├── signals.py # Auto-create profile & cart on user signup
│ ├── context_processors.py # Categories & cart count for all templates
│ ├── templates/
│ │ ├── base.html
│ │ ├── registration/
│ │ │ ├── login.html
│ │ │ └── register.html
│ │ └── store/
│ │ ├── home.html
│ │ ├── product_list.html
│ │ ├── product_detail.html
│ │ ├── cart.html
│ │ ├── checkout.html
│ │ ├── order_history.html
│ │ ├── order_detail.html
│ │ └── profile.html
│ └── static/
│ ├── css/main.css
│ └── js/
│ ├── main.js
│ └── cart.js
├── static/ # Collected static files (production)
└── media/ # User-uploaded product images

text

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step 1: Clone or Download
Extract the project to a folder named `ecommerce`.

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
Step 3: Install Dependencies
bash
pip install -r requirements.txt
Step 4: Apply Migrations
bash
python manage.py makemigrations
python manage.py migrate
Step 5: Create Superuser (Admin)
bash
python manage.py createsuperuser
Follow the prompts to set username, email, and password.

Step 6: Run Development Server
bash
python manage.py runserver
Open your browser at http://127.0.0.1:8000

Step 7: Add Sample Products (Optional)
Visit http://127.0.0.1:8000/admin

Log in with your superuser credentials

Click "Add" under Categories → create categories (e.g., Electronics, Clothing)

Click "Add" under Products → fill details, upload images, set price and stock

🖥️ Usage Guide
For Customers
Register a new account or Login.

Browse products via Home or Shop page.

Use Search bar or Category filters to find products.

Click View Details to see full product info.

Click Add to Cart – a toast notification confirms.

Go to Cart page to update quantities or remove items.

Proceed to Checkout, fill shipping details, and Place Order.

View all orders in My Orders section.

Update personal info in Profile page.

Toggle Dark Mode using the moon icon in navbar.

For Admin (via /admin)
Products: Add, edit, delete products. Stock and price editable directly from list view.

Categories: Manage product categories.

Orders: Update order status (Pending → Processing → Shipped → Delivered).

Users: View registered users (profiles automatically created).

Cart/Items: Monitor active carts (read-only).

🌙 Dark Mode
Click the moon icon in the top-right corner.

Preference is saved in localStorage and persists across sessions.

Smooth transition between light and dark themes.

📱 Responsive Design
Mobile: Stacked navigation, full-width search, single-column product grid.

Tablet: Two-column product grid, adjusted spacing.

Desktop: Multi-column grid, sticky navbar, side-by-side checkout.

🔒 Security Features
CSRF protection on all POST forms.

Login required for cart, checkout, profile, and orders.

Password validation (minimum length, not too common, not entirely numeric).

Order items linked to authenticated user; users cannot view others' orders.

Stock validation prevents over-purchasing.

🧪 Testing the Application
After setup, test these flows:

Registration → http://127.0.0.1:8000/register/

Login → http://127.0.0.1:8000/login/

Product browsing → http://127.0.0.1:8000/products/

Add to cart – open browser console to see AJAX responses.

Checkout – after adding items.

Order history – after placing an order.

🚢 Deployment
Deploy to Render (Recommended)
Push this project to a GitHub repository.

Create a new Web Service on Render.

Connect your repository.

Set:

Build Command: pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate

Start Command: gunicorn ecommerce.wsgi:application

Add environment variables:

SECRET_KEY (generate a new one)

DEBUG=False

ALLOWED_HOSTS=.onrender.com

(Optional) Use Cloudinary for media files or switch to PostgreSQL.

Deploy to Railway
Similar steps: connect GitHub repo, set start command to gunicorn ecommerce.wsgi:application, add environment variables.

Deploy to PythonAnywhere
Upload files (or use Git).

Set up virtual environment, install requirements.

Configure ALLOWED_HOSTS and static files.

Set up a web app with WSGI pointing to ecommerce.wsgi.

Production Checklist
Set DEBUG = False

Generate a new SECRET_KEY

Configure ALLOWED_HOSTS

Switch to PostgreSQL (add psycopg2-binary to requirements)

Set up static file serving via WhiteNoise or CDN

Use environment variables for sensitive data

Configure media storage (e.g., AWS S3, Cloudinary)

📦 Database Schema
Model	Fields
Category	name, slug
Product	category, name, slug, image, description, price, stock
Profile	user (OneToOne), phone, address, city, postal_code
Cart	user (OneToOne)
CartItem	cart, product, quantity
Order	user, full_name, address, city, postal_code, phone, total_amount, status, created_at
OrderItem	order, product, quantity, price
🐛 Troubleshooting
Issue	Solution
No module named 'store'	Run python manage.py makemigrations store
Images not loading	Ensure MEDIA_URL and MEDIA_ROOT are set. Run python manage.py runserver (development serves media).
AJAX add to cart fails	Check browser console for CSRF errors. Ensure you're logged in.
Dark mode not saving	Clear localStorage or check console for JavaScript errors.
Cart count not updating	Verify cart_count context processor is in settings.py TEMPLATES context_processors.
🤝 Contributing
This project is for portfolio and educational purposes. Feel free to fork and enhance.

📄 License
MIT License – free to use, modify, and distribute with attribution.

📧 Support
For issues, create a GitHub issue or check Django documentation.