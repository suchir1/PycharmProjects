best_list=[["Go"  ],["Purple",60,2,10,30,90,160,250 ],["Community Chest"  ],["Purple",60,4,20,60,180,320,450 ],["Income Tax"  ],["Railroad",200  ],["Light-Blue",100,6,30,90,270,400,550 ],["Chance"  ],["Light-Blue",100,6,30,90,270,400,550 ],["Light-Blue",120,8,40,100,300,450,600 ],["Jail"  ],["Violet",140,10,50,150,450,625,750 ],["Utilities",150  ],["Violet",140,10,50,150,450,625,750 ],["Violet",160,12,60,180,500,700,900 ],["Railroad",200  ],["Orange",180,14,70,200,550,750,950 ],["Community Chest"  ],["Orange",180,14,70,200,550,750,950 ],["Orange",200,16,80,220,600,800,1000 ],["Free Parking"  ],["Red",220,18,90,250,700,875,1050 ],["Chance"  ],["Red",220,18,90,250,700,875,1050 ],["Red",240,20,100,300,750,925,1100 ],["Railroad",200  ],["Yellow",260,22,110,330,800,975,1150 ],["Yellow",260,22,110,330,800,975,1150 ],["Utilities",150  ],["Yellow",280,24,120,360,850,1025,1200 ],["Go to Jail"  ],["Dark-Green",300,26,130,390,900,1100,1275 ],["Dark-Green",300,26,130,390,900,1100,1275 ],["Community Chest"  ],["Dark-Green",320,28,150,450,1000,1200,1400 ],["Railroad",200  ],["Chance"  ],["Dark-Blue",350,35,175,500,1100,1300,1500 ],["Luxury Tax"  ],["Dark-Blue",400,50,200,600,1400,1700,2000 ]]

pos_list = list(range(40))
print(len(best_list))
print(pos_list)

best_dictionary = dict(zip(pos_list, best_list))

print(best_dictionary)

empty_names = [['', 0] for _ in range(40)]



next_best_dictionary = dict(zip(pos_list, empty_names))



print(empty_names)
print(len(empty_names))

print(dict(zip(pos_list, empty_names)))