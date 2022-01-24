def getFilesInFolder(path):
    from os import walk
    f = []
    names = []
    for (dirpath, dirnames, filenames) in walk(path):
        f.extend(filenames)
        names = filenames
        break
    return names

def checkKMLInFolder(path):
    import os
    count = []
    files = getFilesInFolder(path)
    for file in files:
        file = str(file)
        name, extension = os.path.splitext(path+file)
        if extension == ".kml":
            count.append(file)
    for kml in count:
        if kml[:2] == "~$":
            count.remove(kml)
    return count

def printArray(array):
    array_numbers = 0
    for i, j in enumerate(array):
        print(str(i+1)+'_ '+str(j.split(".")[0]))
        array_numbers += 1
    return array_numbers

def clear(): 
    import os
    return os.system("cls")

def main():
    import pandas as pd
    from bs4 import BeautifulSoup as bs
    import pyperclip
    import os
    almostList = []
    finalList = []
    cacheList = []
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99"]
    path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    kmls = checkKMLInFolder(path)
    lines = "="*80
    counter = 0
    clear()
    print(lines)
    print("Detectamos",len(kmls),"kmls en la carpeta, seleccione el que quiere usar")
    print(lines)
    printArray(kmls)
    print(lines)
    kmlSeleccion = input("Opcion: ")
    while str(kmlSeleccion) not in numbers[0:len(kmls)+1]:
        clear()
        print(lines)
        print("Ingrese una opcion valida")
        print(lines)
        printArray(kmls)
        print(lines)
        kmlSeleccion = input("Opcion: ")

    kmlSeleccion = int(kmlSeleccion)
    excelSeleccionado = kmls[kmlSeleccion-1]
    with open(excelSeleccionado, "r") as f:
        soup = bs(f,'lxml')
        coordinates = soup.find("coordinates")
        for element in coordinates:
            elementList = element.split(",")
        for element in elementList:
            elementClean = element.split("-")
            try: 
                almostList.append(elementClean[1])
            except:
                pass
        for element in almostList:
            if counter == 0:            
                cacheList.append(float("-"+element))
                counter += 1
            elif counter == 1:
                cacheList.append(float("-"+element))
                finalList.append((cacheList[1], cacheList[0]))
                cacheList = []
                counter = 0
    clear()
    print(finalList)
    pyperclip.copy(str(finalList))
    input("copia tranqui capo")
    main()

if __name__ == '__main__':
    main()

