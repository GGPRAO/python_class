from flask import Flask, render_template, request, redirect, url_for, flash, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import io
import csv
from datetime import datetime
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'maintenance.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DB_PATH
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dev-secret'

db = SQLAlchemy(app)

class House(db.Model):
    # Use house_number as the primary key (list publishing - no auto-increment id)
    house_number = db.Column(db.String(20), primary_key=True)
    payment_status = db.Column(db.String(20), nullable=False)  # paid, not_paid
    availability = db.Column(db.String(20), nullable=False)    # available, rented, occupied
    maintenance_paid_months = db.Column(db.Text, nullable=False, default='')  # comma-separated months (e.g., "2024-01,2024-02,2024-03")

    def __repr__(self):
        return f"<House {self.house_number} pay:{self.payment_status} avail:{self.availability}>"

    def get_maintenance_months(self):
        """Return list of months where maintenance is paid"""
        if not self.maintenance_paid_months:
            return []
        return [m.strip() for m in self.maintenance_paid_months.split(',') if m.strip()]

    def add_maintenance_month(self, month):
        """Add a maintenance month (format: YYYY-MM)"""
        months = self.get_maintenance_months()
        if month not in months:
            months.append(month)
            months.sort()
            self.maintenance_paid_months = ','.join(months)

    def remove_maintenance_month(self, month):
        """Remove a maintenance month"""
        months = self.get_maintenance_months()
        if month in months:
            months.remove(month)
            self.maintenance_paid_months = ','.join(months)

    def is_maintenance_paid_for_month(self, month):
        """Check if maintenance is paid for a specific month"""
        return month in self.get_maintenance_months()

@app.route('/')
def index():
    total = House.query.count()
    paid = House.query.filter_by(payment_status='paid').count()
    not_paid = House.query.filter_by(payment_status='not_paid').count()
    available = House.query.filter_by(availability='available').count()
    rented = House.query.filter_by(availability='rented').count()
    occupied = House.query.filter_by(availability='occupied').count()

    # Count houses with maintenance paid for current month
    current_month = datetime.now().strftime('%Y-%m')
    houses = House.query.order_by(House.house_number).all()
    maintenance_paid_count = sum(1 for h in houses if current_month in h.get_maintenance_months())

    return render_template('index.html', total=total, paid=paid, not_paid=not_paid, available=available,
                         rented=rented, occupied=occupied, maintenance_paid_count=maintenance_paid_count,
                         current_month=current_month, houses=houses)

# Set payment status via dropdown form - SYNCED with maintenance
@app.route('/set_payment/<house_number>', methods=['POST'])
def set_payment(house_number):
    house = House.query.filter_by(house_number=house_number).first_or_404()
    status = request.form.get('payment_status')
    if status not in ['not_paid', 'paid']:
        flash('Invalid payment status')
        return redirect(url_for('index'))

    current_month = datetime.now().strftime('%Y-%m')
    house.payment_status = status

    # SYNC: If payment is marked as "paid", automatically add current month to maintenance
    if status == 'paid':
        house.add_maintenance_month(current_month)
        flash(f"House {house.house_number} marked as PAID (Payment & Maintenance synced for {current_month})")
    # SYNC: If payment is marked as "not_paid", automatically remove current month from maintenance
    else:
        house.remove_maintenance_month(current_month)
        flash(f"House {house.house_number} marked as NOT PAID (Maintenance removed for {current_month})")

    db.session.commit()
    return redirect(url_for('index'))

# Set availability via dropdown form (independent)
@app.route('/set_availability/<house_number>', methods=['POST'])
def set_availability(house_number):
    house = House.query.filter_by(house_number=house_number).first_or_404()
    status = request.form.get('availability')
    if status not in ['available', 'rented', 'occupied']:
        flash('Invalid availability')
        return redirect(url_for('index'))
    house.availability = status
    db.session.commit()
    flash(f"House {house.house_number} availability set to {house.availability}")
    return redirect(url_for('index'))

# Set maintenance month explicitly - also updates payment status
@app.route('/set_maintenance/<house_number>', methods=['POST'])
def set_maintenance(house_number):
    house = House.query.filter_by(house_number=house_number).first_or_404()
    month = request.form.get('maintenance_month')
    action = request.form.get('action')  # 'add' or 'remove'
    current_month = datetime.now().strftime('%Y-%m')

    # Validate month format (YYYY-MM)
    if not month or not (len(month) == 7 and month[4] == '-'):
        flash('Invalid month format. Use YYYY-MM')
        return redirect(url_for('index'))

    if action == 'add':
        house.add_maintenance_month(month)
        # SYNC: If adding current month maintenance, also mark payment as paid
        if month == current_month:
            house.payment_status = 'paid'
            flash(f"House {house.house_number} maintenance marked as paid for {month} (Payment synced to PAID)")
        else:
            flash(f"House {house.house_number} maintenance marked as paid for {month}")
    elif action == 'remove':
        house.remove_maintenance_month(month)
        # SYNC: If removing current month maintenance, also mark payment as not_paid
        if month == current_month:
            house.payment_status = 'not_paid'
            flash(f"House {house.house_number} maintenance removed for {month} (Payment synced to NOT PAID)")
        else:
            flash(f"House {house.house_number} maintenance removed for {month}")
    else:
        flash('Invalid action')
        return redirect(url_for('index'))

    db.session.commit()
    return redirect(url_for('index'))

# Export CSV of houses (includes all fields)
@app.route('/export')
def export_csv():
    si = io.StringIO()
    writer = csv.writer(si)
    writer.writerow(['house_number', 'payment_status', 'availability', 'maintenance_paid_months'])
    for h in House.query.order_by(House.house_number):
        writer.writerow([h.house_number, h.payment_status, h.availability, h.maintenance_paid_months])
    output = make_response(si.getvalue())
    output.headers['Content-Disposition'] = 'attachment; filename=houses.csv'
    output.headers['Content-Type'] = 'text/csv; charset=utf-8'
    return output

# Toggle availability for backward compatibility (cycles available->rented->occupied->available)
@app.route('/toggle/<house_number>', methods=['POST'])
def toggle(house_number):
    house = House.query.filter_by(house_number=house_number).first_or_404()
    order = ['available', 'rented', 'occupied']
    try:
        i = order.index(house.availability)
        house.availability = order[(i+1) % len(order)]
        db.session.commit()
        flash(f"House {house.house_number} availability changed to {house.availability}")
    except ValueError:
        flash('Unknown availability')
    return redirect(url_for('index'))

# Add house route updated to accept both fields
@app.route('/add', methods=['POST'])
def add_house():
    number = request.form.get('house_number')
    payment = request.form.get('payment_status') or 'not_paid'
    availability = request.form.get('availability') or 'available'
    if not number:
        flash('House number required')
        return redirect(url_for('index'))
    if House.query.filter_by(house_number=number).first():
        flash('House already exists')
        return redirect(url_for('index'))

    # SYNC: If adding a house with payment='paid', also add current month to maintenance
    current_month = datetime.now().strftime('%Y-%m')
    maintenance_months = ''
    if payment == 'paid':
        maintenance_months = current_month

    h = House(house_number=number, payment_status=payment, availability=availability, maintenance_paid_months=maintenance_months)
    db.session.add(h)
    db.session.commit()
    flash('House added')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
