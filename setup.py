from setuptools import setup, find_packages

setup(
    name="TxtMagic",
    version="0.1.1",
    author="Pooja V",
    author_email="poojavelm@gmail.com",
    description="A Python package for adding style, emojis, and colors to your text effortlessly! 🎨✨",
    long_description="TxtMagic is a Python package designed to add magic to your text! With TextMagic, you can easily transform your text into colorful, emoji-filled, and stylized formats. ",
    long_description_content_type="text/markdown",
    url="https://github.com/Pooja-Velmurugen",
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',  # Fixed typo here
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.0',
    install_requires=[
        'textblob==0.17.1',
        'nltk==3.8.1',
        'rich==13.7.0'
    ]
)