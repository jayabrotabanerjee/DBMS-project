import sys
import mysql.connector
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton,
    QComboBox, QMessageBox, QTableWidget, QTableWidgetItem, QHBoxLayout
)

# Database connection configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'username',
    'password': 'password',
    'database': 'RealEstateDB'
}

# Main Application Window
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Real Estate Management System")
        self.setGeometry(150, 150, 800, 600)
        self.connection = self.connect_to_db()
        self.initUI()

    def connect_to_db(self):
        try:
            connection = mysql.connector.connect(**DB_CONFIG)
            return connection
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error connecting to database: {err}")
            sys.exit(1)

    def initUI(self):
        layout = QVBoxLayout()

        # Buttons for different management windows
        property_btn = QPushButton("Manage Properties")
        property_btn.clicked.connect(self.open_properties_window)
        
        listings_btn = QPushButton("Manage Listings")
        listings_btn.clicked.connect(self.open_listings_window)
        
        transactions_btn = QPushButton("Manage Transactions")
        transactions_btn.clicked.connect(self.open_transactions_window)
        
        bidding_btn = QPushButton("Manage Bidding")
        bidding_btn.clicked.connect(self.open_bidding_window)

        layout.addWidget(property_btn)
        layout.addWidget(listings_btn)
        layout.addWidget(transactions_btn)
        layout.addWidget(bidding_btn)

        self.setLayout(layout)

    def open_properties_window(self):
        self.properties_window = PropertiesWindow(self.connection)
        self.properties_window.show()

    def open_listings_window(self):
        self.listings_window = ListingsWindow(self.connection)
        self.listings_window.show()

    def open_transactions_window(self):
        self.transactions_window = TransactionsWindow(self.connection)
        self.transactions_window.show()

    def open_bidding_window(self):
        self.bidding_window = BiddingWindow(self.connection)
        self.bidding_window.show()

