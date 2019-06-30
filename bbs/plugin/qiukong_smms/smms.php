<?php
!defined('DEBUG') AND exit('Access Denied.');
?>
<style>
#smms_list{margin:2px 0 !important;font-size:14px !important;}
.smms_pic{margin:2px;width:120px;max-width:48%;height:90px;display:inline-block;background-position:center;background-size:cover;background-repeat:no-repeat;}
.smms_act{padding-top:35px;width:100%;height:90px;background:rgba(0,0,0,0.2);text-align:center;}
.smms_act a{display:inline-block;color:#FFF;font-weight:bold;text-shadow:1px 1px 3px #000;text-decoration:none;vertical-align:top;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}
.smms_pn{max-width:70%;}
</style>
<input type="file" onchange="smms_cpick()" id="smms_pick" multiple="multiple" accept="image/jpeg,image/png,image/gif" />
<input type="button" onclick="smms_cpush()" id="smms_push" value="开始" />
<input type="button" onclick="smms_cpall()" value="插入" />
<div id="smms_list"></div>
<script>
function smms_cpave(html){
if(typeof(KindEditor)!='undefined'){KindEditor.insertHtml('#message',html);}
else if(typeof(UE)!='undefined'){UE.getEditor('message').execCommand('insertHtml',html);}
else if(typeof(UM)!='undefined'){UM.getEditor('message').execCommand('insertHtml',html);}
else{var msg=document.getElementById('message');if(document.selection){this.focus();var sel=document.selection.createRange();sel.text=html;this.focus();}else if(msg.selectionStart||msg.selectionStart=='0'){var startPos=msg.selectionStart;var endPos=msg.selectionEnd;var scrollTop=msg.scrollTop;msg.value=msg.value.substring(0,startPos)+html+msg.value.substring(endPos, msg.value.length);this.focus();msg.selectionStart=startPos+html.length;msg.selectionEnd=startPos+html.length;msg.scrollTop=scrollTop;}else{this.value+=html;this.focus();};};
};
function smms_cpick(){
if(!document.getElementById('smms_pick').files.length){return;};
smms_pool=[];smms_item=[];Array.prototype.push.apply(smms_pool,document.getElementById('smms_pick').files);
document.getElementById('smms_list').innerHTML='';
for(var numb=0;numb<smms_pool.length;numb++){
document.getElementById('smms_list').innerHTML+='<div class="smms_pic" name="pending" task="'+numb+'" style="background-image:url('+URL.createObjectURL(document.getElementById('smms_pick').files[numb])+');"><div class="smms_act"><a class="smms_pn">'+smms_pool[numb].name+'...</a>&nbsp;<a href="javascript:;" onclick="smms_cpdis(this);">(&#x274C;&#xFE0E;)</a></div></div>';
};
};
function smms_cpush(){
var item=document.getElementsByName('pending');
if(!item.length){smms_cstop(null);return;};
document.getElementById('smms_push').setAttribute('onclick','');
document.getElementById('smms_push').value='停止';
var myfd=new FormData();myfd.append('smfile',smms_pool[item[0].getAttribute('task')]);
var ajax=$.ajax({url:'https://sm.ms/api/upload',type:'POST',processData:false,contentType:false,data:myfd,success:function(res){
switch(res.code){
case 'success':smms_item[item[0].getAttribute('task')]=res.data;item[0].innerHTML='<div class="smms_act"><a href="javascript:;" onclick="smms_cpone(this);">上传成功</a>&nbsp;<a href="javascript:;" onclick="smms_cpdel(this);">(&#x274C;&#xFE0E;)</a></div>';item[0].removeAttribute('name');smms_cpush();break;
case 'error':alert(res.msg);smms_cstop(ajax);break;
default:alert('未知错误');smms_cstop(ajax);break;
};
}});
document.getElementById('smms_push').onclick=function(){if(!document.getElementById('smms_push').getAttribute('onclick')){smms_cstop(ajax);}};
};
function smms_cstop(ajax){
if(ajax){ajax.abort();};
document.getElementById('smms_push').setAttribute('onclick','smms_cpush();');
document.getElementById('smms_push').value='开始';
alert('任务结束');
};
function smms_cpdel(node){
if(confirm('删除远程图片？')){
var item=node.parentNode.parentNode;
$.get(smms_item[item.getAttribute('task')].delete+'?ajax=1',function(res){
if(res.code=='success'){
delete smms_item[item.getAttribute('task')];
item.parentNode.removeChild(item);
}
else{alert('删除失败');};
});
};
};
function smms_cpdis(node){
if(confirm('删除队列图片？')){
var item=node.parentNode.parentNode;
delete smms_item[item.getAttribute('task')];
item.parentNode.removeChild(item);
};
};
function smms_cpone(node){
var item=node.parentNode.parentNode;
if(!smms_item.length){return;};
smms_cpave('<a href="'+smms_item[item.getAttribute('task')].url+'" target="_blank"><img src="'+smms_item[item.getAttribute('task')].url+'" alt="'+smms_item[item.getAttribute('task')].filename+'" /></a>');
};
function smms_cpall(){
if(!smms_item.length || !confirm('插入全部图片？')){return;};
for(var numb=0;numb<smms_item.length;numb++){if(smms_item[numb]){smms_html+='<a href="'+smms_item[numb].url+'" target="_blank"><img src="'+smms_item[numb].url+'" alt="'+smms_item[numb].filename+'" /></a><br />';};};
smms_cpave(smms_html);smms_html='';
};
var smms_pool=[],smms_item=[],smms_html='';
</script>