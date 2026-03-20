<h2>📊 Database Q&A System (Retail T-Shirt Store)</h2>

An AI-powered Question Answering system that allows users to query a MySQL database using natural language. The system
converts user questions into SQL queries, executes them, and returns clean, human-readable answers.

<h4>🚀 Features</h4>
<ul>
    <li>🔍 Ask questions in plain English</li>
    <li>🧠 Uses LLM to generate SQL queries automatically</li>
    <li>🗄️ Connects to MySQL database</li>
    <li>📊 Retrieves accurate data from database</li>
    <li>🎯 Displays only the final answer (no SQL clutter)</li>
    <li>⚡ Streamlit-based interactive UI</li>
</ul>

<h4>🛠️ Tech Stack</h4>
<ul>
    <li>Python</li>
    <li>LangChain</li>
    <li>OpenRouter (LLM API)</li>
    <li>MySQL</li>
    <li>HuggingFace Embeddings</li>
    <li>ChromaDB (Vector Store)</li>
    <li>Streamlit</li>
</ul>

<h4>📁 Project Structure</h4>

├── main.py # Streamlit UI <br>
├── langchain_helper.py # LLM + DB chain logic <br>
├── few_shots.py # Few-shot examples <br>
├── key.py # Database credentials <br>
├── .env # API keys <br>
├── requirements.txt # Dependencies <br>

<h4>⚙️ Setup Instructions</h4>

<h4>1️⃣ Clone the Repository </h4>
git clone (your-repo-link) <br>
cd (your-project-folder)<br>

<h4>2️⃣ Install Dependencies</h4>
pip install -r requirements.txt
<br>

<h4>3️⃣ Setup Environment Variables</h4>
Create a .env file: <br>
OPENROUTER_API_KEY=your_api_key_here


<h4>4️⃣ Configure Database</h4>
<ol>
    <li>Update key.py: </li>
    sql_pass = "your_mysql_password" <br><br>
    <li>Make sure your MySQL database: </li>
    <ul>
        <li>is running</li>
        <li>contains the atliq_tshirts dataset</li>
    </ul>
</ol>

<h4>5️⃣ Run the Application </h4>
<ul>In terminal-  
    <li>streamlit run main.py</li>
</ul>

<h4>💡 Example Questions </h4>

<ul style="list-style: circle;">
    <li>How many white Adidas t-shirts are in stock?</li>
    <li>What is the total stock of Nike products?</li>
    <li>Which brand has the highest inventory?</li>
</ul>

<h4>🔄 How It Works</h4>
<ol>
    <li>User enters a question</li>
    <li>LLM converts it → SQL query</li>
    <li>Query runs on MySQL database</li>
    <li>Result is processed</li>
    <li>Only final answer is displayed</li>
</ol>

<h4>⚠️ Challenges Faced </h4>
<ul>
    <li>Handling incorrect SQL generation</li>
    <li>Cleaning LLM output (removing SQLQuery, SQLResult)</li>
    <li>Ensuring only final answer is shown</li>
    <li>Managing prompt engineering effectively</li>
</ul>

<h4>🔥 Future Improvements</h4>

✅ Chat-style UI (like ChatGPT) <br>

✅ Error handling for invalid queries <br>

✅ Query history <br>

✅ Multi-database support <br>

✅ Authentication system <br>

<h4>👩‍💻 Author</h4>

<b>Sakshi Dethe</b>

<h4>⭐ If you like this project</h4>

Give it a ⭐ on GitHub and share it!
