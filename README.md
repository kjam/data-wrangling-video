## Data Wrangling with Python (video edition)

Welcome to the code repository for [Data Wrangling with Python]()! If you have any questions reach out to @kjam on Twitter or GitHub.

### Code Structure

Most of the code covered in the videos is here; but not all of it. I highly recommend you take time to type out all the code along with the videos and simply use these scripts to "double check" or remind yourself of the work you've already completed.

### Data folder

Although I don't recommend keeping your data in a repository, I've done so here for the purpose of our shared use. In the data directory you'll find all of the examples used for the video series. You'll also find a copy of some example API responses and web pages in case these change after the video is available. If you find one of the scripts handling API or web data doesn't work, you can use the files here by accessing them via the File URI (normally file://file_name.html ).

### Installation

If you are using Python2, use the requirements.txt file. If you are using Python3, use the py3_requirements.txt file. 

```pip install -r requirements.txt```

or 

```pip install -r py3_requirements.txt```

### Python2 v. Python3

This repository is primarily compliant for both versions. There is a problem with PDFMiner and pdf_tables being non-Python3 compliant. I have begun some investigation into their portability, but my current advice is, if you are using Python3, simply switch to Python2 for just your PDF wrangling, export that into a form you can read (like a database or file) and then switch back. :)

### Corrections?

If you find any issues in these code examples, feel free to submit an Issue or Pull Request. I appreciate your input!

### Questions?

Reach out to @kjam on Twitter or GitHub. @kjam is also often on freenode. :)
