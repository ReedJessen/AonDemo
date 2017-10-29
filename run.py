import client
import charts

ips = client.IPStreetClient()

raw_text = '1. An electric vehicle battery charging system, comprising: a user interface configured for entering a travel plan for a driving period; a charging system controller coupled to said user interface and configured to calculate total travel miles for said driving period based on said travel plan, said charging system controller further configured to calculate battery pack electrical energy requirements for a battery pack of an electric vehicle based on said calculated total travel miles, and said charging system controller further configured to set battery pack charging conditions based on said calculated battery pack electrical energy requirements and based on a current state of charge of said battery pack; and a configurable battery pack charging system coupled to said charging system controller, said battery pack and a power source, wherein said configurable battery pack charging system charges said battery pack in accordance with said battery pack  harging conditions set by said charging system controller. 2. The electric vehicle battery charging system of claim 1, wherein said user interface is comprised of a touch-sensitive screen. 3. The electric vehicle battery charging system of claim 1, wherein said user interface is integrated within said electric vehicle. 4. The electric vehicle battery charging system of claim 1, further comprising a system memory coupled to said charging system controller, said system memory storing battery pack data and electrical energy per mile conversion factors. 5. The electric vehicle battery charging system of claim 1, further comprising a system memory coupled to said charging system controller, said system memory storing a location database, wherein said charging system controller is configured to allow it to search said location database. 6. The electric vehicle battery charging system of claim 1, said charging system controller further configured to calculate a battery power safety margin, wherein said charging system controller calculates said battery pack requirements based on said calculated total travel miles, said current state of charge of said battery pack and said battery power safety margin. 7. The electric vehicle battery charging system of claim 1, said user interface further configured for entering departure times corresponding to at least one location of said travel plan, and wherein said charging system controller is further configured to calculate said battery pack requirements based on said calculated total travel miles, said current state of charge of said battery pack and said departure times. 8. The electric vehicle battery charging system of claim 1, further comprising a communication link coupled to an external source of road and traffic conditions, and wherein said charging system controller is further configured to calculate said battery pack requirements based on said calculated total travel miles, said current state of charge of said battery pack and said road and traffic conditions. 9. The electric vehicle battery charging system of claim 1, further comprising a communication link coupled to an external source of weather conditions, and wherein said charging system controller is further configured to calculate said battery pack requirements based on said calculated total travel miles, said current state of charge of said battery pack and said weather conditions. 10. A method of charging a battery pack of an electric vehicle, the method comprising the steps of: inputting a travel plan into a battery pack charging controller using a user interface, wherein said travel plan is comprised of location information; calculating a total travel miles corresponding to said travel plan; determining a present battery pack state of charge, wherein said present battery pack state of charge corresponds to a first quantity of electrical energy stored within said battery pack; converting said total travel miles to a second quantity of electrical energy, wherein said second quantity of electrical energy corresponds to a level of electrical energy required to be stored in the battery pack for the electric vehicle to travel said total travel miles; calculating a third quantity of electrical energy, wherein said third quantity of electrical energy corresponds to the difference between said second quantity of electrical energy and said first quantity of electrical energy; determining a set of battery pack charging conditions, wherein said set of battery pack charging conditions is based on said third quantity of electrical energy; inputting said set of battery pack charging conditions into an electric vehicle charging system; and charging the battery pack of the electric vehicle with said electric vehicle charging system in accordance with said set of battery pack charging conditions. 11. The method of claim 10, wherein said battery pack charging controller is an on-board battery pack charging controller, and wherein said on-board battery pack charging controller performs said steps of calculating said total travel miles, converting said total travel miles to said second quantity of electrical energy, calculating said third quantity of electrical energy, determining said set of battery pack charging conditions, and inputting said set of battery pack charging conditions into said electric vehicle charging system. 12. The method of claim 10, wherein said step of determining a set of battery pack charging conditions further comprises the step of setting a cut-off voltage. 13. The method of claim 10, further comprising the step of calculating a battery power safety margin, wherein said battery power safety margin corresponds to a fourth quantity of electrical energy, and wherein said set of battery pack charging conditions is based on said third quantity of electrical energy and on said fourth quantity of electrical energy. 14. The method of claim 13, further comprising the step of setting a minimum battery power safety margin. 15. The method of claim 10, further comprising the steps of inputting a battery power safety margin using said user interface, converting said battery power safety margin to a fourth quantity of electrical energy, and wherein said set of battery pack charging conditions is based on said third quantity of electrical energy and on said fourth quantity of electrical energy. 16. The method of claim 10, wherein said step of inputting said travel plan into said battery pack charging controller further comprises the step of inputting location departure time information into said battery pack charging controller using said user interface, wherein said converting step uses a miles-to-electrical energy conversion factor, and wherein said miles-to-electrical energy conversion factor varies with said location departure time information. 17. The method of claim 10, further comprising the steps of: obtaining road and traffic condition information, wherein said road and traffic condition information obtaining step is performed by said battery pack charging controller; and modifying a miles-to-electrical energy conversion factor in response to said road and traffic condition information, wherein said converting step uses said miles-to-electrical energy conversion factor. 18. The method of claim 10, further comprising the steps of: obtaining road and traffic condition information, wherein said road and traffic condition information obtaining step is performed by said battery pack charging controller; and modifying said travel plan in response to said road and traffic condition information, wherein said total travel miles corresponds to said travel plan as modified in response to said road and traffic conditions. 19. The method of claim 10, further comprising the steps of:obtaining weather condition information, wherein said weather condition information obtaining step is performed by said battery pack charging controller; and modifying a miles-to-electrical energy conversion factor in response to said weather condition information, wherein said converting step uses said miles-to-electrical energy conversion factor. 20. The method of claim 10, further comprising the steps of: obtaining weather condition information, wherein said weather condition information obtaining step is performed by said battery pack charging controller; and modifying said travel plan in response to said weather condition information, wherein said total travel miles corresponds to said travel plan as modified in response to said weather conditions. 21. The method of claim 10, wherein said step of inputting said travel plan into said battery pack charging controller further comprises the step of inputting location departure time information into said battery pack charging controller using said user interface, and wherein said method further comprises the steps of; determining a battery pack charging start time based on said location departure time information; inputting said battery pack charging start time into said electric vehicle charging system; and initiating said battery pack charging step in response to said battery pack charging start time. 22. The method of claim 21, further comprising the step of inputting electricity cost as a function of usage time data into said battery pack charging controller, wherein said battery pack charging start time determining step is based on said location departure time information and on said electricity cost as a function of usage time data. 23. The method of claim 21, further comprising the step of obtaining electricity cost as a function of usage time data, wherein said electricity cost as a function of usage time data obtaining step is performed by said battery pack charging controller, and wherein said battery pack charging start time determining step is based on said location departure time information and on said electricity cost as a function of usage time data. 24. The method of claim 10, further comprising the step of inputting mid-travel recharging information into said battery pack charging controller using said user interface, wherein said set of battery pack charging conditions is based on said third quantity of electrical energy and on said mid-travel recharging information. 25. The method of claim 10, further comprising the step of inputting driving style information into said battery pack charging controller using said user interface, wherein said set of battery pack charging conditions is based on said third quantity of electrical energy and on said driving style information.'

semantic_results = ips.get_semantic_search(raw_text,filter={'page_size':100})
bibliographic_results = ips.get_bibliographic_from_semantic_results(semantic_results)
claim_scope_results = ips.get_claim_scope_scores_from_semantic_results(semantic_results)
merged_results = ips.merge_semantic_bibliographic_claim_scope()
print(merged_results)

charts = charts.IPStreetCharting()
#
# charts.owner_distribution_chart(merged_results)
charts.closeness_density_chart(merged_results)