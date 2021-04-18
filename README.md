python script to scrape stuff, rnz &amp; scoop for latest news

<h1 align="center">
  news-scrapper-script
</h1>
<p align="center">
Cron Job on AWS EC2 to populate AWS MySQL RDS instance to support <a href="https://daily-roundup.netlify.app/">daily-roundup.netlify.app</a> website
</p>
<h2>Purpose</h2>
<p>
Purpose of this api is to scrape the latest headlines from stuff, RadioNZ & Scoop and store it in a AWS RDS instance so that it can be served for <a href="https://github.com/rykumar13/react-news-website">
react-news-website</a>
</p>
<br>
<h2> How it works</h2>
<p align="center">
  <ul>
  <li>Python script created using beautifulsoup4 that scrapes data from stuff, radioNZ & scoop</li>
  <li>AWS RDS instance is created to store all this data. mysql.connector library is used for this</li>
  <li>A Cron Job is setup on an AWS EC2 instance to scrap these websites every 15 mins and populate the DB</li>
  </ul>
  <br>
  <h2> Architecture Diagram</h2>
  <p>
  <img alt="diagram" src="https://raw.githubusercontent.com/rykumar13/react-news-website/4f574629a632a87e3cc2d86c6d9c21c73ccb330b/diagrams/diagram.svg" />
    <p>
</p>
<br>
<h2>
Technologies & Libraries used 🚀
  </h2>
  <p> 
    <ul>
     <li>React</li>
     <li>AWS RDS</li>
     <li>AWS EC2</li>
     <li>Flask API</li>
     <li>Zappa Library</li>
     <li>mysql.connector library</li>
    </ul>
  </p>
<h2>
  <br>
