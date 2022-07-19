# Web Scraping Behind A Login

## Using requests session object:

- For both methods of logging in the first thing needed is the name of the fields used to login and the url the login post data to. 
This can be found using the inspect tool and finding the name of the login input fields.
<img width="1410" alt="Screen Shot 2022-07-19 at 18 23 12" src="https://user-images.githubusercontent.com/13583303/179859862-65bddcb9-731a-4b9d-84cb-c76739303486.png">


- Another option is to open the nextwork tab within inspect and select preserve log before logging in. Once logged in, find the login request to view the request headers and payload parameters.

![image](https://user-images.githubusercontent.com/13583303/179860059-91d2b049-3737-42fc-878f-8b0aed789b59.png)


- A simple requests module POST method will only work for single instances, as it doesn't save cookies. 
A requests [session](https://requests.readthedocs.io/en/latest/user/advanced/#session-objects) object is need to persist cookies and other parameters, keeping an account logged in. 

- Create a dictionary with the input field names and username/password and pass this data into the post request. 
  Once the post request is sent, you should be able to make GET requests to other URL's as logged in. 

- Authentication/csrf tokens might be required. It's possible to find hidden in the login page html of some websites, but I didn't have much luck for many sites. If you do find them, you can send an initial GET request to the login page and use Beautiful soup to parse/collect the token value. 

#### Packages: 
- bs4 

## Using Selenium WebDriver

- [Selenium WebDriver](https://selenium-python.readthedocs.io/getting-started.html) is a tool for automated web application testing. It provides a way to interact with multiple elements on a web page and is another option for getting past logins. 

- The webdriver is pretty straight forward. Once you know the html element ID names, you can instruct the driver insert the username/passwords into the input fields. Then you can instruct the driver to click on a submit button via an element name or its XPath. 

- I used [WebDriver Manager](https://pypi.org/project/webdriver-manager/) package to save time since it sets driver binaries without having to actually download them. 

- There is the option of running the driver headless, that is, without a GUI which can save resources and time. It is commented out in the script.

![Screen Recording 2022-07-19 at 17 32 57 (1)](https://user-images.githubusercontent.com/13583303/179855987-f6a3e839-20c8-4727-9151-fe90f0835198.gif)
*Example of Selenium logging into HackerRank*

#### Packages: 
- selenium
- webdriver_manager
