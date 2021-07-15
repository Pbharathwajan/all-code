print("CHEMISTRY PROJECT 2021-2022")
print("/n")
print(
    "ANIONS:\n1.chloride\n2.sulphate\n3.acetate\n4.nitrate\n5.carbonate\nCATIONS:\n1.magnesium\n2.zinc\n3.manganese\n4.lead\n5.calcium\n6.barium"
)
from prettytable import PrettyTable

s = "SALT ANALYSIS"
print("_".join(s))
anion = input("Enter the anion name:").lower()
cation = input("Enter the cation name:").lower()
# chloride
if anion == "chloride":
    myTable = PrettyTable(
        ["      experiment     ", "    observation    ", "   inferrence   "]
    )
    myTable.add_row(
        [
            "1. Colour of the salt\n is noted ",
            "white ",
            "Maybe lead , \ncadmium ,\n aluminium\n , zinc , calcium ,\n barium ,\n magnesium ions.",
        ]
    )
    myTable.add_row(
        [
            "2. Solubility        ",
            "Salt dissolves\n in water ",
            "Presence of water \nsoluble salt.",
        ]
    )
    myTable.add_row(
        [
            "3. Action of heat    ",
            "No characteristic\n change ",
            "Absence of \ncarbonate ,\n nitrate , zinc\n and ammonium\n ion.",
        ]
    )
    myTable.add_row(
        [
            "4. To a pinch of salt,\ndil. HCl is \nadded ",
            "Brisk effervescence\nis not observed ",
            "Absence of \ncarbonate ion.",
        ]
    )
    myTable.add_row(
        [
            "5. To a pinch of salt,\ndil. H2SO4 is\n added ",
            "Vinegar like smell\n is not observed ",
            "Absence of \nacetate ion",
        ]
    )
    myTable.add_row(
        [
            "6. To a pinch of salt,\nconc. H2SO4 is \nadded and\n heated ",
            "Colourless gas\n is evolved \nwhich gives\n dense white \nfumes with\n glass rod \ndipped in \nammonium hydroxide ",
            "Presence \nof chloride ion",
        ]
    )
    myTable.add_row(
        [
            "6.a To a pinch of salt\n,solid manganese \ndioxide and\n conc. H2SO4 is \nadded and\n the mixture is \nheated ",
            "Irritating greenish \nyellow gas is\n evolved ",
            "Presence of\n chloride\n ion is \nconfirmed",
        ]
    )
    myTable.add_row(
        [
            "6.b Chromyl Chloride\n Test:\nTo a pinch \nof salt,\npotassium dichromate\n and conc.H2SO4 is \nadded.Fumes \nare passed through\nNaOH solution;the\n resultant \nmixture acidified\n with \nlead acetate\n and acetic\n acid ",
            "Dark red vapours \ncondense at the \ncooler parts\n of the test tube\n and yellow\n solution is got which\n gives yellow\n precipitate \nwith lead acetate ",
            "Presence of chloride\n ion is confirmed",
        ]
    )
    myTable.add_row(
        [
            "7. To a pinch of salt,\nconc. H2SO4 and\n copper turnings\n are added and heated ",
            "Evolution of reddish\n brown\n gas is not observed ",
            "Absence of\n nitrate ion",
        ]
    )
    print(myTable)
    print("Preparation Of Sodium Carbonate Extract:")
    print(
        "1 gram of the given salt is mixed with 2 grams of sodium carbonate in a 100ml beaker.20ml of distilled water is added to it and the solution is boiled for 10 minutes.The solution is then filtered and the filtrate is called as sodium carbonate extract."
    )
    myTable = PrettyTable(
        [
            "experiment                  ",
            "observation                 ",
            "inferrence                         ",
        ]
    )
    myTable.add_row(
        [
            "6.c To the extract\ndil.HNO3 \nis added till effervescence\n stops after which\n silver nitrate\n solution is added ",
            "White precipitate which is soluble\n in ammonium hydroxide is\n obtained ",
            "Presence of chloride \nion is confirmed",
        ]
    )
    myTable.add_row(
        [
            "8. To the extract\n dil.HCl \nis added till effervescence \nstops and then barium\n chloride\n is added ",
            "No white precipitate \nis obtained ",
            "Absence of \nsulphate ion",
        ]
    )
    myTable.add_row(
        [
            "9. To the extract\n conc.HNO3 \nis added till effervescence \nstops;ammonium \nmolybdate\n is then added and the \nmixture boiled ",
            "Canary yellow precipitate\n is not obtained ",
            "Absence of\n phosphate ion",
        ]
    )
    myTable.add_row(myTable)
    print("The given salt contains the anion:Chloride")
