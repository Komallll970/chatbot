<h1 align="center">🤖 Streaming AI Chatbot</h1>

<p align="center">
<b>An Interactive AI Chatbot powered by Mistral-7B (Hugging Face API) & Streamlit</b><br>
<i>Real-time conversational AI with simulated streaming responses</i>
</p>

<hr>

<h2>📌 Project Overview</h2>

<p>
The <b>Streaming AI Chatbot</b> is a web-based conversational AI application built using 
<b>Streamlit</b>, <b>LangChain</b>, and <b>Hugging Face's Mistral-7B-Instruct Model</b>.
</p>

<p>
This chatbot delivers intelligent, context-aware responses while maintaining chat history 
and simulating real-time streaming for a smooth and engaging user experience.
</p>

<hr>

<h2>🚀 Features</h2>

<ul>
<li>💬 <b>Interactive Chat Interface</b> using Streamlit</li>
<li>🧠 <b>Mistral-7B-Instruct Model</b> via Hugging Face Endpoint</li>
<li>⚡ <b>Simulated Streaming Response</b> (word-by-word output)</li>
<li>📜 <b>Session-based Chat History</b></li>
<li>🔐 <b>Environment Variable Support</b> using <code>.env</code></li>
<li>🎯 Clean and minimal UI design</li>
</ul>

<hr>

<h2>🛠️ Tech Stack</h2>

<ul>
<li><b>Frontend:</b> Streamlit</li>
<li><b>LLM Framework:</b> LangChain</li>
<li><b>Model Provider:</b> Hugging Face API</li>
<li><b>Model Used:</b> mistralai/Mistral-7B-Instruct-v0.2</li>
<li><b>Environment Management:</b> python-dotenv</li>
</ul>

<hr>



<h2>⚙️ Installation & Setup</h2>

<h3>1️⃣ Clone the Repository</h3>

<pre>
git clone https://github.com/your-username/streaming-ai-chatbot.git
cd streaming-ai-chatbot
</pre>

<h3>2️⃣ Install Dependencies</h3>

<pre>
pip install -r requirements.txt
</pre>

<h3>3️⃣ Add Hugging Face API Key</h3>

<p>Create a <code>.env</code> file in the root directory:</p>

<pre>
HUGGINGFACEHUB_API_TOKEN=your_api_key_here
</pre>

<h3>4️⃣ Run the Application</h3>

<pre>
streamlit run app.py
</pre>

<hr>

<h2>🧠 How It Works</h2>

<ul>
<li>The user enters a prompt via Streamlit chat input.</li>
<li>Messages are stored in <b>Streamlit session state</b>.</li>
<li>LangChain sends the full conversation to the <b>Mistral-7B model</b>.</li>
<li>The response is generated and streamed word-by-word.</li>
<li>Chat history persists throughout the session.</li>
</ul>

<hr>

<h2>📸 UI Preview</h2>

<p>
<i>Minimalistic chat interface with streaming cursor effect (▌)</i>
</p>

<hr>

<h2>🎯 Future Improvements</h2>

<ul>
<li>🔄 Real-time token streaming instead of simulated streaming</li>
<li>💾 Persistent database-based chat history</li>
<li>🎨 Enhanced UI styling with custom CSS</li>
<li>🧠 Multi-model selection support</li>
<li>🌍 Deployment on Streamlit Cloud / Hugging Face Spaces</li>
</ul>

<hr>

<h2>🤝 Contributing</h2>

<p>
Contributions, issues, and feature requests are welcome!<br>
Feel free to fork this repository and submit a pull request.
</p>

<hr>

<h2>📜 License</h2>

<p>
This project is open-source and available under the <b>MIT License</b>.
</p>

<hr>

<p align="center">
<b>⭐ If you like this project, consider giving it a star!</b><br>
<i>Built with ❤️ using AI & Python</i>
</p>
