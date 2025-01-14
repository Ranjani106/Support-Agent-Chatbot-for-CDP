# Support-Agent-Chatbot-for-CDP

## Description
The **Support Agent Chatbot for CDP** is a chatbot application designed to provide assistance to users by answering common how-to questions for different platforms like Segment, mParticle, Lytics, and Zeotap. This chatbot provides quick responses to help users understand platform-related queries efficiently.

The project is built with **Flask** for the backend and uses **HTML**, **CSS**, and **JavaScript** for the frontend.

## Features
- Dynamic chatbot that provides responses based on user queries.
- Simple and responsive UI to enhance the user experience.
- Built using **Flask** for backend and **HTML/CSS/JavaScript** for frontend.

## Technologies Used
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Version Control**: Git, GitHub
- **Deployment**: Heroku (Optional)
  
Setup and Installation
1. Clone the Repository
git clone https://github.com/yourusername/chatbot.git
cd cdp-chatbot
2. Install Dependencies
Create a virtual environment and install required libraries:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
3. Preprocess Documentation
Fetch and preprocess the official documentation for Segment, mParticle, Lytics, and Zeotap:

Update the data/ folder with preprocessed text files or use the script:
python preprocess_docs.py
4. Start the Flask Application
Run the chatbot server:

python app.py
The application will be accessible at: http://127.0.0.1:5000.

Usage
Run the Chatbot:

Open a terminal and start the Flask app.
Alternatively, deploy the application to a cloud service like Heroku or AWS for public access.
Ask Questions:

Use the web interface or API endpoint to ask questions about Segment, mParticle, Lytics, or Zeotap.
Example API request (via Postman or cURL):
POST /chat
{
  "query": "How do I set up a new source in Segment?"
}
File Structure
cdp-chatbot/
├── app.py                 # Main Flask application
├── preprocess_docs.py     # Script to fetch and preprocess documentation
├── requirements.txt       # Python dependencies
├── data/                  # Preprocessed documentation (Segment, mParticle, etc.)
├── templates/             # HTML files for web interface (if any)
├── static/                # CSS/JS for styling
└── README.md              # Project README
Evaluation Checklist
 Accurate Responses: Retrieves relevant steps for "how-to" questions.
 Added some advanced features and dynamic questions
 Error Handling: Responds gracefully to invalid queries.
 Cross-CDP Comparisons: Handles comparative questions.
 Scalability: Easily extendable to include other CDPs.
Future Enhancements
Continuous Learning: Use machine learning to improve question understanding.
Dynamic Updates: Automatically fetch updates from the official documentation.
Multi-language Support: Extend support to other languages.
License
This project is licensed under the MIT License.

Contributors
Sriram: [ranjanivaratharajan20@gmail.com]
Feel free to contribute by submitting pull requests or reporting issues!
