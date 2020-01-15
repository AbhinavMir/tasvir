# tasveer

**Notice:** This project is still under maintainence, I would love your support as I have to dedicate time to a few other projects as of now. The final project will be beautifully integrated into the Python ecosystem with perfect OOPs, Clean Code and the Zen of Python .☺

A Python Package to help you quickly download a few images for testing/validation purposes. It help you to download tons of images!

## Installation

Use the python package manager (pip) to install.

```bash
pip install tasveer
```

## Usage

```python
from tasveer import download
download()
```

Output:

```bash
Enter query: cat
Enter limit count images: 2
Downloading images for: cat ...
Saved at:
downloads/cat/1.grumpy-cat.jpg
downloads/cat/2.1339479807_1GG.jpg
```

## Local develop

```bash
pip install ".[dev]"
```

Lint and auto pep8:

```bash
pyint .
autopep8 -i tasveer
```

Once you are done, you will get a prompt to enter queries and number of downloads to do. After you enter, your downloads will be saved in your current directory under downloads/query_entered.

## Future Work

Feel free to pull. Here's what I plan to work on-

1. Include a lightweight cleaning and processing function

2. Change from prompt to argument

Kindly refer to [issues](https://github.com/AbhinavMir/tasveer/issues) to see list of requested enhancements and easy tasks you could help the community with plus have your own OSS contribution!

If there is any problem you have, want quick answers or want to dicuss with core developers, kindly use the slack channel at <https://tasveer-group.slack.com/>

If you're new to the Open Source community,programming or Python, please message me for any doubts! ^_^

Sincerely,
Abhinav

## License

[MIT](https://choosealicense.com/licenses/mit/)
