from setuptools import setup

setup(
    name="termgpt",
    version="0.1.0",
    description="A command-line interface for ChatGPT.",
    author="Tony Okeke",
    install_requires=["click", "rich", "openai"],
    entry_points={
        "console_scripts": [
            "termgpt=termgpt.termgpt:TermGPT.cli",
        ],
    },
)
