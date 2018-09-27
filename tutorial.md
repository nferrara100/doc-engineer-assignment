# Implementing Search for Structured HTML in Python

In a basic search all pages on a website are indexed and the page with the closest match is returned first, regardless of where the result was in the page. This is suboptimal as text in headers is probably more relevant than paragraph text, and if the page is long the user would just be dumped at the top of the page, far away from what they actually were looking for at the bottom. This tutorial will explain how to use Algolia to take advantage of the structure of the pages on your website for more relevant results and link directly to the part of the page your users want.

For this tutorial we will use a simple page with the following structure, although you could adjust the parser to accept a different structure more relevant to you.

    <h1><a id="my_first_heading"></a>My First Heading</h1>
    <h2><a id="my_second_heading"></a>My Second Heading</h2>
    <p>The begining of the main content with lots of things the user might search for, like JavaScript.</p>

H1 and h2 might also be used. In this example, if the user searched for JavaScript we would want to link to the second heading since it is more specifically related to that term than the first or the entire page as a whole.

