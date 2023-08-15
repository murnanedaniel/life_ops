from app import app, db
from app.models import LifeDocument, MergeRequest
from app.ai_logic import review_request, ai_merge
from flask import render_template, request, redirect, url_for

@app.route('/', methods=['GET', 'POST'])
def index():
    life_document = LifeDocument.query.order_by(LifeDocument.id.desc()).first()
    if life_document:
        content = life_document.content
    else:
        content = """
# Life Document
---

A document describing a person's life. The equivalent of a Model Card, for a human!

## Life Goals
---

- An example life goal (you can delete this!)

## Projects
---

- An example project (you can delete this!)

## Habits
---

- An example habit (you can delete this!)

"""

    if request.method == 'POST':
        merge_request_content = request.form.get('content')
        feedback = review_request(merge_request_content)
        return render_template('review.html', merge_request_content=merge_request_content, feedback=feedback)

    return render_template('index.html', life_document_content=content)

@app.route('/commit', methods=['POST'])
def commit():
    merge_request_content = request.form.get('content')
    
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
    return redirect(url_for('index'))