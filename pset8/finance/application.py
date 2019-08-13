import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # Fetch data form db
    rows = db.execute("SELECT * FROM transactions WHERE userid = :userid ORDER BY symbol", 
        userid=session["user_id"])
    grand_total = 0
    
    # Travarse all rows for logged in user
    if rows:
        for row in rows:

            # Get the symbol from db
            symbol = row["symbol"]

            # Get information for symbol
            info = lookup(symbol)

            # If information is received
            if info:

                # Total value of each holding
                per_stock_total = row["shares"] * info["price"]

                # Calculate total spent money
                grand_total += per_stock_total

                # Insert required indices into row to display in template
                row["name"] = info["name"]
                row["price"] = usd(info["price"])
                row["total"] = usd(per_stock_total)


    # Check user's available balance
    cash_row = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
    current_cash = cash_row[0]["cash"]
    grand_total += current_cash

    # Render index template
    return render_template("index.html", rows=rows, current_cash=usd(current_cash), grand_total=usd(grand_total))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    
    # When user submits form
    if request.method == "POST":

        # Check for empty symbol
        if request.form.get("symbol") == "":
            return apology("missing symbol", 400)

        # Check for empty shares
        elif request.form.get("shares") == "":
            return apology("missing shares", 400)

        # Get data for given symbol
        info = lookup(request.form.get("symbol"))
        
        # Data available
        if info:

            # Calculate new cost
            new_cost = int(request.form.get("shares"))*float(info["price"])

            # Check user's available balance
            cash_row = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
            current_balance = cash_row[0]["cash"]

            # Check user's affordability
            if new_cost > current_balance:
                return apology("Not enough cash", 400)

            # Check if user has purchased same stock before
            symbol_row = db.execute("SELECT * FROM transactions WHERE userid = :userid AND symbol = :symbol",
            	userid=session["user_id"], symbol=info["symbol"])

            # Update shares if user has already purchased a stock before
            if symbol_row:

            	# Get the current number of shares
            	current_shares = int(symbol_row[0]["shares"])

            	# Calculate updated shares
            	updated_shares = current_shares + int(request.form.get("shares"))

            	# Update database
            	db.execute("UPDATE transactions SET shares = :shares WHERE userid = :userid AND symbol = :symbol",
            		shares=updated_shares, userid=session["user_id"], symbol=info["symbol"])

            	# Calculate new cash
            	updated_cash = current_balance - new_cost

            	# Update database
            	db.execute("UPDATE users SET cash = :cash WHERE id = :id", cash=updated_cash, id=session["user_id"])
            
            # Insert data into transactions table
            else:
	            
            	# Insert data into database
	            db.execute("INSERT INTO transactions (userid, symbol, shares) VALUES (:userid, :symbol, :shares)",
	              userid=session["user_id"], symbol=info["symbol"], shares=request.form.get("shares"))

	            # Calculate post purchase balance
	            updated_balance = current_balance - new_cost

	            # Update cash of users table
	            db.execute("UPDATE users SET cash = :cash WHERE id = :id", cash=updated_balance, id=session["user_id"])


            # Get transaction time
            current_time = (datetime.now()).replace(microsecond=0)

            # Update history
            db.execute("INSERT INTO history (userid, symbol, shares, price, date_time) VALUES (:userid, :symbol, :shares, :price, :date_time)",
                userid=session["user_id"], symbol=info["symbol"], shares=request.form.get("shares"), price=info["price"], date_time=current_time)


        
        # Notify user for invalid symbol
        else:
            return apology("invalid symbol", 400)

        # Redirect to homepage
        return redirect("/")
    
    # If user clicks the buy button   
    return render_template("buy.html")


