from flask import request, jsonify, current_app as app
from app import db
from app.models import Quote

@app.route("/quote", methods=['POST'])
def create_quote():
    data = request.get_json()
    text = data.get('text')
    author = data.get('author')

    if not text or not author:
        return jsonify({
            "status": "Failed",
            "message": "You need to have a text and an author",
            "data": None
        }), 403
    
    quote = Quote(text = text,author = author)
    db.session.add(quote)
    db.session.commit()
    return jsonify({
        "status": "Success",
        "message": "Added quote successfully",
        "data": quote.to_dict()
    }), 201

@app.route("/quotes", methods=['GET'])
def list_quotes():
    quotes = Quote.query.all()
    quotes_data = [quote.to_dict() for quote in quotes]
    return jsonify({
        "status": "Success",
        "message": "Retrieved quotes successfully",
        "data": quotes_data
    })

