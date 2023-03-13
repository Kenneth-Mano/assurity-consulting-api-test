# Assurity Consulting Technical Test
<h1>Introduction</h1>
This repository contains my solution for the Assurity Consulting technical test. 

<h2>Description of Technical Test</h2>
The test requires that the API <a href="https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false">https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false</a> be called and the following assertions tested:

<ul>
<li> The "Name" property returned is "Carbon credits". </li>
<li> The "CanRelist" property is true. </li>
<li> The "Promotions" element which has the "Name" equal to "Gallery" has a "Description"  property that contains the text "Good position in category". </li>
</ul>

<h2>How to Run the Tests</h2>
To run the tests, perform the following steps:

<ol>
<li> Clone the repository using the command <code>git clone https://github.com/Kenneth-Mano/assurity-consulting-api-test.git</code></li>
<li> Run the tests by doing one of the following:</li>
<ul>
<li>Running the command <code>python solution.py</code> in command prompt. <a href="#section1">[1]</a></li>
<li>Opening the solution.py file in Visual Studio Code and pressing F5 to run the file. <a href="#section1">[2]</a></li>
</ul>
</ol>
<p id="section1">[1] If the <code>python</code> command does not work in your command prompt, try following these <a href="https://www.dataquest.io/blog/installing-python-on-windows/#:~:text=To%20do%20so%2C%20open%20the,and%20type%20there%20python%20%2DV%20.">steps</a> to install and set up your python environment.</p>
<p id="section1">[2] Other IDEs can be used too, but the steps and requirements for running Python files in those will be different. Please refer to the specific documentation for the IDE that is being used.</p>