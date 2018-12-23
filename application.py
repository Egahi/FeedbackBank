from flask import redirect, render_template, request
from sqlalchemy import asc
from alchemy import Entry, db, app

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    """Render Landing page"""
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def buy():
    """Log entery in database"""
    title = request.form.get("title")
    description = request.form.get("description")
    client = request.form.get("client")
    priority = request.form.get("priority")
    iPriority = int(priority)
    date = request.form.get("date")
    area = request.form.get("area")

    # select entries for same client
    previousEntry = Entry.query.filter_by(client=client).order_by(asc(Entry.priority)).all()

    # modify priority list to accommodate latest entry
    for i in range(len(previousEntry)):
        iPrePriority = int(previousEntry[i].priority)

        # priority level assigned to new request, increment previous request's priority by 1
        if iPriority == iPrePriority:
            temp = iPriority + 1
            previousEntry[i].priority = previousEntry[i].priority + 1

            for j in range(i, len(previousEntry)):
	        # increment subsequent priority levels by one if previously asigned
                if temp == int(previousEntry[j].priority):
                    previousEntry[j].priority = previousEntry[j].priority + 1
                    temp = temp + 1
                else:
                    break

            db.session.commit()
            break

    # log new entry
    entry = Entry(title, description, client, priority, date, area)
    db.session.add(entry)
    db.session.commit()

    # Redirect user to home page
    return redirect("/")
