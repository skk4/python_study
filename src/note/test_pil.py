import os  
from PIL import Image  
import images2gif  
 
def GetGifAnimationFromImages(targetGifFilePath, srcImageFilePaths, type = 0):  
    
        #�����ϳɵ�ͼƬ  
    images = []  
           
        #ȡ������ͼƬ����󳤶ȣ���ȡ��߶ȣ�  
    maxWidthAndHeight = 1 
        #����Ⱥ͸߶�  
    maxWidth = 1 
    maxHeight = 1 
        #ȡ��ͼƬ����ȴӴ�С�����·��˳��  
    widthAndFilePaths = []  
        #ȡ��ͼƬ���߶ȴӴ�С�����·��˳��  
    heightAndFilePaths = []  
           
    for imageFilePath in srcImageFilePaths:  
        fp = open(imageFilePath, "rb")  
        width,height = Image.open(fp).size  
        widthAndFilePaths.append((width, imageFilePath))  
        heightAndFilePaths.append((height, imageFilePath))  
        maxWidth = max(maxWidth, width)  
        maxHeight = max(maxHeight, height)  
        fp.close()  
       
    maxWidthAndHeight = max(maxWidthAndHeight, maxWidth, maxHeight)  
               
        #��������  
    widthAndFilePaths.sort(key=lambda item: item[0], reverse=True)  
    heightAndFilePaths.sort(key=lambda item: item[0], reverse=True)  
           
    if type == 4 or type == 5:  
            #ԭͼֱ�Ӻϳ�(���������)  
        if type == 4:  
            for widthAndFilePath in widthAndFilePaths:  
                img = Image.open(widthAndFilePath[1])  
                images.append(img)  
            #ԭͼֱ�Ӻϳ�(���߶�����)  
        if type == 5:  
            for heightAndFilePath in heightAndFilePaths:  
                img = Image.open(heightAndFilePath[1])  
                images.append(img)  
#www.iplaypy.com
 
    else:  
        for imageFilePath in srcImageFilePaths:  
            fp = open(imageFilePath, "rb")  
            img = Image.open(fp)  
            width,height = img.size  
                #���ɿյİ�ɫ����ͼƬ  
            if type == 0 or type == 2:    
                    #������  
                imgResizeAndCenter = Image.new("RGB", [maxWidth,maxHeight], (255,255,255))  
            elif type == 1 or type == 3:  
                    #������  
                imgResizeAndCenter = Image.new("RGB", [maxWidthAndHeight,maxWidthAndHeight], (255,255,255))  
       
            if type == 0:  
                    #���/�����>=�߶�/���߶ȣ�ʹ��С�����ű���  
                if maxWidth / width >= maxHeight / height:  
                    resizeImg = img.resize((width * maxHeight / height, maxHeight),Image.ANTIALIAS)  
                    imgResizeAndCenter.paste(resizeImg, ((maxWidth - width * maxHeight / height)/ 2,0))  
                else:  
                    resizeImg = img.resize((maxWidth, height * maxWidth / width),Image.ANTIALIAS)  
                    imgResizeAndCenter.paste(resizeImg, (0,(maxHeight - height * maxWidth / width)/ 2))  
            if type == 1:  
                    #���>=�߶ȣ���������ŵ���󳤶�  
                if width >= height:  
                    resizeImg = img.resize((maxWidthAndHeight, height * maxWidthAndHeight / width),Image.ANTIALIAS)  
                    imgResizeAndCenter.paste(resizeImg, (0,(maxWidthAndHeight - height * maxWidthAndHeight / width)/ 2))  
                else:  
                    resizeImg = img.resize((width * maxWidthAndHeight / height, maxWidthAndHeight),Image.ANTIALIAS)  
                    imgResizeAndCenter.paste(resizeImg, ((maxWidthAndHeight - width * maxWidthAndHeight / height)/ 2, 0))  
            elif type == 2:  
                imgResizeAndCenter.paste(img, ((maxWidth - width) / 2,(maxHeight - height) / 2))  
            elif type == 3:  
                imgResizeAndCenter.paste(img, ((maxWidthAndHeight - width) / 2,(maxWidthAndHeight - height) / 2))  
                       
        #        #�������ž��к��ͼƬ  
        #        imgResizeAndCenter.convert("RGB").save(os.path.dirname(imageFilePath) + os.sep + "ResizeAndCenter" + os.path.basename(imageFilePath), 'jpeg')  
            images.append(imgResizeAndCenter)  
            fp.close()  
               
    images2gif.writeGif(targetGifFilePath, images, duration=1, nq=0.1)  
       
    #ȡ��Ŀ¼������ļ��б�  
def GetDirImageList(dir_proc, recusive = True):  
    resultList = []  
 
    for file in os.listdir(dir_proc):  
        if os.path.isdir(os.path.join(dir_proc, file)):  
            if (recusive):  
                resultList.append(GetDirImageList(os.path.join(dir_proc, file), recusive))  
            continue 
       
        resultList.append(os.path.join(dir_proc, file))  
               
        return resultList  
       
    if __name__ == "__main__":  
        GetGifAnimationFromImages(r"D:\hecheng.gif", [r"D:\a.jpg", r"D:\b.jpg", r"D:\c.jpg"])  
        GetGifAnimationFromImages(r"D:\hecheng1.gif", [r"D:\a.jpg", r"D:\b.jpg", r"D:\b.jpg", r"D:\c.jpg"], 1)  
        GetGifAnimationFromImages(r"D:\hecheng2.gif", [r"D:\a.jpg", r"D:\b.jpg", r"D:\c.jpg"], 2)  
        GetGifAnimationFromImages(r"D:\hecheng3.gif", [r"D:\a.jpg", r"D:\b.jpg", r"D:\c.jpg"], 3)  
        GetGifAnimationFromImages(r"D:\hecheng4.gif", [r"D:\a.jpg", r"D:\b.jpg", r"D:\c.jpg"], 4)  
        GetGifAnimationFromImages(r"D:\hecheng5.gif", [r"D:\a.jpg", r"D:\b.jpg", r"D:\c.jpg"], 5)  
           
        GetGifAnimationFromImages(r"D:\hechengTest.gif", GetDirImageList(r"D:\GifMarker"), type = 4)