<?php

!defined('DEBUG') AND exit('Access Denied.');

$action = param(1);

user_login_check();



if($action == 'create') {
	
	$tid = param(2);
	$quick = param(3);
	$quotepid = param(4);
		
	$thread = thread_read($tid);
	empty($thread) AND message(-1, lang('thread_not_exists'));
	
	$fid = $thread['fid'];
	
	$forum = forum_read($fid);
	empty($forum) AND message(-1, lang('forum_not_exists'));
	
	$r = forum_access_user($fid, $gid, 'allowpost');
	if(!$r) {
		message(-1, lang('user_group_insufficient_privilege'));
	}
	
	($thread['closed'] && ($gid == 0 || $gid > 5)) AND message(-1, lang('thread_has_already_closed'));
	
	
		// todo:
		$tagids = tag_thread_find_tagid_by_tid($tid, $forum['tagcatelist']);

	
	if($method == 'GET') {
		
		
		
		$header['title'] = lang('post_create');
		$header['mobile_title'] = lang('post_create');
		$header['mobile_link'] = url("thread-$tid");

		include _include(APP_PATH.'view/htm/post.htm');
		
	} else {
		
		
		
		$message = param('message', '', FALSE);
		empty($message) AND message('message', lang('please_input_message'));
		
		$doctype = param('doctype', 0);
		xn_strlen($message) > 2028000 AND message('message', lang('message_too_long'));
		
		$thread['top'] > 0 AND thread_top_cache_delete();
		
		$quotepid = param('quotepid', 0);
		$quotepost = post__read($quotepid);
		(!$quotepost || $quotepost['tid'] != $tid) AND $quotepid = 0;
		
		$post = array(
			'tid'=>$tid,
			'uid'=>$uid,
			'create_date'=>$time,
			'userip'=>$longip,
			'isfirst'=>0,
			'doctype'=>$doctype,
			'quotepid'=>$quotepid,
			'message'=>$message,
		);
		$pid = post_create($post, $fid, $gid);
		empty($pid) AND message(-1, lang('create_post_failed'));
		
		// thread_top_create($fid, $tid);

		$post = post_read($pid);
		$post['floor'] = $thread['posts'] + 2;
		$postlist = array($post);
		
		$allowpost = forum_access_user($fid, $gid, 'allowpost');
		$allowupdate = forum_access_mod($fid, $gid, 'allowupdate');
		$allowdelete = forum_access_mod($fid, $gid, 'allowdelete');
		
		

if (isset($haya_post_info_config['at_user_to_notice']) 
	&& $haya_post_info_config['at_user_to_notice'] == 1
) { 

	if (function_exists("notice_send")) {
		$haya_post_info_pagesize = $conf['postlist_pagesize'];
		$haya_post_info_page = ceil(($thread['posts'] + 1) / $haya_post_info_pagesize);
		$haya_post_info_page = max(1, $haya_post_info_page);
		
		$notice_thread_subject = $thread['subject'];
		$notice_thread_substr_subject = notice_substr($thread['subject'], 20);
		$notice_thread_url = url('thread-'.$thread['tid']);
		$notice_thread = '<a target="_blank" href="'.$notice_thread_url.'">《'.$notice_thread_subject.'》</a>';
		
		$notice_post_message = $post['message'];
		$notice_post_substr_message = notice_substr($post['message'], 40, FALSE);
		$notice_post_url = url('thread-'.$thread['tid'].'-'.$haya_post_info_page).'#'.$post['pid'];
		
		$notice_user_url = url('user-'.$user['uid']);
		$notice_user_avatar_url = $user['avatar_url'];
		$notice_user_username = $user['username'];
		$notice_user = '<a href="'.$notice_user_url.'" target="_blank"><img class="avatar-1" src="'.$notice_user_avatar_url.'"> '.$notice_user_username.'</a>';
		
		$notice_msg_tpl = '<div class="comment-info">在主题 <a target="_blank" href="{thread_url}" title="{thread_subject}">《{thread_substr_subject}》</a> 的回复中提到了你：</div> '
			.'<div class="single-comment pt-1"><a target="_blank" href="{post_url}">{post_substr_message}</a></div>';
		$notice_msg = str_replace(
			array(
				'{thread_subject}', '{thread_substr_subject}', '{thread_url}', '{thread}', 
				'{post_message}', '{post_substr_message}', '{post_url}', 
				'{user_url}', '{user_avatar_url}', '{user_username}', '{user}'
			),
			array(
				$notice_thread_subject, $notice_thread_substr_subject, $notice_thread_url, $notice_thread, 
				$notice_post_message, $notice_post_substr_message, $notice_post_url,  
				$notice_user_url, $notice_user_avatar_url, $notice_user_username, $notice_user
			),
			$notice_msg_tpl
		);
	}

	preg_match_all('/@([^\s|\/|:|@]+)/', $post['message_fmt'], $haya_post_info_usernames_fmt);
	preg_match_all('/@([^\s|\/|:|@]+)/', $post['message'], $haya_post_info_usernames);
	$haya_post_info_usernames_count = count($haya_post_info_usernames[1]);
	if ($haya_post_info_usernames_count > 0) {
		for ($i = 0; $i < $haya_post_info_usernames_count; $i++) {
			$haya_post_info_username = trim($haya_post_info_usernames[1][$i]);
			$haya_post_info_user = haya_post_info_user_read_by_username($haya_post_info_username);
			if (!$haya_post_info_user || empty($haya_post_info_user['uid'])) {
				continue;
			}
			
			$post['message_fmt'] = str_replace($haya_post_info_usernames_fmt[0][$i], '<a href="' . url('user-' . $haya_post_info_user['uid']) . '" target="_blank" class="haya-post-info-at"><em>@' . $haya_post_info_user['username'] . '</em></a>', $post['message_fmt']);
			$post['message'] = str_replace($haya_post_info_usernames[0][$i], '<a href="' . url('user-' . $haya_post_info_user['uid']) . '" target="_blank" class="haya-post-info-at"><em>@' . $haya_post_info_user['username'] . '</em></a>', $post['message']);
			
			if (function_exists("notice_send")) {				
				notice_send($user['uid'], $haya_post_info_user['uid'], $notice_msg, 156);
			}
		}
	}
	
	post__update($pid, array(
		"message_fmt" => $post['message_fmt'],
		"message" => $post['message'],
	));
}

include _include(APP_PATH . 'plugin/di_email_notice/model/email_notice.fun.php');
//获取帖子标题
$thread_msg=thread_read($tid);
$thread_title=$thread_msg['subject'];
$thread_uid=$thread_msg['uid'];//楼主uid
//获取楼主用户名
$thread_user_msg=user_read($thread_uid);
$user_name=$thread_user_msg['username'];
$user_email=$thread_user_msg['email'];
//获取回帖者用户名
$reply_user_msg=user_read($uid);
$reply_nick=$reply_user_msg['username'];
//回复内容
$reply_content=$message;
//回复时间
$reply_time=date("Y/m/d H:i:s",$time);

//帖子链接
$thread_url=$_SERVER['SERVER_NAME'].url("thread-".$tid);

//判断是否为引用
if($quotepid !=0){
	$quotepost_msg=user_read($quotepost['uid']);
	$user_email=$quotepost_msg['email'];
	$user_name=$quotepost_msg['username'];
	
	
}

 //获取配置信息
$email=kv_get('email_notice');
$fromname=$email['fromname'];
$email_title=$email['email_title'];
$email_message=$email["email_message"];
$email_user=$email['email'];
$email_password=(string)$email['password'];
$email_smtp=$email['smtp'];
$email_port=$email['port'];


//变量替换
$str=array('{thread_title}','{user_name}','{reply_nick}','{reply_content}','{reply_time}','{thread_url}');

$var=array($thread_title,$user_name,$reply_nick,$reply_content,$reply_time,$thread_url);

$email_message=str_replace($str,$var,$email["email_message"]);
$email_title=str_replace($str,$var,$email["email_title"]);
$fromname=str_replace($str,$var,$email["fromname"]); 
$Tuser=user_read($uid);
if($thread_user_msg['email_notice']){
	sendEmail($user_email,$email_title,$email_message,$email_user,$email_password,$email_smtp,$email_port,$fromname); 
}

 
		$return_html = param('return_html', 0);
		$forum = forum_read($fid);
		$credits = $forum['post_credits'];
		$golds = $forum['post_golds'];
		$uid AND user_update($uid, array('credits+'=>$credits, 'golds+'=>$golds));
		user_update_group($uid);
		$message = '';
		!empty($credits) AND $message = lang('sg_creditsplus',  array('credits'=>$credits));
		!empty($golds) AND $message = lang('sg_goldsplus',  array('golds'=>$golds));
		!empty($credits) && !empty($golds) AND $message = lang('sg_creditsplus',  array('credits'=>$credits)).'、'.lang('sg_goldsplus',  array('golds'=>$golds));
		if($return_html) {
			$filelist = array();
			ob_start();
			include _include(APP_PATH.'view/htm/post_list.inc.htm');
			$s = ob_get_clean();
			message(0, $s);
		} else {
			$message = $message ? $message : lang('create_post_sucessfully');
			message(0, $message);
		}

		
		// 直接返回帖子的 html
		// return the html string to browser.
		$return_html = param('return_html', 0);
		if($return_html) {
			$filelist = array();
			ob_start();
			include _include(APP_PATH.'view/htm/post_list.inc.htm');
			$s = ob_get_clean();
						
			message(0, $s);
		} else {
			message(0, lang('create_post_sucessfully'));
		}
	
	}
	
} elseif($action == 'update') {

	$pid = param(2);
	$post = post_read($pid);
	empty($post) AND message(-1, lang('post_not_exists'));
	
	$tid = $post['tid'];
	$thread = thread_read($tid);
	empty($thread) AND message(-1, lang('thread_not_exists'));
	
	$fid = $thread['fid'];
	$forum = forum_read($fid);
	empty($forum) AND message(-1, lang('forum_not_exists'));
	
	$isfirst = $post['isfirst'];
	
	!forum_access_user($fid, $gid, 'allowpost') AND message(-1, lang('user_group_insufficient_privilege'));
	$allowupdate = forum_access_mod($fid, $gid, 'allowupdate');
	!$allowupdate AND !$post['allowupdate'] AND message(-1, lang('have_no_privilege_to_update'));
	!$allowupdate AND $thread['closed'] AND message(-1, lang('thread_has_already_closed'));
	
	
	
	if($method == 'GET') {
		
		
		
		$forumlist_allowthread = forum_list_access_filter($forumlist, $gid, 'allowthread');
		$forumarr = xn_json_encode(arrlist_key_values($forumlist_allowthread, 'fid', 'name'));
		
		// 如果为数据库减肥，则 message 可能会被设置为空。
		// if lost weight for the database, set the message field empty.
		$post['message'] = htmlspecialchars($post['message'] ? $post['message'] : $post['message_fmt']);
		
		($uid != $post['uid']) AND $post['message'] = xn_html_safe($post['message']);
		
		$attachlist = $imagelist = $filelist = array();
		if($post['files']) {
			list($attachlist, $imagelist, $filelist) = attach_find_by_pid($pid);
		}
		
		
		// todo:
		$tagids = tag_thread_find_tagid_by_tid($tid, $forum['tagcatelist']);
				
			// 编辑器支持 HTML 编辑
			if($post['doctype'] == 1) {
				$post['message'] = htmlspecialchars($post['message_fmt']);
			}
		
		include _include(APP_PATH.'view/htm/post.htm');
		
	} elseif($method == 'POST') {
		
		$subject = htmlspecialchars(param('subject', '', FALSE));
		$message = param('message', '', FALSE);
		$doctype = param('doctype', 0);
		
		
		
		empty($message) AND message('message', lang('please_input_message'));
		mb_strlen($message, 'UTF-8') > 2048000 AND message('message', lang('message_too_long'));
		
		$arr = array();
		if($isfirst) {
			$newfid = param('fid');
			$forum = forum_read($newfid);
			empty($forum) AND message('fid', lang('forum_not_exists'));
			
			if($fid != $newfid) {
				!forum_access_user($fid, $gid, 'allowthread') AND message(-1, lang('user_group_insufficient_privilege'));
				$post['uid'] != $uid AND !forum_access_mod($fid, $gid, 'allowupdate') AND message(-1, lang('user_group_insufficient_privilege'));
				$arr['fid'] = $newfid;
			}
			if($subject != $thread['subject']) {
				mb_strlen($subject, 'UTF-8') > 80 AND message('subject', lang('subject_max_length', array('max'=>80)));
				$arr['subject'] = $subject;
			}
			$arr AND thread_update($tid, $arr) === FALSE AND message(-1, lang('update_thread_failed'));
		}
		$r = post_update($pid, array('doctype'=>$doctype, 'message'=>$message));
		$r === FALSE AND message(-1, lang('update_post_failed'));
		
		
		// todo:
		/*
		$tag_cate_id_arr = param('tag_cate_id', array(0));
		
		
		$tagids_new = array_values($tag_cate_id_arr);
		$tagids_old = tag_thread_find_tagid_by_tid($tid);
		//print_r($tagids_new);print_r($tagids_old);exit;
		//新增的、删除的 
		$tag_id_delete = array_diff($tagids_old, $tagids_new);
		$tag_id_add = array_diff($tagids_new, $tagids_old);
		foreach($tag_id_delete as $tagid) {
			tag_thread_delete($tagid, $tid);
		}
		foreach($tag_id_add as $tagid) {
			tag_thread_create($tagid, $tid);
		}
		thread_update($tid, array('tagids'=>'', 'tagids_time'=>0));

		*/
		
		if($isfirst) {
			$tagids = param('tagid', array(0));
			$tagcatemap = $forum['tagcatemap'];
			foreach($forum['tagcatemap'] as $cate) {
				$defaulttagid = $cate['defaulttagid'];
				$isforce = $cate['isforce'];
				$catetags = array_keys($cate['tagmap']);
				$intersect = array_intersect($catetags, $tagids); // 比较数组交集
				// 判断是否强制
				if($isforce) {
					if(empty($intersect)) {
						message(-1, '请选择 ['.$cate['name'].']');
					}
				}
				// 判断是否默认
				if($defaulttagid) {
					if(empty($intersect)) {
						array_push($tagids, $defaulttagid);
					}
				}
				
			}
			
			$tagids = array_diff($tagids, array(0));
			$tagids_new = $tagids;
			$tagids_old = tag_thread_find_tagid_by_tid($tid, $forum['tagcatelist']);
			$tag_id_delete = array_diff($tagids_old, $tagids_new);
			$tag_id_add = array_diff($tagids_new, $tagids_old);
			if($tag_id_delete) {
				foreach($tag_id_delete as $tagid) {
					$tagid AND tag_thread_delete($tagid, $tid);
				}
			}
			if($tag_id_add) {
				foreach($tag_id_add as $tagid) {
					$tagid AND tag_thread_create($tagid, $tid);
				}
			}
			thread_update($tid, array('tagids'=>'', 'tagids_time'=>0));
			/*
			foreach($tagids as $tagid) {
				$tagid AND tag_thread_create($tagid, $tid);
			}*/
		}

		
		message(0, lang('update_successfully'));
		//message(0, array('pid'=>$pid, 'subject'=>$subject, 'message'=>$message));
	}
	
} elseif($action == 'delete') {

	$pid = param(2, 0);
	
	
	
	if($method != 'POST') message(-1, lang('method_error'));
	
	$post = post_read($pid);
	empty($post) AND message(-1, lang('post_not_exists'));
	
	$tid = $post['tid'];
	$thread = thread_read($tid);
	empty($thread) AND message(-1, lang('thread_not_exists'));
	
	$fid = $thread['fid'];
	$forum = forum_read($fid);
	empty($forum) AND message(-1, lang('forum_not_exists'));
	
	$isfirst = $post['isfirst'];
	
	!forum_access_user($fid, $gid, 'allowpost') AND message(-1, lang('user_group_insufficient_privilege'));
	$allowdelete = forum_access_mod($fid, $gid, 'allowdelete');
	!$allowdelete AND !$post['allowdelete'] AND message(-1, lang('insufficient_delete_privilege'));
	!$allowdelete AND $thread['closed'] AND message(-1, lang('thread_has_already_closed'));
	
	

	if($isfirst) {
		thread_delete($tid);
	} else {
		post_delete($pid);
		//post_list_cache_delete($tid);
	}
	
	
	
	message(0, lang('delete_successfully'));

}