# sulphate
elif anion == "sulphate":
    myTable = PrettyTable(
        ["      experiment     ", "    observation    ", "   inferrence   "]
    )
    myTable.add_row(
        [
            "1. Colour of the salt is noted ",
            "white          ",
            "Maybe lead ,\n cadmium , aluminium\n , zinc , calcium\n , barium ,\n magnesium ions.",
        ]
    )
    myTable.add_row(
        [
            "2. Solubility                  ",
            "Salt dissolves in \nwater ",
            "Presence of water soluble salt.",
        ]
    )
    myTable.add_row(
        [
            "3. Action of heat              ",
            "White colour substance\n changed into\n yellow colour on\n heating ",
            "Maybe zinc ion",
        ]
    )
    myTable.add_row(
        [
            "4. To a pinch of salt,dil. HCl \nis added ",
            "Brisk effervescence is\n not observed",
            "Absence of carbonate\n ion.",
        ]
    )
    myTable.add_row(
        [
            "5. To a pinch of salt,dil. H2SO4\n is added ",
            "Vinegar like smell\n is not observed",
            "Absence of acetate\n ion",
        ]
    )
    myTable.add_row(
        [
            "6. To a pinch of salt,conc. H2SO4 \nis added\n and heated",
            "No characterstic change",
            "Absence of chloride\n and nitrate ion",
        ]
    )
    print(myTable)
    print("Preparation Of Sodium Carbonate Extract:")
    print(
        "1 gram of the given salt is mixed with 2 grams of sodium carbonate in a 100ml beaker.20ml of distilled water is added to it and the solution is boiled for 10 minutes.The solution is then filtered and the filtrate is called as sodium carbonate extract."
    )
    myTable = PrettyTable(
        ["      experiment     ", "    observation    ", "   inferrence   "]
    )
    myTable.add_row(
        [
            "7. To a pinch of salt dil.HCl\n is added till the effervescence\n stops and then barium\n chloride is added",
            "White precipitate\n insoluble in conc.HCl\n is obtained ",
            "Presence of sulphate\n ion",
        ]
    )
    myTable.add_row(
        [
            "7.a To the extract dil.CH3COOH\n is added till the effervescence\n stops and then barium\n chloride is added",
            "White precipitate\n soluble in ammonium \nacetate and NaOH is\n obtained",
            "Presence of sulphate\n ion is confirmed",
        ]
    )
    myTable.add_row(
        [
            "8. To the extract conc.HNO3\n is added till effervescence stops;\nammonium molybdate is \nthen added and the mixture\n boiled",
            "Canary yellow\n precipitate is not\n obtained",
            "Absence of phosphate ion",
        ]
    )
    print(myTable)
    print("The given salt contains the anion:Sulphate")
# acetate
elif anion == "acetate":
    myTable = PrettyTable(
        ["      experiment     ", "    observation    ", "   inferrence   "]
    )
    myTable.add_row(
        [
            "1. Colour of the salt is noted",
            "white ",
            "Maybe lead , cadmium ,\n aluminium , zinc , calcium \n, barium , magnesium ions.",
        ]
    )
    myTable.add_row(
        [
            "2. Solubility                 ",
            "Salt dissolves in water ",
            "Presence of water soluble \nsalt.",
        ]
    )
    myTable.add_row(
        [
            "3. Action of heat             ",
            "No characteristic change ",
            "Absence of carbonate , nitrate ,\n zinc and ammonium ion.",
        ]
    )
    myTable.add_row(
        [
            "4. To a pinch of salt,dil. \nHCl is added ",
            "Brisk effervescence is not \nobserved ",
            "Absence of \ncarbonate ion.",
        ]
    )
    myTable.add_row(
        [
            "5. To a pinch of salt,dil. \nH2SO4 is added ",
            "Vinegar like smell is \nobserved ",
            "Presence of \nacetate ion",
        ]
    )
    myTable.add_row(
        [
            "6.a To a salt solution \nneutral ferric chloride\n solution is \nadded ",
            "Reddish brown \ncoloration is\n observed ",
            "Presence of acetate \nion is confirmed",
        ]
    )
    myTable.add_row(
        [
            "6.b To a pinch of salt,conc.\nH2SO4 is added and\n heated.Then \nethyl alcohol is added,\nthe mixture poured into\n beaker full of water \nand stirreed ",
            "Fruity odour is \nobserved ",
            "Presence of acetate \nion is confirmed",
        ]
    )
    myTable.add_row(
        [
            "7. To a pinch of salt,conc. \nH2SO4 is added and\n heated ",
            "No characterstic change ",
            "Absence of chloride\n and nitrate ion",
        ]
    )
    print(myTable)
    myTable = PrettyTable(
        ["      experiment     ", "    observation    ", "   inferrence   "]
    )
    print("Preparation Of Sodium Carbonate Extract:")
    print(
        "1 gram of the given salt is mixed with 2 grams of sodium carbonate in a 100ml beaker.20ml of distilled water is added to it and the solution is boiled for 10 minutes.The solution is then filtered and the filtrate is called as sodium carbonate extract."
    )
    myTable.add_row(
        [
            "8. To a pinch of salt dil.HCl\n is added till the effervescence\n stops and then barium\n chloride is added ",
            "White precipitate insoluble\n in conc.HCl is not\n obtained ",
            "Absence of sulphate ion",
        ]
    )
    myTable.add_row(
        [
            "9. To the extract conc.HNO3\n is added till effervescence stops;\nammonium molybdate is then\n added and the mixture boiled",
            "Canary yellow precipitate\n is not obtained ",
            "Absence of phosphate ion",
        ]
    )
    print(myTable)
    print("The given salt contains the anion:Acetate")
