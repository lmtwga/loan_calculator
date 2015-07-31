#!/usr/bin/env python
#coding=utf8

yue_shu=12*40
zong_dai_kuan=1200000
huan_yue=input("Please input how many huandai per month?:")
huan_lixi=[]
huan_benjin=[]
lixi=0.035
yue_lixi=lixi/12

for i in range(1,yue_shu+1):
    yue_li=zong_dai_kuan*yue_lixi
    yue_bj=huan_yue-yue_li
    huan_lixi.append(yue_li)
    huan_benjin.append(yue_bj)
    zong_dai_kuan=zong_dai_kuan-yue_bj

benjin=0
lixi=0
print "nian yue  lixi   benjin"
for i in range(0,yue_shu):
    yue=(i+1)%12
    nian=i/12+1
    if yue==0:
        yue=12
    print str(nian)+" "+str(yue)+" "+ str(round(huan_lixi[i],1))+" "+str(round(huan_benjin[i],1))
    if huan_lixi[i]>0:
        benjin = benjin+huan_benjin[i]
        lixi = lixi+huan_lixi[i]
    else:
        print "zong  li  xi: "+ str(lixi)
        print "zong ben jin: "+ str(benjin)
        print "huan kuan dao: " +str(nian) +" nian/ "+str(yue)+" yue !"
        break


