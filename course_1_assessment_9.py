# 1.Write code to add ‘horseback riding’ to the third position (i.e., right before volleyball) in the list sports.
sports.insert(2,'horseback riding')
print(sports)

#*******************************************************************************************************************************

#2 Write code to take ‘London’ out of the list trav_dest.
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'London', 'Melbourne']
trav_dest.pop(7)


#*******************************************************************************************************************************

#3 Write code to add ‘Guadalajara’ to the end of the list trav_dest using a list method.
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne']
trav_dest.append('Guadalajara')

#*******************************************************************************************************************************

# 4. Write code to rearrange the strings in the list winners so that they are in alphabetical order from A to Z.
winners = ['Kazuo Ishiguro', 'Rainer Weiss', 'Youyou Tu', 'Malala Yousafzai', 'Alice Munro', 'Alvin E. Roth']
winners.sort()


#*******************************************************************************************************************************

# 5.Write code to switch the order of the winners list so that it is now Z to A. Assign this list to the variable z_winners.
winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']
z_winners=sorted(winners,reverse=True)

