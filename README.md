# Tuis Spider for single article / 图虫单篇文章图像爬虫

# 描述
这是一个非常简单的基于BS4和Request库的Python爬虫，可以爬取图虫网某篇文章内所有图像，适用于单篇文章内图像的爬取（喜欢哪篇下哪篇）。当然，爬虫程序仅供学习研究使用，如果要使用图像，务必先向作者获取图像的使用授权，请尊重每一篇作品每一张照片。

url示例：http://flacst.tuchong.com/22730385/

在程序内直接输入文章的url即可下载该文章内发布的所有图像，在获取所有图像后程序会等待下一个url的输入，若没有更多可直接按回车键退出程序。

我在程序中所设置的保存图像的地址是“C:/abc/”，程序每次运行之后需要手动将获取的图像挪到其他地方保存，否则在程序下次运行时这些图像会被覆盖。

# description
This is a simple python spider program to capture images from Tuchong.com, using BS4 and Request Lib. It is also the first spider program of mine. This program for studying use only, if you want to use the images from Tuchong.com, please get copyright from the author of images first.

You can input the url of article into the program(Just like: http://flacst.tuchong.com/22730385/), the spider will save all images in the article, when the last image have been saved, you can input the another article url to continue saving.

The default path for save images is "C:/abc/", if you want to change it, please edit the value of variable 'path'.

After the program running once, please move images you have downloaded to another folder or they will be overwritten when the program working next time.(You can change 'path' also)
