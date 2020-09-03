import random
import sys
sys.path.append('class')
from FlashcardList import FlashcardList
#'id':
#{
#   'flashcard': F
#   'next': F 
#}

class FlashcardDict:
    def __init__(self,f_list: FlashcardList):
        dic = {}
        prev = ''
        self.first = None
        self.last = None
        for i,f in enumerate(f_list):
            if i == 0:
                self.first = f.get_id()
            if i == len(f_list)-1:
                self.last = f.get_id()
            dic[f.get_id()] = {'flashcard': f,'eq_prev': False, 'last_res': '','next': None}
            if prev != '':
                dic[prev]['next'] = f.get_id()
            prev = f.get_id()
        self.flashcard_dict = dic

    def __len__(self):
        return len(self.flashcard_dict)

    def current(self):
        return self.first

    def get_first(self):
        return self.first

    def get_flashcard(self,fid):
        return self.flashcard_dict[fid]['flashcard']

    def get_next(self,fid):
        return self.flashcard_dict[fid]['next']
    
    def get_eq_prev(self,fid):
        return self.flashcard_dict[fid]['eq_prev']

    def get_last_res(self,fid):
        return self.flashcard_dict[fid]['last_res']

    def set_eq_prev(self,fid,eq_prev):
        self.flashcard_dict[fid]['eq_prev'] = eq_prev

    def set_last_res(self,fid,last_res):
        self.flashcard_dict[fid]['last_res'] = last_res

    def pop(self,fid):
        try:
            res = self.flashcard_dict.pop(fid)
            if fid == self.first and fid ==self.last:
                self.first = None
                self.last = None
            elif fid == self.first:
                self.first = res['next']
            elif fid == self.last:
                for key in self.flashcard_dict.keys():
                    if self.flashcard_dict[key]['next'] == fid:
                        self.flashcard_dict[key]['next'] = None
                        self.last = key
            else:
                for key in self.flashcard_dict.keys():
                    if self.flashcard_dict[key]['next'] == fid:
                        self.flashcard_dict[key]['next'] = res['next']
            return res
        except KeyError:
            print('error en pop')
            return None

    def repos(self):
        try:
            if not (self.first is None or len(self.flashcard_dict) == 1):
                r_key = random.choice(list(self.flashcard_dict.keys()))
                if r_key != self.first:
                    second = self.flashcard_dict[self.first]['next']
                    self.flashcard_dict[self.first]['next'] = self.flashcard_dict[r_key]['next']
                    self.flashcard_dict[r_key]['next'] = self.first
                    self.first = second
        except IndexError:
            pass
    