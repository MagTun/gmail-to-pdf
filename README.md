# gmail-to-pdf-mac

## Description

This script will connect to your Gmail account and download as .eml files all your email from a specified label. Then you can convert the .eml files to pdf with this [open source program](https://github.com/nickrussler/eml-to-pdf-convert). I forked this project from [here](https://github.com/MagTun/gmail-to-pdf) and updated it to work on a mac.

## Dependencies

- JAVA 8
- `wkhtmltopdf` (If you have Homebrew installed run: `brew  install wkhtmltopdf`)
- Python 3

## Installation and setting up

1. Setup Gmail API Key [(Documentation)](https://developers.google.com/gmail/api/quickstart/python)

    a. [Create a Google Cloud project](https://developers.google.com/workspace/guides/create-project)
    
    b. [Enable Google Workspace APIs](https://developers.google.com/workspace/guides/enable-apis)

    c. [Create credentials - OAuth client ID](https://developers.google.com/workspace/guides/create-credentials)

    

2. Clone the repo
   ```sh
   git clone https://github.com/shuhang-cai/gmail-to-pdf-mac.git
   ```
3. Download OAuth json from 1c, rename json file to `credentials.json` and save this file in the root folder of these scripts. 

4. Run the script `1 get labels ids.py`. You will be sent to a consent screen: choose your Gmail account where you want to download your email and accept the credential (this will save a token file so that the next time, you don't have to go through this consent screen).
   


## Usage

Because GMAIL API doesn't use the labels' names but the labels' IDs, you need to first get all the labels' IDs with the script `1 get labels ids.py` (E.g.: `Label_4186509458417029489`)

Edit the following variables in `2 download email as eml files.py`:

* `labelid`
* `eml_folder_name`

Run `2 download email as eml files.py`: your emails will be save as `.eml` file in a subfolder `eml_folder_name`

Open the program eml-to-pdf-converter (you will need Java installed)
```sh
java -jar emailconverter-2.5.3-all.jar -gui = true
```

You should see something like this:

<img src="https://www.whitebyte.info/wp-content/uploads/2015/02/scr1.png" />



Select your folder to convert the .eml files to .pdf files.


Run `4 process files.py`, if you want to:

* Copy only last emails of a thread
* Get path of emails with date problem (added zzz in filename)
* Delete all `.eml`
* Split `.eml` and `.pdf` files into their own subdirectories

Different configurations of folder/filename can be found in `5 alternatives.py` (You can use this instead of `2 download email as eml files.py` ― the different part need to be uncommented)

* folder = subject / filename = date
* folder = threadID / filename = emailID
* no folder / filename = date (converted into " 2017_02_04") + subject

## Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

I'm not really a developer so I don't really know how I can improve the code. Maybe I'll refactor it to accept user inputs instead of hard coding in the script when I have some free time.


## License
[MIT](https://choosealicense.com/licenses/mit/)


## Contact

[LinkedIn](https://www.linkedin.com/in/cai-shuhang) 

Project Link: [https://github.com/shuhang-cai/gmail-to-pdf-mac.git](https://github.com/shuhang-cai/gmail-to-pdf-mac.git)

## Acknowledgments

* Original code was written by [MagTun](https://github.com/MagTun/gmail-to-pdf). 
* [nickrussler](https://github.com/nickrussler/eml-to-pdf-convert)