@app.route("/check", methods=["GET"])
def check():
    """Return true if username available, else false, in JSON format"""
    
    # Grab the name from data of ajax call via GET method
    user_name = request.args.get("username")
    
    # Query db for username
    user_row = db.execute("SELECT id FROM users where username = :username LIMIT 1",
                            username=user_name)

    # If username exists
    if user_row:
        return jsonify({"status": "true"})
    
    # username doesn't exist
    else:
        return jsonify({"status": "false"})


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    # Fetch data form db
    rows = db.execute("SELECT * FROM history WHERE userid = :userid ORDER BY date_time DESC", userid=session["user_id"])

    # Travarse all rows for logged in user
    for row in rows:
        # Get the symbol from db
        symbol = row["symbol"]

        # Get information for symbol
        info = lookup(symbol)

        # Insert required indices into row to display in template
        row["price"] = usd(info["price"])

    return render_template("history.html", rows=rows)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():

    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        
        # Check for empty symbol
        if symbol == "":
            return apology("missing symbol", 400)
        
        # Get information for given symbol
        info = lookup(symbol)
        
        # Show information
        if info:
            return render_template('quoted.html', info=info)    
        
        # Notify for invalid symbol
        else:
            return apology("invalid symbol", 400)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    """Register user"""
    # Clear any previous session
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Get username and password
        user_name = request.form.get("username")
        user_password = request.form.get("password")
        user_password_confirmation = request.form.get("confirmation")

        # Ensure username was submitted
        if not user_name:
            return apology("Must provide username", 403)

        # Ensure is username is more than 3 characters
        if not len(user_name) > 2:
            return apology("username must be more than 2 characters!", 403)            

        # Ensure password was submitted
        elif not user_password:
            return apology("Must provide password", 403)

         # Ensure password confirmation was submitted
        elif not user_password_confirmation:
            return apology("Must provide password again", 403)

        # Check both passwords
        if user_password != user_password_confirmation:
            return apology("Passwords mismatched!", 403)

        # Check if username alrady exists
        users = db.execute("SELECT id FROM users where username = :username LIMIT 1",
                            username=user_name)

        # If users is empty
        if users:
            return apology("Not available!", 403)         

        # Insert data into database
        new_user = db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)",
              username=user_name, hash=generate_password_hash(user_password))

        # Save the session for new user to log him/her in right away
        session["user_id"] = new_user

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    # Grab form data if user submits the form
    if request.method == "POST":
        # Check for empty stock
        if not request.form.get("symbols"):
            return apology("Must provide symbol", 400)

        # Check for empty shares
        elif not request.form.get("shares"):
            return apology("Must provide number of shares", 400)

        # Number of shares of a stock
        shares_row = db.execute("SELECT shares FROM transactions WHERE userid = :userid AND symbol = :symbol",
            userid=session["user_id"], symbol=request.form.get("symbols"))
        
        # Restrict user from selling more shares than s/he has
        if (int(request.form.get("shares")) > shares_row[0]["shares"]):
            return apology("Don't have enough shares", 400)

        # Get information about this stock
        info = lookup(request.form.get("symbols"))

        # Current selling price
        selling_price = info["price"] * int(request.form.get("shares"))

        # Update the cash in users table
        cash_row = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
        updated_cash = cash_row[0]["cash"] + selling_price
        db.execute("UPDATE users SET cash = :cash WHERE id = :id", cash=updated_cash, id=session["user_id"])

        # DELETE row if user wills to sell all of his shares of a stock
        if (int(request.form.get("shares")) == shares_row[0]["shares"]):
            db.execute("DELETE FROM transactions WHERE userid = :userid AND symbol = :symbol",
                userid=session["user_id"], symbol=request.form.get("symbols"))

        # Update number of shares
        else:
            updated_share = shares_row[0]["shares"] - int(request.form.get("shares"))
            db.execute("UPDATE transactions SET shares = :shares WHERE userid = :userid AND symbol = :symbol",
                shares=updated_share, userid=session["user_id"], symbol=request.form.get("symbols"))

        # Get transaction time
        current_time = (datetime.now()).replace(microsecond=0)
        sold_shares = int(request.form.get("shares")) * -1

        # Update history table
        db.execute("INSERT INTO history (userid, symbol, shares, price, date_time) VALUES (:userid, :symbol, :shares, :price, :date_time)",
            userid=session["user_id"], symbol=request.form.get("symbols"), shares=sold_shares, price=info["price"], date_time=current_time)

        return redirect("/")
    
    
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        # Get all the symbols a user has bought
        symbol_rows = db.execute("SELECT symbol FROM transactions WHERE userid = :userid GROUP BY symbol", userid=session["user_id"])
        return render_template("sell.html", symbol_rows=symbol_rows)


@app.route("/save_symbol")
def save_symbol():
    """ Save the symbol into session """
    session["symbol"] = request.args.get("sym")
    return jsonify({"success": "True"})


@app.route("/buythis", methods=["GET"])
def buythis():
    """Buy shares of specific stock"""
    symbol = session["symbol"]
    return render_template("buy_this.html", symbol=symbol)

@app.route("/save_selected")
def save_selected():
    """ Save the selected symbol into session """
    session["selected"] = request.args.get("sym")
    return jsonify({"success": "True"})

@app.route("/sellthis", methods=["GET"])
def sellthis():
    """Sell shares of specific stock"""
    selected = session["selected"]
    return render_template("sell_this.html", selected=selected)

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)

# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