# Properties Management Window
class PropertiesWindow(QWidget):
    def __init__(self, connection):
        super().__init__()
        self.setWindowTitle("Manage Properties")
        self.setGeometry(150, 150, 700, 500)
        self.connection = connection
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Form fields
        self.address1_input = QLineEdit()
        self.address1_input.setPlaceholderText("Address Line 1")
        self.address2_input = QLineEdit()
        self.address2_input.setPlaceholderText("Address Line 2 (optional)")
        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("City")
        self.state_input = QLineEdit()
        self.state_input.setPlaceholderText("State")
        self.zip_input = QLineEdit()
        self.zip_input.setPlaceholderText("Zip Code")
        self.country_input = QLineEdit()
        self.country_input.setPlaceholderText("Country")
        self.bedrooms_input = QLineEdit()
        self.bedrooms_input.setPlaceholderText("Number of Bedrooms")
        self.bathrooms_input = QLineEdit()
        self.bathrooms_input.setPlaceholderText("Number of Bathrooms")
        self.square_feet_input = QLineEdit()
        self.square_feet_input.setPlaceholderText("Square Footage")
        self.lot_size_input = QLineEdit()
        self.lot_size_input.setPlaceholderText("Lot Size")
        self.year_built_input = QLineEdit()
        self.year_built_input.setPlaceholderText("Year Built")
        self.description_input = QLineEdit()
        self.description_input.setPlaceholderText("Description")
        self.negotiable_price_input = QLineEdit()
        self.negotiable_price_input.setPlaceholderText("Negotiable Price")

        # Add Property Button
        add_btn = QPushButton("Add Property")
        add_btn.clicked.connect(self.add_property)

        # Properties Table
        self.properties_table = QTableWidget()
        self.properties_table.setColumnCount(14)
        self.properties_table.setHorizontalHeaderLabels([
            "Address 1", "Address 2", "City", "State", "Zip", "Country",
            "Bedrooms", "Bathrooms", "Square Feet", "Lot Size", "Year Built",
            "Description", "Negotiable Price"
        ])
        self.load_properties()

        # Layout arrangement
        layout.addWidget(QLabel("Add New Property"))
        layout.addWidget(self.address1_input)
        layout.addWidget(self.address2_input)
        layout.addWidget(self.city_input)
        layout.addWidget(self.state_input)
        layout.addWidget(self.zip_input)
        layout.addWidget(self.country_input)
        layout.addWidget(self.bedrooms_input)
        layout.addWidget(self.bathrooms_input)
        layout.addWidget(self.square_feet_input)
        layout.addWidget(self.lot_size_input)
        layout.addWidget(self.year_built_input)
        layout.addWidget(self.description_input)
        layout.addWidget(self.negotiable_price_input)
        layout.addWidget(add_btn)
        layout.addWidget(QLabel("Existing Properties"))
        layout.addWidget(self.properties_table)

        self.setLayout(layout)

    def add_property(self):
        address1 = self.address1_input.text()
        address2 = self.address2_input.text()
        city = self.city_input.text()
        state = self.state_input.text()
        zip_code = self.zip_input.text()
        country = self.country_input.text()
        bedrooms = self.bedrooms_input.text()
        bathrooms = self.bathrooms_input.text()
        square_feet = self.square_feet_input.text()
        lot_size = self.lot_size_input.text()
        year_built = self.year_built_input.text()
        description = self.description_input.text()
        negotiable_price = self.negotiable_price_input.text()

        if not address1 or not city or not state or not zip_code or not country:
            QMessageBox.warning(self, "Input Error", "Address Line 1, City, State, Zip Code, and Country are required.")
            return

        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO Properties (
                    AddressLine1, AddressLine2, City, State, ZipCode, Country, 
                    NumberOfBedrooms, NumberOfBathrooms, SquareFootage, 
                    LotSize, YearBuilt, Description, NegotiablePrice
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (
                address1, address2, city, state, zip_code, country,
                bedrooms if bedrooms else None,
                bathrooms if bathrooms else None,
                square_feet if square_feet else None,
                lot_size if lot_size else None,
                year_built if year_built else None,
                description, negotiable_price if negotiable_price else None
            ))
            self.connection.commit()
            QMessageBox.information(self, "Success", "Property added successfully.")
            self.load_properties()
            self.clear_inputs()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error: {err}")

    def load_properties(self):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT 
                    AddressLine1, AddressLine2, City, State, ZipCode, 
                    Country, NumberOfBedrooms, NumberOfBathrooms, 
                    SquareFootage, LotSize, YearBuilt, Description, NegotiablePrice
                FROM Properties
            """
            cursor.execute(query)
            records = cursor.fetchall()
            self.properties_table.setRowCount(0)
            for row_number, row_data in enumerate(records):
                self.properties_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.properties_table.setItem(row_number, column_number, QTableWidgetItem(str(data) if data else ""))
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error: {err}")

    def clear_inputs(self):
        self.address1_input.clear()
        self.address2_input.clear()
        self.city_input.clear()
        self.state_input.clear()
        self.zip_input.clear()
        self.country_input.clear()
        self.bedrooms_input.clear()
        self.bathrooms_input.clear()
        self.square_feet_input.clear()
        self.lot_size_input.clear()
        self.year_built_input.clear()
        self.description_input.clear()
        self.negotiable_price_input.clear()

# Listings Management Window
class ListingsWindow(QWidget):
    def __init__(self, connection):
        super().__init__()
        self.setWindowTitle("Manage Listings")
        self.setGeometry(150, 150, 700, 500)
        self.connection = connection
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Form fields
        self.property_id_input = QLineEdit()
        self.property_id_input.setPlaceholderText("Property ID")
        self.agent_id_input = QLineEdit()
        self.agent_id_input.setPlaceholderText("Agent ID")
        self.listing_price_input = QLineEdit()
        self.listing_price_input.setPlaceholderText("Listing Price")
        self.listing_status_input = QComboBox()
        self.listing_status_input.addItems(['Active', 'Inactive', 'Pending'])

        # Add Listing Button
        add_btn = QPushButton("Add Listing")
        add_btn.clicked.connect(self.add_listing)

        # Listings Table
        self.listings_table = QTableWidget()
        self.listings_table.setColumnCount(6)
        self.listings_table.setHorizontalHeaderLabels([
            "ID", "Property ID", "Agent ID", "Price", "Status", "Listing Date"
        ])
        self.load_listings()

        # Layout arrangement
        layout.addWidget(QLabel("Add New Listing"))
        layout.addWidget(self.property_id_input)
        layout.addWidget(self.agent_id_input)
        layout.addWidget(self.listing_price_input)
        layout.addWidget(self.listing_status_input)
        layout.addWidget(add_btn)
        layout.addWidget(QLabel("Existing Listings"))
        layout.addWidget(self.listings_table)

        self.setLayout(layout)

    def add_listing(self):
        property_id = self.property_id_input.text()
        agent_id = self.agent_id_input.text()
        listing_price = self.listing_price_input.text()
        listing_status = self.listing_status_input.currentText()

        if not property_id or not agent_id or not listing_price:
            QMessageBox.warning(self, "Input Error", "Property ID, Agent ID, and Listing Price are required.")
            return

        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO Listings (PropertyID, AgentID, Price, Status)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (property_id, agent_id, listing_price, listing_status))
            self.connection.commit()
            QMessageBox.information(self, "Success", "Listing added successfully.")
            self.load_listings()
            self.clear_inputs()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error: {err}")

    def load_listings(self):
        try:
            cursor = self.connection.cursor()
            query = "SELECT ID, PropertyID, AgentID, Price, Status, ListingDate FROM Listings"
            cursor.execute(query)
            records = cursor.fetchall()
            self.listings_table.setRowCount(0)
            for row_number, row_data in enumerate(records):
                self.listings_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.listings_table.setItem(row_number, column_number, QTableWidgetItem(str(data) if data else ""))
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error: {err}")

    def clear_inputs(self):
        self.property_id_input.clear()
        self.agent_id_input.clear()
        self.listing_price_input.clear()

# Transactions Management Window
class TransactionsWindow(QWidget):
    def __init__(self, connection):
        super().__init__()
        self.setWindowTitle("Manage Transactions")
        self.setGeometry(150, 150, 700, 500)
        self.connection = connection
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Form fields
        self.transaction_id_input = QLineEdit()
        self.transaction_id_input.setPlaceholderText("Transaction ID")
        self.property_id_input = QLineEdit()
        self.property_id_input.setPlaceholderText("Property ID")
        self.agent_id_input = QLineEdit()
        self.agent_id_input.setPlaceholderText("Agent ID")
        self.sale_price_input = QLineEdit()
        self.sale_price_input.setPlaceholderText("Sale Price")

        # Add Transaction Button
        add_btn = QPushButton("Add Transaction")
        add_btn.clicked.connect(self.add_transaction)

        # Transactions Table
        self.transactions_table = QTableWidget()
        self.transactions_table.setColumnCount(5)
        self.transactions_table.setHorizontalHeaderLabels([
            "ID", "Property ID", "Agent ID", "Sale Price", "Transaction Date"
        ])
        self.load_transactions()

        # Layout arrangement
        layout.addWidget(QLabel("Add New Transaction"))
        layout.addWidget(self.transaction_id_input)
        layout.addWidget(self.property_id_input)
        layout.addWidget(self.agent_id_input)
        layout.addWidget(self.sale_price_input)
        layout.addWidget(add_btn)
        layout.addWidget(QLabel("Existing Transactions"))
        layout.addWidget(self.transactions_table)

        self.setLayout(layout)

    def add_transaction(self):
        transaction_id = self.transaction_id_input.text()
        property_id = self.property_id_input.text()
        agent_id = self.agent_id_input.text()
        sale_price = self.sale_price_input.text()

        if not property_id or not agent_id or not sale_price:
            QMessageBox.warning(self, "Input Error", "Property ID, Agent ID, and Sale Price are required.")
            return

        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO Transactions (PropertyID, AgentID, SalePrice)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (property_id, agent_id, sale_price))
            self.connection.commit()
            QMessageBox.information(self, "Success", "Transaction added successfully.")
            self.load_transactions()
            self.clear_inputs()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error: {err}")

    def load_transactions(self):
        try:
            cursor = self.connection.cursor()
            query = "SELECT ID, PropertyID, AgentID, SalePrice, TransactionDate FROM Transactions"
            cursor.execute(query)
            records = cursor.fetchall()
            self.transactions_table.setRowCount(0)
            for row_number, row_data in enumerate(records):
                self.transactions_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.transactions_table.setItem(row_number, column_number, QTableWidgetItem(str(data) if data else ""))
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error: {err}")

    def clear_inputs(self):
        self.transaction_id_input.clear()
        self.property_id_input.clear()
        self.agent_id_input.clear()
        self.sale_price_input.clear()

# Bidding Management Window
class BiddingWindow(QWidget):
    def __init__(self, connection):
        super().__init__()
        self.setWindowTitle("Manage Bidding")
        self.setGeometry(150, 150, 700, 500)
        self.connection = connection
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Form fields
        self.property_id_input = QLineEdit()
        self.property_id_input.setPlaceholderText("Property ID")
        self.bidder_id_input = QLineEdit()
        self.bidder_id_input.setPlaceholderText("Bidder ID")
        self.bid_amount_input = QLineEdit()
        self.bid_amount_input.setPlaceholderText("Bid Amount")

        # Add Bid Button
        add_btn = QPushButton("Add Bid")
        add_btn.clicked.connect(self.add_bid)

        # Bids Table
        self.bids_table = QTableWidget()
        self.bids_table.setColumnCount(4)
        self.bids_table.setHorizontalHeaderLabels([
            "ID", "Property ID", "Bidder ID", "Bid Amount", "Bid Date"
        ])
        self.load_bids()

        # Layout arrangement
        layout.addWidget(QLabel("Add New Bid"))
        layout.addWidget(self.property_id_input)
        layout.addWidget(self.bidder_id_input)
        layout.addWidget(self.bid_amount_input)
        layout.addWidget(add_btn)
        layout.addWidget(QLabel("Existing Bids"))
        layout.addWidget(self.bids_table)

        self.setLayout(layout)

    def add_bid(self):
        property_id = self.property_id_input.text()
        bidder_id = self.bidder_id_input.text()
        bid_amount = self.bid_amount_input.text()

        if not property_id or not bidder_id or not bid_amount:
            QMessageBox.warning(self, "Input Error", "Property ID, Bidder ID, and Bid Amount are required.")
            return

        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO Bids (PropertyID, BidderID, BidAmount)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (property_id, bidder_id, bid_amount))
            self.connection.commit()
            QMessageBox.information(self, "Success", "Bid added successfully.")
            self.load_bids()
            self.clear_inputs()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error: {err}")

    def load_bids(self):
        try:
            cursor = self.connection.cursor()
            query = "SELECT ID, PropertyID, BidderID, BidAmount, BidDate FROM Bids"
            cursor.execute(query)
            records = cursor.fetchall()
            self.bids_table.setRowCount(0)
            for row_number, row_data in enumerate(records):
                self.bids_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.bids_table.setItem(row_number, column_number, QTableWidgetItem(str(data) if data else ""))
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error: {err}")

    def clear_inputs(self):
        self.property_id_input.clear()
        self.bidder_id_input.clear()
        self.bid_amount_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
