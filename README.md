<h1 align="center">DocAI</h1>
<h3 align="center">A documentation assistant made for MLH Hack at Home II</h3>
<p align="center">
<img src="https://user-images.githubusercontent.com/54677274/116788609-92c34400-aa78-11eb-93e3-e49d4aae68f4.png" alt="drawing" align="center" width="200" height="200"/>
</p>

### How to get it running:

First, clone the repository:

`git clone https://github.com/MintStudios/DocAI.git`

Install the required packages:

`pip install -r src/requirements.txt`

Run the main file:

`python3 src/main.py`

Now you're all set. Doc is semi-dormant at this time, and only activates when she hears her name. After that, she's at your service!

Example:
(Assuming Doc is running)

Say: `Hey Doc`

Doc: `Doc here!`

Say: `Search up the python documentation for boolean.`

Doc: `Pulling up boolean in the python documentation.`

### Troubleshooting
#### Doc doesn't understand me. What should I do?
Make sure you're pronunciating the language and the term you want to look up correctly. If that doesn't work, ambient noise might be the problem. Move to a quiet location.

#### This term isn't on Doc's vocabulary list. What should I do?
You can contribute and add your own terms! Visit /src/terms.json and see how I've listed the terms with possible pronunciations.

#### My favourite language isn't on here. How could you...?
Well, there are about 700 programming languages (according to Wikipedia) and I can't include them all. I've put down some of them. Create a github issue with the name of the programming language and I'll add it to the list.
