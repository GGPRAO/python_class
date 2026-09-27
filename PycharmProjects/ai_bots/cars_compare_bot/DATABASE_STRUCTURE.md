# Cars Database - Complete Data Structure

## Overview
The Cars Compare Bot now includes comprehensive data for 11 popular Indian vehicles with complete specifications, features, and safety information.

---

## Sample Car Data: Hyundai Creta

```json
{
  "Hyundai Creta": {
    "brand": "Hyundai",
    "type": "Compact SUV",
    "price": "₹9,50,000 - ₹14,50,000",
    "engine": "1.5L Petrol/Diesel",
    "horsepower": "113-113 hp",
    "torque": "144-250 Nm",
    "0-100": "10.5s",
    "top_speed": "190 km/h",
    "fuel_efficiency": "16.5-18.5 km/l",
    "range": "900 km",
    "transmission": "Manual/Automatic",
    "seats": "5",
    "cargo": "480L",
    "features": "Touchscreen (7-10.25 inch), Bluetooth, USB, Rear Camera, Sunroof (top variant)",
    "safety": "ABS, 6 Airbags, ESC, Hill Assist, Rear Parking Sensors",
    "pros": "Great styling, good ground clearance, features-rich, powerful diesel engine",
    "cons": "Higher price, average fuel economy on petrol, maintenance costs"
  }
}
```

---

## Complete Database Structure

Each car in the database contains:

| Field | Description | Example |
|-------|-------------|---------|
| `brand` | Car manufacturer | "Maruti Suzuki" |
| `type` | Vehicle category | "Compact SUV" |
| `price` | Price range in INR | "₹9,50,000 - ₹14,50,000" |
| `engine` | Engine specifications | "1.5L Petrol/Diesel" |
| `horsepower` | Power output | "113-113 hp" |
| `torque` | Rotational force | "144-250 Nm" |
| `0-100` | Acceleration time | "10.5s" |
| `top_speed` | Maximum speed | "190 km/h" |
| `fuel_efficiency` | Mileage | "16.5-18.5 km/l" |
| `range` | Distance on full tank | "900 km" |
| `transmission` | Gear type | "Manual/Automatic" |
| `seats` | Number of seats | "5" |
| `cargo` | Boot space | "480L" |
| `features` | Tech & comfort features | "Touchscreen, Bluetooth, USB..." |
| `safety` | Safety systems | "ABS, 6 Airbags, ESC..." |
| `pros` | Advantages | "Great styling, good ground clearance..." |
| `cons` | Disadvantages | "Higher price, average fuel economy..." |

---

## All Cars in Database

### 1. Maruti Swift
- **Type**: Compact Hatchback
- **Price**: ₹5,50,000 - ₹6,50,000
- **Engine**: 1.2L Petrol
- **Seats**: 5
- **Best For**: Budget, city driving, fuel efficiency

### 2. Hyundai Venue
- **Type**: Sub-Compact SUV
- **Price**: ₹6,50,000 - ₹9,50,000
- **Engine**: 1.2L Petrol/1.0L Diesel
- **Seats**: 5
- **Best For**: First-time SUV buyers, affordability

### 3. Tata Nexon
- **Type**: Compact SUV
- **Price**: ₹7,50,000 - ₹11,50,000
- **Engine**: 1.2L Petrol/1.5L Diesel
- **Seats**: 5
- **Best For**: Safety-conscious buyers

### 4. Maruti Brezza
- **Type**: Compact SUV
- **Price**: ₹8,00,000 - ₹11,50,000
- **Engine**: 1.5L Petrol/Diesel
- **Seats**: 5
- **Best For**: Fuel efficiency, affordable SUV

### 5. Renault Duster
- **Type**: Compact SUV
- **Price**: ₹8,50,000 - ₹12,50,000
- **Engine**: 1.5L Petrol/Diesel
- **Seats**: 5
- **Best For**: Adventure, budget SUV

### 6. Hyundai Creta
- **Type**: Compact SUV
- **Price**: ₹9,50,000 - ₹14,50,000
- **Engine**: 1.5L Petrol/Diesel
- **Seats**: 5
- **Best For**: Features, styling, performance

### 7. Kia Seltos
- **Type**: Compact SUV
- **Price**: ₹9,50,000 - ₹15,50,000
- **Engine**: 1.5L Petrol/Diesel
- **Seats**: 5
- **Best For**: Latest tech, warranty, value

### 8. Skoda Kushaq
- **Type**: Compact SUV
- **Price**: ₹10,50,000 - ₹17,50,000
- **Engine**: 1.0L TSI/1.5L TSI Petrol
- **Seats**: 5
- **Best For**: Performance, driving dynamics

### 9. Honda City
- **Type**: Compact Sedan
- **Price**: ₹11,50,000 - ₹14,50,000
- **Engine**: 1.5L Petrol
- **Seats**: 5
- **Best For**: Reliability, comfort, luxury feel

### 10. Mahindra XUV700
- **Type**: Premium 7-Seater SUV
- **Price**: ₹14,50,000 - ₹20,50,000
- **Engine**: 2.0L Turbo Petrol/2.0L Diesel
- **Seats**: 7
- **Best For**: Premium features, family SUV

