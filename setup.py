from distutils.core import setup
setup(
  name = 'KarmaFarmer',         # How you named your package folder (MyLib)
  packages = ['KarmaFarmer'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='wtfpl',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Joins and participates in r/KarmaStreet to upvote other users thus creating an upvote "pool". Contains anti-spam solution.',   # Give a short description about your library
  author = 'Dmitri Shevchenko',                   # Type in your name
  author_email = 'dmitri.shevchenko.au@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/CodingCoda/KarmaFarmer',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/CodingCoda/KarmaFarmer/archive/refs/tags/0.1.tar.gz',    # I explain this later on
  keywords = ['reddit', 'karma', 'bot'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
            'datetime',
            'time',
            'math',
            'requests', 
            'praw',
            'random',
            'hashlib',
            'logging',
            'atexit'
      ],

  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3.0',   # Again, pick a license
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',

  ],
)
