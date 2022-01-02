import requests
class Coderhub:
    def userInfo(self,user:str,programingName:str)->str:
        """information about the challenges that the user has solved"""
        if programingName == 'python':
            url_leader,programingName=3,'Python'
        elif programingName == 'javascript':
            url_leader,programingName=2,'JavaScript'
        elif programingName == 'swift':
            url_leader,programingName=6,'Swift'
        elif programingName == 'java':
            url_leader,programingName=1, 'Java'
        else:
            return 'The language was not added or you typed it incorrectly'
        try:
                stops = False
                r = requests.get(f'https://api.coderhub.sa/api/profile/public/{user}/').json()
                r = r["user_information"]["id"]
                rank = 'None'
                for i in range(10):
                    leaderboardd = requests.get(f'https://api.coderhub.sa/api/leaderboard/?language={url_leader}&offset={str(i)}&limit=10&type=ALL').json()#العثور علي المركز
                    for zz in range(10):
                        if r == leaderboardd['leaderboard'][zz]['user_id']:
                            
                            rank = leaderboardd['leaderboard'][zz]['rank']
                            stops = True
                            break
                    if stops == True:
                        break
                u = f'https://api.coderhub.sa/api/profile/public/get-user-statistics/{r}/'#معلومات التحديات المحلوله
                t = requests.get(u).json()
                pro = t['programming_languages']
                number_Difficult,number_Average,number_Easy = None,None,None
                for i in range(len(pro)):
                    if pro[i]['name'] == 'متوسط' and programingName in pro[i].values():
                        number_Average=i
                    elif pro[i]['name'] == 'صعب' and programingName in pro[i].values():
                        number_Difficult=i
                    elif pro[i]['name'] == 'سهل' and programingName in pro[i].values() :
                        number_Easy=i
                solvesEasy= 0 if number_Easy == None else pro[number_Easy]['solved_challenges']
                solvesAverage=0 if number_Average==None else pro[number_Average]['solved_challenges']
                solvesDifficult=0 if number_Difficult==None else pro[number_Difficult]['solved_challenges']
                Number_of_points= (solvesEasy*5)+(solvesAverage*10)+(solvesDifficult*20)
                return (f'user : {user}\nin programming : {programingName}\nyour rank : {rank}\nin easy you solved : {solvesEasy}\nin Average you solved : {solvesAverage}\nin Difficult you solved : {solvesDifficult}\nNumber_of_points : {Number_of_points} ')
        except:
                return ('user is private')
    def Rlist(self,program:str,page:int,typeR:str='ALL')->str:
        """ranking list
        program->name of Programming language;
        \npage->The page number is from 1 to 10;
        typeR->all or weeks or day"""
        typeR = 'WEEKLY' if typeR == 'week' else 'DAILY' if typeR == 'day' else 'ALL'
        try:page = int(page);page-=1
        except:return ' Error'
        if page >= 10 or page<0:
            return 'The number from 1 to 10 only'
        program = program.lower()
        if program == 'python':url_leader=3
        elif program == 'javascript':url_leader=2
        elif program == 'swift':url_leader=6
        elif program == 'java':url_leader=1
        else:return ('The language was not added or you typed it incorrectly')
        ranks = ''
        leader = requests.get(f'https://api.coderhub.sa/api/leaderboard/?language={url_leader}&offset={page}&limit=10&type={typeR}').json()
        try:
            for zz in range(10):
                ranknum = (str(leader['leaderboard'][zz]['rank'])+'| ')
                rankname = leader['leaderboard'][zz]['user_info']["username"]
                rankcount = str(int(leader['leaderboard'][zz]["points"]))
                ranks += str(ranknum)+rankname+' | '+rankcount+'\n\n'
            return ranks
        except:
            return ranks
        

