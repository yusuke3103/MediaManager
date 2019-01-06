'''
Created on Jan 5, 2019

@author: Yusuke
'''
from animes.models import SubTitle, Title
from process import FileProcess


def UpdateOrCreate(tid, dic):
    
    for key in dic:
        SubTitle.objects.update_or_create(
            tid=tid,
            rno='{:02}'.format(int(key)),
            subtitle=dic[key].replace("/", "／").replace(":", "：")
        )

        
def MappingFile(tid, data):
    subtitles = SubTitle.objects.filter(tid=tid)
    
    for dic in data:
        rno = dic['rno']
        path = dic['path']
        
        obj = SubTitle.objects.get(tid=tid, rno=rno)
        obj.path = FileProcess.FileRename(tid, obj.subtitle, obj.rno, path)
        obj.save()
        
    
def GetSubTitles(tid):
    return SubTitle.objects.filter(tid=tid)
