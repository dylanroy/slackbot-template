import logging

from flask import Flask, jsonify, request


app = Flask(__name__)
app.url_map.strict_slashes = False
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    return 'Slack Bot Template'


@app.route("/hello", methods=['GET', 'POST'])
def hello_command():
    print request.form
    return "Hello"


@app.route("/hello-name", methods=['GET', 'POST'])
def hello_name_command():
    """
    ImmutableMultiDict([('user_id', u'U025QN6JL'),
                        ('response_url', u'https://hooks.slack.com/commands/T025QN6JG/274575376198/EXHqAKoLAhjVBRrmoT1BSVTU'),
                        ('text', u''),
                        ('token', u'Q7LlsfFWyAE8f5WmkZDMbfh9'),
                        ('trigger_id', u'273698057714.2194754628.ac2f9b4a943053797690dfbea1dbb743'),
                        ('channel_id', u'C026SBRHZ'),
                        ('team_id', u'T025QN6JG'),
                        ('command', u'/hello'),
                        ('team_domain', u'dowjones'),
                        ('user_name', u'dylan.roy'),
                        ('channel_name', u'test')])
    """
    user_name = request.form.get("user_name")
    return jsonify({"text": "Hello {0}".format(user_name)})


@app.route("/hello-echo", methods=['GET', 'POST'])
def hello_echo_command():
    text = request.form.get("text", "")
    user_name = request.form.get("user_name", "")
    return jsonify({'text': '{0} said "{1}"'.format(user_name, text)})


@app.route("/hello-attachment", methods=['GET', 'POST'])
def hello_attachment_command():
    user_name = request.form.get("user_name")

    # Generate Fields
    fields_list = [{'title': k, 'value': v, 'short': "true"} for k, v in request.form.to_dict().items()]
    return jsonify({"text": "Hello {0}".format(user_name),
                    "attachments": [{"color": "0ba7d7",
                                     "attachment_type": "default",
                                     "fields": fields_list}]})