polilynes_list = [(-31.652203, -64.462856), (-31.652231, -64.46287), (-31.652267, -64.462867), (-31.65232, -64.462816), (-31.652578, -64.46251), (-31.65308, -64.461888), (-31.653372, -64.461421), (-31.653432, -64.461276), (-31.653436, -64.461234), (-31.65342, -64.461099), (-31.653377, -64.460938), (-31.653304, -64.460794), (-31.653212, -64.460665), (-31.653103, -64.460523), (-31.653082, -64.460477), (-31.653069, -64.460421), (-31.653064, -64.460343), (-31.653123, -64.45982), (-31.653201, -64.458975), (-31.65329, -64.45809), (-31.653448, -64.456835), (-31.653617, -64.455598), (-31.653644, -64.455376), (-31.653646, -64.455276), (-31.653639, -64.455217), (-31.653624, -64.455174), (-31.653461, -64.45493), (-31.653454, -64.454896), (-31.653459, -64.454839), (-31.653514, -64.454689), (-31.653669, -64.454195), (-31.653834, -64.453624), (-31.653968, -64.45308), (-31.653989, -64.452964), (-31.654034, -64.452519), (-31.654181, -64.45198), (-31.654315, -64.451433), (-31.654386, -64.45117), (-31.654413, -64.451025), (-31.654429, -64.450888), (-31.654429, -64.450781), (-31.654411, -64.450663), (-31.654302, -64.450263), (-31.654279, -64.450148), (-31.65427, -64.450051), (-31.654274, -64.449874), (-31.654306, -64.448614), (-31.654306, -64.448458), (-31.654279, -64.448077), (-31.654224, -64.447729), (-31.654114, -64.44727), (-31.654018, -64.447053), (-31.653984, -64.446956), (-31.653989, -64.4469), (-31.654048, -64.446669), (-31.654117, -64.446514), (-31.65421, -64.446382), (-31.654386, -64.446262), (-31.654633, -64.446154), (-31.654877, -64.446084), (-31.655096, -64.446023), (-31.655126, -64.446028), (-31.655151, -64.446052), (-31.655272, -64.44631), (-31.655457, -64.446624), (-31.655466, -64.44668), (-31.655452, -64.446728), (-31.655361, -64.446795), (-31.655128, -64.446908), (-31.654838, -64.446988), (-31.654388, -64.447066), (-31.654112, -64.447109), (-31.654062, -64.447096), (-31.653993, -64.447012), (-31.653973, -64.446924), (-31.65395, -64.446892), (-31.6539, -64.446846), (-31.653754, -64.446771), (-31.653528, -64.446723), (-31.653436, -64.446674), (-31.653379, -64.446597), (-31.653327, -64.446479), (-31.653103, -64.446146), (-31.652993, -64.445969), (-31.652865, -64.445693), (-31.652722, -64.445301), (-31.652648, -64.445148), (-31.652635, -64.445111), (-31.652622, -64.445058), (-31.652642, -64.445028), (-31.652922, -64.443845), (-31.65294, -64.443795), (-31.652965, -64.44376), (-31.652999, -64.44374), (-31.653192, -64.443649), (-31.653248, -64.443597), (-31.653726, -64.442969), (-31.653884, -64.442771), (-31.654071, -64.442567), (-31.654477, -64.442146), (-31.654633, -64.441985), (-31.654701, -64.441888), (-31.654829, -64.441564), (-31.655539, -64.438943), (-31.655763, -64.438203), (-31.655879, -64.437803), (-31.656066, -64.437157), (-31.656127, -64.436953), (-31.656145, -64.436934), (-31.656172, -64.436929), (-31.656268, -64.436957), (-31.656541, -64.437008), (-31.656669, -64.437005), (-31.656722, -64.436981), (-31.656763, -64.436906), (-31.656827, -64.436758), (-31.656859, -64.436724), (-31.656907, -64.436705), (-31.657014, -64.436681), (-31.657672, -64.436635), (-31.657722, -64.436622), (-31.657735, -64.436584), (-31.65787, -64.435774), (-31.657891, -64.435723), (-31.657925, -64.435694), (-31.657973, -64.435691), (-31.65898, -64.435954), (-31.66016, -64.436179), (-31.660598, -64.436284), (-31.660954, -64.436372), (-31.66098, -64.436361), (-31.661005, -64.43634), (-31.661112, -64.436093), (-31.66177, -64.434714), (-31.661779, -64.434674), (-31.661755, -64.434619), (-31.661714, -64.434594), (-31.661041, -64.434179), (-31.66003, -64.433542), (-31.659959, -64.433502), (-31.659297, -64.433357), (-31.658505, -64.433186), (-31.658078, -64.433127), (-31.65762, -64.433054), (-31.656598, -64.432791), (-31.656375, -64.432751), (-31.654872, -64.432472), (-31.654773, -64.432456), (-31.654752, -64.432423), (-31.65476, -64.432313), (-31.654914, -64.43078), (-31.655135, -64.42852), (-31.65523, -64.427455), (-31.655245, -64.427424), (-31.65528, -64.427413), (-31.655332, -64.427418), (-31.655953, -64.427494), (-31.65711, -64.42765), (-31.657876, -64.42777), (-31.658093, -64.427806), (-31.658188, -64.427815), (-31.658279, -64.427831), (-31.658324, -64.427851), (-31.658701, -64.428075), (-31.659414, -64.428488), (-31.660379, -64.429087), (-31.660406, -64.42909), (-31.660437, -64.429079), (-31.660462, -64.429052), (-31.660918, -64.428123), (-31.661106, -64.42767), (-31.661133, -64.427643), (-31.66117, -64.427638), (-31.662462, -64.427879), (-31.6627769, -64.4279464), (-31.6633612, -64.4283408), (-31.664263, -64.4288633), (-31.6642992, -64.428866), (-31.664327, -64.4288421), (-31.6645544, -64.4282518), (-31.665494, -64.426095), (-31.665704, -64.425693), (-31.665795, -64.425508), (-31.665873, -64.425328), (-31.665891, -64.425312), (-31.665916, -64.425312), (-31.666096, -64.425476), (-31.666587, -64.425993), (-31.666738, -64.426264), (-31.666772, -64.426291), (-31.666818, -64.426299), (-31.667386, -64.426315), (-31.668874, -64.426401), (-31.668911, -64.42639), (-31.668925, -64.426355), (-31.668929, -64.426272), (-31.669002, -64.424599), (-31.669098, -64.423496), (-31.669089, -64.423467), (-31.669064, -64.423443), (-31.669023, -64.42344), (-31.668203, -64.423416), (-31.667571, -64.423421), (-31.667546, -64.423408), (-31.667528, -64.423373), (-31.667452, -64.423193), (-31.667334, -64.422944), (-31.667226, -64.422651), (-31.667181, -64.422429), (-31.667144, -64.422201), (-31.667133, -64.422171), (-31.667112, -64.422147), (-31.667087, -64.422139), (-31.6659158, -64.422123), (-31.6659391, -64.4234269), (-31.6655382, -64.4234147), (-31.6650091, -64.4233524), (-31.6639754, -64.4233409), (-31.6628243, -64.4233431), (-31.6628016, -64.4233244), (-31.6627976, -64.4232894), (-31.6628069, -64.4221335), (-31.662798, -64.420999), (-31.662813, -64.420481), (-31.662795, -64.418757), (-31.662798, -64.417072), (-31.66282, -64.415348), (-31.662823, -64.413588), (-31.662795, -64.411794), (-31.662807, -64.410152), (-31.662782, -64.410058), (-31.662736, -64.41001), (-31.66267, -64.409991), (-31.661656, -64.409889), (-31.659998, -64.409744), (-31.65922, -64.409696), (-31.658992, -64.409661), (-31.658731, -64.409562), (-31.658581, -64.40942), (-31.658455, -64.409154), (-31.658412, -64.409012), (-31.6584, -64.40891), (-31.6583997, -64.4087011), (-31.6583751, -64.4082558), (-31.6583389, -64.4068074), (-31.6583342, -64.4063288), (-31.6583435, -64.4063059), (-31.6583664, -64.4062958), (-31.6584932, -64.4062961), (-31.6585131, -64.4063191), (-31.658508, -64.4066397)]

maps.polyline()