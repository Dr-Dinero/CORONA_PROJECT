from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)



@app.route("/")
def hello():
    return '''<!DOCTYPE HTML>
<html>
	<head>
		<title>CORONA PROJECT</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1"/>
		<link rel="stylesheet"  href= 'static/css/main.css'>
	</head>
	<body>

		<!-- Header -->
			<header id="header" class="alt">
				<div class="logo"><a href="index.html">DO NOT FEAR <span>by JOHN,MATHEW,ISAIAS</span></a></div>
				<a href="#menu">Menu</a>
			</header>

		<!-- Nav -->
			<nav id="menu">
				<ul class="links">
					<li><a href="index.html">Home</a></li>
					<li><a href="generic.html">Generic</a></li>
					<li><a href="elements.html">Elements</a></li>
				</ul>
			</nav>

		<!-- Banner -->
			<section class="banner full">
				<article>
					<div class="inner">
						<header>
							<p>Life has been crazy but #'s only tell half the story <a href="https://templated.co">Glory to Jesus Christ</a></p>
							<h2>WE CAME FOR IT ALL</h2>
						</header>
					</div>
				</article>
				<article>
					<img src="images/slide02.jpg" alt="" />
					<div class="inner">
						<header>
							<p>Data in live Time</p>
							<h2>Designing Best We can</h2>
						</header>
					</div>
				</article>
				<article>
					<img src="images/slide03.jpg"  alt="" />
					<div class="inner">
						<header>
							<p>OVERVIEW OF LANDING PAGE</p>
							<h2>For the best outcome</h2>
						</header>
					</div>
				</article>
				<article>
					<img src="images/slide04.jpg"  alt="" />
					<div class="inner">
						<header>
							<p>There will be great earthquakes, famines and pestilences in various places, and fearful events and great signs from heaven.</p>
							<h2>Luke 21:11</h2>
						</header>
					</div>
				</article>
				<article>
					<img src="images/slide05.jpg"  alt="" />
					<div class="inner">
						<header>
							<p>These Times have been mentioned of old</p>
							<h2>Let us Seek the Lord</h2>
						</header>
					</div>
				</article>
			</section>

		<!-- One -->
			<section id="one" class="wrapper style2">
				<div class="inner">
					<div class="grid-style">

						<div>
							<div class="box">
								<div class="image fit">
									<img src="images/pic02.jpg" alt="" />
								</div>
								<div class="content">
									<header class="align-center">
										<p>Data intervention</p>
										<h2>Understanding</h2>
									</header>
									<p>Our Project was on the relation of information collected by diffrent states on there coronavirus updates</p>
									<footer class="align-center">
										<a href="#" class="button alt">Learn More</a>
									</footer>
								</div>
							</div>
						</div>

						<div>
							<div class="box">
								<div class="image fit">
									<img src="images/pic03.jpg" alt="" />
								</div>
								<div class="content">
									<header class="align-center">
										<p>Information on the left </p>
										<h2>John Hopkins Statistics</h2>
									</header>
									<p>Intaking information from diffrent Json files</p>
									<footer class="align-center">
										<a href="#" class="button alt">Learn More</a>
									</footer>
								</div>
							</div>
						</div>

					</div>
				</div>
			</section>

		<!-- Two -->
			<section id="two" class="wrapper style3">
				<div class="inner">
					<header class="align-center">
						<p>Corona Statistics</p>
						<h2>Imported information</h2>
					</header>
				</div>
			</section>

		<!-- Three -->
			<section id="three" class="wrapper style2">
				<div class="inner">
					<header class="align-center">
						<p class="special">Corona Virus Data</p>
						<h2>Corona Virus</h2>
					</header>
					<div class="gallery">
						<div>
							<div class="image fit">
						    <iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plotly.com/~Facilitator/9/#/" height="525" width="100%"></iframe>
							</div>
						</div>
						<div>
							<div class="image fit">
							</div>
						</div>
						<div>
							<div class="image fit">
							<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plotly.com/~Facilitator/12/" height="525" width="100%"></iframe>
							</div>
						</div>
						<div>
							<div class="image fit">
							</div>
						</div>
					</div>
				</div>
			</section>


		<!-- Footer -->
			<footer id="footer">
				<div class="container">
					<ul class="icons">
						<li><a href="#" class="icon fa-twitter"><span class="label">Twitter</span></a></li>
						<li><a href="#" class="icon fa-facebook"><span class="label">Facebook</span></a></li>
						<li><a href="#" class="icon fa-instagram"><span class="label">Instagram</span></a></li>
						<li><a href="#" class="icon fa-envelope-o"><span class="label">Email</span></a></li>
					</ul>
				</div>
				<div class="copyright">
					&copy; Jesus Boys
				</div>
			</footer>

		<!-- Scripts -->
			<script src="assets/js/jquery.min.js"></script>
			<script src="assets/js/jquery.scrollex.min.js"></script>
			<script src="assets/js/skel.min.js"></script>
			<script src="assets/js/util.js"></script>
			<script src="assets/js/main.js"></script>

	</body>
</html>'''