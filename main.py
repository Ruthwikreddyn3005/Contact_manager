from flask import request, jsonify
from config import app, db
from models import Contact


@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts})

@app.route("/create_contact", methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    middle_name = request.json.get("middleName")
    email = request.json.get("email")

    if not first_name or not last_name or not middle_name or not email:
        return (jsonify({"message": "you must fill all the feilds"}), 400,)
    
    new_contact = Contact(first_name = first_name, last_name=last_name, middle_name=middle_name, email= email)

    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message":"succesfully added new contact"}),201

@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
    contact= Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "contact not exists"}), 400
    
    data = request.json
    contact.first_name = data.get("firstName", contact.first_name) #here get method uses te first parametr checks if theres any value in json data matchnf if not user dont want updtae so get method uses second place parameter to not chnage kep it same old
    contact.last_name = data.get("lastName", contact.last_name)
    contact.middle_name = data.get("middleName", contact.middle_name)
    contact.email = data.get("email", contact.email)    

    db.session.commit()
    return jsonify({"message":"contact updated succesfully"}), 200

@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    contact= Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "contact not found"}), 400
    
    db.session.delete(contact)
    db.session.commit()
    return jsonify({"message": "contact deleted succesfully"}), 200


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)

