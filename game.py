#dhini motham ni programming with tim ane channel keli chusthunam  how to make a game in python ane dhi video peru
import pygame
import time
import random
#manam draw chesindhi kuda kani piyali ka 1 sec 2 sec ani dhani kosam edhi 
pygame.font.init()

#window size entha pixels lo pedthunam,win ante window , set caption ante paina kani piche peru 
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodgers XIX")# ekkadi dhaka window set 

#edhi background picture set cheyanike 
BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))


#mana ship size entha unadaliani 
PLAYER_WIDTH = 20
PLAYER_HEIGHT = 40
# player vel ante manam left arrow kani right arrow kotinapudu manadfhi move aithadhi chudu adhi eda vachedhi 
#dhaniki manam player vel ani peru echinam entha move avvali oka sari key press chesinapudu ani check cheyadaniki
PLAYER_VEL = 5
# stars painunchi padthayi ka dhani size entha ani set chesthunam 
STAR_WIDTH = 10
STAR_HEIGHT = 20
#stars kadhile speed enti dhantla manam eda se chesthunam enka fasat or slow cheskonike
STAR_VEL = 3

FONT = pygame.font.SysFont("ariel", 40)


def draw(player, elapsed_time, stars):
    #blit anedhi  emaina draw cheyaniki kani leka pothe nak emmaina cheyadaniki baga pani chesthadhi 
    WIN.blit(BG, (0, 0))
    #eda manam time ni print cheyaniki vaduthunam
    #round anedhi nearest second ki round off cheyanike vaaduthunam 
    #$1 anedhi anti aliasing ki color okati pedthunam 
    #dheni motham ni manam render chesthunam
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    #ekkada petrtali ani manam blit thoni set chesthunam
    #10,10 anedhi position
    WIN.blit(time_text, (10, 10))
    
    #eda draw chesthbunam em draw chesthunam andedhi eda pedthunam aada draw functiopn vaadinapudu eda funtion lo manmamem upda`te chesthunam enti ani eda chustham`
    #format(ekkada draw chesthunam , color enti , ee dhani em antar [kadhiliyanike])
    #player ki manam cordinates assign chesinam edhi ekkada ani adhi ekkadas pedtham
    pygame.draw.rect(WIN, "red", player)

    #manam edadhini particular dhani thoni stars ni draw chesthunam,
    for star in stars:
        pygame.draw.rect(WIN, "aqua", star)
    
    #manam chesina dharidralanu update cheyaniki eda update vaadutham 
    pygame.display.update()


def main():
    #asal program run aithundhi aa ledha ani chudanike manam ee run ni pettukunam true ante nadusthadhi false aithe pothadhi 
    run = True
    #edhi mana charecter dheni move cheyadaniki manam edhi raasthunam
    #rect lopala mana player ekkada strart chesathunam anidhi chla important so edhi formate(x cordinaate , y cordinate , player widht , player height  )
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    #ani systems la same funcction avvanike manam ee dhani vadutham leka pothe konitla fast ga vasthadhi konitla slow ga vasthadhi dheni valla probelms raavochu
    #py game la inbuilt clock untadhi adhuke dhini vaaduthunam 
    clock = pygame.time.Clock()
    #current time endhi ani ee time.time isthadhoi
    start_time = time.time()
    #first eda initialise chestrhunam dhini kinda loop la second line undhi chudu 
    #ee elapsed time ni thuiskeli manam draw function la kuda pedtham
    elapsed_time = 0
    #stars ni entha sep petanike 
    star_add_increment = 2000
    #eppud add cheyali ani increement eppud reach aithundhi ani chustrthadhi
    star_count = 0
    
    #eda mana screen midha ASAL ENI STARS unnayi ani add chestham dhini prakaram manam potha untam 
    
    stars = []
    #undefined error rakunda manam mundhe dhini initialise chesi pettukuntunam 
    hit = False

    while run:
        #clock tick 60 ante maxinmin number of frames persond
        #ante enni sarlu ee while loop run ayyi  
        star_count += clock.tick(60)
        #entha time ayyindhi ani chusi start time la keli misus chesthunam entha time ayyindhi ani chudanike 
        elapsed_time = time.time() - start_time

        #oka stars increment kante ekkuva unte ne stars add aithayi 
        #manam eni stars oka sariki add chestham anedhi eda set chestham for loop la
        
        if star_count > star_add_increment:
            #for loop la eda oka sariki 3 stars ni add chesthunam 
            #enjka ekkuva thakuva kuda cheskovachu 
            for _ in range(3):
                #rondon ga ee star ni place chestham manam stars ni eda add chestham aoo chuskuntasm 
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                #hieght entha ani isthunam oka particual point la dhinitho manaki malli kindhiki raanike kuda help aithadhi 
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                #paina unde star list la add chesthunam dheni thikoni velli 
                stars.append(star)
            #star nmi jaldi add chestha undanike manaki edhi vasthadhi 
            #eda prati  saari time entha aithe thiskuntadhi oo star incremtn cheyanike adhi thaguthadhi 
            #ante mundhu first star anedhi 2000 milli seconds ki vachindhi ka 
            #next saari 1950 ki vasthadhi 
            #prati saari 50 thaguthadhi kinda dhani valla 
            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0
            
        #ee particual loop asal window close cheyanike okavela cross button ni press chesthe close chayanike manam ee button ni vadutham 
        #event ante  close chesinama ledha ani check cheyanike

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        #eda manam player ni jarapa nike manam vaade key prakaram ee key press chesthunam ani chusoi edhi jaruputhadhi 
        #andhjuke ee part motham manam ee key vathuthunam ani check cheyanike        
        keys = pygame.key.get_pressed()
        #k_left anedhi event name manam left arraow vadinapudu manam edhi occur chestham
        #adhi occurr ayyinapudu manam unde position keli manam 5 (manam set chesina step size )minus aihtadhi 
        #k_left anedhi key code enka emamina add chedham anukunte seach key code in documentation
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        #k_right kuda same 
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
        
        #stars ni move cheyali ka  dhani kosam edhi 
        #eda manam copy chesthunam aa stars list ni 
        #endhuk ante stars ni manam screen kindaki reach ayyinanka thiseyali kabati 
        
        for star in stars[:]:
            #velcocity prakaam kindaki testhunam
            star.y += STAR_VEL
            #oka vela kindaki velli pothe thuisesthunam
            if star.y > HEIGHT:
                stars.remove(star)
            #vela thakuthe katha endhi ani chusthunam nuvvu pakkana thakuthe ni katha enti ani chudanike edhi pani chesthadhi 
            #hit ni true isthunam
            #pygame thop kkabati collide ayyindha ledha ani direct ga check cheyagaltthunam manam 
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
        
        #oka vela thakindha ledh anai check cheyanike manam ee part vaaduthunam
        
        if hit:
            #render chesthunam lost6 ane message ni 
            lost_text = FONT.render("You Lost!", 1, "white")
            #center la prtint cheyanike edhi chesthunam 
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            #motham ayyinanka update chesthunam
            pygame.display.update()
            #AYYIPOYINAKA time ichi motham ni quit chesthunam
            pygame.time.delay(4000)
            break
        #prati frAME tharvatha draw chesi update cheyadaniki prati frame ki player eda unnadu starts em vasthunayi , time entha ayyindhi anedhi updatye chesthadhi draw 
        draw(player, elapsed_time, stars)
    
    #pygame.quit window close chesesthadhi
    pygame.quit()

#oka vela ee file ni direct ga run chesara ;ledha ani check cheyanike edhi import chesthe fase vasthadhi , direct ga run chesthe true vasthadhi 
if __name__ == "__main__":
    main()