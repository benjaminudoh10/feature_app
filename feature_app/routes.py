from flask import render_template
from flask import request, jsonify, redirect, url_for
from datetime import datetime

from feature_app import app, models, db
from config import Config


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        value = request.get_json(force=True)
        form = {
            key: value for (key, value) in (
                d.values() for d in value
            )
        }

        # check if Client & Product Area exists in database
        # client_model = models.Client.query.filter_by(
        #     name=form['client']).first()
        client_model = models.Client.get_client(form['client'])
        product_area = models.ProductArea.get_product_area(
            form['product_area'])

        # create both product area and client if they do not exist
        if not product_area:
            product_area = models.ProductArea(name=form['product_area'])
            db.session.add(product_area)
        if not client_model:
            client_model = models.Client(name=form['client'])
            db.session.add(client_model)

        client_priority = form['client_priority']
        # check if client's previous feature requests already
        # has the given client_priority
        client_priority_exists = models.FeatureRequest.query.filter_by(
            client_id=client_model.id,
            client_priority=client_priority).first()

        if client_priority_exists:
            # Increment client priority of all feature_requests
            # greater than or equal to client_priority by 1
            old_feature_requests = models.FeatureRequest.query.filter(
                models.FeatureRequest.client_id==client_model.id,
                models.FeatureRequest.client_priority >= client_priority).all()
            for req in old_feature_requests:
                req.client_priority += 1
                db.session.add(req)

        feature_request = models.FeatureRequest(
            title=form['title'],
            description=form['description'],
            client_priority=client_priority,
            target_date=datetime.strptime(form['target_date'], '%Y-%m-%d')
        )
        db.session.add(feature_request)

        client_model.feature_requests.append(feature_request)
        product_area.feature_requests.append(feature_request)

        db.session.commit()

        return jsonify({'result': 'OK'})

    # get paginated feature requests from db
    page = request.args.get('page', 1, type=int)
    pagination = models.FeatureRequest.query.order_by(
        models.FeatureRequest.timestamp.desc()).paginate(
            page, per_page=Config.FEATURES_PER_PAGE, error_out=False)
    feature_requests = pagination.items

    return render_template(
        'index.html', feature_requests=feature_requests,
        pagination=pagination)

@app.route('/delete/<int:feature_id>')
def delete(feature_id):
    feature = models.FeatureRequest.query.get(feature_id)
    db.session.delete(feature)
    db.session.commit()

    return redirect(url_for('index'))
