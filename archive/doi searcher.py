import re
string = '''25. Ahmed, F. et al. Te addition of submergence-tolerant Sub1 gene into high yielding MR219 rice variety and analysis of its BC2F3
population in terms of yield and yield contributing characters to select advance lines as a variety. Biotechnol Biotechnol Equip 30,
853–863 (2016).
26. Sarkar, R. K. et al. Performance of submergence tolerant rice genotypes carrying the Sub1 QTL under stressed and non-stressed
natural feld conditions. Indian J Agric Sci 79, 876–83 (2009).
27. Singh, R. et al. From QTL to variety harnessing the benefts of QTLs for drought, food and salt tolerance in mega rice varieties of
India through a multi-institutional network. Plant Sci 242, 278–287 (2015).
28. Brown, J. K. M. Yield penalties of disease resistance in crops. Curr Opin Plant Biol 5, 339–344 (2002).
29. Johnston, P. et al. Marker assisted separation of resistance genes Rph22 and Rym16Hb from an associated yield penalty in a barley:
Hordeum bulbosum introgression line. Teor Appl Genet 128, 1137–1149 (2015).
30. Sheng, X. & Li, Z. Genetic efects of cytoplasm in hybrid rice, in Hybrid Rice, IRRI, Los Banos, Philippines, 258–259 (1988).
31. Waza, S. A. & Jaiswal, H. K. Effects of WA cytoplasm on various quality characteristics of rice hybrids. J Anim Plant Sci 25,
1693–1698 (2015).
32. Neeraja, C. N. et al. A marker-assisted backcross approach for developing submergence-tolerant rice cultivars. Teor Appl Genet 115,
767–776, https://doi.org/10.1007/s00122-007-0607-0 (2007).
33. Dar, M. H. et al. Transforming rice cultivation in food prone coastal Odisha to ensure food and economic security. Food Sec. 9,
711–722, https://doi.org/10.1007/s12571-017-0696-9 (2017).
34. Courtois, B. et al. Mapping QTL associated with drought avoidance in upland rice. Mol Breed 6, 55–66 (2000).
35. Brunings, A. M. et al. Diferential gene expression of rice in response to silicon and rice blast fungus Magnaporthe oryzae. Ann Appl
Biol 155, 161–170, https://doi.org/10.1111/j.1744-7348.2009.00347.x (2009).
36. Divya, B., Biswas, A., Robin, S., Rabindran, R. & Joel, A. J. Gene interactions and genetics of blast resistance and yield attributes in
rice (Oryza sativa L.). J Genet 93, 415–424, https://doi.org/10.1007/s12041-014-0395-7 (2014).
37. Vikram, P. et al. Linkage and interaction analysis of major efect drought grain yield QTLs in rice. PLoS One 11, e0151532 (2016).
38. Diaz, L., Hossain, M., Merca, S. & Mew, T. Seed quality and efect on rice yield: fndings from farmer participatory experiments in
Central Luzon, Philippines. Philipp J Crop Sci 23, 111–119 (1998).
39. Sinha, D. D., Singh, A. N. & Singh, U. S. Site suitability analysis for dissemination of salt'''

doiSearchRegex = re.compile(r'\b(10[.][0-9]{4,}(?:[.][0-9]+)*/(?:(?!["&\'])\S)+)\b')
mo = doiSearchRegex.search(string)
print(mo.group())