# nitrate
elif anion == "nitrate":
    myTable = PrettyTable(
        ["      experiment     ", "    observation    ", "   inferrence   "]
    )
    myTable.add_row(
        [
            "1. Colour of the salt is noted",
            "white ",
            "Maybe lead , cadmium ,\n aluminium , zinc ,\n calcium , barium ,\n magnesium ions.",
        ]
    )
    myTable.add_row(
        [
            "2. Solubility                 ",
            "Salt dissolves in water",
            "Presence of water soluble\n salt.",
        ]
    )
    myTable.add_row(
        [
            "3. Action of heat             ",
            "Salt decrepitates;evolution\n of brown gas ",
            "Maybe nitrate of lead\n or bariumS",
        ]
    )
    myTable.add_row(
        [
            "4. To a pinch of salt,dil. HCl\n is added ",
            "Brisk effervescence is\n not observed ",
            "Absence of carbonate ion.",
        ]
    )
    myTable.add_row(
        [
            "5. To a pinch of salt,dil.\n H2SO4 is added ",
            "Vinegar like smell is\n not observed ",
            "Absence of acetate\n ion",
        ]
    )
    myTable.add_row(
        [
            "6. To a pinch of salt,conc.\n H2SO4 is added and heated",
            "No colourless gas\n evolved that gives \ndense white fumes when\n a glass rod dipped in\n aquous ammonia is brought\n near the mouth of the\n test tube ",
            "Absence of chloride ion",
        ]
    )
    myTable.add_row(
        [
            "7. To a pinch of salt conc.\n H2SO4 and copper turnings\n are added and heated ",
            "Evolution of reddish \nbrown gas is observed ",
            "Presence of nitrate ion",
        ]
    )
    print(myTable)
    print("Preparation Of Sodium Carbonate Extract:")
    print(
        "1 gram of the given salt is mixed with 2 grams of sodium carbonate in a 100ml beaker.20ml of distilled water is added to it and the solution is boiled for 10 minutes.The solution is then filtered and the filtrate is called as sodium carbonate extract."
    )
    myTable = PrettyTable(
        ["      experiment     ", "    observation    ", "   inferrence   "]
    )
    myTable.add_row(
        [
            "7.a To the extract dil.H2SO4\n is added to expel CO2\n after which freshly prepared\n ferrous sulphate solution \nis added followed by \nconc.H2SO4 added along\n the sides of the test tube\n without shaking it",
            "Brown ring is formed \nat the junction of the \ntwo liquids ",
            "Presence of nitrate\n ion is confirmed",
        ]
    )
    myTable.add_row(
        [
            "8. To the extract dil.HCl\nis added till the effervescence\n stops and then barium \nchloride is added ",
            "White precipitate is not\n obtained ",
            "Absence of sulphate ion",
        ]
    )
    myTable.add_row(
        [
            "9. To the extract conc.HNO3\n is added till effervescence\n stops;ammonium molybdate \nis then added and the\n mixture boiled ",
            "Canary yellow precipitate\n is not obtained",
            "Absence of phosphate ion",
        ]
    )
    print(myTable)
    print("The given salt contains the anion:Nitrate")
