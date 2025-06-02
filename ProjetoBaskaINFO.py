#DJRoscowski
print('Project: Baska Team\n')

print('+ --------------------  INFO TEAM  -------------------- +')
print('|                                                       |')
print('| 1. Atlanta Hawks           16. Miami Heat             |')
print('| 2. Boston Celtics          17. Milwaukee Bucks        |')
print('| 3. Brooklyn Nets           18. Minnesota Timberwolves |')
print('| 4. Charlotte Hornets       19. New York Knicks        |')
print('| 5. Chicago Bulls           20. New Orleans Pelicans   |')
print('| 6. Cleveland Cavaliers     21. Oklahoma City Thunder  |')
print('| 7. Dallas Mavericks        22. Orlando Magic          |')
print('| 8. Denver Nuggets          23. Philadelphia 76ers     |')
print('| 9. Detroit Pistons         24. Phoenix Suns           |')
print('| 10. Golden State Warriors  25. Portland Trail Blazers |')
print('| 11. Houston Rockets        26. Sacramento Kings       |')
print('| 12. Indiana Pacers         27. San Antonio Spurs      |')
print('| 13. Los Angeles Clippers   28. Toronto Raptors        |')
print('| 14. Los Angeles Lakers     29. Utah Jazz              |')
print('| 15. Memphis Grizzlies      30. Washington Wizards     |')
print('+ ----------------------------------------------------- +')

#team - conference - founded - championships
ATL = ['Atlanta Hawks', 'Eastern', 1946, 1]
BOS = ['Boston Celtics', 'Eastern', 1946, 17]
BKN = ['Brooklyn Nets', 'Eastern', 1967, 2]
CHA = ['Charlotte Hornets', 'Eastern', 1988, 0]
CHI = ['Chicago Bulls', 'Eastern', 1966, 6]
CLE = ['Cleveland Cavaliers', 'Eastern', 1970, 1]
DAL = ['Dallas Mavericks', 'Western', 1980, 1]
DEN = ['Denver Nuggets', 'Western', 1967, 0]
DET = ['Detroit Pistons', 'Eastern', 1937, 3]
GSW = ['Golden State Warriors', 'Western', 1946, 7]
HOU = ['Houston Rockets', 'Western', 1946, 2]
IND = ['Indiana Pacers', 'Eastern', 1967, 0]
LAC = ['Los Angeles Clippers', 'Western', 1970, 0]
LAL = ['Los Angeles Lakers', 'Western', 1947, 17]
MEM = ['Memphis Grizzlies', 'Western', 1995, 0]
MIA = ['Miami Heat', 'Eastern', 1988, 3]
MIL = ['Milwaukee Bucks', 'Eastern', 1968, 2]
MIN = ['Minnesota Timberwolves', 'Western', 1989, 0]
NYK = ['New York Knicks', 'Eastern', 1946, 2]
NOP = ['New Orleans Pelicans', 'Western', 2002, 0]
OKC = ['Oklahoma City Thunder', 'Western', 1967, 1]
ORL = ['Orlando Magic', 'Eastern', 1989, 0]
PHI = ['Philadelphia 76ers', 'Eastern', 1946, 3]
PHX = ['Phoenix Suns', 'Western', 1968, 0]
POR = ['Portlans Trail Blazers', 'Western', 1970, 1]
SAC = ['Sacramento Kings', 'Western', 1923, 1]
SAS = ['San Antonio Spurs', 'Western', 1967, 5]
TOR = ['Torondo Raptors', 'Eastern', 1995, 1]
UTA = ['Utah Jazz', 'Western', 1974, 0]
WAS = ['Washington Wizards', 'Eastern', 1961, 1]


