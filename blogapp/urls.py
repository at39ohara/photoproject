from django.urls import path
from . import views

# URLconfのURLパターンを逆引きできるようにアプリ名をとうろく
app_name = 'blogapp'

# URLパターンを登録するためのリスト
urlpatterns = [
    # http(s)://ホスト名/以下のパスが''(無し)の場合
    # viewsモジュールノIndexViewを実行
    # URLパターン名は'Index'
    path('', views.IndexView.as_view(), name = 'index'),

    # http(s)://ホスト名/以下のパスが''(無し)の場合
    # viewsモジュールのindex_view()を実行
    # URLパターン名は'index'
    # path('', views.index_view, name = 'index'),

    path(
        # 詳細ページノURLは『blog-detail/レコードのid』
        'blog-detail/<int:pk>/',
        # viewsモジュールのBlogDetailを実行
        views.BlogDeteil.as_view(),
        # URLパターンの名前を'blod_detail'にする
        name = 'blog_detail'
        ),

    # コンタクトカテゴリの
    path('contact/', views.ContactView.as_view(), name = 'contact'),

    # scienceカテゴリの一覧ページノURLパターン
    path(
        # scienceカテゴリの一覧ページのURLは『science-list/』
        'science-list/',
        # viewsもじゅーるのBlogDetailを実行
        views.ScienceView.as_view(),
        # URLパターンの名前を'science_list'にする
        name = 'science_list'
    ),

    # dailylifeカテゴリの一覧ページノURLパターン
    path(
        # dailylifeカテゴリの一覧ページのURLは『dailylife-list/』
        'dailylife-list/',
        # viewsもじゅーるのDailylifeViewを実行
        views.DailylifeView.as_view(),
        # URLパターンの名前を'dailylife_list'にする
        name = 'dailylife_list'
    ),

    # musicカテゴリの一覧ページノURLパターン
    path(
        # musicカテゴリの一覧ページのURLは『music-list/』
        'music-list/',
        # viewsもじゅーるのMusicViewを実行
        views.MusicView.as_view(),
        # URLパターンの名前を'music_list'にする
        name = 'music_list'
    ),

]