# carbonate
elif anion == "carbonate":
    myTable = PrettyTable(
        ["      experiment     ", "    observation    ", "   inferrence   "]
    )
    myTable.add_row(
        [
            "1. Colour of the salt is noted",
            "white ",
            "Maybe lead , cadmium ,\n aluminium , zinc , \ncalcium , barium ,\n magnesium ions.",
        ]
    )
    myTable.add_row(
        [
            "2. Solubility                 ",
            "Salt dissolves in water",
            "Presence of water soluble\n salt.",
        ]
    )
    myTable.add_row(
        [
            "3. Action of heat             ",
            "Evolution of colourless,\nodourless gas which turns \nlime water milky ",
            "Maybe carbonate ion",
        ]
    )
    myTable.add_row(
        [
            "3.a Sublimes on the upper part \nof the test tube ",
            "-",
            "Maybe ammonium ion",
        ]
    )
    myTable.add_row(
        [
            "4. To a pinch of salt,dil. HCl\nis added ",
            "Brisk effervescence is \nobserved",
            "Presence of carbonate ion.",
        ]
    )
    myTable.add_row(
        [
            "4.a To a pinch of salt,dil.\nbarium chloride is added\n and heated ",
            "White precipitate which is\n soluble in dil.HCl is \nobtained ",
            "Presence of carbonate ion\n is confirmed",
        ]
    )
    myTable.add_row(
        [
            "5. To a pinch of salt,dil. \nH2SO4 is added ",
            "Vinegar like smell is not\n observed ",
            "Absence of acetate ion",
        ]
    )
    myTable.add_row(
        [
            "6. To a pinch of salt,conc. \nH2SO4 is added and heated ",
            "No characterstic change ",
            "Absence of chloride and nitrate\n ion",
        ]
    )
    print(myTable)
    print("Preparation Of Sodium Carbonate Extract:")
    print(
        "1 gram of the given salt is mixed with 2 grams of sodium carbonate in a 100ml beaker.20ml of distilled water is added to it and the solution is boiled for 10 minutes.The solution is then filtered and the filtrate is called as sodium carbonate extract."
    )
    myTable = PrettyTable(
        ["      experiment     ", "    observation    ", "   inferrence   "]
    )
    myTable.add_row(
        [
            "7. To the extract dil.HCl is\n added till the effervescence stops \nand then barium chloride is\n added ",
            "White precipitate is not \nobtained ",
            "Absence of sulphate ion",
        ]
    )
    myTable.add_row(
        [
            "9. To the extract conc.HNO3 is \nadded till effervescence stops;\nammonium molybdate is then\n added and the mixture boiled ",
            "Canary yellow precipitate is\n not obtained ",
            "Absence of phosphate ion",
        ]
    )
    print("The given salt contains the anion:Carbonate")
    print(myTable)
else:
    print("The given anion is out of the list.")

# magnesium
if cation == "magnesium":
    print(
        "preparation of orginal solution(OS):OS is prepared by dissolving the salt in water"
    )
    print("GROUP SEPERATION:")
    myTable = PrettyTable(
        ["      experiment     ", "    observation    ", "   inferrence   "]
    )
    myTable.add_row(
        [
            "0.To OS few drop of Nesslers\n reagent and excess of \nNaoh is added",
            "brown precipate is not\n obtained",
            "absence of group 0 \ncation",
        ]
    )
    myTable.add_row(
        [
            "1.To a few drop of OS dil.\n HCl is added ",
            "White precipitate is not \nobtained",
            "Absence of group I \ncation",
        ]
    )
    myTable.add_row(
        [
            "2.To a few drop of OS dil.\n HCl and YAS are added ",
            "Black precipitate is not \nobtained",
            "Absence of group II \ncation",
        ]
    )
    myTable.add_row(
        [
            "3.To a few drops of OS NH4Cl\n AND NH4OH are added ",
            "Gelatinous white precipitate\n is not obtained",
            "Abasence of gropup III\n cation",
        ]
    )
    myTable.add_row(
        [
            "4.TO a few drops of OS NH4Cl\n,NH4OH are added ",
            "NO characteristic change",
            "Absence of IV cation",
        ]
    )
    myTable.add_row(
        [
            "5.TO a few drops of OS NH4CL\n,NH4OH and (NH4)2co3 are\n added",
            "white is not obtained",
            "Absence of group V \ncation",
        ]
    )
    myTable.add_row(
        [
            "6.TO a few drops of OS NH4OH\n and disodium hydrogen phosphate\n solution are added",
            "White precipitate is\n Obtained",
            "presence of group VI \ncation[Magnesium ion]",
        ]
    )
    print(myTable)
    print("CONFIRMATORY TEST:")
    print("GROUP-5")
    myTable = PrettyTable(
        ["      experiment     ", "    observation    ", "   inferrence   "]
    )
    myTable.add_row(
        [
            "1.TO the salt solution,\nmagnesium reagent and NAoh\n are added",
            "Blue precipitate is \nobtained",
            "Presence of Magnesium \nion is confirmed",
        ]
    )
    myTable.add_row(
        [
            "2.ASH TEST A small amount of\n the salt is made into a \npaste with conc.HNO3 and 2\n drops of cobalt nitrate \nsolution.A filter paper soked\n in this mixture is introdeced\n into the bunsen flame and ignited.\nThe colour of the ash is noted",
            "pink ash is obtained",
            "presence of magnesium is\n confirmed",
        ]
    )
    print(myTable)
    print("RESULT: ")
    print("the given salt contains cation: Magnesium")
