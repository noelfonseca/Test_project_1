import re
string = '''A new decision support system to analyse the impacts of climate change on the Hungarian forestry and agricultural sectors, 2016

10.1080/02827581.2016.1212088

2

Upland development, climate-related risk and institutional conditions for adaptation in Vietnam, 2016

10.1080/17565529.2015.1067178

3

Vulnerability of tropical forest ecosystems and forest dependent communities to droughts, 2016

10.1016/j.envres.2015.10.022

4

Assessing the potential for forest management practitioner participation in climate change adaptation, 2016

10.1016/j.foreco.2015.09.038

5

Exploring the role of forest resources in reducing community vulnerability to the heat effects of climate change

10.1016/j.forpol.2015.09.001

6

A complex adaptive systems perspective of forest policy in China

10.1016/j.techfore.2016.08.024

7

Socio-economic factors influencing household dependence on forests and its implication for forest-based climate change interventions

10.2989/20702620.2016.1255420

8

Climate change and Australian production forests: impacts and adaptation

10.1080/00049158.2017.1360170

9

A walk on the wild side: Disturbance dynamics and the conservation and management of European mountain forest ecosystems

10.1016/j.foreco.2016.07.037

10

Vulnerability of Community-Based Forest Management to Climate Variability and Extremes: Emerging Insights on the Contribution of REDD

10.1007/s11842-016-9354-x

11

The importance of socio-ecological system dynamics in understanding adaptation to global change in the forestry sector

10.1016/j.jenvman.2017.02.066



I also attached a word copy of this list.


Thanks you so much!


Best,

'''
def doi_searcher(text):
	doiSearchRegex = re.compile(r'\b(10[.][0-9]{4,}(?:[.][0-9]+)*/(?:(?!["&\'])\S)+)\b')
	mo = doiSearchRegex.findall(text)
	print(mo)
	
doi_searcher(string)

print(len(string))