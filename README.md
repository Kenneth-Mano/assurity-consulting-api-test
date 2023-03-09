# Assurity Consulting Technical Test
<h1>Introduction</h1>
This repository contains my solution for the Assurity Consulting technical test. 

<h2>Description of Technical Test</h2>
The test requires that the API https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false be called and the following assertions tested:

<ul>
<li> The "Name" property returned is "Carbon credits". </li>
<li> The "CanRelist" property is true. </li>
<li> The "Promotions" element which has the "Name" equal to "Gallery" has a "Description"  property that contains the text "Good position in category". </li>
</ul>

<h2>How to Run the Tests</h2>
To run the tests, perform the following steps:

<ol>
<li> Clone the repository using the command `git clone https://github.com/Kenneth-Mano/assurity-consulting-api-test.git`</li>
<li> Run the tests by doing one of the following:</li>
<ul>
<li>Running the command `python solution.py` in command prompt</li>
<li>Opening the solution.py file in Visual Studio Code and pressing F5 to run the file</li>
</ul>
</ol>