# zinc
elif cation == "zinc":
    print(
        "preparation of orginal solution(OS):OS is prepared by dissolving the salt in water"
    )
    print("GROUP SEPERATION:")
    myTable = PrettyTable(
        ["      experiment     ", "    observation    ", "   inferrence   "]
    )
    myTable.add_row(
        [
            "0.To a few drop OS a few drops\n Nessler reagent and excess \nof NAOH are added ",
            "Brown precipiate is not \nobtained",
            "Absence of Group 0 cation",
        ]
    )
    myTable.add_row(
        [
            "1.TO a few drops of OS dil Hcl\n is added ",
            "White precipitate is not \nobtained",
            "Absence of group I cation",
        ]
    )
    myTable.add_row(
        [
            "2.TO a few drops of OS dil Hcl\n and YAS are added ",
            "Black precipitate is not \nobtained",
            "Absence of Group II cation",
        ]
    )
    myTable.add_row(
        [
            "3.TO a few drops of OS NH4Cl\n and NA4OH are added ",
            "Gelatinous white precipitate is \nnot obtained",
            "Absence of Group III cation",
        ]
    )
    myTable.add_row(
        [
            "4.To a few drops drops of NH4Cl\n,NH4OH and YAS are added ",
            "dirty white precipitate is \nobtained",
            "Presence of Group IV \ncation[Zinc]",
        ]
    )
    print(myTable)
    print("CONFIRMATORY TEST:")
    myTable = PrettyTable(
        ["      experiment     ", "    observation    ", "   inferrence   "]
    )
    myTable.add_row(
        [
            "1.To a few drop of OS,NAOH\n solution is added in excess",
            "White precipitate solution in\n excess of NAOH is got",
            "presence of Zinc ion is\n confirmed",
        ]
    )
    myTable.add_row(
        [
            "2.To a few drop of OS ,2ml\n of potassium ferrocyanide\n is added",
            "Dirty white precipitate\n solute in excess of NAOH is\n obtained ",
            "presence of Zinc ion is\n confirmed",
        ]
    )
    myTable.add_row(
        [
            "3.ASH TEST A small amount of\n the salt is made into a \npaste with conc.HNO3 and 2\n drops of cobalt nitrate \nsolution.A filter paper soked\n in this mixture is introdeced\n into the bunsen flame and ignited.\nThe colour of the ash is noted",
            "pinmanns green ash is \nobtained",
            "Presence of zinc ion is \nconfirmed",
        ]
    )
    print(myTable)
    print("RESULT: ")
    print("the given salt contains cation: Zinc")
# manganese
elif cation == "maganese":
    print(
        "preparation of orginal solution(OS):OS is prepared by dissolving the salt in water"
    )
    print("GROUP SEPERATION:")
    myTable = PrettyTable(
        ["      experiment     ", "    observation    ", "   inferrence   "]
    )
    myTable.add_row(
        [
            "0.To a few drops of OS a few\n drops nessler reagent and\n excess of NAOH are added ",
            "Brown precipitate is \nobtained",
            "Absence of group 0 catiom",
        ]
    )
    myTable.add_row(
        [
            "1.To a few drops of OS dil.\nHCl is added ",
            "white precipate is not \nobtained",
            "Absence of group I cation",
        ]
    )
    myTable.add_row(
        [
            "2.To few drop of OS dil.HCl\n and YAS are added ",
            "Black precipate is not\n obtained",
            "Absence of group II cation",
        ]
    )
    myTable.add_row(
        [
            "3.To a few drop of OS NH4Cl\n and NH4OH are added ",
            "Gelatinous white precipitate is\n not obtained",
            "Absence group III cation",
        ]
    )
    myTable.add_row(
        [
            "4.To a few drop of OS NH4Cl,\nNH4OH and YAS are added ",
            "Buff coloured precipitate is \nnot obtained",
            "Presence of group IV \ncation[Maganese ion]",
        ]
    )
    print(myTable)
    print("CONFIRMATORY TEST:")
    myTable = PrettyTable(
        ["      experiment     ", "    observation    ", "   inferrence   "]
    )
    myTable.add_row(
        [
            "1.To afew drop of OS,NAOH\n solution is added ",
            "white precipitate is obtained",
            "Presence of maganese ion is \nconfirmed",
        ]
    )
    myTable.add_row(
        [
            "2.Toa few drop pf OS,dilute\n HNO3 and sodium are added and\n solution is diluted",
            "Pink coloration is observed",
            "presence of maganese ion is\n confirmed",
        ]
    )
    print(myTable)
    print("RESULT: ")
    print("the given salt contains cation: manganese")