elseif ($action == 'post_like') {

	$header['title'] = lang('haya_post_like')." - " . $conf['sitename'];
	
	if (!$uid) {
		message(0, lang('haya_post_like_login_like_tip'));
	}
	
	
	
	if ($method == 'POST') {

		$pid = param('pid');

		$post = post_read($pid);
		empty($post) AND message(0, lang('post_not_exists'));

		if ($post['isfirst'] == 1) {
			if (isset($haya_post_like_config['open_thread'])
				&& $haya_post_like_config['open_thread'] != 1
			) {
				message(0, lang('haya_post_like_close_thread_tip'));
			}
		} else {
			if (isset($haya_post_like_config['open_post'])
				&& $haya_post_like_config['open_post'] != 1
			) {
				message(0, lang('haya_post_like_close_post_tip'));
			}
		}
	
		haya_post_like_cache_delete($post['tid']);
		
		$haya_post_like_check = haya_post_like_find_by_uid_and_pid($uid, $pid);
		
		$action2 = param(2, 'create');
		if ($action2 == 'create') {
			
			
			if (!empty($haya_post_like_check)) {
				message(0, lang('haya_post_like_user_has_like_tip'));
			}
			
			haya_post_like_create(array(
				'tid' => $post['tid'], 
				'pid' => $pid, 
				'uid' => $user['uid'],
				'create_date' => time(),
				'create_ip' => $longip,
			));			
			
			if (isset($haya_post_like_config['post_like_count_type'])
				&& $haya_post_like_config['post_like_count_type'] == 1
			) {
				$haya_post_like_count = haya_post_like_count(array('pid' => $pid));
				
				post__update($post['pid'], array('likes' => $haya_post_like_count));
				
				if ($post['isfirst'] == 1) {
					thread__update($post['tid'], array('likes' => $haya_post_like_count));
				}
			} else {
				$haya_post_like_count = intval($post['likes']) + 1;
				
				haya_post_like_loves($pid, 1);
				
				if ($post['isfirst'] == 1) {
					thread__update($post['tid'], array('likes+' => 1));
				}
			}
			
			$haya_post_like_msg = array(
				'count' => intval($haya_post_like_count),
				'msg' => lang('haya_post_like_like_success_tip'),
			);
			
			

if (function_exists("notice_send")) {
	
	
	$notice_user = '<a href="'.url('user-'.$user['uid']).'" target="_blank"><img class="avatar-1" src="'.$user['avatar_url'].'"> '.$user['username'].'</a>';

	$thread = thread_read($post['tid']);
	$thread['subject'] = notice_substr($thread['subject'], 20);
	$notice_thread = '<a target="_blank" href="'.url('thread-'.$post['tid']).'">《'.$thread['subject'].'》</a>';

	$post['message'] = htmlspecialchars(strip_tags($post['message']));
	$post['message'] = notice_substr($post['message'], 40);
	$notice_post = '<a target="_blank" href="'.url('thread-'.$post['tid'].'-1').'#'.$post['pid'].'">【'.$post['message'].'】</a>';
	
	if ($post['isfirst'] == 1) {
		$notice_msg_tpl = lang('haya_post_like_send_notice_for_thread');
		
		
	} else {
		$notice_msg_tpl = lang('haya_post_like_send_notice_for_post');
		
		
	}
	
	$notice_msg = str_replace(
		array('{thread}', '{post}', '{user}'),
		array($notice_thread, $notice_post, $notice_user),
		$notice_msg_tpl
	);

	notice_send($user['uid'], $post['uid'], $notice_msg, 150);
	
	
}


			
			message(1, $haya_post_like_msg);
		} elseif ($action2 == 'delete') {
			
			
			if (isset($haya_post_like_config['like_is_delete'])
				&& $haya_post_like_config['like_is_delete'] != 1
			) {
				message(0, lang('haya_post_like_no_unlike_tip'));
			}
			
			if (empty($haya_post_like_check)) {
				message(0, lang('haya_post_like_user_no_like_tip'));
			}
			
			$post_like = haya_post_like_read_by_uid_and_pid($uid, $pid);

			$delete_time = intval($haya_post_like_config['delete_time']);
			if ($post_like['create_date'] + $delete_time > time()) {
				message(0, lang('haya_post_like_no_fast_like_tip'));
			}
			
			haya_post_like_delete_by_pid_and_uid($pid, $user['uid']);
			
			if (isset($haya_post_like_config['post_like_count_type'])
				&& $haya_post_like_config['post_like_count_type'] == 1
			) {
				$haya_post_like_count = haya_post_like_count(array('pid' => $pid));
				
				post__update($post['pid'], array('likes' => $haya_post_like_count));
				
				if ($post['isfirst'] == 1) {
					thread__update($post['tid'], array('likes' => $haya_post_like_count));
				}
			} else {
				$haya_post_like_count = MAX(0, intval($post['likes']) - 1);
				
				haya_post_like_loves($pid, -1);
				
				if ($post['isfirst'] == 1) {
					$haya_post_like_thread = thread__read($post['tid']);
					
					if ($haya_post_like_thread['likes'] > 0) {
						thread__update($post['tid'], array('likes-' => 1));
					}
				}
			}			
			
			$haya_post_like_msg = array(
				'count' => intval($haya_post_like_count),
				'msg' => lang('haya_post_like_unlike_success_tip'),
			);
			
			
			
			message(1, $haya_post_like_msg);
		}
		
		
		
		message(0, lang('haya_post_like_like_error_tip'));	
	}
	
	
	
	message(0, lang('haya_post_like_like_error_tip'));

}




?>