from app import app, db
from app.models import LifeDocument, MergeRequest
from app.services.ai_logic import review_request, ai_merge, send_messages
from flask import render_template, request, redirect, url_for, jsonify, Response, stream_template



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print("POST input:", request.json)
        chat_history = request.json.get('chat_history', [])

        def event_stream():
            for line in send_messages(chat_history=chat_history):
                text = line.choices[0].delta.get('content', '')
                if len(text): 
                    yield text

        return Response(event_stream(), mimetype='text/event-stream')
    else:
        return stream_template('./index.html')



@app.route('/life_document', methods=['GET', 'POST'])
def life_doc():
    life_document = LifeDocument.query.order_by(LifeDocument.id.desc()).first()
    if life_document:
        content = life_document.content
    else:
        content = """
# Life Document

A document describing a person's life. The equivalent of a Model Card, for a human!

## Life Goals

- An example life goal (you can delete this!)

## Projects

- An example project (you can delete this!)

## Habits

- An example habit (you can delete this!)

"""
        life_document = LifeDocument(content=content)
        db.session.add(life_document)
        db.session.commit()

    if request.method == 'POST':
        merge_request_content = request.form.get('content')
        feedback, approval = review_request(merge_request_content, content)
        return render_template('review.html', merge_request_content=merge_request_content, feedback=feedback, approval=approval)

    return render_template('life_document.html', life_document_content=content)

@app.route('/merge_requests', methods=['GET'])
def merge_requests():
    merge_requests = MergeRequest.query.order_by(MergeRequest.timestamp.desc()).all()
    return render_template('merge_requests.html', merge_requests=merge_requests)


@app.route('/commit', methods=['POST'])
def commit():
    merge_request_content = request.get_json().get('content')
    
    # Fetch the latest Life Document
    life_document = LifeDocument.query.order_by(LifeDocument.id.desc()).first()
    if life_document:
        current_content = life_document.content
    else:
        current_content = ""

    # Send the merge request and current content to the AI for merging
    merged_content = ai_merge(merge_request_content, current_content)

    # Update the Life Document in the database
    if life_document:
        life_document.content = merged_content
    else:
        life_document = LifeDocument(content=merged_content)
        db.session.add(life_document)
    
    db.session.commit()
    return jsonify({"status": "success", "message": "Committed successfully"})

@app.route('/get_review', methods=['POST'])
def get_review():
    merge_request_content = request.get_json().get('content')

    # Fetch the latest Life Document
    life_document = LifeDocument.query.order_by(LifeDocument.id.desc()).first()
    if life_document:
        life_document_content = life_document.content
    else:
        life_document_content = ""

    feedback, approval = review_request(merge_request_content, life_document_content)

    # Save the merge request to the database
    merge_request = MergeRequest(content=merge_request_content, ai_review=feedback, approval=approval)
    db.session.add(merge_request)
    db.session.commit()

    return jsonify({"content": merge_request_content, "feedback": feedback, "approval": approval})

@app.route('/update_merge_request', methods=['POST'])
def update_merge_request():
    merge_request_content = request.get_json().get('content')
     
    # Fetch the latest Life Document
    life_document = LifeDocument.query.order_by(LifeDocument.id.desc()).first()
    if life_document:
        current_content = life_document.content
    else:
        current_content = ""
    
    # Send the merge request and current content to the AI for merging
    merged_content = ai_merge(merge_request_content, current_content)

    # Update the Life Document in the database
    if life_document:
        life_document.content = merged_content
    else:
        life_document = LifeDocument(content=merged_content)
        db.session.add(life_document)
    
    db.session.commit()
    return jsonify({"merged_content": merged_content})

