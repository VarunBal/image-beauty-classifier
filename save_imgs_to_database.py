import flickrapi as flickr
##import urllib
import xml.etree.ElementTree as ET
import to_database as db
import cv2 as cv

key = ''
secret = ''

flickr = flickr.FlickrAPI(api_key = key, secret = secret,)

def search(tags):
    pcount = 0
    ncount = 0
    
    photos =flickr.walk(tags = tags,tag_mode='all',per_page = 5000, extras='url_c')
    
    for photo in photos:
        try:
##                print('photo',photo.keys())
                pic_id=photo.get('id')
                
                owner_id=photo.get('owner')
                owner_info=flickr.people.getInfo(user_id=owner_id)[0]
##                ET.dump(owner_info)
                ispro=owner_info.get('ispro')
                
                sizes=flickr.photos.getSizes(photo_id=pic_id)[0]
##                    print(ET.dump(sizes))
                size=sizes.find("./size[@label='Large Square']")
                url=size.get('source')
##                    print('small source:',url)

                if ispro == '1':
                    db.insert_url(pic_id,url,True)
##                    urllib.request.urlretrieve(url,'flickr_img\\pos_'+ pic_id +".jpg")
                    pcount+=1
                    print(pcount,'Pos. pic saved')
                elif ispro == '0':
                    db.insert_url(pic_id,url,False)
##                    urllib.request.urlretrieve(url,'flickr_img\\neg_'+ pic_id +".jpg")
                    ncount+=1
                    print(ncount,'Neg. pic saved')
                else:
                    print('not saved')
        except Exception as e:
                print(e)
    print('pos:',pcount)
    print('neg:',ncount)
    print('total:',pcount+ncount)
    cv.waitKey(0)

if __name__ == '__main__':
    urls = search('dslr,traveler')
