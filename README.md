# Installation

```bash
pip3 install -r requirements.txt
```

Put this repo in your path

```bash
# from the root folder of the repo
echo "export PATH=\$PATH:$(pwd)" >> ~/.zshrc # or ~/.bashrc
```

# Usage

In any github repo

```bash
git pr
```

If you have pr template files in your `.github` folder it should find them and use them.
Currently this fills out checkboxes and any section headed by `Description`.
