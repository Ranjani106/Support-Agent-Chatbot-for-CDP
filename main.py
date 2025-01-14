
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# How-to questions and responses dictionary for each platform
dynamic_responses = {
    "What is your name?": "I am a dynamic chatbot!",
    "What is Python?": "Python is a programming language that lets you work quickly and integrate systems more effectively.",
    "Tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs!"
}

HOW_TO_RESPONSES = {
    "segment": {
        "How do I find my source slug?": "To find your source slug in Segment, go to the Source settings and check the URL. The slug is part of the URL.",
        "How do I find my warehouse ID?": "To find your warehouse ID, navigate to the Warehouses tab in Segment, and the ID will be listed alongside each warehouse.",
        "How do I prevent a source from syncing to some or all warehouse?": "To prevent a source from syncing to a warehouse, go to the Source settings, and disable the sync for specific warehouses.",
        # Add more Segment-specific questions...
    },
    "mparticle": {
        "How do I get my Device ID?": "To get your Device ID in mParticle, follow these steps:\n1. Log in to your mParticle account.\n2. Go to the 'Device Info' section.\n3. You can find the Device ID under the relevant section depending on the platform (iOS, Android, etc.).",
        "What does an Indicative Realtime Data Source represent?": "An Indicative Realtime Data Source in mParticle represents a live data feed from a specific source that is integrated into your system in real-time.",
        "How To Download An Audience?": "Go to the 'Audiences' section, select the audience, and click 'Download' or export it to a destination.",
        "Why are there differences between the Event Volume and the Credit Usage reports?": "Differences may arise due to event sampling, aggregation, or reporting delays.",
#     "How do I get my Device ID?": "You can retrieve the Device ID from your app's logs or through debugging tools.",
        "How do you meter usage of Real-Time Products?": "Usage is metered based on events processed, API calls made, and other product-specific metrics.",
        "How do I purchase more mParticle Credits?": "Contact mParticle support or your account representative to purchase additional credits.",
        "How can I update event tiers in bulk for multiple events?": "Use the bulk editing tool in the 'Events' section of the mParticle dashboard.",
    },
    "lytics": {
        "What is a 'sync' in the context of Cloud Connect?": "In Cloud Connect, a 'sync' refers to transferring data from Lytics to an external system based on configured rules.",
        "Why can't I create a Data Model that returns no rows?": "You can't create a Data Model in Lytics that returns no rows, as it must have at least one row of data to work with.",
        "Why are the sync times slightly different than what I’d expect?": "Sync times may vary due to processing delays or resource availability.",
#     "Why can’t I create a Data Model that returns no rows?": "Lytics requires a Data Model to return at least one row to ensure it is functional.",
        "Why can’t I create/update a Data Model when my schema has unpublished changes?": "Unpublished changes in the schema must be published before creating or updating a Data Model.",
        "Can I select any field as the Lytics key?": "No, the field must uniquely identify records and meet Lytics requirements.",
        "Can I select any field as the primary key?": "The field must meet specific criteria, including being unique and properly indexed.",
    },
    "zeotap": {
        "How does this consent update relate to Google's operations?": "The consent update in Zeotap relates to Google’s operations by ensuring compliance with the GDPR and other data protection regulations for user consent.",
        "What should the customers do if they are unclear of Google consent update?": "If customers are unclear about the Google consent update, they should contact Zeotap support for clarification on how the update impacts their data.",
        "How can the customers onboard relevant consent signals for online and offline users?": "Customers should use Zeotap's consent management tools to onboard consent signals.",
        "What should the customers do if they are unclear about the Google consent update?": "Customers should consult Zeotap support or Google's official documentation for clarification.",

    }
}
HOW_TO_RESPONSES["segment"]["How do I find my source slug?"] = "To find your source slug in Segment, go to the Source settings and check the URL. The slug is part of the URL."
HOW_TO_RESPONSES["segment"]["How do I find my warehouse ID?"] = "To find your warehouse ID, navigate to the Warehouses tab in Segment, and the ID will be listed alongside each warehouse."
HOW_TO_RESPONSES["segment"]["How do I prevent a source from syncing to some or all warehouse?"] = "To prevent a source from syncing to a warehouse, go to the Source settings, and disable the sync for specific warehouses."
HOW_TO_RESPONSES["segment"]["How do I create a new source in Segment?"] = "To create a new source in Segment, go to the Sources page and click 'Add Source'. Then, follow the on-screen instructions to configure the new source."

