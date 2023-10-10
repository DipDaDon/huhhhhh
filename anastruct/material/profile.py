import csv
import io
from typing import Dict

s_hea = """profiel,G,A,h,b,tw,tf,AL,Iy,Wy,Iz,Wz
nr.,kg/m,mm2,mm,mm,mm,mm,m2/m,mm4,mm3,mm4,mm3
100,17.0,2124,96,100,5,8,0.561,349,72.8,134,26.8
120,20.3,2534,114,120,5,8,0.677,606,106,231,38.5
140,25.1,3142,133,140,5.5,8.5,0.794,1033,155,389,55.6
160,31.0,3877,152,160,6,9,0.906,1673,220,616,76.9
180,36.2,4525,171,180,6,9.5,1.02,2510,294,925,103
200,43.1,5383,190,200,6.5,10,1.14,3692,389,1336,134
220,51.5,6434,210,220,7,11,1.26,5410,515,1955,178
240,61.5,7684,230,240,7.5,12,1.37,7763,675,2769,231
260,69.5,8682,250,260,7.5,12.5,1.48,10455,836,3668,282
280,77.8,9726,270,280,8,13,1.60,13673,1013,4763,340
300,90.0,11253,290,300,8.5,14,1.72,18263,1260,6310,421
320,99.5,12437,310,300,9,15.5,1.76,22929,1479,6985,466
340,107,13347,330,300,9.5,16.5,1.79,27693,1678,7436,496
360,114,14276,350,300,10,17.5,1.83,33090,1891,7887,526
400,127,15989,390,300,11,19,1.91,45069,2311,8564,571
450,142,17803,440,300,11.5,21,2.01,63722,2896,9465,631
500,158,19754,490,300,12,23,2.11,86975,3550,10367,691
550,169,21176,540,300,12.5,24,2.21,111932,4146,10819,721
600,181,22646,590,300,13,25,2.31,141208,4787,11271,751
650,193,24164,640,300,13.5,26,2.41,175178,5474,11724,782
700,208,26048,690,300,14.5,27,2.50,215301,6241,12179,812
800,229,28583,790,300,15,28,2.70,303443,7682,12639,843
900,256,32053,890,300,16,30,2.90,422075,9485,13547,903
1000,277,34685,990,300,16.5,31,3.10,553846,11189,14004,934
"""

s_ipe = """profiel,G,A,h,b,tw,tf,AL,Iy,Wy,Iz,Wz
nr.,kg/m,mm2,mm,mm,mm,mm,m2/m,mm4,mm3,mm4,mm3
80,6,764,80,46,3.8,5.2,328,80.1,20.0,8.49,3.69
100,8,1032,100,55,4.1,5.7,400,171,34.2,15.9,5.79
120,10,1321,120,64,4.4,6.3,475,318,53.0,27.7,8.65
140,13,1643,140,73,4.7,6.9,551,541,77.3,44.9,12.3
160,16,2009,160,82,5,7.4,623,869,109,68.3,16.7
180,19,2395,180,91,5.3,8,698,1317,146,101,22.2
200,22,2848,200,100,5.6,8.5,768,1943,194,142,28.5
220,26,3337,220,110,5.9,9.2,848,2772,252,205,37.3
240,31,3912,240,120,6.2,9.8,922,3892,324,284,47.3
270,36,4595,270,135,6.6,10.2,1.04,5790,429,420,62.2
300,43,5381,300,150,7.1,10.7,1.16,8356,557,604,80.5
330,50,6261,330,160,7.5,11.5,1.25,11767,713,788,98.5
360,58,7273,360,170,8,12.7,1.35,16266,904,1043,123
400,67,8446,400,180,8.6,13.5,1.47,23128,1156,1318,146
450,79,9882,450,190,9.4,14.6,1.61,33743,1500,1676,176
500,92,11552,500,200,10.2,16,1.74,48199,1928,2142,214
550,108,13442,550,210,11.1,17.2,1.88,67117,2441,2668,254
600,125,15598,600,220,12,19,2.01,92083,3069,3387,308"""


def load(st: str) -> Dict[int, dict]:
    """Load profile data from string

    Args:
        st (str): String containing profile data

    Returns:
        Dict[int, dict]: Profile data
    """
    with io.StringIO(st) as f:
        r = csv.reader(f)
        profile = {}

        headers = next(r)
        next(r)  # units not needed
        for row in r:
            params = {}
            for i in range(1, len(row)):
                k = headers[i]
                v = float(row[i])

                if k[0] == "W":
                    v *= 1e3
                elif k[0] == "I":
                    v *= 1e4

                params[k] = v
            profile[int(row[0])] = params

    return profile


HEA = load(s_hea)
IPE = load(s_ipe)

if __name__ == "__main__":
    from pprint import pprint

    print("HEA")
    pprint(HEA)
    print("IPE")
    pprint(IPE)
