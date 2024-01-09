# To install and run:

pip install jupyter

jupyter notebook
(from within the directory the repository is at)

# To set up a virtual environment

- Create a virtual environment 
pipenv shell

- install packages
pipenv install python-dotenv
pipenv install langchain

# Make sure jupyter notebook uses my own virtual environment

- install the ipykernel package
pipenv install ipykernel

- Add the virtual environment to jupyter "--name=myenv" - replace myenv with my own virtual environment
python -m ipykernel install --user --name=QuestionImprover-nzF_yrZm

- restart the notebook

- Change the kernel of the notebook file to my virtual environment kernel, by selecting QuestionImprover-nzF_yrZm from the dropdown menu

# How to work with Jupyter Notebook and VS code:

- Always work from either VS code or Jupyter notebook on the same file, because changes do not get instantly synchronized between the two instances of the same file, as they are opened separately and one needs to be refreshed/restarted in order to reflect the changes made in the other file.