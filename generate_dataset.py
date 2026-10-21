"""
E-Commerce Transaction & Retention Dataset Generator
Generates 50,000+ realistic transaction records with customer cohorts,
engineered repeat purchase behavior, and realistic catalog data.
Timeline: Jan 2025 - Oct 2026.
"""

import os
import random
import datetime
import numpy as np
import pandas as pd

# Set random seeds for deterministic reproducibility
SEED = 42
random.seed(SEED)
np.random.seed(SEED)

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---------------------------------------------------------
# 1. GENERATE PRODUCT CATALOG
# ---------------------------------------------------------
CATEGORIES = {
    "Electronics": [
        ("Noise-Canceling Wireless Headphones", 149.99, 65.00),
        ("Ultra-Slim Power Bank 20000mAh", 39.99, 14.50),
        ("Mechanical Gaming Keyboard RGB", 89.99, 36.00),
        ("Ergonomic Bluetooth Mouse", 49.99, 18.00),
        ("Smart Fitness Watch v4", 129.99, 52.00),
        ("4K Ultra-HD Webcam with Mic", 79.99, 31.00),
        ("USB-C Dual Display Docking Station", 99.99, 41.00),
        ("Smart Home Wi-Fi Security Cam", 59.99, 22.00),
        ("Portable Bluetooth Speaker IPX7", 69.99, 27.00),
        ("Fast Wireless Charging Pad 15W", 24.99, 8.50),
    ],
    "Apparel & Fashion": [
        ("Organic Cotton Classic Crewneck Tee", 29.99, 9.50),
        ("Performance Stretch Chino Trousers", 64.99, 21.00),
        ("Merino Wool Blend Knit Sweater", 89.99, 32.00),
        ("Water-Resistant Commuter Jacket", 119.99, 44.00),
        ("Seamless High-Rise Yoga Leggings", 49.99, 16.00),
        ("Relaxed Fit French Terry Hoodie", 59.99, 20.00),
        ("Everyday Canvas Low-Top Sneakers", 74.99, 26.00),
        ("All-Weather Polarized Sunglasses", 44.99, 12.00),
        ("Leather Minimalist Bifold Wallet", 39.99, 13.50),
        ("Durable Canvas Everyday Tote Bag", 34.99, 11.00),
    ],
    "Home & Living": [
        ("Aroma Ceramic Essential Oil Diffuser", 38.99, 14.00),
        ("French Linen Queen Duvet Cover Set", 129.99, 48.00),
        ("Insulated Stainless Steel Pour-Over Kettle", 54.99, 20.00),
        ("Bamboo Desktop Organizer Caddy", 28.99, 9.50),
        ("Ergonomic Memory Foam Lumbar Cushion", 42.99, 15.00),
        ("Double-Walled Glass Coffee Mugs (Set of 4)", 36.99, 12.50),
        ("Hand-Poured Soy Wax Scented Candle", 24.99, 7.50),
        ("Minimalist LED Desk Task Lamp", 49.99, 17.50),
        ("Cast Iron Pre-Seasoned Skillet 10-inch", 44.99, 16.50),
        ("Microfiber Ultra-Absorbent Bath Towels (Pair)", 34.99, 11.00),
    ],
    "Beauty & Wellness": [
        ("Hydrating Hyaluronic Acid Facial Serum", 32.99, 9.00),
        ("Botanical Nourishing Face Cleanser", 24.99, 6.50),
        ("SPF 50 Daily Mineral Sunscreen Fluid", 28.99, 8.00),
        ("Detoxifying Pink Clay Purifying Mask", 26.99, 7.00),
        ("Organic Cold-Pressed Argan Hair Oil", 29.99, 8.50),
        ("Vitamin C Radiance Glow Daily Cream", 36.99, 10.50),
        ("Ultrasonic Silicone Facial Scrub Brush", 45.99, 15.00),
        ("Natural Shea Butter Body Moisturizer", 22.99, 6.00),
        ("Lavender Sleep & Calming Pillow Mist", 18.99, 4.50),
        ("Vegan Biotin & Keratin Hair Supplements", 34.99, 11.00),
    ],
    "Sports & Outdoors": [
        ("Extra-Thick Non-Slip Eco Yoga Mat", 44.99, 15.50),
        ("Adjustable Dumbbell Hand Weights 20lb", 79.99, 32.00),
        ("Vacuum Insulated Steel Water Bottle 32oz", 29.99, 9.00),
        ("Multi-Resistance Band Workout Set", 24.99, 7.00),
        ("Lightweight Trail Running Hydration Pack", 64.99, 22.00),
        ("Compact Trekking Aluminum Poles (Pair)", 49.99, 17.00),
        ("Ultra-Lightweight Microfiber Travel Towel", 19.99, 5.50),
        ("Foam Roller Deep Muscle Massager", 27.99, 8.50),
        ("Emergency Solar Outdoor Power Lantern", 39.99, 13.50),
        ("Speed Cable Skipping Rope with Counter", 16.99, 4.50),
    ],
    "Books & Productivity": [
        ("Daily Habit & Goal Tracker Planner (Dated)", 24.99, 6.50),
        ("Hardcover Dot-Grid Bullet Journal 160gsm", 19.99, 5.00),
        ("Luxury Rollerball Executive Pen Set", 34.99, 10.00),
        ("Deep Work & Focus Timer Pomodoro Clock", 29.99, 9.00),
        ("Noise-Dampening Felt Desk Blotter Pad", 32.99, 10.50),
        ("Aluminum Ergonomic Laptop Elevator Stand", 44.99, 15.00),
        ("Sticky Notes & Page Flags Indexing Kit", 12.99, 3.00),
        ("Blue-Light Filtering Reading Glasses", 27.99, 7.50),
        ("Digital Stylus Pen with Palm Rejection", 39.99, 12.00),
        ("Magnetic Cable Management Cord Organizer", 15.99, 4.00),
    ]
}

