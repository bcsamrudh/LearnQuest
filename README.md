# LearnQuest

Welcome to LearnQuest! 

LearnQuest is a note sharing website that allows users to share their notes, comment on notes, upvote their favorite notes, download notes, and generate questions based on the notes.

## Technologies Used

LearnQuest is built using the following technologies:

- Django: Django is a high-level Python web framework that provides a clean and efficient way to build web applications.
- Django-unicorn: Django-unicorn is a Django library that integrates with the Unicorn library to provide real-time, reactive components in Django applications.
- Bootstrap: Bootstrap is a popular CSS framework that provides pre-styled components and a responsive grid system.
- HTML: HTML is the standard markup language used to structure the content of web pages.
- CSS: CSS is used to style the HTML elements and provide a visually appealing design.
- JavaScript: JavaScript is a programming language that adds interactivity and dynamic behavior to web pages.
- Google PALM API: The Google PALM API is used to generate questions based on the content of the notes.

## Setting Up the Project

To set up the LearnQuest project on your local machine, follow these steps:

1. Clone the repository to your local machine using the following command:

   ```
   git clone <repository-url>
   ```

1. Navigate to the project directory:

   ```
   cd learnquest
   ```

1. Create a virtual environment to isolate the project's dependencies:

   ```
   python -m venv venv
   ```

1. Activate the virtual environment:

   - On Windows:

     ```
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```
     source venv/bin/activate
     ```

1. Install the project dependencies:

   ```
   pip install -r requirements.txt
   ```

1. Apply the database migrations:

   ```
   python manage.py migrate
   ```

1. Start the development server:

   ```
   python manage.py runserver
   ```

1. Open your web browser and visit `http://localhost:8000` to access LearnQuest.

## Features

LearnQuest provides the following features:

- **Note Sharing**: Users can upload and share their notes with the community.
- **Comments**: Users can comment on notes to provide feedback or ask questions.
- **Upvoting**: Users can upvote their favorite notes to show appreciation.
- **Note Download**: Users can download notes for offline access.
- **Question Generation**: Users can generate questions based on the content of the notes.
- **Accessible UI**: The website is made accessible, so that everybody can take advantage of the website.

## Contributing 😊

If you're interested in contributing to LearnQuest, you're welcome to submit pull requests and issues.

## License

LearnQuest is released under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and distribute the code as per the terms of the license.

## Acknowledgements

- Django: [https://www.djangoproject.com/](https://www.djangoproject.com/)
- Django-unicorn: [https://django-unicorn.readthedocs.io/](https://django-unicorn.readthedocs.io/)
- Bootstrap: [https://getbootstrap.com/](https://getbootstrap.com/)
- Cohere API: The Cohere API is used for question generation. [https://www.cohere.ai/](https://www.cohere.ai/)
- Django Snippets: I used there code snippets to make my development faster [https://djangosnippets.org/](https://djangosnippets.org/)