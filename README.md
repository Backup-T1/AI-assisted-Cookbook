# AI-Assisted Cookbook — Gemini Integration Prototype


**Original Implementation:** April 27, 2026 (with minor subsequent error-handling improvements)


## Project Overview 
This repository showcases my contributions to an AI-assisted cookbook developed as part of a five-person university group project.

The original project aimed to create a digital cookbook featuring AI-generated recipes, nutritional information, and motion controls for hands-free navigation.

This repository is not meant to reproduce my team's final application and instead focuses on my implementation of Google's Gemini AI, structured recipe generation, and supporting Flask and SQLAlchemy functionality.

Since the original group repository is private, this portfolio version excludes the team's motion-control implementation and focuses on the components I worked on.


## My Contributions

### 1. Google Gemini Integration and JSON Schema

My primary responsibility was integrating Google's Gemini AI into the team's existing application.

I developed a JSON response schema to structure AI-generated recipes into a consistent format containing:

- Recipe names and descriptions

- Ingredients and servings

- Preparation and cooking times

- Calories and other recipe information

- Additional cooking notes

The implementation processes user requests and uses the Gemini API to generate recipe information according to the defined schema.



### 2. Flask Application and Database Integration

At the time of my implementation, the team had developed an early HTML interface that required additional functionality to support AI-generated recipes.

With assistance from ChatGPT, I developed a prototype HTML interface, expanded the Flask application, and implemented SQLAlchemy database functionality to test the Gemini integration without delaying the team's progress. This involved connecting recipe generation to the interface, configuring database models, and implementing functionality for saving and retrieving recipes.



### 3. Troubleshooting and Debugging

Several challenges arose while integrating Gemini into the existing application.

#### JSON Response Formatting

- Designed and refined the JSON schema to meet the required recipe format.

- Debugged discrepancies between AI-generated responses and the data structures expected by the application.

- Converted generated ingredient lists into a compatible format for database storage.

- Added error handling for empty Gemini API responses to prevent attempting to parse missing data with `json.loads()`.


#### Application Integration

- Modified existing Flask functionality to process user requests and display generated recipes.

- Worked on aligning database fields with the information returned by Gemini.

- Added input validation and checks for empty API responses to improve error handling.

- Corrected an input-validation type mismatch by returning an error dictionary instead of a string, ensuring consistency with the function's declared return type.

These challenges required investigating unexpected behavior, modifying existing code, and testing changes against the desired output.


## Local Setup:
This application uses Google's Gemini API to generate structured recipe information. A valid Gemini API key is required for local recipe generation.

1. Install dependencies from the repository root:

   ```bash
   python -m pip install -r requirements.txt
   ```

2. Navigate to the application directory:

   ```bash
   cd Web-Dev
   ```

3. Configure your Gemini API key (macOS/Linux):

   ```bash
   export GEMINI_API_KEY="your_api_key"
   ```

(Replace the placeholder with your own API key).

4. Start the Flask application:

   ```bash
   python app.py
   ```

5. Open http://127.0.0.1:5000 in your browser.

**Note:** API keys are not included in this repository for security reasons.


## Functional Testing 
The following functionality was successfully tested during development:

- Recipe Generation: Verified that Google Gemini generates recipes from user requests using the defined JSON schema.

- Structured Output: Confirmed that generated recipes contain the required information, including ingredients, cooking times, and nutritional details.

- Database Storage: Successfully saved AI-generated recipes using Flask and SQLAlchemy.

- Data Persistence: Confirmed that previously saved recipes remain accessible after restarting the Flask application.


## Known Limitations: 
- The HTML interface is an early prototype designed primarily to test the Gemini integration and database functionality.