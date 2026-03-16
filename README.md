<h1>userAPI</h1>
<p>A RESTful notes API that allows users to create, read, update, and delete personal notes with full user authentication.</p>
<p>To see the <strong>live API documentation</strong>, click <a href="https://userapi-production-8bfe.up.railway.app/docs" target="_blank">here</a>.</p>

<h2>Tech Stack</h2>
<h3>Languages</h3>
<ul>
    <li><a href="https://python.org" target="_blank">Python</a></li>
</ul>
<h3>Frameworks</h3>
<ul>
    <li><a href="https://fastapi.tiangolo.com/" target="_blank">FastAPI</a></li>
</ul>
<h3>Technical Features</h3>
<ul>
    <li><a href="https://alembic.sqlalchemy.org/en/latest/" target="_blank">Alembic</a> migrations</li>
    <li>Authentication service with JWT tokens</li>
    <li>Backend server running on <a href="https://uvicorn.dev/" target="_blank">uvicorn</a></li>
    <li>bcrypt-sha256 password encryption</li>
    <li>Data validation with <a href="https://docs.pydantic.dev/latest/" target="_blank">Pydantic</a></li>
    <li><a href="https://www.postgresql.org/" target="_blank">PostgreSQL</a> database</li>
    <li><a href="https://www.sqlalchemy.org/" target="_blank">SQLAlchemy</a> for ORM interaction</li>
</ul>

<h2>Technical Decisions</h2>
<h3>Why FastAPI over something like Flask?</h3>
<p>FastAPI was chosen for its performance, widespread industry adoption, and automatic Swagger/OpenAPI documentation generation. It also has a rich ecosystem of tools for building robust APIs, including built-in support for Pydantic data validation and async request handling. Flask is a lightweight micro-framework and lacks many of these features out of the box.</p>
<h3>Why PostgreSQL over SQLite?</h3>
<p>PostgreSQL was chosen because it is the standard for modern production applications. Unlike SQLite, which stores the entire database in a single file, PostgreSQL is a full object-relational database system with strong support for concurrency, data integrity, and security - all of which are important for a multi-user API.</p>
<h3>Why use Alembic for migrations?</h3>
<p>Alembic provides version-controlled schema migrations, which means changes to the database structure are tracked and reproducible. This is far safer than manually altering tables, and it allows the schema to evolve over time without losing existing data.</p>

<h2>How to run <em>userAPI</em> locally</h2>
<ol>
    <li>Clone the Git repository by running <code>git clone https://github.com/dylanmckay04/userAPI.git</code></li>
    <li>Create a <code>.env</code> file and add the necessary environment variables (<a href="#env">see section below</a>)</li>
    <li>Ensure <a href="https://www.docker.com/" target="_blank">Docker</a> is running and change directory to the project root, then run <code>docker compose up --build</code></li>
    <li>Go to <a href="http://localhost:8000/health" target="_blank">http://localhost:8000/health</a> in your browser and you should see <code>{"status": "ok"}</code></li>
    <li>Visit <a href="http://localhost:8000/docs" target="_blank">http://localhost:8000/docs</a> to explore the interactive API documentation</li>
</ol>

<h2 id="env">Environment Variables</h2>
<ol>
    <li><strong>DATABASE_URL</strong> - ex. <code>postgresql://postgres:postgres@localhost:5433/userapidb</code> (ensure DB exists & name matches)</li>
    <li><strong>SECRET_KEY</strong> - create a secure token using something like <code>import secrets;secrets.token_urlsafe(32)</code> - used to encode/decode JWT auth tokens</li>
</ol>

<h2>API Endpoints</h2>
<p>Interactive documentation is available at the live API: <a href="https://userapi-production-8bfe.up.railway.app/docs" target="_blank">https://userapi-production-8bfe.up.railway.app/docs</a></p>

### Authentication
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | /auth/register | Create a new user account | No |
| POST | /auth/login | Login and receive a JWT token | No |
| GET | /auth/me | Get the current authenticated user | Yes |

### Notes
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | /notes | Get all notes for the current user | Yes |
| POST | /notes | Create a new note | Yes |
| GET | /notes/{note_id} | Get a single note by ID | Yes |
| PUT | /notes/{note_id} | Update a note | Yes |
| DELETE | /notes/{note_id} | Delete a note | Yes |

### Health
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | /health | Health check | No |

<h2>Future Improvements</h2>
<ul>
    <li>Search/filter system for notes</li>
    <li>Tagging feature</li>
    <li>File attachments</li>
</ul>