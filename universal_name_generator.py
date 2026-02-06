#!/bin/python

# Universal Player Generator
# Great Lakes Game Library
# CC BY-SA 4.0

# Used to generate lists of players as well as background information

import random
import os


def load_resources():
	# Return arrays of first name, last name, hometowns, Minor League Hockey, College Football

	#first names
	mypath = os.path.join(os.path.dirname(__file__),"resources","first_names.txt")
	fn_data = open(mypath,"r")
	f_name = fn_data.readlines()
	fn_data.close()

	for l in f_name:
		l = l.strip()

	#last names
	mypath = os.path.join(os.path.dirname(__file__),"resources","last_names.txt")
	ln_data = open(mypath,"r")
	l_name = ln_data.readlines()
	ln_data.close()

	for l in l_name:
		l = l.strip()

	#city names (Weighted)
	mypath = os.path.join(os.path.dirname(__file__),"resources","hometowns.txt")
	tn_data = open(mypath,"r")
	t_name = tn_data.readlines()
	tn_data.close()

	for l in t_name:
		l = l.strip()

	#Birthdays
	mypath = os.path.join(os.path.dirname(__file__),"resources","date_list.txt")
	dn_data = open(mypath,"r")
	d_name = dn_data.readlines()
	dn_data.close()

	for l in d_name:
		l = l.strip()

	#CHL and NCAA Hockey
	mypath = os.path.join(os.path.dirname(__file__),"resources","hockey_juniors.txt")
	hn_data = open(mypath,"r")
	h_name = hn_data.readlines()
	hn_data.close()

	for l in h_name:
		l = l.strip()

	#D1 College Football (Weighted)
	mypath = os.path.join(os.path.dirname(__file__),"resources","fbs_colleges.txt")
	cn_data = open(mypath,"r")
	c_name = cn_data.readlines()
	cn_data.close()

	for l in c_name:
		l = l.strip()

	return f_name,l_name,t_name,h_name,c_name,d_name



if __name__ == '__main__':

	print("Loading Resources")
	f_name,l_name,t_name,h_name,c_name,d_name = load_resources()


	p_count = input("Number of players: ")
	p_count = int(p_count)
	o_name = input("Output_Name: ")



	# Include Minor League
	player_list = []
	m_choice = ""

	while m_choice == "":
		m_choice = input("Type of Minor League (Hockey, Football, None): ")

		if m_choice == "H":
			player_list.append("Name\tHometown\tBirthday\tJuniors Team")

		elif m_choice == "F":
			player_list.append("Name\tHometown\tBirthday\tCollege Team")
		elif m_choice == "N":
			player_list.append("Name\tHometown\tBirthday")
		else:
			print("Not a valid choice")
			m_choice = ""

	while p_count > 0:
		# Name
		first_name = random.choice(f_name).rstrip()
		last_name = random.choice(l_name).rstrip()
		town_name = random.choice(t_name).rstrip()
		birthday = random.choice(d_name).rstrip()

		if m_choice == "H":
			minor = "\t"+random.choice(h_name).rstrip()
		elif m_choice == "F":
			minor = "\t"+random.choice(c_name).rstrip()
		else:
			minor = ""


		player_list.append(first_name+" "+last_name+"\t"+town_name+"\t"+birthday+minor)
		#player_list.append(first_name+" "+last_name)
		p_count = p_count - 1


	my_output_path = os.path.join(os.path.dirname(__file__),"outputs",o_name+".csv")
	t_data = open(my_output_path,"w")
	for f in player_list:
		t_data.write(str(f)+"\n")
	t_data.close()	