products_list = []
prod_id = 101
for cat, items in CATEGORIES.items():
    for name, price, cost in items:
        sku = f"SKU-{cat[:3].upper()}-{prod_id}"
        products_list.append({
            "product_id": prod_id,
            "sku": sku,
            "product_name": name,
            "category": cat,
            "unit_price": round(price, 2),
            "unit_cost": round(cost, 2),
            "margin_pct": round((price - cost) / price * 100, 2)
        })
        prod_id += 1

df_products = pd.DataFrame(products_list)
print(f"Generated {len(df_products)} products.")

# ---------------------------------------------------------
# 2. GENERATE CUSTOMERS
# ---------------------------------------------------------
NUM_CUSTOMERS = 15000
CHANNELS = ["Paid Social", "Organic Search", "Google Ads", "Email Referral", "Influencer Partner"]
CHANNEL_WEIGHTS = [0.32, 0.28, 0.22, 0.10, 0.08]

CITIES = [
    ("New York", "NY"), ("Los Angeles", "CA"), ("Chicago", "IL"),
    ("Houston", "TX"), ("Phoenix", "AZ"), ("Philadelphia", "PA"),
    ("San Antonio", "TX"), ("San Diego", "CA"), ("Dallas", "TX"),
    ("Austin", "TX"), ("Seattle", "WA"), ("Denver", "CO"),
    ("Boston", "MA"), ("Atlanta", "GA"), ("San Francisco", "CA"),
    ("Miami", "FL"), ("Portland", "OR"), ("Minneapolis", "MN"),
    ("Nashville", "TN"), ("Raleigh", "NC")
]

FIRST_NAMES = [
    "James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda",
    "William", "Elizabeth", "David", "Barbara", "Richard", "Susan", "Joseph", "Jessica",
    "Thomas", "Sarah", "Charles", "Karen", "Christopher", "Nancy", "Daniel", "Lisa",
    "Matthew", "Betty", "Anthony", "Margaret", "Mark", "Sandra", "Donald", "Ashley",
    "Steven", "Kimberly", "Paul", "Emily", "Andrew", "Donna", "Joshua", "Michelle",
    "Kenneth", "Dorothy", "Kevin", "Carol", "Brian", "Amanda", "George", "Melissa",
    "Edward", "Deborah", "Ronald", "Stephanie", "Timothy", "Rebecca", "Jason", "Sharon",
    "Jeffrey", "Laura", "Ryan", "Cynthia", "Jacob", "Kathleen", "Gary", "Amy",
    "Nicholas", "Shirley", "Eric", "Angela", "Jonathan", "Helen", "Stephen", "Anna",
    "Larry", "Brenda", "Justin", "Pamela", "Scott", "Nicole", "Brandon", "Emma",
    "Benjamin", "Samantha", "Samuel", "Katherine", "Gregory", "Christine", "Frank", "Debra",
    "Alexander", "Rachel", "Raymond", "Catherine", "Patrick", "Carolyn", "Jack", "Janet",
    "Dennis", "Ruth", "Jerry", "Maria", "Tyler", "Heather", "Aaron", "Diane"
]

