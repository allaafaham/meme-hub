# [meme-hub](https://meme-hub-14ccc52cb51a.herokuapp.com)

Developer: Allaa Faham ([allaafaham](https://www.github.com/allaafaham))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/allaafaham/meme-hub)](https://www.github.com/allaafaham/meme-hub/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/allaafaham/meme-hub)](https://www.github.com/allaafaham/meme-hub/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/allaafaham/meme-hub)](https://www.github.com/allaafaham/meme-hub)



![screenshot](documentation/mockup.png)

source: [meme-hub amiresponsive](https://ui.dev/amiresponsive?url=https://meme-hub-14ccc52cb51a.herokuapp.com)

> [!IMPORTANT]
> The examples in these templates are strongly influenced by the Code Institute walkthrough project called "I Think Therefore I Blog".

## UX

### The 5 Planes of UX

#### 1. Strategy

**Purpose**
- Provide meme creators with tools to share, manage, and moderate engaging meme content and user interactions.
- Offer users and guests an intuitive platform to explore, engage, and contribute to meme discussions.

**Primary User Needs**
- Meme creators need seamless tools for publishing and managing memes and comments.
- Registered users need the ability to engage with meme content through comments, likes, and account features.
- Guests need the ability to browse and enjoy meme content without registration.

**Business Goals**
- Foster a dynamic meme-sharing platform with active user participation.
- Build a sense of community through meme discussions and user engagement.
- Ensure easy meme content management for creators.

#### 2. Scope

**[Features](#features)** (see below)

**Content Requirements**
- Meme post management (create, update, delete, and preview).
- Comment moderation and management tools.
- User account features (register, log in, edit/delete comments).
- 404 error page for lost users.

#### 3. Structure

**Information Architecture**
- **Navigation Menu**:
  - Links to Home, Meme Posts, Login/Register, and Dashboard (for meme creators).
- **Hierarchy**:
  - Meme content displayed prominently for easy browsing.
  - Clear call-to-action buttons for account creation and engagement (e.g., commenting).

**User Flow**
1. Guest users browse meme content → read captions and see commenter names.
2. Guest users register for an account → log in to leave comments and see NSFW content.
3. Registered users leave comments
4. Meme creators create, update, and manage posts 

#### 4. Skeleton

**[Wireframes](#wireframes)** (see below)

#### 5. Surface

**Visual Design Elements**
- **[Colours](#colour-scheme)** (see below)
- **[Typography](#typography)** (see below)

### Colour Scheme


- `#6C63FF` (Vibrant Purple) - Primary brand color used for main elements and brand identity
- `#FF6B6B` (Coral Red) - Secondary brand color used for interactive elements
- `#4ECDC4` (Turquoise) - Accent color used for highlights and special elements
- `#2D3436` (Dark Gray) - Main text color for optimal readability
- `#F7F7F7` (Light Gray) - Background color for clean, modern look

Additional colors:
- Success: `#00B894` (Green) - For success messages
- Warning: `#FFD93D` (Yellow) - For warning messages
- Danger: `#FF4757` (Red) - For error messages

### Typography

The project uses a combination of system fonts and icon libraries:

- **System Fonts**: The project uses the default system font stack from Bootstrap which provides optimal performance and native feel across different operating systems.
- **[Font Awesome 6.0.0](https://fontawesome.com)**: Used throughout the site for icons.

## Wireframes

> **Note:**  
> I did not create formal wireframes for this project. Instead, I designed the user interface directly in the browser, iteratively refining the layout and user experience based on feedback and personal testing. This approach allowed for rapid prototyping and adjustment, ensuring the final design met the needs of the project.

## User Stories

Each user story below represents a core feature and may encompass several tasks or subtasks required to accomplish the full functionality.

| Target | Expectation | Outcome |
| --- | --- | --- |
| As a user | I want to register for an account | so that I can access meme-hub features and personalize my experience. |
| As a user | I want to log in to my account | so that I can securely access my profile and interact with memes. |
| As a user | I want to manage my profile | so that I can update my personal information and preferences. |
| As a user | I want to upload memes | so that I can share my creations with the community. |
| As a user | I want to view memes | so that I can browse and enjoy content shared by others. |
| As a user | I want to like memes | so that I can show appreciation for content I enjoy. |
| As a user | I want to comment on memes | so that I can engage in discussions and provide feedback. |
| As a user | I want to manage meme labels | so that I can organize and categorize memes for easier discovery. |

## Features

### Existing Features

| Feature            | Notes                                                                 | Screenshot                                      |
|--------------------|-----------------------------------------------------------------------|-------------------------------------------------|
| Register           | Authentication is handled by allauth, allowing users to register accounts. | ![screenshot](documentation/features/register.png) |
| Login              | Authentication is handled by allauth, allowing users to log in to their existing accounts. | ![screenshot](documentation/features/login.png)    |
| Logout             | Authentication is handled by allauth, allowing users to log out of their accounts. | ![screenshot](documentation/features/logout.png)   |
| Meme List          | The homepage displays basic information about memes, including image, title, author, date, and a brief excerpt. | ![screenshot](documentation/features/meme-list.png) |
| View Meme          | Users can view the full meme details, including any comments.         | ![screenshot](documentation/features/view-post.png) |
| Add Comments       | Authenticated visitors can comment on memes.                          | ![screenshot](documentation/features/add-comment.png) |
| Edit Comments      | Authenticated visitors can edit their own comments.                   | ![screenshot](documentation/features/edit-comment.png) |
| Delete Comments    | Authenticated visitors can delete their own comments.                 | ![screenshot](documentation/features/delete-comment.png) |
| Create Meme        | Site owners can create/publish memes, including setting a featured image using Cloudinary, all from the Django admin dashboard. | ![screenshot](documentation/features/create-post.png) |
| Update Meme        | Site owners can update/manage memes from the Django admin dashboard.  | ![screenshot](documentation/features/update-post.png) |
| Delete Meme        | Site owners can delete memes from the Django admin dashboard.         | ![screenshot](documentation/features/delete-post.png) |
| Labels & Filtering | Users can assign labels to memes and filter memes by selected labels for easier discovery. | ![screenshot](documentation/features/labels.png) |
| User Feedback      | Clear and obvious Django messages are used to provide feedback to user actions. | ![screenshot](documentation/features/messages.png) |
| Heroku Deployment  | The site is fully deployed to Heroku, making it accessible online and easy to manage. | ![screenshot](documentation/features/heroku.png) |
| 404                | The 404 error page will indicate when a user has navigated to a page that doesn't exist, replacing the default Heroku 404 page with one that ties into the site's look and feel. | ![screenshot](documentation/features/404.png) |

### Future Features

- **Meme Search Functionality**: Add a search bar for users to quickly find memes by keywords, captions, or tags.
- **Meme Reactions**: Implement a variety of reactions (e.g., 😂, 😮, 😍) in addition to likes, to increase user engagement and expressiveness.
- **Comment Replies & Threads**: Enable users to reply to comments, creating nested comment threads for better discussions under each meme.
- **Meme Sharing**: Add social media sharing buttons (e.g., Twitter, Facebook, Instagram, Reddit) for users to share memes directly from the site.
+- **Meme Analytics**: Provide meme creators with analytics such as views, shares, and engagement rates for their memes.
- **Related Memes Recommendations**: Show related memes at the bottom of a meme page to encourage further browsing and engagement.
- **Weekly Meme Contests**: Host weekly meme contests where users can submit memes and vote for their favorites, with winners featured on the homepage.
- **Notifications**: Implement a notification system that alerts users when their comments are approved, when new comments are made on a post they've commented on, or when new posts are published.
- **Email Subscriptions**: Allow users to subscribe to receive email notifications for new posts, updates, or newsletters.
- **Content Flagging/Reporting**: Allow users to flag or report inappropriate content (comments or posts) for moderation.
- **Admin Dashboard Analytics**: Provide site admins with an analytics dashboard showing user activity, popular posts, most commented articles, etc.
- **Custom Themes for Users**: Allow users to customize the visual theme of the site (colors, fonts, etc.) to suit their preferences.

## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/VSCode-grey?logo=htmx&logoColor=007ACC)](https://code.visualstudio.com) | Local IDE for development. |
| [![badge](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) | Main site content and layout. |
| [![badge](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) | Design and layout. |
| [![badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) | Front-end CSS framework for modern responsiveness and pre-built components. |
| [![badge](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) | Python framework for the site. |
| [![badge](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) | Relational database management. |
| [![badge](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) | Online static file storage. |
| [![badge](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) | Serving static files with Heroku. |
| [![badge](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) | Icons. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, and explain things. |
| [![badge](https://img.shields.io/badge/Mermaid-grey?logo=mermaid&logoColor=FF3670)](https://mermaid.live) | Generate an interactive diagram for the data/schema. |

## Database Design

### Data Model

Entity Relationship Diagrams (ERD) help to visualize database architecture before creating models. Understanding the relationships between different tables can save time later in the project.


I have used `Mermaid` to generate an interactive ERD of my project.

![screenshot](documentation/mermaid-erd.png) 


## Agile Development Process

### GitHub Projects


[GitHub Projects](https://www.github.com/allaafaham/meme-hub/projects) served as an Agile tool for this project. Through it, EPICs, User Stories, issues/bugs, and Milestone tasks were planned, then subsequently tracked on a regular basis using the Kanban project board.

![screenshot](documentation/gh-projects.png)

![screenshot](documentation/gh-projects-example.png)


### GitHub Issues

[GitHub Issues](https://www.github.com/allaafaham/meme-hub/issues) served as an another Agile tool. There, I managed my User Stories and Milestone tasks, and tracked any issues/bugs.

![screenshot](documentation/milestones.png)


### MoSCoW Prioritization

I've decomposed my Epics into User Stories for prioritizing and implementing them. Using this approach, I was able to apply "MoSCoW" prioritization and labels to my User Stories within the Issues tab.

- **Must Have**: guaranteed to be delivered - required to Pass the project (*max ~60% of stories*)
- **Should Have**: adds significant value, but not vital (*~20% of stories*)
- **Could Have**: has small impact if left out (*the rest ~20% of stories*)

## Testing

> [!NOTE]
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://meme-hub-14ccc52cb51a.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), then finally, click **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables to match your private `env.py` file.

> [!IMPORTANT]
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user-inserts-own-cloudinary-url |
| `DATABASE_URL` | user-inserts-own-postgres-database-url |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | any-random-secret-key |

Heroku needs some additional files in order to deploy properly.

- [requirements.txt](requirements.txt)
- [Procfile](Procfile)

You can install this project's **[requirements.txt](requirements.txt)** (*where applicable*) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **[Procfile](Procfile)** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace `app_name` with the name of your primary Django app name; the folder where `settings.py` is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either (*recommended*):

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (*replace `app_name` with your app name*)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For "Primary Interest", you can choose **Programmable Media for image and video API**.
- *Optional*: edit your assigned cloud name to something more memorable.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the leading `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.
    - `cloudinary://123456789012345:AbCdEfGhIjKlMnOpQrStuVwXyZa@1a2b3c4d5)`
- This will go into your own `env.py` file, and Heroku Config Vars, using the **key** of `CLOUDINARY_URL`.

### PostgreSQL

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net) for the Relational Database with Django.

> [!CAUTION]
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method if you plan to clone/fork this repository.
> - Code Institute students are allowed a maximum of 8 databases.
> - Databases are subject to deletion after 18 months.

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Submitted my email address to the CI PostgreSQL Database link above.
- An email was sent to me with my new Postgres Database.
- The Database connection string will resemble something like this:
    - `postgres://<db_username>:<db_password>@<db_host_url>/<db_name>`
- You can use the above URL with Django; simply paste it into your `env.py` file and Heroku Config Vars as `DATABASE_URL`.

### WhiteNoise

This project uses the [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) to aid with static files temporarily hosted on the live Heroku site.

To include WhiteNoise in your own projects:

- Install the latest WhiteNoise package:
    - `pip install whitenoise`
- Update the `requirements.txt` file with the newly installed package:
    - `pip freeze --local > requirements.txt`
- Edit your `settings.py` file and add WhiteNoise to the `MIDDLEWARE` list, above all other middleware (apart from Django's "SecurityMiddleware"):

```python
# settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # any additional middleware
]
```


### Local Development

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the [requirements.txt](requirements.txt) file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level, and include the same environment variables listed above from the Heroku deployment steps.

> [!IMPORTANT]
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

Sample `env.py` file:

```python
import os

os.environ.setdefault("SECRET_KEY", "any-random-secret-key")
os.environ.setdefault("DATABASE_URL", "user-inserts-own-postgres-database-url")
os.environ.setdefault("CLOUDINARY_URL", "user-inserts-own-cloudinary-url")  # only if using Cloudinary

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` (*Windows/Linux*) or `⌘+C` (*Mac*)
- Make any necessary migrations: `python3 manage.py makemigrations --dry-run` then `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate --plan` then `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (*if applicable*): `python3 manage.py loaddata file-name.json` (*repeat for each file*)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*
- **NOTE**: You should never make a backup of the default *admin* or *users* data with confidential information.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://www.github.com/allaafaham/meme-hub).
2. Locate and click on the green "Code" button at the very top, above the commits and files.
3. Select whether you prefer to clone using "HTTPS", "SSH", or "GitHub CLI", and click the "copy" button to copy the URL to your clipboard.
4. Open "Git Bash" or "Terminal".
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:
	- `git clone https://www.github.com/allaafaham/meme-hub.git`
7. Press "Enter" to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://www.github.com/allaafaham/meme-hub)

**Please Note**: in order to directly open the project in Gitpod, you should have the browser extension installed. A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/allaafaham/meme-hub).
2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

There are no remaining major differences between the local version when compared to the deployed version online.

## Credits

### Content

| Source | Notes |
| --- | --- |
| [Markdown Builder](https://markdown.2bn.dev) | Help generating Markdown files |
| [I Think Therefore I Blog](https://codeinstitute.net) | Code Institute walkthrough project inspiration |
| [Bootstrap](https://getbootstrap.com) | Various components / responsive front-end framework |
| [Cloudinary API](https://cloudinary.com) | Cloud storage for static/media files |
| [Whitenoise](https://whitenoise.readthedocs.io) | Static file service |
| [Python Tutor](https://pythontutor.com) | Additional Python help |
| [ChatGPT](https://chatgpt.com) | Help with code logic and explanations |

### Media


| Source | Notes |
| --- | --- |
| [favicon.io](https://favicon.io) | Generating the favicon |
| [Font Awesome](https://fontawesome.com) | Icons used throughout the site |
| [ChatGPT](https://chatgpt.com) | Help with creating images |


### Acknowledgements



- I would like to thank my Code Institute mentor, [Tim Nelson](https://www.github.com/TravelTimN) for the support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) Tutor Team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support; it kept me going during periods of self doubt and impostor syndrome.
- I would like to thank my partner, for believing in me, and allowing me to make this transition into software development.

