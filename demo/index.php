<?php
	require_once("sac_library/sac.php");

	$media = 'blog';
	if(isset($_GET['media']))
	   $media = $_GET['media'];


	$sac = new SAC();

	if(!isset($_POST['sac_num']))
	{
		try {
		    $captcha = $sac->getCaptcha($media);
		}
		catch (Exception $e){
		      	die("Exception: ".$e->getMessage());
		}
	}
	else
	{
	   $first_name = '';
	   $last_name = '';
	   if (isset($_POST['firstname']) && isset($_POST['lastname']) && $_POST['firstname'] != '' && $_POST['lastname'] != '')
	   {
	      $first_name = $_POST['firstname'];
	      $last_name = $_POST['lastname'];
	   }
	   try{
		$captcha = $sac->submitCaptcha($_POST);
	   }
	   catch (Exception $e){
	     	die("Exception: ".$e->getMessage());
	   }
	}

	if ($captcha->is_valid)
	   include 'templates/success.html';
	else
	   include 'templates/index.html';
?>