class User():
    ranks = [-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8]
    def __init__(self):
        self.rank = -8
        self.idx = 0
        self.progress = 0
    def inc_progress(self, rank):
        if rank not in User.ranks: raise ValueError
        if rank > self.rank:
            self.progress += 10*(User.ranks.index(rank) - User.ranks.index(self.rank)) ** 2
        elif rank == self.rank:
            self.progress += 3
        elif rank > User.ranks[self.idx - 2]:
             self.progress += 1
                
        if self.rank < 8:
            if self.progress>=100:
            
#                 if self.rank == -1:
#                     self.rank+=2
#                 else:
                progRank = self.progress // 100
                self.rank = User.ranks[progRank+self.idx] if progRank+self.idx<len(User.ranks) else ranks[-1]
                self.idx = User.ranks.index(self.rank)
                self.progress = self.progress % 100 if self.rank != 8 else 0
                    
#                     self.progress -= 100
#                     self.progress = self.progress if self.progress>=0 else 0
        else:
            self.idx = len(User.ranks)
            self.rank = User.ranks[-1]
            self.progress = 0
        return 