LAST_NAMES = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
    "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson",
    "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker",
    "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill",
    "Flores", "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell",
    "Mitchell", "Carter", "Roberts", "Gomez", "Phillips", "Evans", "Turner", "Diaz",
    "Parker", "Cruz", "Edwards", "Collins", "Reyes", "Stewart", "Morris", "Morales",
    "Murphy", "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper", "Peterson",
    "Bailey", "Reed", "Kelly", "Howard", "Ramos", "Kim", "Cox", "Ward", "Richardson"
]

# Timeline: 22 months from 2025-01-01 to 2026-10-20
START_DATE = datetime.date(2025, 1, 1)
END_DATE = datetime.date(2026, 10, 20)
TOTAL_DAYS = (END_DATE - START_DATE).days

# Distribute customer acquisition over time with healthy growth
customer_records = []
customer_first_dates = {}

for cust_id in range(1001, 1001 + NUM_CUSTOMERS):
    fn = random.choice(FIRST_NAMES)
    ln = random.choice(LAST_NAMES)
    name = f"{fn} {ln}"
    email = f"{fn.lower()}.{ln.lower()}{cust_id}@example.com"
    city, state = random.choice(CITIES)
    channel = np.random.choice(CHANNELS, p=CHANNEL_WEIGHTS)
    
    # Skew acquisition dates slightly towards earlier/middle months so we observe full cohorts
    # Beta distribution favoring uniform spread across the 22 months
    day_offset = int(np.random.beta(1.3, 1.2) * TOTAL_DAYS)
    first_date = START_DATE + datetime.timedelta(days=day_offset)
    
    customer_records.append({
        "customer_id": cust_id,
        "customer_name": name,
        "email": email,
        "city": city,
        "state": state,
        "country": "USA",
        "acquisition_channel": channel,
        "registration_date": first_date.isoformat()
    })
    customer_first_dates[cust_id] = first_date

df_customers = pd.DataFrame(customer_records)
print(f"Generated {len(df_customers)} customers.")

# ---------------------------------------------------------
# 3. GENERATE ORDERS & TRANSACTIONS (50,000+)
# ---------------------------------------------------------
# Retention engineering:
# Month 0: 100% (First purchase)
# Month 1: 44.5% chance of purchase in month 1
# Month 2: 29.5% chance of purchase in month 2 -> DROP-OFF of ~15.0%!
# Month 3: 24.0% chance of purchase
# Month 4: 22.0%
# Month 5: 21.0%
# Month 6+: 19.5%

orders_records = []
order_items_records = []

order_counter = 100001
item_counter = 1

PAYMENT_METHODS = ["Credit Card", "PayPal", "Apple Pay", "UPI / Bank Transfer"]
PAYMENT_WEIGHTS = [0.55, 0.25, 0.15, 0.05]

STATUSES = ["Completed", "Completed", "Completed", "Completed", "Completed", "Completed", "Returned", "Cancelled"]
STATUS_WEIGHTS = [0.91, 0.06, 0.03] # Completed, Returned, Cancelled