# lead
elif cation == "lead":
    print(
        "preparation of orginal solution(OS):OS is prepared by dissolving the salt in water"
    )
    print("GROUP SEPERATION:")
    myTable = PrettyTable(
        ["      experiment     ", "    observation    ", "   inferrence   "]
    )
    myTable.add_row(
        [
            "0. To a few drops of OS a\n few drops of nessler's \nreagent and excess of NaOH\n is added ",
            "brown precipitate is not\n obtained ",
            "absence of group 0 cation\n (ammonium) ",
        ]
    )
    myTable.add_row(
        [
            "1. To a few drops of OS \ndil.Hcl is added ",
            "white precipitate soluble\n in excess hot water ",
            "presence of group 1 cation\n (lead)",
        ]
    )
    print(myTable)
    print("CONFIRMATORY TEST:")
    print("GROUP-1")
    myTable = PrettyTable(
        ["      experiment     ", "    observation    ", "   inferrence   "]
    )
    myTable.add_row(
        [
            "1. To a few drops of OS add\n few drops of pottaisum chromate\n solution",
            "yellow precipitate is obtained",
            "presence of lead ion is\n confirmed",
        ]
    )
    myTable.add_row(
        [
            "2. To a few drops of OS add\n 2ml of potassium iodide solution",
            "yelow precipitate that dissolves\n in hot water and reappears as\n golden spangles is obtained",
            "presence of lead ion is\n confirmed",
        ]
    )
    print(myTable)
    print("RESULT: ")
    print("the given salt conains cation:lead")
# calcium
elif cation == "calcium":
    print(
        "preparation of orginal solution(OS):OS is prepared by dissolving the salt in water"
    )
    print("GROUP SEPERATION:")
    myTable = PrettyTable(
        ["      experiment     ", "    observation    ", "   inferrence   "]
    )
    myTable.add_row(
        [
            "0. To a few drops of OS a few\n drops of nessler's reagent\n and excess of NaOH is added",
            "brown precipitate is not \nobtained",
            "absence of group\n 0 cation",
        ]
    )
    myTable.add_row(
        [
            "1. To a few drops of OS dil.Hcl\n is added",
            "white precipitate is not\n obtained",
            "absence of group 1 \ncation",
        ]
    )
    myTable.add_row(
        [
            "2. To a few drops of OS dil.Hcl\n and YAS are added",
            "black precipitate is\n not obtained",
            "absence of group\n 2 cation",
        ]
    )
    myTable.add_row(
        [
            "3. To a few drops of OS NH4cl\n and NH4OH are added",
            "gelatanious white precipitate\n is not obtained",
            "absence of group 3\n cation",
        ]
    )
    myTable.add_row(
        [
            "4. To a few drops of OS NH4cl\n ,NH4OH and YAS are added",
            "no characteristic change",
            "absence of group 4\n cation",
        ]
    )
    myTable.add_row(
        [
            "5. To a few drops of OS NH4cl\n ,NH4OH and (NH4)2CO3 \nare added",
            "white precipitate is\n obtained",
            "presence of group 5\n cation",
        ]
    )
    print(myTable)
    print("CONFIRMATORY TEST:")
    print("GROUP-5")
    myTable = PrettyTable(
        ["      experiment     ", "    observation    ", "   inferrence   "]
    )
    myTable.add_row(
        [
            "1. To a few drops of OS, 2ml\n of ammonium acetate is added",
            "white precipitate is\n obtained",
            "presence of calcium ion\n is confirmed",
        ]
    )
    myTable.add_row(
        [
            "2. FLAME TEST: a small amount\n of salt is made into paste\n with conc.Hcl in a watch\n glass and introduced into the\n non- luminous past of the\n flame using a glass rod. \nColour of the flame is noted",
            "brick red flame is \nseen",
            "presence of calcium ion\n is confirmed",
        ]
    )
    print(myTable)
    print("RESULT: ")
    print("the given salt contains cation: calcium")