HOW_TO_RESPONSES["mparticle"]["How To Download An Audience in mParticle?"] = "To download an audience, go to the 'Audiences' section in mParticle and select the desired audience. Then click on 'Download' or export it to a destination."
HOW_TO_RESPONSES["mparticle"]["How do I get my Device ID?"] = "To get your Device ID in mParticle, follow these steps:\n1. Log in to your mParticle account.\n2. Go to the 'Device Info' section.\n3. You can find the Device ID under the relevant section depending on the platform (iOS, Android, etc.)."
HOW_TO_RESPONSES["mparticle"]["What does an Indicative Realtime Data Source represent?"] = "An Indicative Realtime Data Source in mParticle represents a live data feed from a specific source that is integrated into your system in real-time."
HOW_TO_RESPONSES["mparticle"]["How To Download An Audience?"] = "Go to the 'Audiences' section, select the audience, and click 'Download' or export it to a destination."
HOW_TO_RESPONSES["mparticle"]["Why are there differences between the Event Volume and the Credit Usage reports?"] = "Differences may arise due to event sampling, aggregation, or reporting delays."
HOW_TO_RESPONSES["mparticle"]["How do you meter usage of Real-Time Products?"] = "Usage is metered based on events processed, API calls made, and other product-specific metrics."
HOW_TO_RESPONSES["mparticle"]["How do I purchase more mParticle Credits?"] = "Contact mParticle support or your account representative to purchase additional credits."
HOW_TO_RESPONSES["mparticle"]["How can I update event tiers in bulk for multiple events?"] = "Use the bulk editing tool in the 'Events' section of the mParticle dashboard."

HOW_TO_RESPONSES["lytics"]["What is a 'sync' in the context of Cloud Connect?"] = "In Cloud Connect, a 'sync' refers to transferring data from Lytics to an external system based on configured rules."
HOW_TO_RESPONSES["lytics"]["Why can't I create a Data Model that returns no rows?"] = "You can't create a Data Model in Lytics that returns no rows, as it must have at least one row of data to work with."
HOW_TO_RESPONSES["lytics"]["Why are the sync times slightly different than what I’d expect?"] = "Sync times may vary due to processing delays or resource availability."
HOW_TO_RESPONSES["lytics"]["Why can’t I create/update a Data Model when my schema has unpublished changes?"] = "Unpublished changes in the schema must be published before creating or updating a Data Model."
HOW_TO_RESPONSES["lytics"]["Can I select any field as the Lytics key?"] = "No, the field must uniquely identify records and meet Lytics requirements."
HOW_TO_RESPONSES["lytics"]["Can I select any field as the primary key?"] = "The field must meet specific criteria, including being unique and properly indexed."

HOW_TO_RESPONSES["zeotap"]["How does this consent update relate to Google's operations?"] = "The consent update in Zeotap relates to Google’s operations by ensuring compliance with the GDPR and other data protection regulations for user consent."
HOW_TO_RESPONSES["zeotap"]["What should the customers do if they are unclear of Google consent update?"] = "If customers are unclear about the Google consent update, they should contact Zeotap support for clarification on how the update impacts their data."
HOW_TO_RESPONSES["zeotap"]["How can the customers onboard relevant consent signals for online and offline users?"] = "Customers should use Zeotap's consent management tools to onboard consent signals."
HOW_TO_RESPONSES["zeotap"]["What should the customers do if they are unclear about the Google consent update?"] = "Customers should consult Zeotap support or Google's official documentation for clarification."

dynamic_responses["What is your name?"] = "I am a dynamic chatbot!."


def get_response(question):
    # Check all platforms for the question with a case-insensitive match
    for platform, questions in HOW_TO_RESPONSES.items():
        for key in questions:
            if key.lower() in question.lower():
                return questions[key]
    return "I'm sorry, I don't know how to answer that yet. Can you ask something else?"


# Route to handle chat requests
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    if user_message:
        response = get_response(user_message)
        return jsonify({"response": response})
    else:
        return jsonify({"response": "No message provided. Please send a message."})


# Home route to check if the app is running
@app.route('/')
def home():
    return render_template('index.html')
    return "Flask app is working!"


if __name__ == '__main__':
    # app.run(debug=True)
    # app.run(host="0.0.0.0", port=5000)
    app.run(host='0.0.0.0', port=5000, debug=True)


