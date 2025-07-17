# Sweet Shop 🍬

A Flask-based sweet shop management system with JSON storage for managing inventory, orders, and customer data.

## 📋 Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **Inventory Management**: Add, update, delete, and view sweet products
- **Order Processing**: Handle customer orders and order history
- **Customer Management**: Manage customer information and profiles
- **JSON Storage**: Lightweight data persistence using JSON files
- **Responsive Design**: Mobile-friendly user interface
- **Search & Filter**: Find products by name, category, or price range
- **Dashboard**: Admin panel for managing the shop operations

## 🛠️ Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Data Storage**: JSON files
- **Styling**: Bootstrap/CSS3
- **Version Control**: Git

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/KrishPatel5611/Sweet_Shop.git
   cd Sweet_Shop
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser and visit**
   ```
   http://localhost:5000
   ```

## 🚀 Usage

### For Customers
- Browse available sweets and their details
- Add items to cart
- Place orders
- View order history

### For Admins
- Manage inventory (add/edit/delete products)
- View and process orders
- Manage customer data
- Generate reports

## 📁 Project Structure

```
Sweet_Shop/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
│
├── static/
│   ├── css/
│   │   └── style.css     # Custom styles
│   ├── js/
│   │   └── script.js     # JavaScript functionality
│   └── images/           # Product images
│
├── templates/
│   ├── base.html         # Base template
│   ├── index.html        # Home page
│   ├── products.html     # Products listing
│   ├── cart.html         # Shopping cart
│   └── admin/            # Admin templates
│
├── data/
│   ├── products.json     # Product data
│   ├── orders.json       # Order data
│   └── customers.json    # Customer data
│
└── utils/
    ├── __init__.py
    ├── data_manager.py   # JSON data operations
    └── helpers.py        # Helper functions
```

## 🔗 API Endpoints

### Products
- `GET /api/products` - Get all products
- `POST /api/products` - Add new product
- `PUT /api/products/<id>` - Update product
- `DELETE /api/products/<id>` - Delete product

### Orders
- `GET /api/orders` - Get all orders
- `POST /api/orders` - Create new order
- `GET /api/orders/<id>` - Get specific order

### Customers
- `GET /api/customers` - Get all customers
- `POST /api/customers` - Register new customer
- `GET /api/customers/<id>` - Get customer details

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 Future Enhancements

- [ ] User authentication and authorization
- [ ] Payment gateway integration
- [ ] Email notifications
- [ ] Database migration (from JSON to SQLite/PostgreSQL)
- [ ] Product categories and tags
- [ ] Inventory alerts for low stock
- [ ] Sales analytics and reporting

## 🐛 Known Issues

- JSON file locking in concurrent access scenarios
- No data validation on frontend forms
- Limited error handling for file operations

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Krish Patel**
- GitHub: [@KrishPatel5611](https://github.com/KrishPatel5611)
- LinkedIn: [Your LinkedIn Profile](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Flask documentation and community
- Bootstrap for responsive design
- Icons from Font Awesome
- Inspiration from various e-commerce projects

---

⭐ If you found this project helpful, please give it a star!