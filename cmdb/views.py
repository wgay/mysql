from django.shortcuts import render # pycharm一般会自动帮你导入这个模块
from django.shortcuts import HttpResponse #导入这个模块

# Create your views here.

def index(request): #request参数必须有，名字是类似self的默认规则，可以改。它封装了用户请求的所有内容
    #request.POST
    #request.GET
    # 当你想返回一个html文件时，就要用render方法来渲染（其实就是打包的意思），render是django提供的方法和规则，用就行，别问为什么要这样
    #return HttpResponse("hello world!") #不能直接返回字符串，必须是由这个类封装起来，这是django的规则，不是python的
    return render(request,"index.html") # 1.第一个参数是固定的（request），第二个参数，你指定的文件（index.html）