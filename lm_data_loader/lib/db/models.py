# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models



class AdDetail(models.Model):
    uid = models.BigIntegerField(primary_key=True)
    uip = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'ad_detail'

class OwAdCreative(models.Model):
    cid = models.AutoField(primary_key=True)
    pid = models.IntegerField()
    uid = models.IntegerField()
    pkgid = models.IntegerField()
    name = models.CharField(max_length=64)
    logo = models.IntegerField()
    description = models.CharField(max_length=128)
    point = models.BigIntegerField()
    price = models.BigIntegerField()
    feedback = models.IntegerField()
    url = models.CharField(max_length=1024)
    createtime = models.IntegerField()
    lastupdate = models.IntegerField()
    nopoint = models.SmallIntegerField()
    detail = models.CharField(max_length=2048)
    action_type = models.IntegerField()
    text = models.CharField(max_length=128)
    interstitial_status = models.IntegerField()
    interstitial_template = models.IntegerField()
    sp_price = models.BigIntegerField()
    screenshots = models.CharField(max_length=1024)
    click_button_name = models.CharField(max_length=32)
    corner_mark = models.IntegerField()
    url_action_type = models.IntegerField()
    app_description = models.CharField(max_length=1024)
    launch_prompt = models.CharField(max_length=256)
    display_name = models.CharField(max_length=256)
    video_rgid = models.IntegerField()
    video_min_imp_time = models.IntegerField()
    video_show_on_list = models.IntegerField()
    video_imp_tracker = models.CharField(max_length=1024)
    rating_level = models.IntegerField()
    rating_count = models.IntegerField()
    template = models.IntegerField()
    creative_type = models.IntegerField()
    search_query = models.CharField(max_length=16)
    search_rank = models.IntegerField()
    is_deleted = models.IntegerField()
    video_ad_img = models.IntegerField()
    logo_url = models.CharField(max_length=1024)
    simple_description = models.CharField(max_length=256)
    manual_tags = models.CharField(max_length=128)
    video_template_id = models.IntegerField()
    video_poster_id = models.CharField(max_length=128)
    video_cost_target = models.BigIntegerField()
    sub_task_enable = models.IntegerField()
    supermacy_task = models.IntegerField()
    task_marking = models.CharField(max_length=8)
    notice = models.CharField(max_length=256)
    prompt = models.CharField(max_length=1024)
    aow_advertiser_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ow_ad_creative'

class OwMediaMedia(models.Model):
    mid = models.AutoField(primary_key=True)
    uid = models.IntegerField()
    pubid = models.CharField(max_length=32)
    status = models.IntegerField()
    paused = models.IntegerField()
    name = models.CharField(max_length=64)
    category = models.IntegerField()
    url = models.CharField(max_length=1024)
    currency_name = models.CharField(max_length=16)
    mediashare_rate = models.IntegerField()
    exchange_rate = models.IntegerField()
    mediadelivery_rate = models.IntegerField()
    sr = models.SmallIntegerField()
    cid_sequence = models.CharField(max_length=1024)
    placement = models.IntegerField()
    createtime = models.IntegerField()
    lastupdate = models.IntegerField()
    comment = models.CharField(max_length=255)
    admintime = models.IntegerField()
    channel = models.CharField(max_length=7)
    admin = models.CharField(max_length=128)
    interstitial_status = models.IntegerField()
    interstitial_paused = models.IntegerField()
    interstitial_loading_scene = models.CharField(max_length=255)
    interstitial_priority = models.IntegerField()
    platform = models.IntegerField()
    admin_category = models.IntegerField()
    package_ugc_id = models.IntegerField()
    package_name = models.CharField(max_length=256)
    show_video_on_list = models.IntegerField()
    video_status = models.IntegerField()
    chn_clk_type = models.IntegerField()
    is_location = models.IntegerField()
    is_video_to_list = models.IntegerField()
    ad_filter = models.CharField(max_length=4096)
    iai_enable = models.IntegerField()
    score_balance = models.IntegerField()
    ad_filter_status = models.IntegerField()
    video_ecpm = models.BigIntegerField()
    video_finish_point = models.IntegerField()
    act_proportion = models.IntegerField()
    task_mediashare_rate = models.IntegerField()
    media_type = models.IntegerField()
    clk_url = models.CharField(max_length=1024)
    wx_user_rate = models.IntegerField()
    wx_media_type = models.IntegerField()
    wx_media_authenticate = models.IntegerField()
    decimal_num = models.IntegerField()
    wx_account = models.CharField(max_length=128)
    wx_lottery = models.IntegerField()
    wx_custom_mall = models.IntegerField()
    video_charge_type = models.IntegerField()
    video_floor_price = models.BigIntegerField()
    sendurl = models.CharField(max_length=1024)
    server_secret = models.CharField(max_length=32)
    video_profit_protect_rate = models.IntegerField()
    report_token = models.CharField(max_length=128, blank=True, null=True)
    channel_callback_url = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'ow_media_media'

