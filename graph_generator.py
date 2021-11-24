import os

#-N			number of nodes x
#-k			average degree x
#-maxk		maximum degree x
#-t1		minus exponent for the degree sequence x
#-t2		minus exponent for the community size distribution
#-minc		minimum for the community sizes x
#-maxc		maximum for the community sizes x
#-mu		mixing parameter (0.1 - 0.6)
#-on		number of overlapping nodes (10% - 60%)
#-om		number of memberships of the overlapping nodes (2 - 4)

for mui in (0.1, 0.2, 0.3, 0.4, 0.5, 0.6):
	for oni in (0.1, 0.2, 0.3, 0.4, 0.5, 0.6):
		for omi in (2,3,4):
			for i in range(1,11):
				print(str(mui) + "-" + str(oni) + "-"+str(omi) + " number:" + str(i))
				N = 1000
				k = 7
				maxk = 9
				t1 = -2
				t2 = -1.5
				minc = 10
				maxc = 50
				mu = mui
				on = N * oni
				om = omi
				base = "./package1/binary_networks/benchmark"
				base = base + " -N " + str(N) + " -k " + str(k) + " -maxk " + str(maxk) + " -mu " + str(mu) + " -t1 " + str(t1) +" -t2 " + str(t2)+ " -minc " + str(minc) + " -maxc " + str(maxc) + " -on " + str(on) + " -om " + str(om)
				print(base)
				os.system(base);
				print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
				os.system("mkdir -p ./networks/" + str(i) + "/")
				os.system("mv network.dat ./networks/" + str(i) + "/")
				os.system("mv community.dat ./networks/" + str(i) + "/")
				os.system("mv statistics.dat ./networks/" + str(i) + "/")
				f = open("./networks/"+str(i) + "/parameters.txt","w")
				f.write(base)
				f.close()