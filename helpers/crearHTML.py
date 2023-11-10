import pandas as pd
from bs4 import BeautifulSoup
def crearTabla(dataframe,nombre):

    archivoHTML=dataframe.to_html()
    rutaArchivo=f"tables/{nombre}.html"

    encabezado=''' 
 
<!DOCTYPE html>
<html lang="en">
	<head>
        <base href="../">
		<meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=0">
        <meta name="description" content="POS - Bootstrap Admin Template">
		<meta name="keywords" content="admin, estimates, bootstrap, business, corporate, creative, invoice, html5, responsive, Projects">
        <meta name="author" content="Dreamguys - Bootstrap Admin Template">
        <meta name="robots" content="noindex, nofollow">
        <title>Dreams Pos admin template</title>
        <link rel="shortcut icon" type="image/x-icon" href="images/ilustracion-diseno-logotipo-arbol-abstracto_43582-134.avif">
        <link rel="stylesheet" href="assets/css/bootstrap.min.css">
		<link rel="stylesheet" href="assets/css/bootstrap-datetimepicker.min.css">
        <link rel="stylesheet" href="assets/css/animate.css">
		<link rel="stylesheet" href="assets/plugins/select2/css/select2.min.css">
		<link rel="stylesheet" href="assets/css/dataTables.bootstrap4.min.css">
		<link rel="stylesheet" href="assets/plugins/fontawesome/css/fontawesome.min.css">
		<link rel="stylesheet" href="assets/plugins/fontawesome/css/all.min.css">
        <link rel="stylesheet" href="assets/css/style.css">
		
	</head>
	
	<body>
		<div id="global-loader" >
			<div class="whirly-loader"> </div>
		</div>
		<div class="main-wrapper">
			<div class="header">
				 <div class="header-left active">
					<a href="index.html" class="logo logo-normal">
						<img src="images/Logo-arbol-singular-COLOR-letras-revista-300px-.png"  alt="">
					</a>
					<a href="index.html" class="logo logo-white">
						<img src="images/Logo-arbol-singular-COLOR-letras-revista-300px-.png"  alt="">
					</a>
					<a href="index.html" class="logo-small">
						<img src="images/ilustracion-diseno-logotipo-arbol-abstracto_43582-134.avif"  alt="" class="img-fluid" style="width: 500px;">
					</a>
					<a id="toggle_btn" href="javascript:void(0);">
						<i data-feather="chevrons-left" class="feather-16"></i>
					</a>
				</div>
				<a id="mobile_btn" class="mobile_btn" href="#sidebar">
					<span class="bar-icon">
						<span></span>
						<span></span>
						<span></span>
					</span>
				</a>
				<ul class="nav user-menu">
					<li class="row">
						<h1>RESERVA ARBOLES COLOMBIA</h1>
					</li>
				</ul>
			</div>
			<div class="sidebar" id="sidebar">
				<div class="sidebar-inner slimscroll">
					<div id="sidebar-menu" class="sidebar-menu">
						<ul>
                            <li class="submenu-open">
								<h6 class="submenu-hdr">DashBoard</h6>
								<ul>
									<li class="active">
										<a href="dashboard.html" ><i data-feather="grid"></i><span>DashBoard</span></a>
									</li>
								</ul>								
							</li>
							<li class="submenu-open">
								<h6 class="submenu-hdr">Importar Datos</h6>
								<ul>
									<li><a href="analizarDatos.html"><i data-feather="minimize-2"></i><span>Importar Datos</span></a></li>
								</ul>
							</li>
                            <li class="submenu-open">
								<h6 class="submenu-hdr">Exportar Datos</h6>
								<ul>
									<li><a href="exportarDatos.html"><i data-feather="shuffle"></i><span>Exportar Datos</span></a></li>
								</ul>
							</li>
							<li class="submenu-open">
								<h6 class="submenu-hdr">Analizar Datos</h6>
								<ul>
									<li><a href="analizarDatos.html"><i data-feather="codepen"></i><span>Analizar Datos</span></a></li>
								</ul>
							</li>
                            <li class="submenu-open">
								<h6 class="submenu-hdr">Lista Arboles</h6>
								<ul>
									<a href="tables/arboles.html" ><i data-feather="grid"></i><span>Lista Arboles</span></a>
								</ul>								
							</li>
						</ul>
					</div>
				</div>
			</div>
			<div class="page-wrapper">
				<div class="content">
					<div class="row">
						<div class="col-lg-6 col-sm-6 col-12">
							<div class="dash-widget">
								<div class="dash-widgetimg">
									<span><img src="assets/img/icons/dash1.svg" alt="img"></span>
								</div>
								<div class="dash-widgetcontent">
									<h5 >$<span class="counters" data-count="307144.00">$307,880.00</span></h5>
									<h6>Total de Dinero Recaudado</h6>
								</div>
							</div>
						</div>
						<div class="col-lg-6 col-sm-6 col-12">
							<div class="dash-widget dash1">
								<div class="dash-widgetimg">
									<span><img src="assets/img/icons/dash2.svg" alt="img"></span>
								</div>
								<div class="dash-widgetcontent">
									<h5 >$<span class="counters" data-count="4385.00">$4,385.00</span></h5>
									<h6>Total Arboles Vendidos</h6>
								</div>
							</div>
						</div>
					</div>

					<div class="card mb-0">
						<div class="card-body">
							<h4 class="card-title">Tipo de Arboles</h4>
							<div class="table-responsive dataview">
		


        '''

    scripts=''' 

             		</div>
						</div>
					</div>
				</div>
			</div>
		</div>
 

             		<!-- jQuery -->
		<script src="assets/js/jquery-3.6.0.min.js"></script>

		<!-- Feather Icon JS -->
		<script src="assets/js/feather.min.js"></script>

		<!-- Slimscroll JS -->
		<script src="assets/js/jquery.slimscroll.min.js"></script>

		<!-- Datatable JS -->
		<script src="assets/js/jquery.dataTables.min.js"></script>
		<script src="assets/js/dataTables.bootstrap4.min.js"></script>
		
		<!-- Bootstrap Core JS -->
		<script src="assets/js/bootstrap.bundle.min.js"></script>

		<!-- Chart JS -->
		<script src="assets/plugins/apexchart/apexcharts.min.js"></script>
		<script src="assets/plugins/apexchart/chart-data.js"></script>
		
		<!-- Custom JS -->
		<script src="assets/js/script.js"></script>
		
  
        
</body>
</html>
  
        '''
    
    sopa=BeautifulSoup(archivoHTML,'html.parser')

    for tr in sopa.find_all('tr'):
        tr.attrs.pop('style',None)

    archivoHTML=str(sopa) 
    archivoHTML=archivoHTML.replace('<table border="1" class="dataframe">','<table class="table table-striped">')

    with open(rutaArchivo,"w") as archivo:
        archivo.write(f"{encabezado}\n{archivoHTML}\n{scripts}")