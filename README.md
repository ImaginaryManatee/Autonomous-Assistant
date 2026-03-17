# Autonomous-Assistant
An AI assistant that uses a Retrieval Augmented Generation pipeline to answer questions about a user's personal documents and can perform actions like scheduling a meeting based on the information contained in an email.

#Daily update 03/12
Retrieved necessary background applications and libraries. Need to ensure that the API key is connected to the program. Overall, some errors were caused by the learning curve of beginning my first project on GitHub.

#Daily update 03/13
Happy Friday the 13th! Today has been a day of learning and updating "behind the curtain" requirements to resolve the connection errors from the previous day. This included ensuring that Python was added to the global variables to communicate with PowerShell, as well as updating Execution policies for Scripts to run. I successfully created the VE for the project, and the .gitignore was produced automatically. I ran into some errors invoking Claude, but was able to ensure the connection to the main program and invoke my first request!

#Daily update 03/16
Today has been a fantastic day of development! I have evolved my AI assistant to generate responses based on a user prompt and save the response to a file when directed. Some errors were caused by continued learning of the langchain library. E.g., AgentExecutor had been moved to langchain_classic. Other errors were resolved by pip installing additional packages, which were added to the requirements.txt file. Next steps include creating a RAG pipeline for the assistant, researching additional tools to equip the assistant, and uploading the code to GitHub.

#Daily update 03/17
Happy St. Patrick's Day! Today, I have begun to create the building blocks for the RAG pipeline. I integrated Inngest for durability of execution and to handle background jobs. I chose Docker Desktop as the database to load the PDFs for the AI assistant to review. I encountered errors caused by missing packages and software. However, once the proper programs were installed and added to PATH, I successfully connected to both Inngest and the Docker database. I have begun working in the repository, but my current work is only showing on my GitHub Desktop. Goals for tomorrow are to begin loading PDFs into the database, create a front end, and find a way to connect the local repository files to GitHub's website.