# barium
elif cation == "barium":
    print(
        "preparation of orginal solution(OS):OS is prepared by dissolving the salt in water"
    )
    print("GROUP SEPERATION:")
    myTable = PrettyTable(
        ["      experiment     ", "    observation    ", "   inferrence   "]
    )
    myTable.add_row(
        [
            "0. To a few drops of OS \na few drops of nessler's\n reagent and excess of NaOH\n is added",
            "brown precipitate is not\n obtained",
            "absence of group 0 \ncation",
        ]
    )
    myTable.add_row(
        [
            "1. To a few drops of OS \ndil.Hcl is added",
            "white precipitate is not\n obtained",
            "absence of group 1 \ncation",
        ]
    )
    myTable.add_row(
        [
            "2. To a few drops of OS \ndil.Hcl and YAS are added",
            "black precipitate is not\n obtained",
            "absence of group 2 \ncation",
        ]
    )
    myTable.add_row(
        [
            "3. To a few drops of OS \nNH4cl and NH4OH are added",
            "gelatanious white precipitate\n is not obtained",
            "absence of group 3 \ncation",
        ]
    )
    myTable.add_row(
        [
            "4. To a few drops of OS \nNH4cl ,NH4OH and YAS are \nadded",
            "no characteristic change",
            "absence of group 4\n cation",
        ]
    )
    myTable.add_row(
        [
            "5. To a few drops of OS \nNH4cl ,NH4OH and (NH4)2CO3\n are added",
            "white precipitate is \nobtained",
            "presence of group 5\n cation",
        ]
    )
    print(myTable)
    print("CONFIRMATORY TEST:")
    print("GROUP-5")
    myTable = PrettyTable(
        ["      experiment     ", "    observation    ", "   inferrence   "]
    )
    myTable.add_row(
        [
            "1. To a few drops of OS, 2ml\n of ammonium acetate is added",
            "yellow precipitate \nis obtained",
            "presence of barium is\n confirmed",
        ]
    )
    myTable.add_row(
        [
            "2. FLAME TEST: a small amount\n of salt is made into paste\n with conc.Hcl in a watch\n glass and introduced into the\n non- luminous past of the\n flame using a glass rod. \nColour of the flame is noted",
            "apple green colour\n flame is seen",
            "presence of barium ion \nis confirmed",
        ]
    )
    print(myTable)
    print("RESULT: ")
    print("the given salt contains cation: Barium")
# aluminium
elif cation == "aluminum":
    myTable = PrettyTable(
        ["      experiment     ", "    observation    ", "   inferrence   "]
    )

    myTable.add_row(
        [
            "1. The color of salt noted ",
            " white            ",
            "Maybe Lead,Cadmium,Aluminium\n,Zinc,Calcium,Barium\n,Magnessium ions",
        ]
    )
    myTable.add_row(
        [
            "2. Solubility              ",
            "Dissloves in water",
            "Presence of water soluble salt",
        ]
    )
    myTable.add_row(
        ["3. Action of the Heat      ", "Evolution of brown gas ", "Maybe Nitrate ion"]
    )
    myTable.add_row(
        [
            "4. To a pinch of Salt, dil \nHCl is added ",
            "Brisk efferense isnt \noberserved ",
            "Absence of Carbonate ion",
        ]
    )
    myTable.add_row(
        [
            "5. To a pinch of Salt, H2So4\n is added ",
            "Vinegar like smell isnt\nobserved ",
            "Absence of Acetate ion",
        ]
    )
    myTable.add_row(
        [
            "6. To a pinch of Salt, conc\n H2So4 and Copper turnings are\n added and heated ",
            "Evolution of reddish \nbrown gas ",
            "Presebce of Nitrate ion",
        ]
    )
    myTable.add_row(
        [
            "7. To a extract dil H2So4 is\n added to expel Co2 after \nwhich freshky prepared \nFerrous Sulphate Solution is\n added followed by addition \nof coonc H2So4 is added\n without shaking ",
            "Brown ring is formed at\n the junction ",
            "Presence of Nitrate ion is \nConfirmed",
        ]
    )
    myTable.add_row(
        [
            "8. The extract dil HCl is \nadded till efferesence is \nstopped ",
            "White precipitate is\n obtained ",
            "Absence of Sulphate ion",
        ]
    )
    print(myTable)
    print("GROUP SELECTION:")
    myTable = PrettyTable(
        ["      experiment     ", "    observation    ", "   inferrence   "]
    )

    myTable.add_row(
        [
            "1. To a few drops of OS dil\n HCl ",
            "White precipitate ist obtained",
            "Absence of Group I cation",
        ]
    )
    myTable.add_row(
        [
            "2. To a few drops of dil HCl\n and YAS are added ",
            "Black precipitate isnt obtaied",
            "Absence of Group II cation",
        ]
    )
    myTable.add_row(
        [
            "3. To a few drops of OS,NH4Cl\n and NH4OH are added",
            "Gelatanious White is obtained",
            "Presence of Group III cation",
        ]
    )
    print(myTable)
    print("CONFIRMATORY TEST:")
    myTable = PrettyTable(
        ["      experiment     ", "    observation    ", "   inferrence   "]
    )

    myTable.add_row(
        [
            "1. To a few drops of OS, NaOH is\n added",
            "White precipitate sol\n inn excess in excess NaoH",
            "Presence of Aluminium ion\n is confirmed ",
        ]
    )
    myTable.add_row(
        [
            "2. ASH TEST: A small amount of\n salt is made into a paste with\n HNO3 and 2 drops of cobalt \nniterate solution.A filter is \nsoaked and burnt in flame",
            "Ther=nard blue ash id got",
            "Presence of aluminium ion is\n confirmed",
        ]
    )
    print(myTable)
    print("RESULT:")
    print("The given salt contains contains:cation:ALUMINIUM")