### 11. Tesla Model 3
- **Type**: Electric Sedan
- **Price**: ₹42,90,000 - ₹52,90,000
- **Engine**: Electric Motor
- **Seats**: 5
- **Best For**: EV enthusiasts, luxury, eco-friendly

---

## Sample Comparison Output

When comparing "Hyundai Creta vs Tata Nexon", the bot provides:

### 💰 Price Comparison
- **Hyundai Creta**: ₹9,50,000 - ₹14,50,000
- **Tata Nexon**: ₹7,50,000 - ₹11,50,000
- **Verdict**: Nexon is more affordable, Creta offers more premium features

### 🔧 Specifications & Engine
- **Hyundai Creta**: 1.5L with 113 hp (Petrol/Diesel)
- **Tata Nexon**: 1.2L/1.5L with 110 hp
- **Verdict**: Creta offers more power in diesel variant

### ⚡ Performance Metrics
- **Hyundai Creta**: 0-100 in 10.5s, Top Speed 190 km/h
- **Tata Nexon**: 0-100 in 10.4s, Top Speed 185 km/h
- **Verdict**: Both have similar acceleration

### 🛢️ Fuel Efficiency & Range
- **Hyundai Creta**: 16.5-18.5 km/l, 900 km range
- **Tata Nexon**: 16.8-20.5 km/l, 850 km range
- **Verdict**: Nexon diesel offers better efficiency (20.5 km/l)

### 🎨 Features & Technology
- **Hyundai Creta**: 
  - 7-10.25" Touchscreen, Bluetooth, USB
  - Sunroof (top variant)
  - Rear Camera
  
- **Tata Nexon**: 
  - Touchscreen, Bluetooth, Climate Control
  - Rear Camera
  - Basic infotainment in lower variants

- **Verdict**: Creta offers more features, especially in higher variants

### 🛡️ Safety Features
- **Hyundai Creta**: 6 Airbags, ABS, ESC, Hill Assist, Rear Parking Sensors
- **Tata Nexon**: 6 Airbags, ABS, Electronic Stability Program, Rear Parking Sensors
- **Verdict**: Both have excellent safety; Creta has Hill Assist

### ✅ Pros & Cons

**Hyundai Creta Pros**:
- Great styling and design
- Good ground clearance
- Feature-rich (especially in top variants)
- Powerful diesel engine

**Hyundai Creta Cons**:
- Higher price point
- Average fuel economy in petrol variant
- Higher maintenance costs

**Tata Nexon Pros**:
- More affordable
- Excellent safety features
- Spacious interior
- Great ground clearance

**Tata Nexon Cons**:
- Interior quality not premium
- Basic infotainment in lower variants

### 🎯 Recommendation
**Best for Budget**: Tata Nexon
**Best for Features**: Hyundai Creta
**Best Overall**: Depends on priorities (features vs. affordability)

---

## Data Access Points

The database is used in three main contexts:

### 1. **System Prompt Context**
```python
AVAILABLE CAR DATA:
{json data of all cars}
```

### 2. **Enhanced Query**
```python
Price Range: ₹7 lakhs - ₹20 lakhs
(Prices converted from slider values)
```

### 3. **Sample Comparison Table**
```python
DataFrame with selected cars showing:
- Model name
- Type
- Price (₹)
- Engine
- Horsepower
- 0-100 time
- Fuel efficiency
- Range
- Seats/Cargo
```

---

## New Features Added to Database

### Before
- Basic specs only (engine, price, power, torque, etc.)

### After (NEW)
- ✅ **Features**: Infotainment, connectivity, comfort features
- ✅ **Safety**: Airbags, stability systems, sensors
- ✅ **Pros & Cons**: Advantages and disadvantages
- ✅ **Indian Rupee Pricing**: All in ₹, not USD
- ✅ **More Cars**: 11 vehicles instead of 6
- ✅ **Price Ranges**: Min-max prices for each variant

---

## JSON Structure Example

```json
{
  "car_name": {
    "brand": "Manufacturer",
    "type": "Vehicle Category",
    "price": "₹X,XX,000 - ₹Y,YY,000",
    "engine": "Engine Displacement & Type",
    "horsepower": "HP",
    "torque": "Nm",
    "0-100": "seconds",
    "top_speed": "km/h",
    "fuel_efficiency": "km/l or km/kWh",
    "range": "km",
    "transmission": "Type of gears",
    "seats": "number",
    "cargo": "liters",
    "features": "Feature list",
    "safety": "Safety features",
    "pros": "Advantages",
    "cons": "Disadvantages"
  }
}
```

---

## Usage in AI Prompts

The database is included in the system prompt to help the AI:
1. Provide accurate specifications
2. Make fair comparisons
3. Recommend suitable vehicles
4. Calculate value-for-money
5. Consider market positioning
6. Give informed pros/cons

---

## Price Format

All prices use Indian Rupee format:
- ₹5,50,000 (5 lakhs 50 thousand)
- ₹14,50,000 (14 lakhs 50 thousand)
- ₹42,90,000 (42 lakhs 90 thousand)

Conversion in sidebar:
- Slider: 5-50 (in lakhs)
- Display: ₹{value} lakhs = ₹{value * 100000} rupees

---

**Database Last Updated**: April 26, 2026
**Total Cars**: 11
**Total Fields per Car**: 14
**Database Format**: JSON (integrated into Python dict)

