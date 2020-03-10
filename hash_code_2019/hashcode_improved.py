from random import shuffle, sample


pics = open('/users/bscdsa2022/mc64/b_lovely_landscapes.txt')

pictures = {}

count = -1

for line in pics:
    words = line.split(' ')
    words[-1] = words[-1][:-1]

    pictures[count] = words

    count += 1

del pictures[-1]
#print(pictures)

pics.close()

#---------------------------------------------------------

V_list = []
H_list = []

for id, att in pictures.items():
    if att[0] == 'V':
        V_list.append(id)
    else:
        H_list.append(id)





#------------------------------------------------------------------

def countPoints(sl):
    total = 0


    for i in range(0, len(sl)-1):
        if isinstance(sl[i], list):
            tags1 = list(set([tag for tag in pictures[sl[i][0]][2:] + pictures[sl[i][1]][2:]]))
        else:
            tags1 = [tag for tag in pictures[sl[i]][2:]]

        if isinstance(sl[i+1], list):
            tags2 = list(set([tag for tag in pictures[sl[i+1][0]][2:] + pictures[sl[i+1][1]][2:]]))
        else:
            tags2 = [tag for tag in pictures[sl[i+1]][2:]]

        points = []
        c = 0
        for tag in tags1:
            if tag in tags2:
                c += 1

        points.append(c)


        points.append(len(tags1)-c)
        points.append(len(tags2)-c)

        total += min(points)


    return total

print(countPoints([0, 3, [1, 2]]))

#----------------------------------------------------------------------------------------------------

def countDups(i, j, V_slides, pictures):
    tags_a = [tag for tag in pictures[V_slides[i]][2:]]
    tags_b = [tag for tag in pictures[V_slides[j]][2:]]


    c = 0

    for tag in tags_a:
        if tag in tags_b:
            c+=1

    return c



def CountPairPoints(i, j, slide, pictures):
    if isinstance(slide[i], list):
        tags_a = list(set([tag for tag in pictures[slide[i][0]][2:] + pictures[slide[i][1]][2:]]))
    else:
        tags_a = [tag for tag in pictures[slide[i]][2:]]

    if isinstance(slide[j], list):
        tags_b = list(set([tag for tag in pictures[slide[j][0]][2:] + pictures[slide[j][1]][2:]]))
    else:
        tags_b = [tag for tag in pictures[slide[j]][2:]]


    points = []

    c = 0
    for tag in tags_a:
        if tag in tags_b:
            c += 1

    points.append(c)
    points.append(len(tags_a)-c)
    points.append(len(tags_b)-c)

    return min(points)





def slideGenerator(dic):
    V_slide_order = sample(V_list, len(V_list))

#===================================================================================
    for i in range(0, len(V_slide_order), 2):
        minV = 2000
        for j in range(i+1, len(V_slide_order)):
            PairDups = countDups(i, j, V_slide_order, dic)
            if PairDups < minV:
                minV = PairDups
                indexJ = j
            if minV == 0:
                break
        V_slide_order[i+1], V_slide_order[indexJ] = V_slide_order[indexJ], V_slide_order[i+1]

#=============================================================================================
    V_pairs = []

    for i in range(0, len(V_slide_order)-1, 2):
        V_pairs.append([V_slide_order[i], V_slide_order[i+1]])

    total_slide = sample(V_pairs + H_list, len(V_pairs + H_list))


    for i in range(0, len(total_slide)-1):
        maxT = -1
        for j in range(i+1, len(total_slide)):
            PairPoints = CountPairPoints(i, j, total_slide, pictures)
            if PairPoints > maxT:
                maxT = PairPoints
                indexJ = j
                if maxT > 6:
                    break
        total_slide[i+1], total_slide[indexJ] = total_slide[indexJ], total_slide[i+1]







    return total_slide



points=0
while points < 2:
    slide = slideGenerator(pictures)
    points = countPoints(slide)

print(points)


f = open('answ.txt', 'w')
f.writelines(str(len(slide))+ '\n')
for line in slide:
    if isinstance(line, list):
        f.writelines(str(line[0])+ ' ' + str(line[1]) + '\n')
    else:
        f.writelines (str(line) + '\n')

f.close()
