# conda create -n python-12 python=3.12

# conda env export > environment.yml

# conda env create -f environment.yml

# streamlit langchain langchain_community langchain_ollama langchain_groq faiss-cpu pdfplumber 



Usage:
  ollama [flags]
  ollama [command]

Available Commands:
  serve       Start ollama
  create      Create a model from a Modelfile
  show        Show information for a model
  run         Run a model
  stop        Stop a running model
  pull        Pull a model from a registry
  push        Push a model to a registry
  list        List models
  ps          List running models
  cp          Copy a model
  rm          Remove a model
  help        Help about any command

Flags:
  -h, --help      help for ollama
  -v, --version   Show version information