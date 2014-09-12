<?php
class SACAsirra {
      var $num;
      var $format;
      var $baseurl;
      var $is_valid = false;
      var $html = '';
      var $form_attr = '';

      public function __construct($baseurl, $num = '')
      {
	$this->num = $num;
	$this->format = 'asirra_ticket=%s';
      	$this->baseurl = $baseurl;
      }

      public function submit($post)
      {
	$data = sprintf($this->format, $post['Asirra_Ticket']);
      	
	$curl = curl_init();
	curl_setopt($curl, CURLOPT_POST, TRUE);
	curl_setopt($curl, CURLOPT_URL, $this->baseurl.'/submit/'.$this->num);
	curl_setopt($curl, CURLOPT_POSTFIELDS, $data);
	curl_setopt($curl, CURLOPT_RETURNTRANSFER, TRUE);
      	
	$ret = curl_exec($curl);
	curl_close($curl);
	
	$ret = json_decode($ret);
      	$this->is_valid = $ret->success;
	$this->html = $ret->html;
	$this->form_attr = $ret->form_attr;
      }
}

?>