while True : #Repetição de interação

    try:

        resp = int(input('\nPara Sair Digite: 0 \nEscolha o número do seu TIME na lista: '))

        if resp == 1:
            print('|Team: {} \n|Conference: {} \n|Founded: {} \n|Championships: {}'.format(ATL[0], ATL[1], ATL[2], ATL[3]))
        elif resp == 2:
            print('|Team: {} \n|Conference: {} \n|Founded: {} \n|Championships: {}'.format(BOS[0], BOS[1], BOS[2], BOS[3]))
        elif resp == 3:
            print('|Team: {} \n|Conference: {} \n|Founded: {} \n|Championships: {}'.format(BKN[0], BKN[1], BKN[2], BKN[3]))
        elif resp == 4:
            print('|Team: {} \n|Conference: {} \n|Founded: {} \n|Championships: {}'.format(CHA[0], CHA[1], CHA[2], CHA[3]))
        elif resp == 5:
            print('|Team: {} \n|Conference: {} \n|Founded: {} \n|Championships: {}'.format(CHI[0], CHI[1], CHI[2], CHI[3]))
        elif resp == 6:
            print('|Team: {} \n|Conference: {} \n|Founded: {} \n|Championships: {}'.format(CLE[0], CLE[1], CLE[2], CLE[3]))
        elif resp == 7:
            print('|Team: {} \n|Conference: {} \n|Founded: {} \n|Championships: {}'.format(DAL[0], DAL[1], DAL[2], DAL[3]))
        elif resp == 8:
            print('|Team: {} \n|Conference: {} \n|Founded: {} \n|Championships: {}'.format(DEN[0], DEN[1], DEN[2], DEN[3]))
        elif resp == 9:
            print('|Team: {} \n|Conference: {} \n|Founded: {} \n|Championships: {}'.format(DET[0], DET[1], DET[2], DET[3]))
        elif resp == 10:
            print('|Team: {} \n|Conference: {} \n|Founded: {} \n|Championships: {}'.format(GSW[0], GSW[1], GSW[2], GSW[3]))
        elif resp == 11:
            print('|Team: {} \n|Conference: {} \n|Founded: {} \n|Championships: {}'.format(HOU[0], HOU[1], HOU[2], HOU[3]))
        elif resp == 12:
            print('|Team: {} \n|Conference: {} \n|Founded: {} \n|Championships: {}'.format(IND[0], IND[1], IND[2], IND[3]))
        elif resp == 13:
            print('|Team: {} \n|Conference: {} \n|Founded: {} \n|Championships: {}'.format(LAC[0], LAC[1], LAC[2], LAC[3]))
        elif resp == 14:
            print('|Team: {} \n|Conference: {} \n|Founded: {} \n|Championships: {}'.format(LAL[0], LAL[1], LAL[2], LAL[3]))
        elif resp == 15:
            print('|Team: {} \n|Conference: {} \n|Founded: {} \n|Championships: {}'.format(MEM[0], MEM[1], MEM[2], MEM[3]))
        elif resp == 16:
            print('|Team: {} \n|Conference: {} \n|Founded: {} \n|Championships: {}'.format(MIA[0], MIA[1], MIA[2], MIA[3]))
        elif resp == 17:
            print('|Team: {} \n|Conference: {} \n|Founded: {} \n|Championships: {}'.format(MIL[0], MIL[1], MIL[2], MIL[3]))
        elif resp == 18:
            print('|Team: {} \n|Conference: {} \n|Founded: {} \n|Championships: {}'.format(MIN[0], MIN[1], MIN[2], MIN[3]))
        elif resp == 19:
            print('|Team: {} \n|Conference: {} \n|Founded: {} \n|Championships: {}'.format(NYK[0], NYK[1], NYK[2], NYK[3]))
        elif resp == 20:
            print('|Team: {} \n|Conference: {} \n|Founded: {} \n|Championships: {}'.format(NOP[0], NOP[1], NOP[2], NOP[3]))
        elif resp == 21:
            print('|Team: {} \n|Conference: {} \n|Founded: {} \n|Championships: {}'.format(OKC[0], OKC[1], OKC[2], OKC[3]))
        elif resp == 22:
            print('|Team: {} \n|Conference: {} \n|Founded: {} \n|Championships: {}'.format(ORL[0], ORL[1], ORL[2], ORL[3]))
        elif resp == 23:
            print('|Team: {} \n|Conference: {} \n|Founded: {} \n|Championships: {}'.format(PHI[0], PHI[1], PHI[2], PHI[3]))
        elif resp == 24:
            print('|Team: {} \n|Conference: {} \n|Founded: {} \n|Championships: {}'.format(PHX[0], PHX[1], PHX[2], PHX[3]))
        elif resp == 25:
            print('|Team: {} \n|Conference: {} \n|Founded: {} \n|Championships: {}'.format(POR[0], POR[1], POR[2], POR[3]))
        elif resp == 26:
            print('|Team: {} \n|Conference: {} \n|Founded: {} \n|Championships: {}'.format(SAC[0], SAC[1], SAC[2], SAC[3]))
        elif resp == 27:
            print('|Team: {} \n|Conference: {} \n|Founded: {} \n|Championships: {}'.format(SAS[0], SAS[1], SAS[2], SAS[3]))
        elif resp == 28:
            print('|Team: {} \n|Conference: {} \n|Founded: {} \n|Championships: {}'.format(TOR[0], TOR[1], TOR[2], TOR[3]))
        elif resp == 29:
            print('|Team: {} \n|Conference: {} \n|Founded: {} \n|Championships: {}'.format(UTA[0], UTA[1], UTA[2], UTA[3]))
        elif resp == 30:
            print('|Team: {} \n|Conference: {} \n|Founded: {} \n|Championships: {}'.format(WAS[0], WAS[1], WAS[2], WAS[3]))
        elif resp == 0:
            print('\nGoodbye!')
            break
        elif resp < 0 or resp > 30:
            print('\nEste valor NÃO consta na tabela!')

    except ValueError:
        print('\nAlgo deu errado. Tente Novamente!')
        continue