# ammonium
elif cation == "ammonium":
    myTable = PrettyTable(
        ["      experiment     ", "    observation    ", "   inferrence   "]
    )

    myTable.add_row(
        [
            "1. The color of salt noted ",
            " white ",
            "Maybe Lead,Cadmium,Aluminium,\nZinc,Calcium,Barium,\nMagnessium ions",
        ]
    )
    myTable.add_row(
        [
            "2. Solubility              ",
            "Dissloves in water ",
            "Presence of water \nsoluble salt",
        ]
    )
    myTable.add_row(
        ["3. Action of the Heat      ", "Evolution of brown gas ", "Maybe Nitrate ion"]
    )
    myTable.add_row(
        [
            "4. To a pinch of Salt, dil \nHCl is added ",
            "Brisk efferense isnt \noberserved ",
            "Absence of Carbonate ion",
        ]
    )
    myTable.add_row(
        [
            "5. To a pinch of Salt, H2So4\n is added ",
            "Vinegar like smell isnt \nobserved ",
            "Absence of Acetate ion",
        ]
    )
    myTable.add_row(
        [
            "6. To a pinch of Salt, conc\n H2So4 and Copper turnings\n are added and heated ",
            "Evolution of reddish brown\n gas ",
            "Presebce of Nitrate ion",
        ]
    )
    myTable.add_row(
        [
            "7. To a extract dil H2So4 is\n added to expel Co2 after\n which freshky prepared Ferrous\n Sulphate Solution is added \nfollowed by addition of coonc\n H2So4 is added without shaking ",
            "Brown ring is formed at the\n junction ",
            "Presence of Nitrate ion is \nConfirmed",
        ]
    )
    myTable.add_row(
        [
            "8. The extract dil HCl is \nadded till efferesence is\n stopped ",
            "White precipitate is \nobtained ",
            "Absence of Sulphate ion",
        ]
    )
    print(myTable)
    print("GROUP SELECTION:")
    myTable = PrettyTable(
        ["      experiment     ", "    observation    ", "   inferrence   "]
    )

    myTable.add_row(
        [
            "1. To a few drops of OS dil\n HCl is added",
            "White precipitate ist obtained",
            "Absence of Group I cation",
        ]
    )
    myTable.add_row(
        [
            "2. To a few drops of dil HCl\n and YAS are added ",
            "Black precipitate isnt obtaied",
            "Absence of Group II cation",
        ]
    )
    myTable.add_row(
        [
            "3. To a few drops of OS,NH4Cl\n and NH4OH are added",
            "Gelatanious White is obtained",
            "Presence of Group III cation",
        ]
    )
    myTable.add_row(
        [
            "4. To a few drops os OS,NH4Cl\n ,NH4OH and YAS are added",
            "No change",
            "Absence of group IV cation",
        ]
    )
    myTable.add_row(
        [
            "5. To a few drops of OS, NH4OH\n and dis NH4Cl and \(NH4\)2\n , CO3 are added ",
            "White precipitate isnt obtained",
            "Absence of group V cation",
        ]
    )
    myTable.add_row(
        [
            "6. To a few drops of OS, \nNH4OH and disodium hydrogen\n phosphate are added ",
            "White isnt obtained ",
            "Absence of froup VI cation",
        ]
    )
    print(myTable)
    print("CONFIRMATORY TEST:")
    myTable = PrettyTable(
        ["      experiment     ", "    observation    ", "   inferrence   "]
    )

    myTable.add_row(
        [
            "1. To a pinch of salt,dil NAOH\n solution is added and heated",
            "Colorless gas is evolved which\n gives dense white fumes \nwhen glass rod is dipped in HCl",
            "Presence of ammonium ion\n is confirmed",
        ]
    )
    print(myTable)
    print("RESULT:")
    print("The given salt contains the cation:AMMONIUM")