for cust in customer_records:
    cid = cust["customer_id"]
    first_d = customer_first_dates[cid]
    cohort_year = first_d.year
    cohort_month = first_d.month
    
    # 1. Order in Month 0 (Acquisition Order)
    # Day within registration month (or next 1-3 days)
    first_order_date = first_d
    if first_order_date > END_DATE:
        continue
    
    active_dates = [first_order_date]
    
    # 2. Subsequent months repeat simulation up to Month 15
    for m in range(1, 16):
        # Target retention rates designed to produce exact ~15% drop-off in month 2:
        # Month 1: ~44.5%
        # Month 2: ~29.5% (Drop-off = 15.0%)
        # Month 3: ~24.0%
        # Month 4: ~22.0%
        # Month 5: ~21.0%
        # Month 6+: ~19.5%
        if m == 1:
            prob = 0.445
        elif m == 2:
            prob = 0.295 # 44.5% -> 29.5% = 15.0% DROP-OFF in second month
        elif m == 3:
            prob = 0.240
        elif m == 4:
            prob = 0.220
        elif m == 5:
            prob = 0.210
        elif m == 6:
            prob = 0.205
        elif m <= 9:
            prob = 0.198
        else:
            prob = 0.190
            
        # Channel modifiers: Referral and Organic have slightly higher stickiness, Paid Ads slightly lower
        ch = cust["acquisition_channel"]
        if ch == "Email Referral":
            prob *= 1.10
        elif ch == "Organic Search":
            prob *= 1.04
        elif ch == "Paid Social":
            prob *= 0.95
            
        if random.random() < prob:
            # Calculate calendar month (first_d year, month + m)
            target_year = cohort_year + (cohort_month - 1 + m) // 12
            target_month = (cohort_month - 1 + m) % 12 + 1
            # Random day within that target month
            max_day = 28
            target_day = random.randint(1, max_day)
            next_order_d = datetime.date(target_year, target_month, target_day)
            
            if next_order_d <= END_DATE:
                active_dates.append(next_order_d)
                
                # Small chance of multiple orders in the same month (super active customer)
                if random.random() < 0.16:
                    extra_day = random.randint(1, max_day)
                    extra_d = datetime.date(target_year, target_month, extra_day)
                    if extra_d <= END_DATE:
                        active_dates.append(extra_d)

    # Now create order and order_item entries for each active date
    for o_date in sorted(active_dates):
        oid = order_counter
        order_counter += 1
        
        status = np.random.choice(["Completed", "Returned", "Cancelled"], p=STATUS_WEIGHTS)
        pay_method = np.random.choice(PAYMENT_METHODS, p=PAYMENT_WEIGHTS)
        
        # Decide number of items: 1-4 items
        num_items = np.random.choice([1, 2, 3, 4], p=[0.50, 0.30, 0.14, 0.06])
        selected_prods = random.sample(products_list, num_items)
        
        subtotal = 0.0
        total_cost = 0.0
        
        for p in selected_prods:
            qty = np.random.choice([1, 2, 3], p=[0.82, 0.14, 0.04])
            item_price = p["unit_price"]
            item_cost = p["unit_cost"]
            
            # Potential promotional discount on item
            disc_pct = np.random.choice([0.0, 0.05, 0.10, 0.15, 0.20], p=[0.60, 0.15, 0.12, 0.08, 0.05])
            line_total = round(item_price * qty * (1 - disc_pct), 2)
            
            subtotal += line_total
            total_cost += round(item_cost * qty, 2)
            
            order_items_records.append({
                "order_item_id": item_counter,
                "order_id": oid,
                "product_id": p["product_id"],
                "quantity": int(qty),
                "unit_price": item_price,
                "discount_pct": disc_pct,
                "total_price": line_total
            })
            item_counter += 1
            
        shipping_fee = 0.0 if subtotal > 75.0 else 5.99
        tax_amount = round(subtotal * 0.075, 2)
        order_total = round(subtotal + shipping_fee + tax_amount, 2)
        
        orders_records.append({
            "order_id": oid,
            "customer_id": cid,
            "order_date": o_date.isoformat(),
            "status": status,
            "payment_method": pay_method,
            "shipping_cost": shipping_fee,
            "tax_amount": tax_amount,
            "subtotal": round(subtotal, 2),
            "order_total": order_total
        })

df_orders = pd.DataFrame(orders_records)
df_order_items = pd.DataFrame(order_items_records)

print(f"Total Transactions Generated: {len(df_orders):,}")
print(f"Total Line Items Generated: {len(df_order_items):,}")

# Export raw CSV files
df_products.to_csv(os.path.join(OUTPUT_DIR, "products.csv"), index=False)
df_customers.to_csv(os.path.join(OUTPUT_DIR, "customers.csv"), index=False)
df_orders.to_csv(os.path.join(OUTPUT_DIR, "orders.csv"), index=False)
df_order_items.to_csv(os.path.join(OUTPUT_DIR, "order_items.csv"), index=False)

print(f"CSVs successfully written to {OUTPUT_DIR}")
