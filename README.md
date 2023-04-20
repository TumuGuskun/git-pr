# Installation

```bash
pip3 install -r requirements.txt
brew install gum gh
gh auth login
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

It will find any `.md` file in your `.github` folder and use that as a template.

To mark a section as fillable, put a comment after it with `fill=true` in the comment body.

```md
### Description <!-- fill=true -->
```

To set the number of checkboxes you want to select in a list of checkboxes put `limit=n` in a comment block before the list.

```md
<!-- limit=2 -->

-   [ ] [Describe customer-facing change]
-   [ ] Feature flagged: [exampleFlag]
-   [ ] No customer-facing change
```
